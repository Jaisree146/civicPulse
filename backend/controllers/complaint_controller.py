from flask import g
from flask import request

from common.api_response import ApiResponse
from common.constants import Roles

from middleware.auth_middleware import token_required
from middleware.rbac_middleware import roles_required

from services.complaint_service import ComplaintService
from validators.complaint_validator import ComplaintValidator


class ComplaintController:

    @staticmethod
    @token_required
    @roles_required(Roles.CITIZEN)
    def create():

        data = request.get_json() or {}

        ComplaintValidator.validate_create(
            data
        )

        complaint = ComplaintService.create(
            citizen_id=g.current_user.id,
            title=data["title"],
            description=data["description"],
            latitude=data["latitude"],
            longitude=data["longitude"]
        )

        return ApiResponse.success(
            message="Complaint submitted successfully.",
            data={
                "complaint_id": complaint.id,
                "complaint_number": complaint.complaint_number
            },
            status_code=201
        )

    @staticmethod
    @token_required
    @roles_required(Roles.CITIZEN)
    def get_my_complaints():

        complaints = ComplaintService.get_my_complaints(
            g.current_user.id
        )

        return ApiResponse.success(
            message="Complaints fetched successfully.",
            data=[
                {
                    "id": complaint.id,
                    "complaint_number": complaint.complaint_number,
                    "title": complaint.title,
                    "status": complaint.status,
                    "created_at": complaint.created_at
                }
                for complaint in complaints
            ]
        )

    @staticmethod
    @token_required
    def get_by_id(
        complaint_id: int
    ):

        complaint = ComplaintService.get_by_id(
        complaint_id,
        g.current_user
        )

        return ApiResponse.success(
            message="Complaint fetched successfully.",
            data={
                "id": complaint.id,
                "complaint_number": complaint.complaint_number,
                "title": complaint.title,
                "description": complaint.description,
                "latitude": complaint.latitude,
                "longitude": complaint.longitude,
                "status": complaint.status,
                "created_at": complaint.created_at
            }
        )