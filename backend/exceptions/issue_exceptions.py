from exceptions.app_exception import AppException


class IssueNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Issue not found.",
            status_code=404,
            error_code="ISSUE_001"
        )


class InvalidIssueStatusException(AppException):

    def __init__(self):
        super().__init__(
            message="Invalid issue status.",
            status_code=400,
            error_code="ISSUE_002"
        )