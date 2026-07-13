from models.category import Category


class CategoryRepository:

    @staticmethod
    def get_all():

        return Category.query.order_by(
            Category.category_name.asc()
        ).all()

    @staticmethod
    def get_by_id(
        category_id: int
    ):

        return Category.query.filter_by(
            id=category_id
        ).first()

    @staticmethod
    def get_by_name(
        category_name: str
    ):

        return Category.query.filter_by(
            category_name=category_name
        ).first()