from models.department import Department


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