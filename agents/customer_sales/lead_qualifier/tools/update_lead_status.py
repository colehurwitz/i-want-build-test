from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("l-100", "qualified"): {
        "lead_id": "L-100",
        "previous_status": "new",
        "new_status": "qualified",
        "updated_at": "2024-03-15T14:00:00Z",
    },
    ("l-200", "qualified"): {
        "lead_id": "L-200",
        "previous_status": "contacted",
        "new_status": "qualified",
        "updated_at": "2024-03-15T14:30:00Z",
    },
    ("l-100", "assigned"): {
        "lead_id": "L-100",
        "previous_status": "qualified",
        "new_status": "assigned",
        "updated_at": "2024-03-15T15:00:00Z",
    },
    ("l-300", "disqualified"): {
        "lead_id": "L-300",
        "previous_status": "new",
        "new_status": "disqualified",
        "updated_at": "2024-03-15T15:30:00Z",
    },
    ("l-400", "qualified"): {
        "lead_id": "L-400",
        "previous_status": "new",
        "new_status": "qualified",
        "updated_at": "2024-03-15T16:00:00Z",
    },
}


@tool()
def update_lead_status(lead_id: str, status: str, notes: str):
    """
    Updates the status of a sales lead.

    Args:
        lead_id: The unique lead identifier (e.g. "L-100").
        status: The new status (e.g. "new", "contacted", "qualified", "disqualified", "assigned").
        notes: Notes explaining the status change.

    Returns:
        Status update confirmation including previous and new status, or None if update failed.
    """
    key = (
        str(lead_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
