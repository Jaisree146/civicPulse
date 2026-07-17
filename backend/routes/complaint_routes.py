from flask import Blueprint

from controllers.complaint_controller import (
    ComplaintController
)

complaint_bp = Blueprint("complaint",__name__,url_prefix="/api/complaints")

complaint_bp.route(
    "",
    methods=["POST"]
)(
    ComplaintController.create
)

complaint_bp.route(
    "/my",
    methods=["GET"]
)(
    ComplaintController.get_my_complaints
)

complaint_bp.route(
    "/<int:complaint_id>",
    methods=["GET"]
)(
    ComplaintController.get_by_id
)
from flask import Blueprint

from controllers.complaint_controller import (
    ComplaintController
)

complaint_bp = Blueprint(
    "complaint",
    __name__,
    url_prefix="/api/complaints"
)

complaint_bp.route(
    "",
    methods=["POST"]
)(
    ComplaintController.create
)

complaint_bp.route(
    "/my",
    methods=["GET"]
)(
    ComplaintController.get_my_complaints
)

complaint_bp.route(
    "/<string:complaint_number>",
    methods=["GET"]
)(
    ComplaintController.get_by_number
)