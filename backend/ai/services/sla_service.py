from datetime import datetime, timezone


class SlaService:

    @staticmethod
    def evaluate(created_at,sla_days: int) -> dict:

        today = datetime.now(timezone.utc)
        if created_at.tzinfo is None:

            created_at = created_at.replace(
                tzinfo=timezone.utc
            )

        days_elapsed = (today.date() -created_at.date()).days

        return {

            "today": today.strftime(
                "%d-%m-%Y"
            ),

            "created_at": created_at.strftime(
                "%d-%m-%Y"
            ),

            "days_elapsed": days_elapsed,

            "sla_days": sla_days,

            "overdue": days_elapsed > sla_days
        }