from ai.agent.state import AgentState

def route_intent(
    state: AgentState
):

    intent = state["intent"]

    if intent == "complaint_status":
        return "complaint_status"

    if intent == "select_complaint":
        return "complaint_status"

    if intent == "policy_query":
        return "policy"

    if intent == "complaint_registration":
        return "registration"

    return "fallback"