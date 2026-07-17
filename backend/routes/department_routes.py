from flask import Blueprint

from controllers.department_controller import (
    DepartmentController
)

department_bp = Blueprint(
    "department",
    __name__,
    url_prefix="/api/departments"
)

department_bp.route(
    "",
    methods=["GET"]
)(
    DepartmentController.get_all
)

department_bp.route(
    "/<int:department_id>/issues",
    methods=["GET"]
)(
    DepartmentController.get_by_department
)