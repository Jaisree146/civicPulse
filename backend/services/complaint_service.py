from models.complaint import Complaint

from common.constants import Roles

from exceptions.auth_exceptions import AuthenticationException
from exceptions.complaint_exception import (
    ComplaintNotFoundException
)

from repositories.complaint_repository import (
    ComplaintRepository
)


class ComplaintService:

    @staticmethod
    def create(
        citizen_id: int,
        title: str,
        description: str,
        latitude: float,
        longitude: float
    ) -> Complaint:

        complaint = Complaint(
            complaint_number=ComplaintService.generate_complaint_number(),
            citizen_id=citizen_id,
            title=title,
            description=description,
            latitude=latitude,
            longitude=longitude
        )

        return ComplaintRepository.create(
            complaint
        )

    @staticmethod
    def get_my_complaints(
        citizen_id: int
    ) -> list[Complaint]:

        return ComplaintRepository.get_by_citizen_id(
            citizen_id
        )

    @staticmethod
    def get_by_id(
        complaint_id: int,
        current_user: object
    ) -> Complaint:

        complaint = ComplaintRepository.get_by_id(
            complaint_id
        )

        if complaint is None:
            raise ComplaintNotFoundException()

        
        if (
            current_user.role.role_name == Roles.CITIZEN
            and complaint.citizen_id != current_user.id
        ):
            raise AuthenticationException(
                message="You are not authorized to view this complaint.",
                status_code=403,
                error_code="AUTH_010"
            )

        return complaint

    @staticmethod
    def generate_complaint_number():

        last_complaint = ComplaintRepository.get_latest()

        if last_complaint is None:
            next_id = 1
        else:
            next_id = last_complaint.id + 1

        return f"CP{next_id:06d}"