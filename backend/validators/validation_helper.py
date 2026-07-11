from exceptions.validate_exceptions import ValidationException


class ValidationHelper:

    @staticmethod
    def validate_required_fields(
        data: dict,
        required_fields: list
    ):

        errors = {}

        for field in required_fields:

            if (
                field not in data
                or data[field] is None
                or str(data[field]).strip() == ""
            ):
                errors[field] = (
                    f"{field} is required."
                )

        return errors

    @staticmethod
    def validate_string_length(
        field: str,
        value: str,
        min_length: int,
        max_length: int
    ):

        errors = {}

        value = value.strip()

        if len(value) < min_length:
            errors[field] = (
                f"{field} must be at least {min_length} characters."
            )

        elif len(value) > max_length:
            errors[field] = (
                f"{field} must not exceed {max_length} characters."
            )

        return errors

    @staticmethod
    def validate_positive_integer(
        field: str,
        value: int
    ):

        errors = {}

        if (
            not isinstance(value, int)
            or value <= 0
        ):
            errors[field] = (
                f"{field} must be a positive integer."
            )

        return errors

    @staticmethod
    def validate_latitude(
        latitude: float
    ):

        errors = {}

        if (
            latitude < -90
            or latitude > 90
        ):
            errors["latitude"] = (
                "Invalid latitude."
            )

        return errors

    @staticmethod
    def validate_longitude(
        longitude: float
    ):

        errors = {}

        if (
            longitude < -180
            or longitude > 180
        ):
            errors["longitude"] = (
                "Invalid longitude."
            )

        return errors