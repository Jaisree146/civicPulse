from services.complaint_service import ComplaintService


class ComplaintTool:

    def __init__(
        self,
        citizen_id: int
    ):

        self.citizen_id = citizen_id

    def get_pending_complaints(self):

        complaints = (
            ComplaintService.get_pending_by_citizen_id(
                self.citizen_id
            )
        )

        return [

            {
                "id": complaint.id,
                "complaint_number": complaint.complaint_number,
                "status": complaint.status
            }

            for complaint in complaints

        ]

    def get_complaint_details(

        self,

        complaint_number: str

    ):

        complaint = ComplaintService.get_by_number(

            complaint_number,

            self.citizen_id

        )

        issue = complaint.issue

        return {

            "id": complaint.id,

            "complaint_number": complaint.complaint_number,

            "title": complaint.title,

            "description": complaint.description,

            "summary": (
                issue.summary
                if issue
                else None
            ),

            "status": complaint.status,

            "created_at": complaint.created_at,

            "latitude": complaint.latitude,

            "longitude": complaint.longitude,

            "category": (
                issue.category.category_name
                if issue
                else None
            ),

            "issue_id": (
                issue.id
                if issue
                else None
            ),

            "priority": (
                issue.priority
                if issue
                else None
            ),

            "department": (
                issue.department.department_name
                if issue and issue.department
                else None
            ),

            "department_assigned": (
                issue.department is not None
                if issue
                else False
            ),

            "sla_notification_sent": (
                issue.sla_notification_sent
                if issue
                else False
            )

        }