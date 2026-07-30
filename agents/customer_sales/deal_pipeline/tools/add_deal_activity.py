from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("d-100", "demo"): {
        "activity_id": "ACT-2001",
        "deal_id": "D-100",
        "activity_type": "demo",
        "status": "logged",
        "created_at": "2024-03-15T10:30:00Z",
    },
    ("d-100", "follow_up"): {
        "activity_id": "ACT-2001",
        "deal_id": "D-100",
        "activity_type": "follow_up",
        "status": "logged",
        "created_at": "2024-03-15T10:30:00Z",
    },
    ("d-200", "negotiation"): {
        "activity_id": "ACT-2002",
        "deal_id": "D-200",
        "activity_type": "negotiation",
        "status": "logged",
        "created_at": "2024-03-15T11:30:00Z",
    },
    ("d-200", "meeting"): {
        "activity_id": "ACT-2002",
        "deal_id": "D-200",
        "activity_type": "meeting",
        "status": "logged",
        "created_at": "2024-03-15T11:30:00Z",
    },
    ("d-200", "follow_up"): {
        "activity_id": "ACT-2002",
        "deal_id": "D-200",
        "activity_type": "follow_up",
        "status": "logged",
        "created_at": "2024-03-15T11:30:00Z",
    },
    ("d-300", "discovery_call"): {
        "activity_id": "ACT-2003",
        "deal_id": "D-300",
        "activity_type": "discovery_call",
        "status": "logged",
        "created_at": "2024-03-15T12:30:00Z",
    },
    ("d-300", "call"): {
        "activity_id": "ACT-2003",
        "deal_id": "D-300",
        "activity_type": "call",
        "status": "logged",
        "created_at": "2024-03-15T12:30:00Z",
    },
    ("d-300", "follow_up"): {
        "activity_id": "ACT-2003",
        "deal_id": "D-300",
        "activity_type": "follow_up",
        "status": "logged",
        "created_at": "2024-03-15T12:30:00Z",
    },
    ("d-400", "follow_up"): {
        "activity_id": "ACT-2004",
        "deal_id": "D-400",
        "activity_type": "follow_up",
        "status": "logged",
        "created_at": "2024-03-15T13:30:00Z",
    },
    ("d-400", "negotiation"): {
        "activity_id": "ACT-2004",
        "deal_id": "D-400",
        "activity_type": "negotiation",
        "status": "logged",
        "created_at": "2024-03-15T13:30:00Z",
    },
    ("d-400", "meeting"): {
        "activity_id": "ACT-2004",
        "deal_id": "D-400",
        "activity_type": "meeting",
        "status": "logged",
        "created_at": "2024-03-15T13:30:00Z",
    },
    ("d-500", "discovery_call"): {
        "activity_id": "ACT-2005",
        "deal_id": "D-500",
        "activity_type": "discovery_call",
        "status": "logged",
        "created_at": "2024-03-15T14:30:00Z",
    },
    ("d-500", "call"): {
        "activity_id": "ACT-2005",
        "deal_id": "D-500",
        "activity_type": "call",
        "status": "logged",
        "created_at": "2024-03-15T14:30:00Z",
    },
    ("d-700", "discovery_call"): {
        "activity_id": "ACT-2006",
        "deal_id": "D-700",
        "activity_type": "discovery_call",
        "status": "logged",
        "created_at": "2024-03-15T15:30:00Z",
    },
    ("d-700", "call"): {
        "activity_id": "ACT-2006",
        "deal_id": "D-700",
        "activity_type": "call",
        "status": "logged",
        "created_at": "2024-03-15T15:30:00Z",
    },
}


@tool()
def add_deal_activity(deal_id: str, activity_type: str, description: str, next_action_date: str):
    """
    Logs an activity for a deal and schedules the next action.

    Args:
        deal_id: The unique deal identifier (e.g. "D-100").
        activity_type: The type of activity (e.g. "demo", "call", "email", "meeting", "negotiation", "follow_up", "discovery_call").
        description: A description of the activity that took place.
        next_action_date: The date for the next scheduled action (e.g. "2024-04-01").

    Returns:
        Activity confirmation including activity_id and status, or None if logging failed.
    """
    key = (
        str(deal_id).lower().strip(),
        str(activity_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
