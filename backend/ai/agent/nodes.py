import json

from ai.agent.state import AgentState
from ai.agent.prompt import SYSTEM_PROMPT

from ai.services.intent_service import IntentService

from ai.skills.complaint_status_skill import ComplaintStatusSkill
from ai.skills.policy_skill import PolicySkill
from ai.skills.complaint_registration_skill import RegistrationSkill
from ai.skills.fallback_skill import FallbackSkill

from ai.llm.gemini_client import GeminiClient


def intent_node(
    state: AgentState
) -> AgentState:

    result = IntentService.detect(
        state["message"]
    )

    state["intent"] = result["intent"]

    if result.get("complaint_number"):

        state["selected_complaint"] = result[
            "complaint_number"
        ]

    return state


def complaint_status_node(
    state: AgentState
) -> AgentState:

    return ComplaintStatusSkill.execute(
        state
    )


def policy_node(
    state: AgentState
) -> AgentState:

    return PolicySkill.execute(
        state
    )


def registration_node(
    state: AgentState
) -> AgentState:

    return RegistrationSkill.execute(
        state
    )


def fallback_node(
    state: AgentState
) -> AgentState:

    return FallbackSkill.execute(
        state
    )


def response_node(
    state: AgentState
) -> AgentState:

    # If any skill has already prepared the response,
    # do not call Gemini again.
    if state["response"]:

        return state

    prompt = f"""
{SYSTEM_PROMPT}

Some sections below may be empty depending on the user's request.
Only use the sections that contain information.
Do not mention empty sections.

User Message:
{state["message"]}

Complaint Details:
{json.dumps(
    state["complaint"],
    default=str,
    indent=2
)}

Policy:
{json.dumps(
    state["policy"],
    default=str,
    indent=2
)}

SLA Details:
{json.dumps(
    state["sla"],
    default=str,
    indent=2
)}

Department Notified:
{state["notify"]}

Generate a professional response.
Never invent information.
"""

    response = GeminiClient.client.models.generate_content(

        model="gemini-flash-latest",

        contents=prompt

    )

    state["response"] = response.text

    return state