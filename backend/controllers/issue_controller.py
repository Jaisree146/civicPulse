from flask import g, request

from common.api_response import ApiResponse
from services.issue_service import IssueService
from validators.issue_validator import IssueValidator


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
                    )
                }
                for issue in issues
            ]
        )

    @staticmethod
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
                "created_at": issue.created_at,
                "updated_at": issue.updated_at
            }
        )

    @staticmethod
    def assign_department(issue_id):

        data = request.get_json()

        IssueValidator.validate_assign_department(
            data
        )

        issue = IssueService.assign_department(
            issue_id=issue_id,
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
    def update_status(issue_id):

        data = request.get_json()

        IssueValidator.validate_status(
            data["status"]
        )

        issue = IssueService.update_status(
        issue_id=issue_id,
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