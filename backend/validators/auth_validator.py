from email import errors

from validators.validation_helper import ValidationHelper

from exceptions.validate_exceptions import (
    ValidationException
)


class AuthValidator:

    @staticmethod
    def validate_register(data):

        errors = ValidationHelper.validate_required_fields(
            data,
            [
                "full_name",
                "email",
                "password",
                "phone"
            ]
        )

        if errors:
            raise ValidationException(errors)

    @staticmethod
    def validate_login(data):

        errors = ValidationHelper.validate_required_fields(
            data,
            [
                "email",
                "password"
            ]
        )

        if errors:
            raise ValidationException(errors)
    
    @staticmethod
    def validate_change_password(data):

        errors = ValidationHelper.validate_required_fields(
        data,
        [
            "old_password",
            "new_password",
            "confirm_password"
        ]
        )

        if (
        "new_password" in data
        and "confirm_password" in data
        and data["new_password"] != data["confirm_password"]
        ):
            errors["confirm_password"] = (
            "Passwords do not match."
            )

        if errors:
            raise ValidationException(errors)