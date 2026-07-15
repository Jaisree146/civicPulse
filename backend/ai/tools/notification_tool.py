from common.logger import logger

from services.issue_service import IssueService


class NotificationTool:

    @staticmethod
    def notify_department(
        issue_id: int
    ) -> dict:

        issue = IssueService.get_by_id(
            issue_id
        )

        logger.info(

            "Department notified for Issue %s (%s)",

            issue.issue_number,

            issue.summary

        )

        return {

            "success": True,

            "message": f"Department notified for {issue.issue_number}"

        }