from common.logger import logger
from common.api_response import ApiResponse
from exceptions.app_exception import AppException
from exceptions.validate_exceptions import (
    ValidationException
)
def register_error_handlers(app):
    @app.errorhandler(AppException)
    def handle_app_exception(error):
        logger.warning(
            "%s: %s",
            error.error_code,
            error.message
        )

        return ApiResponse.error(
            message=error.message,
            status_code=error.status_code,
            error_code=error.error_code
        )

    @app.errorhandler(Exception)
    def handle_internal_server_error(error):

        logger.exception(error)

        return ApiResponse.error(
            message="Internal server error.",
            status_code=500,
            error_code="SYS_001"
        )
    @app.errorhandler(ValidationException)
    def handle_validation(error):

        return ApiResponse.error(
        message=error.message,
        status_code=error.status_code,
        error_code=error.error_code,
        errors=error.errors
        )