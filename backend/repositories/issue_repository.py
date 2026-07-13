from models.issue import Issue
from config.db import db


class IssueRepository:

    @staticmethod
    def create(
        issue: Issue
    ) -> Issue:

        db.session.add(issue)
        db.session.commit()

        return issue

    @staticmethod
    def get_by_id(
        issue_id: int
    ) -> Issue | None:

        return Issue.query.filter_by(
            id=issue_id
        ).first()

    @staticmethod
    def get_latest() -> Issue | None:

        return Issue.query.order_by(
            Issue.id.desc()
        ).first()

    @staticmethod
    def get_all() -> list[Issue]:

        return Issue.query.order_by(
            Issue.created_at.desc()
        ).all()

    @staticmethod
    def get_pending_review() -> list[Issue]:

        return Issue.query.filter_by(
            status="Pending Review"
        ).order_by(
            Issue.created_at.asc()
        ).all()

    @staticmethod
    def get_by_department_id(
        department_id: int
    ) -> list[Issue]:

        return Issue.query.filter_by(
            department_id=department_id
        ).order_by(
            Issue.created_at.desc()
        ).all()

    @staticmethod
    def update(
        issue: Issue
    ) -> Issue:

        db.session.commit()

        return issue