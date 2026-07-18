from sqlalchemy import func
from config.db import db
from models.department import Department
from models.issue import Issue


class DepartmentRepository:

    @staticmethod
    def get_all():

        return Department.query.order_by(
            Department.department_name.asc()
        ).all()

    @staticmethod
    def get_by_id(
        department_id: int
    ):

        return Department.query.filter_by(
            id=department_id
        ).first()

    @staticmethod
    def get_by_name(
        department_name: str
    ):

        return Department.query.filter_by(
            department_name=department_name
        ).first()


    @staticmethod
    def get_all_with_issue_count():

        return (
            db.session.query(
                Department,
                func.count(Issue.id).label("issue_count")
            )
            .outerjoin(
                Issue,
                Department.id == Issue.department_id
            )
            .group_by(
                Department.id
            )
            .order_by(
                Department.department_name
            )
            .all()
        )