from models.complaint import Complaint

from common.constants import (
    Roles,
    NumberPrefix
)

from exceptions.auth_exceptions import (
    AuthenticationException
)

from exceptions.complaint_exception import (
    ComplaintNotFoundException
)

from common.logger import logger
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

        complaint = ComplaintRepository.create(
            complaint
        )

        from ai.processing.complaint_processor import ComplaintProcessor

        ComplaintProcessor.process(
        complaint
        )

        return complaint

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
        current_user
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

        last = ComplaintRepository.get_latest()

        if last is None:
            next_id = 1
        else:
            next_id = last.id + 1

        return f"{NumberPrefix.COMPLAINT}{next_id:06d}"

    @staticmethod
    def get_unprocessed():

        return ComplaintRepository.get_unprocessed()

    @staticmethod
    def reprocess_unprocessed():

        complaints = ComplaintRepository.get_unprocessed()

        for complaint in complaints:
            try:
                from ai.processing.complaint_processor import ComplaintProcessor

                ComplaintProcessor.process(
                    complaint
                )
            except Exception:
                logger.exception(
                    "Reprocessing failed for complaint %s",
                    complaint.id
                )

        return complaints

    @staticmethod
    def link_issue(
        complaint_id: int,
        issue_id: int
    ) -> Complaint:

        complaint = ComplaintRepository.get_by_id(
            complaint_id
        )

        if complaint is None:
            raise ComplaintNotFoundException()

        return ComplaintRepository.link_issue(
            complaint,
            issue_id
        )

    @staticmethod
    def mark_processed(
        complaint_id: int
    ) -> Complaint:

        complaint = ComplaintRepository.get_by_id(
            complaint_id
        )

        if complaint is None:
            raise ComplaintNotFoundException()

        return ComplaintRepository.mark_processed(
            complaint
        )

    @staticmethod
    def update(
        complaint: Complaint
    ) -> Complaint:

        return ComplaintRepository.update(
            complaint
        )
    
    @staticmethod
    def get_pending_by_citizen_id(
    citizen_id: int
    ):

        return ComplaintRepository.get_pending_by_citizen_id(
        citizen_id
    )

    @staticmethod
    def get_by_number(complaint_number: str,citizen_id: int) -> Complaint:
        complaint = ComplaintRepository.get_by_number(
            complaint_number
        )

        if complaint is None:
            raise ComplaintNotFoundException()

        if complaint.citizen_id != citizen_id:

            raise AuthenticationException(

                message="You are not authorized to view this complaint.",

                status_code=403,

                error_code="AUTH_010"

            )

        return complaint