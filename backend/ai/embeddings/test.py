import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from app import app
from ai.processing.category_classifier import CategoryClassifier


class Complaint:

    title = "Huge pothole near bus stand"

    description = (
        "The road has a huge pothole "
        "causing accidents."
    )


with app.app_context():
    result = CategoryClassifier.classify(
        Complaint()
    )

print(result)