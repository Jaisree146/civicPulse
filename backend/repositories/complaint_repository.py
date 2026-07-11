from config.db import db
from models.complaint import Complaint


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
    def get_latest() -> Complaint | None:

        return Complaint.query.order_by(
            Complaint.id.desc()
        ).first()

    @staticmethod
    def get_by_id(
        complaint_id: int
    ) -> Complaint | None:

        return Complaint.query.filter_by(
            id=complaint_id
        ).first()

    @staticmethod
    def get_by_citizen_id(
        citizen_id: int
    ) -> list[Complaint]:

        return Complaint.query.filter_by(
            citizen_id=citizen_id
        ).order_by(
            Complaint.created_at.desc()
        ).all()

    @staticmethod
    def update():

        db.session.commit()