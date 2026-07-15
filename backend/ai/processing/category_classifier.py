import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from ..llm.llm_service import LLMService

from exceptions.category_exceptions import (
    CategoryNotFoundException
)

from repositories.category_repository import (
    CategoryRepository
)
from repositories.department_repository import (
    DepartmentRepository
)


class CategoryClassifier:

    @staticmethod
    def classify(
        complaint
    ) -> dict:

        result = LLMService.analyze(
            title=complaint.title,
            description=complaint.description
        )

        category = CategoryRepository.get_by_name(
            result["category"]
        )

        if category is None:
            raise CategoryNotFoundException()

        department = None
        if result.get("department"):
            department = DepartmentRepository.get_by_name(
                result["department"]
            )

        return {
            "category_id": category.id,
            "category_name":category.category_name,
            "summary": result["summary"],
            "department_id": department.id if department else None

        }