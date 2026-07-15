from ai.agent.state import AgentState


class FallbackSkill:

    @staticmethod
    def execute(
        state: AgentState
    ) -> AgentState:

        state["response"] = """
Sorry, I couldn't understand your request.

I can help you with:

• Complaint status
• Municipal policies
• Complaint registration
"""

        return state