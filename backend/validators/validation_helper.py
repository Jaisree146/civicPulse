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