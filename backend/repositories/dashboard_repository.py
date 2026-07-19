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

        status_counts = (
            db.session.query(
                Issue.status,
                func.count(Issue.id).label("count")
            )
            .group_by(
                Issue.status
            )
            .all()
        )

        counts = {
            IssueStatus.PENDING_REVIEW: 0,
            IssueStatus.ASSIGNED: 0,
            IssueStatus.IN_PROGRESS: 0,
            IssueStatus.RESOLVED: 0
        }

        for row in status_counts:
            counts[row.status] = row.count

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
            "pending_review": counts[IssueStatus.PENDING_REVIEW],
            "assigned": counts[IssueStatus.ASSIGNED],
            "in_progress": counts[IssueStatus.IN_PROGRESS],
            "resolved": counts[IssueStatus.RESOLVED],
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

        status_counts = (
            db.session.query(
                Issue.status,
                func.count(Issue.id).label("count")
            )
            .filter(
                Issue.department_id == department_id
            )
            .group_by(
                Issue.status
            )
            .all()
        )

        counts = {
            IssueStatus.ASSIGNED: 0,
            IssueStatus.IN_PROGRESS: 0,
            IssueStatus.RESOLVED: 0
        }

        for row in status_counts:
            counts[row.status] = row.count

        return {
            "assigned": assigned,
            "pending": counts[IssueStatus.ASSIGNED],
            "in_progress": counts[IssueStatus.IN_PROGRESS],
            "resolved": counts[IssueStatus.RESOLVED]
        }