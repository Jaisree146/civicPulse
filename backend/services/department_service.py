from repositories.department_repository import (
    DepartmentRepository
)

from repositories.issue_repository import (
    IssueRepository
)

from exceptions.department_exceptions import (
    DepartmentNotFoundException
)


class DepartmentService:

    @staticmethod
    def get_all():

        return DepartmentRepository.get_all()

    @staticmethod
    def get_by_department(
        department_id: int
    ):

        department = DepartmentRepository.get_by_id(
            department_id
        )

        if department is None:
            raise DepartmentNotFoundException()

        return IssueRepository.get_by_department(
            department_id
        )