from typing import TypedDict, Optional


class AgentState(TypedDict):

    citizen_id: int

    current_user: object

    message: str

    intent: Optional[str]

    selected_complaint: Optional[str]

    complaints: list

    complaint: dict

    policy: dict

    sla: dict

    notify: bool

    response: str