from ai.agent.state import AgentState

from ai.tools.complaint_tool import ComplaintTool
from ai.rag.rag_service import RagService
from ai.services.sla_service import SlaService
from ai.tools.notification_tool import NotificationTool

from services.issue_service import IssueService


class ComplaintStatusSkill:

    @staticmethod
    def execute(
        state: AgentState
    ) -> AgentState:

        complaint_tool = ComplaintTool(

            citizen_id=state["citizen_id"]

        )

        complaints = complaint_tool.get_pending_complaints()

        if not complaints:

            state["response"] = (
                "You don't have any active complaints."
            )

            return state

        if state.get("selected_complaint") is None:

            if len(complaints) == 1:

                state["selected_complaint"] = complaints[0][
                    "complaint_number"
                ]

            else:

                state["complaints"] = complaints

                state["response"] = (
                    "Please choose one of the following complaints:\n\n"
                    + "\n".join(
                        c["complaint_number"]
                        for c in complaints
                    )
                )

                return state

        complaint = complaint_tool.get_complaint_details(

            state["selected_complaint"]

        )

        state["complaint"] = complaint

        policy = RagService.retrieve_policy(

            complaint["category"]

        )

        if policy["resolution_days"] is None:

            state["response"] = (
                "No municipal policy was found for this complaint."
            )

            return state

        state["policy"] = policy

        sla = SlaService.evaluate(

            complaint["created_at"],

            policy["resolution_days"]

        )

        state["sla"] = sla

        notify = False

        if (

            sla["overdue"]

            and

            not complaint["sla_notification_sent"]

        ):

            NotificationTool.notify_department(

                complaint["issue_id"]

            )

            IssueService.mark_sla_notification_sent(

                complaint["issue_id"]

            )

            notify = True

        state["notify"] = notify

        return state