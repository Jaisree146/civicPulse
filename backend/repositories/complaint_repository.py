from config.db import db
from models.complaint import Complaint
from models.issue import Issue
from common.constants import IssueStatus


class ComplaintRepository:

    @staticmethod
    def create(
        complaint: Complaint
    ) -> Complaint:

        db.session.add(complaint)
        db.session.commit()
        db.session.refresh(complaint)

        return complaint

    @staticmethod
    def get_latest():

        return (
            Complaint.query
            .order_by(
                Complaint.id.desc()
            )
            .first()
        )

    @staticmethod
    def get_by_id(
        complaint_id: int
    ):

        return Complaint.query.filter_by(
            id=complaint_id
        ).first()

    @staticmethod
    def get_by_citizen_id(
        citizen_id: int
    ):

        return (
            Complaint.query
            .filter_by(
                citizen_id=citizen_id
            )
            .order_by(
                Complaint.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_unprocessed():

        return (
            Complaint.query
            .filter(
                Complaint.processed.is_(False)
            )
            .all()
        )

    @staticmethod
    def link_issue(
        complaint: Complaint,
        issue_id: int
    ):

        complaint.issue_id = issue_id

        db.session.commit()

        db.session.refresh(
            complaint
        )

        return complaint

    @staticmethod
    def mark_processed(
        complaint: Complaint
    ):

        complaint.processed = True

        db.session.commit()

        db.session.refresh(
            complaint
        )

        return complaint

    @staticmethod
    def update(
        complaint: Complaint
    ):

        db.session.commit()

        db.session.refresh(
            complaint
        )

        return complaint
    
    @staticmethod
    def get_pending_by_citizen_id(
    citizen_id: int
    ) -> list[Complaint]:

        return (
        Complaint.query
        .join(Issue)
        .filter(
            Complaint.citizen_id == citizen_id,
            Issue.status.in_([
                IssueStatus.PENDING_REVIEW,
                IssueStatus.ASSIGNED,
                IssueStatus.IN_PROGRESS
            ])
        )
        .order_by(
            Complaint.created_at.desc()
        )
        .all()
        )

    @staticmethod
    def get_by_number(
    complaint_number: str
    ) -> Complaint | None:

        return Complaint.query.filter_by(
        complaint_number=complaint_number
    ).first()