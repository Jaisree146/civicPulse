from datetime import datetime, timezone

from common.constants import Priority


class PriorityService:

    CATEGORY_SCORE = {
        "Road Damage": 25,
        "Water Leakage": 25,
        "Drainage": 20,
        "Street Light": 15,
        "Garbage": 10
    }

    @staticmethod
    def calculate(
        report_count: int,
        category: str,
        created_at=None
    ) -> str:

        score = 0

   

        if report_count >= 20:
            score += 40
        elif report_count >= 10:
            score += 30
        elif report_count >= 5:
            score += 20
        else:
            score += 10

      

        score += PriorityService.CATEGORY_SCORE.get(
            category,
            10
        )

       

        if created_at is not None:

            age_days = (
                datetime.now(timezone.utc)
                - created_at.replace(tzinfo=timezone.utc)
            ).days

            if age_days >= 30:
                score += 30
            elif age_days >= 15:
                score += 20
            elif age_days >= 7:
                score += 10

        

        if score >= 80:
            return Priority.CRITICAL

        if score >= 55:
            return Priority.HIGH

        if score >= 30:
            return Priority.MEDIUM

        return Priority.LOW