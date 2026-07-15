from sqlalchemy import func

from config.db import db
from models.complaint import Complaint
from models.issue import Issue


class DashboardRepository:

    @staticmethod
    def get_citizen_dashboard(
        citizen_id: int
    ):

        total_complaints = (
            db.session.query(
                func.count(Complaint.id)
            )
            .filter(
                Complaint.citizen_id == citizen_id
            )
            .scalar()
        )

        resolved_complaints = (
            db.session.query(
                func.count(Complaint.id)
            )
            .join(
                Issue,
                Complaint.issue_id == Issue.id
            )
            .filter(
                Complaint.citizen_id == citizen_id,
                Issue.status == "Resolved"
            )
            .scalar()
        )

        recent_complaints = (
            db.session.query(
                Complaint.complaint_number,
                Complaint.title,
                Complaint.status
            )
            .filter(
                Complaint.citizen_id == citizen_id
            )
            .order_by(
                Complaint.created_at.desc()
            )
            .limit(5)
            .all()
        )

        recent_complaints = [
            {
                "complaint_number": row.complaint_number,
                "title": row.title,
                "status": row.status
            }
            for row in recent_complaints
        ]

        return {
            "total_complaints": total_complaints,
            "resolved_complaints": resolved_complaints,
            "recent_complaints": recent_complaints
        }

    @staticmethod
    def get_municipal_dashboard():

        total_issues = (
            db.session.query(
                func.count(Issue.id)
            )
            .scalar()
        )

        pending_review = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.status == "Pending Review"
            )
            .scalar()
        )

        return {
            "total_issues": total_issues,
            "pending_review": pending_review
        }

    @staticmethod
    def get_department_dashboard(
        department_id: int
    ):

        assigned = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.department_id == department_id
            )
            .scalar()
        )

        resolved = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.department_id == department_id,
                Issue.status == "Resolved"
            )
            .scalar()
        )

        return {
            "assigned": assigned,
            "resolved": resolved
        }