from common.constants import (
    IssueStatus,
    Priority
)

from validators.validation_helper import ValidationHelper
from exceptions.validate_exceptions import ValidationException


class IssueValidator:

    @staticmethod
    def validate_assign_department(data: dict):

        errors = ValidationHelper.validate_required_fields(
            data,
            [
                "department_id"
            ]
        )

        if errors:
            raise ValidationException(errors)

    @staticmethod
    def validate_status(status: str):

        allowed_status = [
            IssueStatus.ASSIGNED,
            IssueStatus.IN_PROGRESS,
            IssueStatus.RESOLVED,
            IssueStatus.CLOSED
        ]

        if status not in allowed_status:
            raise ValidationException({
                "status": "Invalid issue status."
            })

    @staticmethod
    def validate_priority(priority: str):

        allowed_priority = [
            Priority.LOW,
            Priority.MEDIUM,
            Priority.HIGH,
            Priority.CRITICAL
        ]

        if priority not in allowed_priority:
            raise ValidationException({
                "priority": "Invalid priority."
            })