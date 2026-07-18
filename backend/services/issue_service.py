from common.constants import (
    IssueStatus,
    NumberPrefix
)

from exceptions.auth_exceptions import (
    AuthenticationException
)
from exceptions.category_exceptions import (
    CategoryNotFoundException
)
from exceptions.department_exceptions import (
    DepartmentNotFoundException
)
from exceptions.issue_exceptions import (
    IssueNotFoundException
)

from models.issue import Issue

from repositories.category_repository import (
    CategoryRepository
)
from repositories.department_repository import (
    DepartmentRepository
)
from repositories.issue_repository import (
    IssueRepository
)


class IssueService:

    @staticmethod
    def create(
        category_id: int,
        summary: str,
        latitude: float,
        longitude: float,
        priority: str,
        embedding: list[float],
        department_id: int | None = None
    ) -> Issue:

        category = CategoryRepository.get_by_id(
            category_id
        )

        if category is None:
            raise CategoryNotFoundException()

        issue = Issue(
        issue_number=IssueService.generate_issue_number(),

        category_id=category_id,

        suggested_department_id=department_id,

        department_id=None,

        summary=summary,

        latitude=latitude,

        longitude=longitude,

        priority=priority,

        embedding=embedding
        )

        return IssueRepository.create(
            issue
        )

    @staticmethod
    def get_all():

        return IssueRepository.get_all()

    @staticmethod
    def get_pending_review():

        return IssueRepository.get_pending_review()

    @staticmethod
    def get_by_department_id(
        department_id: int
    ):

        return IssueRepository.get_by_department_id(
            department_id
        )

    @staticmethod
    def get_by_id(
        issue_id: int
    ) -> Issue:

        issue = IssueRepository.get_by_id(
            issue_id
        )

        if issue is None:
            raise IssueNotFoundException()

        return issue

    @staticmethod
    def assign_department(
    issue_number: str,
    department_id: int
    ) -> Issue:

        issue = IssueService.get_by_number(
        issue_number
        )

        department = DepartmentRepository.get_by_id(
        department_id
        )

        if department is None:
            raise DepartmentNotFoundException()

        issue.department_id = department_id
        issue.suggested_department_id = department_id
        issue.status = IssueStatus.ASSIGNED

        return IssueRepository.update(
        issue
        )

    @staticmethod
    def suggest_department(
        issue_id: int,
        department_id: int
    ) -> Issue:

        issue = IssueService.get_by_id(
            issue_id
        )

        department = DepartmentRepository.get_by_id(
            department_id
        )

        if department is None:
            raise DepartmentNotFoundException()

        issue.suggested_department_id = department_id

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def confirm_department_suggestion(
        issue_id: int,
        department_id: int | None = None
    ) -> Issue:

        issue = IssueService.get_by_id(
            issue_id
        )

        if department_id is None:
            department_id = issue.suggested_department_id

        if department_id is None:
            raise DepartmentNotFoundException()

        department = DepartmentRepository.get_by_id(
            department_id
        )

        if department is None:
            raise DepartmentNotFoundException()

        issue.department_id = department_id
        issue.suggested_department_id = department_id
        issue.status = IssueStatus.ASSIGNED

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def update_status(
    issue_number: str,
    status: str,
    current_department_id: int
) -> Issue:

        issue = IssueService.get_by_number(
        issue_number
    )

        if issue.department_id != current_department_id:

            raise AuthenticationException(

            message="You are not authorized to update this issue.",

            status_code=403,

            error_code="AUTH_010"

        )

        issue.status = status

        return IssueRepository.update(
        issue
        )
    
    
    @staticmethod
    def increment_report_count(
        issue_id: int
    ) -> Issue:

        issue = IssueService.get_by_id(
            issue_id
        )

        issue.report_count += 1

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def update_priority(
        issue_id: int,
        priority: str
    ) -> Issue:

        issue = IssueService.get_by_id(
            issue_id
        )

        issue.priority = priority

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def update(
        issue: Issue
    ) -> Issue:

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def generate_issue_number():

        last_issue = IssueRepository.get_latest()

        if last_issue is None:
            next_id = 1
        else:
            next_id = last_issue.id + 1

        return f"{NumberPrefix.ISSUE}{next_id:06d}"
    
    @staticmethod
    def mark_sla_notification_sent(issue_id: int):

        issue = IssueRepository.get_by_id(issue_id)

        issue.sla_notification_sent = True

        return IssueRepository.update(issue)
    
    @staticmethod
    def get_by_number(
    issue_number: str
) -> Issue:

        issue = IssueRepository.get_by_number(
        issue_number
    )

        if issue is None:
            raise IssueNotFoundException()

        return issue