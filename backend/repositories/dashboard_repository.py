from sqlalchemy import func

from config.db import db
from common.constants import IssueStatus
from models.complaint import Complaint
from models.department import Department
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
                Issue.status == IssueStatus.RESOLVED
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
            .limit(6)
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
                Issue.status == IssueStatus.PENDING_REVIEW
            )
            .scalar()
        )

        assigned = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.status == IssueStatus.ASSIGNED
            )
            .scalar()
        )

        in_progress = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.status == IssueStatus.IN_PROGRESS
            )
            .scalar()
        )

        resolved = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.status == IssueStatus.RESOLVED
            )
            .scalar()
        )

        department_summary = (
            db.session.query(
                Department.department_name,
                func.count(Issue.id).label("count")
            )
            .outerjoin(
                Issue,
                Department.id == Issue.department_id
            )
            .group_by(
                Department.id,
                Department.department_name
            )
            .all()
        )

        department_summary = [
            {
                "department": row.department_name,
                "count": row.count
            }
            for row in department_summary
        ]

        return {
            "total_issues": total_issues,
            "pending_review": pending_review,
            "assigned": assigned,
            "in_progress": in_progress,
            "resolved": resolved,
            "department_summary": department_summary
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

        pending = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.department_id == department_id,
                Issue.status == IssueStatus.ASSIGNED
            )
            .scalar()
        )

        in_progress = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.department_id == department_id,
                Issue.status == IssueStatus.IN_PROGRESS
            )
            .scalar()
        )

        resolved = (
            db.session.query(
                func.count(Issue.id)
            )
            .filter(
                Issue.department_id == department_id,
                Issue.status == IssueStatus.RESOLVED
            )
            .scalar()
        )

        return {
            "assigned": assigned,
            "pending": pending,
            "in_progress": in_progress,
            "resolved": resolved
        }