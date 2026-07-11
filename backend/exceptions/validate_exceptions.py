from exceptions.app_exception import AppException


class ValidationException(AppException):

    def __init__(self, errors):

        super().__init__(
            message="Validation failed.",
            status_code=400,
            error_code="VAL_001"
        )

        self.errors = errors