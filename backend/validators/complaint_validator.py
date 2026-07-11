from exceptions.validate_exceptions import ValidationException
from validators.validation_helper import ValidationHelper


class ComplaintValidator:

    @staticmethod
    def validate_create(data: dict):

        errors = {}

        errors.update(
            ValidationHelper.validate_required_fields(
                data,
                [
                    "title",
                    "description",
                    "latitude",
                    "longitude"
                ]
            )
        )

        if errors:
            raise ValidationException(errors)

        errors.update(
            ValidationHelper.validate_string_length(
                "title",
                data["title"],
                min_length=5,
                max_length=255
            )
        )

        errors.update(
            ValidationHelper.validate_string_length(
                "description",
                data["description"],
                min_length=10,
                max_length=5000
            )
        )

        errors.update(
            ValidationHelper.validate_latitude(
                data["latitude"]
            )
        )

        errors.update(
            ValidationHelper.validate_longitude(
                data["longitude"]
            )
        )

        if errors:
            raise ValidationException(errors)