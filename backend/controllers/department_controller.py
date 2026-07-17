from common.api_response import ApiResponse

from services.department_service import (
    DepartmentService
)


class DepartmentController:

    @staticmethod
    def get_all():

        departments = DepartmentService.get_all()

        return ApiResponse.success(
            message="Departments fetched successfully.",
            data=[
                {
                    "id": department.id,
                    "department_name": department.department_name,
                    "description": department.description
                }
                for department in departments
            ]
        )

    @staticmethod
    def get_by_department(
        department_id: int
    ):

        issues = DepartmentService.get_by_department(
            department_id
        )

        return ApiResponse.success(
            message="Department issues fetched successfully.",
            data=[
                {
                    "id": issue.id,
                    "issue_number": issue.issue_number,
                    "summary": issue.summary,
                    "priority": issue.priority,
                    "status": issue.status,
                    "report_count": issue.report_count,
                    "category": issue.category.category_name,
                    "assigned_department": (
                        issue.department.department_name
                        if issue.department
                        else None
                    ),
                    "created_at": issue.created_at
                }
                for issue in issues
            ]
        )