from ai.agent.state import AgentState
from ai.rag.rag_service import RagService


class PolicySkill:

    @staticmethod
    def execute(
        state: AgentState
    ) -> AgentState:

        policy = RagService.retrieve_policy(
            state["message"]
        )

        if policy["resolution_days"] is None:

            state["response"] = (
                "Sorry, I couldn't find any relevant municipal policy."
            )

            return state

        state["policy"] = policy

        return state