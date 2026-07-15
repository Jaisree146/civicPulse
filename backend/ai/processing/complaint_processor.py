import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from ai.embeddings.embedding_service import EmbeddingService
from ai.processing.category_classifier import CategoryClassifier
from ai.processing.duplicate_detector import DuplicateDetector
from ai.processing.priority_service import PriorityService

from services.complaint_service import ComplaintService
from services.issue_service import IssueService

from common.logger import logger


class ComplaintProcessor:

    @staticmethod
    def process(
        complaint
    ):

        duplicate = DuplicateDetector.detect(
            complaint
        )


        if duplicate is not None:

            issue = duplicate["issue"]

            issue = IssueService.increment_report_count(
                issue.id
            )

            issue.priority = PriorityService.calculate(
                report_count=issue.report_count,
                category=issue.category.category_name,
                created_at=issue.created_at
            )

            issue = IssueService.update(
                issue
            )

            ComplaintService.link_issue(
                complaint.id,
                issue.id
            )

            ComplaintService.mark_processed(
                complaint.id
            )

            logger.info(
                "Complaint %s linked with existing issue %s",
                complaint.id,
                issue.id
            )

            return issue



        classification = (
            CategoryClassifier.classify(
                complaint
            )
        )

        logger.info(
            "Classification Result: %s",
            classification
        )

        embedding = (
            EmbeddingService.generate(
                classification["summary"]
            )
        )

        priority = PriorityService.calculate(
            report_count=1,
            category=classification["category_name"]
        )

        issue = IssueService.create(

            category_id=classification["category_id"],

            summary=classification["summary"],

            latitude=complaint.latitude,

            longitude=complaint.longitude,

            priority=priority,

            embedding=embedding,

            department_id=classification.get(
                "department_id"
            )

        )

        ComplaintService.link_issue(
            complaint.id,
            issue.id
        )

        ComplaintService.mark_processed(
            complaint.id
        )

        logger.info(
            "New issue %s created for complaint %s",
            issue.id,
            complaint.id
        )

        return issue


if __name__ == "__main__":

    from app import app

    with app.app_context():

        complaint = ComplaintService.create(
            citizen_id=1,
            title="Large pothole near bus stand",
            description="There is a huge pothole near the bus stand causing accidents.",
            latitude=22.5726,
            longitude=88.3639
        )

        print(complaint.id)
        print(complaint.issue_id)
        print(complaint.processed)