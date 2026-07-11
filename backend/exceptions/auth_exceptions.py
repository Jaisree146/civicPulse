from exceptions.app_exception import AppException


class AuthenticationException(AppException):

    def __init__(
        self,
        message="Authentication failed.",
        status_code=401,
        error_code="AUTH_000"
    ):
        super().__init__(
            message,
            status_code,
            error_code
        )


class UserAlreadyExistsException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "An account with this email already exists.",
            409,
            "AUTH_001"
        )


class UserNotFoundException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "User not found.",
            404,
            "AUTH_002"
        )


class InvalidCredentialsException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Invalid email or password.",
            401,
            "AUTH_003"
        )


class RoleNotFoundException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Required role does not exist.",
            404,
            "AUTH_004"
        )


class InvalidAccessTokenException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Invalid or expired access token.",
            401,
            "AUTH_005"
        )


class InvalidRefreshTokenException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Invalid or expired refresh token.",
            401,
            "AUTH_006"
        )


class RefreshTokenRevokedException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Refresh token has been revoked.",
            401,
            "AUTH_007"
        )


class RefreshTokenMissingException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Refresh token is missing.",
            401,
            "AUTH_008"
        )
class InvalidOldPasswordException(AuthenticationException):

    def __init__(self):
        super().__init__(
            "Old password is incorrect.",
            401,
            "AUTH_009"
        )