from flask import Blueprint

from common.constants import Roles
from controllers.dashboard_controller import DashboardController
from middleware.auth_middleware import token_required
from middleware.rbac_middleware import roles_required


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/api/dashboard"
)


@dashboard_bp.route(
    "/citizen",
    methods=["GET"]
)
@token_required
@roles_required(Roles.CITIZEN)
def citizen_dashboard():
    return DashboardController.citizen_dashboard()

@dashboard_bp.route(
    "/municipal",
    methods=["GET"]
)
@token_required
@roles_required(Roles.MUNICIPAL_OFFICER)
def municipal_dashboard():
    return DashboardController.municipal_dashboard()


@dashboard_bp.route(
    "/department",
    methods=["GET"]
)
@token_required
@roles_required(Roles.DEPARTMENT_OFFICER)
def department_dashboard():
    return DashboardController.department_dashboard()