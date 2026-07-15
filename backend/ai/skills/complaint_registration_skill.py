from ai.agent.state import AgentState


class RegistrationSkill:

    @staticmethod
    def execute(
        state: AgentState
    ) -> AgentState:

        state["response"] = """
To register a complaint, please provide the following details:

• Complaint Title
• Complaint Description
• Location (Latitude & Longitude)

Once all the required information is available, the complaint can be registered successfully.
"""

        return state