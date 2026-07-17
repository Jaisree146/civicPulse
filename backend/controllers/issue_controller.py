from flask import g, request

from common.api_response import ApiResponse
from services.issue_service import IssueService
from validators.issue_validator import IssueValidator
from middleware.rbac_middleware import roles_required
from middleware.auth_middleware import token_required

from common.constants import Roles
class IssueController:

    @staticmethod
    def get_all():

        issues = IssueService.get_all()

        return ApiResponse.success(
            message="Issues fetched successfully.",
            data=[
                {
                    "id": issue.id,
                    "issue_number": issue.issue_number,
                    "summary": issue.summary,
                    "priority": issue.priority,
                    "status": issue.status,
                    "report_count": issue.report_count,
                    "category": issue.category.category_name,
                    "department": (
                        issue.department.department_name
                        if issue.department
                        else None
                    ),
                    "suggested_department": (
                        issue.suggested_department.department_name
                        if issue.suggested_department
                        else None
                    )
                }
                for issue in issues
            ]
        )

    @staticmethod
    @token_required
    @roles_required(Roles.MUNICIPAL_OFFICER)
    def get_pending_review():

        issues = IssueService.get_pending_review()

        return ApiResponse.success(
            message="Pending issues fetched successfully.",
            data=[
                {
                    "id": issue.id,
                    "issue_number": issue.issue_number,
                    "summary": issue.summary,
                    "priority": issue.priority,
                    "report_count": issue.report_count,
                    "category": issue.category.category_name
                }
                for issue in issues
            ]
        )

    @staticmethod
    def get_by_id(issue_id):

        issue = IssueService.get_by_id(
            issue_id
        )

        return ApiResponse.success(
            message="Issue fetched successfully.",
            data={
                "id": issue.id,
                "issue_number": issue.issue_number,
                "summary": issue.summary,
                "priority": issue.priority,
                "status": issue.status,
                "report_count": issue.report_count,
                "category": issue.category.category_name,
                "department": (
                    issue.department.department_name
                    if issue.department
                    else None
                ),
                "suggested_department": (
                    issue.suggested_department.department_name
                    if issue.suggested_department
                    else None
                ),
                "created_at": issue.created_at,
                "updated_at": issue.updated_at
            }
        )

    @staticmethod
    @token_required
    @roles_required(Roles.MUNICIPAL_OFFICER)
    def assign_department(issue_number: str):

        data = request.get_json()

        IssueValidator.validate_assign_department(
            data
        )

        issue = IssueService.assign_department(
        issue_number=issue_number,
        department_id=data["department_id"]
        )

        return ApiResponse.success(
            message="Department assigned successfully.",
            data={
                "issue_id": issue.id,
                "department_id": issue.department_id,
                "status": issue.status
            }
        )

    @staticmethod
    def confirm_department_suggestion(issue_id):

        data = request.get_json() or {}

        department_id = data.get("department_id")

        issue = IssueService.confirm_department_suggestion(
            issue_id=issue_id,
            department_id=department_id
        )

        return ApiResponse.success(
            message="Department suggestion confirmed successfully.",
            data={
                "issue_id": issue.id,
                "department_id": issue.department_id,
                "status": issue.status
            }
        )

    @staticmethod
    @token_required
    @roles_required(Roles.DEPARTMENT_OFFICER)
    def get_my_issues():

        department_id = g.current_user.department_id

        issues = IssueService.get_by_department_id(
            department_id
        )

        return ApiResponse.success(
            message="Assigned issues fetched successfully.",
            data=[
                {
                    "id": issue.id,
                    "issue_number": issue.issue_number,
                    "summary": issue.summary,
                    "priority": issue.priority,
                    "status": issue.status,
                    "report_count": issue.report_count,
                    "category": issue.category.category_name
                }
                for issue in issues
            ]
        )

    @staticmethod
    @token_required
    @roles_required(Roles.DEPARTMENT_OFFICER)
    def update_status(issue_number: str):

        data = request.get_json()

        IssueValidator.validate_status(
            data["status"]
        )

        issue = IssueService.update_status(
        issue_number=issue_number,
        status=data["status"],
        current_department_id=g.current_user.department_id
    )

        return ApiResponse.success(
            message="Issue status updated successfully.",
            data={
                "issue_id": issue.id,
                "status": issue.status
            }
        )
    
    @staticmethod
    @token_required
    @roles_required(Roles.MUNICIPAL_OFFICER)
    
    def get_by_number(
    issue_number: str
):

        issue = IssueService.get_by_number(
        issue_number
    )

        return ApiResponse.success(
        message="Issue fetched successfully.",
        data={
            "id": issue.id,
            "issue_number": issue.issue_number,
            "summary": issue.summary,
            "category": issue.category.category_name,
            "priority": issue.priority,
            "status": issue.status,
            "latitude": issue.latitude,
            "longitude": issue.longitude,
            "report_count": issue.report_count,
            "suggested_department": (
                issue.suggested_department.department_name
                if issue.suggested_department
                else None
            ),
            "assigned_department": (
                issue.department.department_name
                if issue.department
                else None
            ),
            "created_at": issue.created_at
        },
        status_code=200
    )