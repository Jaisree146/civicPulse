from exceptions.app_exception import AppException


class ComplaintNotFoundException(
    AppException
):

    def __init__(self):

        super().__init__(
            message="Complaint not found.",
            error_code="CMP_001",
            status_code=404
        )


class ComplaintAlreadyProcessedException(
    AppException
):

    def __init__(self):

        super().__init__(
            message="Complaint has already been processed.",
            error_code="CMP_002",
            status_code=400
        )