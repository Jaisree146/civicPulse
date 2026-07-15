from langgraph.graph import (
    StateGraph,
    START,
    END
)

from ai.agent.state import AgentState

from ai.agent.nodes import (
    intent_node,
    complaint_status_node,
    policy_node,
    registration_node,
    fallback_node,
    response_node
)

from ai.agent.router import (
    route_intent
)


workflow = StateGraph(
    AgentState
)


workflow.add_node(
    "intent",
    intent_node
)

workflow.add_node(
    "complaint_status",
    complaint_status_node
)

workflow.add_node(
    "policy",
    policy_node
)

workflow.add_node(
    "registration",
    registration_node
)

workflow.add_node(
    "fallback",
    fallback_node
)

workflow.add_node(
    "response",
    response_node
)



workflow.add_edge(
    START,
    "intent"
)



workflow.add_conditional_edges(

    "intent",

    route_intent,

    {

        "complaint_status":
            "complaint_status",

        "policy":
            "policy",

        "registration":
            "registration",

        "fallback":
            "fallback"

    }

)

workflow.add_edge(
    "complaint_status",
    "response"
)

workflow.add_edge(
    "policy",
    "response"
)

workflow.add_edge(
    "registration",
    "response"
)

workflow.add_edge(
    "fallback",
    "response"
)



workflow.add_edge(
    "response",
    END
)


from ai.agent.memory import memory

graph = workflow.compile(

    checkpointer=memory

)