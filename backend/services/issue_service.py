from common.constants import (
    IssueStatus,
    NumberPrefix
)

from exceptions.auth_exceptions import AuthenticationException
from exceptions.category_exceptions import CategoryNotFoundException
from exceptions.department_exceptions import DepartmentNotFoundException
from exceptions.issue_exceptions import IssueNotFoundException

from models.issue import Issue

from repositories.category_repository import CategoryRepository
from repositories.department_repository import DepartmentRepository
from repositories.issue_repository import IssueRepository


class IssueService:

    @staticmethod
    def create(
        category_id: int,
        summary: str,
        priority: str
    ) -> Issue:

        category = CategoryRepository.get_by_id(
            category_id
        )

        if category is None:
            raise CategoryNotFoundException()

        issue = Issue(
            issue_number=IssueService.generate_issue_number(),
            category_id=category_id,
            summary=summary,
            priority=priority
        )

        return IssueRepository.create(
            issue
        )

    @staticmethod
    def get_all() -> list[Issue]:

        return IssueRepository.get_all()

    @staticmethod
    def get_pending_review() -> list[Issue]:

        return IssueRepository.get_pending_review()

    @staticmethod
    def get_by_department_id(
        department_id: int
    ) -> list[Issue]:

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
        issue_id: int,
        department_id: int
    ) -> Issue:

        issue = IssueRepository.get_by_id(
            issue_id
        )

        if issue is None:
            raise IssueNotFoundException()

        department = DepartmentRepository.get_by_id(
            department_id
        )

        if department is None:
            raise DepartmentNotFoundException()

        issue.department_id = department_id
        issue.status = IssueStatus.ASSIGNED

        return IssueRepository.update(
            issue
        )

    @staticmethod
    def update_status(
        issue_id: int,
        status: str,
        current_department_id: int
    ) -> Issue:

        issue = IssueRepository.get_by_id(
            issue_id
        )

        if issue is None:
            raise IssueNotFoundException()

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

        issue = IssueRepository.get_by_id(
            issue_id
        )

        if issue is None:
            raise IssueNotFoundException()

        issue.report_count += 1

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