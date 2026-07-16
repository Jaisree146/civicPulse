import math

from config.db import db
from models.issue import Issue


class IssueRepository:

    @staticmethod
    def create(
    issue: Issue
    ) -> Issue:

        db.session.add(issue)
        db.session.commit()
        db.session.refresh(issue)
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

        return (
            Issue.query
            .order_by(
                Issue.id.desc()
            )
            .first()
        )

    @staticmethod
    def get_all() -> list[Issue]:

        return (
            Issue.query
            .order_by(
                Issue.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_nearby(
        latitude: float,
        longitude: float,
        radius_km: float = 2.0
    ) -> list[Issue]:

        issues = Issue.query.all()

        nearby = []

        for issue in issues:
            if issue.latitude is None or issue.longitude is None:
                continue

            distance = IssueRepository._distance_km(
                latitude,
                longitude,
                issue.latitude,
                issue.longitude
            )

            if distance <= radius_km:
                nearby.append(issue)

        return nearby

    @staticmethod
    def _distance_km(
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float
    ) -> float:

        radius = 6371.0

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(math.radians(lat1))
            * math.cos(math.radians(lat2))
            * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return radius * c

    @staticmethod
    def get_pending_review() -> list[Issue]:

        return (
            Issue.query
            .filter_by(
                status="Pending Review"
            )
            .order_by(
                Issue.created_at.asc()
            )
            .all()
        )

    @staticmethod
    def get_by_department_id(
        department_id: int
    ) -> list[Issue]:

        return (
            Issue.query
            .filter_by(
                department_id=department_id
            )
            .order_by(
                Issue.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def update(
    issue: Issue
    ) -> Issue:

        db.session.commit()
        db.session.refresh(issue)

        return issue

    @staticmethod
    def delete(
        issue: Issue
    ):

        db.session.delete(issue)

        db.session.commit()

    @staticmethod
    def mark_sla_notification_sent(
    issue
    ):

        issue.sla_notification_sent = True

        db.session.commit()

        db.session.refresh(issue)

        return issue
    
    @staticmethod
    def get_by_number(
    issue_number: str
) -> Issue | None:

        return Issue.query.filter_by(
        issue_number=issue_number
        ).first()
    
    @staticmethod
    def get_by_department(
    department_id: int
) -> list[Issue]:

        return (
        Issue.query
        .filter_by(
            department_id=department_id
        )
        .order_by(
            Issue.created_at.desc()
        )
        .all()
    )