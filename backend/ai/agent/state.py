from typing import TypedDict, Optional


class AgentState(TypedDict):

    # User information
    citizen_id: int

    current_user: object

    # Original message
    message: str

    # Intent detected by Gemini
    intent: Optional[str]

    # Complaint selected by citizen
    selected_complaint: Optional[str]

    # Active complaints
    complaints: list

    # Complaint details
    complaint: dict

    # Retrieved municipal policy
    policy: dict

    # SLA evaluation
    sla: dict

    # Department notification status
    notify: bool

    # Final response
    response: str