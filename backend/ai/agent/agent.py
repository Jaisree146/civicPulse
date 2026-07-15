from ai.agent.graph import graph
from ai.agent.state import AgentState


class CivicPulseAgent:

    @staticmethod
    def invoke(
        citizen_id: int,
        current_user,
        message: str
    ) -> str:

        state: AgentState = {

            "citizen_id": citizen_id,

            "message": message,

            "intent": None,

            "selected_complaint": None,

            "complaints": [],

            "complaint": {},

            "policy": {},

            "sla": {},

            "notify": False,

            "response": ""

        }

        result = graph.invoke(

            state,

            config={
                "configurable": {
                    "thread_id": str(citizen_id)
                }
            }

        )

        return result["response"]