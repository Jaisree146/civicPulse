from exceptions.app_exception import AppException


class CategoryNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Category not found.",
            status_code=404,
            error_code="CAT_001"
        )