from exceptions.app_exception import AppException


class DepartmentNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Department not found.",
            status_code=404,
            error_code="DEPT_001"
        )