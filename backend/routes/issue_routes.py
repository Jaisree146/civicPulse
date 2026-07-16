from flask import Blueprint

from controllers.issue_controller import IssueController

issue_bp = Blueprint(
    "issue",
    __name__,
    url_prefix="/api/issues"
)

issue_bp.route(
    "",
    methods=["GET"]
)(
    IssueController.get_all
)

issue_bp.route(
    "/pending",
    methods=["GET"]
)(
    IssueController.get_pending_review
)

issue_bp.route(
    "/<string:issue_number>",
    methods=["GET"]
)(
    IssueController.get_by_number
)

issue_bp.route(
    "/my",
    methods=["GET"]
)(
    IssueController.get_my_issues
)

issue_bp.route(
    "/<string:issue_number>/assign",
    methods=["PUT"]
)(
    IssueController.assign_department
)

issue_bp.route(
    "/<string:issue_number>/status",
    methods=["PUT"]
)(
    IssueController.update_status
)