from flask import Blueprint

from common.constants import Roles
from controllers.issue_controller import IssueController
from middleware.auth_middleware import token_required as jwt_required
from middleware.rbac_middleware import roles_required


issue_bp = Blueprint(
    "issue",
    __name__,
    url_prefix="/api/issues"
)

# Municipal Officer APIs


# Get all issues
issue_bp.route(
    "",
    methods=["GET"]
)(
    jwt_required(
        roles_required(
            Roles.MUNICIPAL_OFFICER
        )(
            IssueController.get_all
        )
    )
)


# Get pending issues
issue_bp.route(
    "/pending",
    methods=["GET"]
)(
    jwt_required(
        roles_required(
            Roles.MUNICIPAL_OFFICER
        )(
            IssueController.get_pending_review
        )
    )
)


# Assign department
issue_bp.route(
    "/<int:issue_id>/assign",
    methods=["PUT"]
)(
    jwt_required(
        roles_required(
            Roles.MUNICIPAL_OFFICER
        )(
            IssueController.assign_department
        )
    )
)

# Confirm AI department suggestion
issue_bp.route(
    "/<int:issue_id>/confirm-department",
    methods=["PUT"]
)(
    jwt_required(
        roles_required(
            Roles.MUNICIPAL_OFFICER
        )(
            IssueController.confirm_department_suggestion
        )
    )
)


# Common APIs


# Get issue by id
issue_bp.route(
    "/<int:issue_id>",
    methods=["GET"]
)(
    jwt_required(
        roles_required(
            Roles.MUNICIPAL_OFFICER,
            Roles.DEPARTMENT_OFFICER
        )(
            IssueController.get_by_id
        )
    )
)


# Department Officer APIs


# Get my assigned issues
issue_bp.route(
    "/my",
    methods=["GET"]
)(
    jwt_required(
        roles_required(
            Roles.DEPARTMENT_OFFICER
        )(
            IssueController.get_my_issues
        )
    )
)


# Update issue status
issue_bp.route(
    "/<int:issue_id>/status",
    methods=["PUT"]
)(
    jwt_required(
        roles_required(
            Roles.DEPARTMENT_OFFICER
        )(
            IssueController.update_status
        )
    )
)