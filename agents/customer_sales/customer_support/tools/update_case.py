from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("cs-200", "escalated"): {
        "case_id": "CS-200",
        "status": "escalated",
        "updated_at": "2024-03-15T15:00:00Z",
        "updated_by": "support_agent",
    },
    ("cs-300", "resolved"): {
        "case_id": "CS-300",
        "status": "resolved",
        "updated_at": "2024-03-15T10:00:00Z",
        "updated_by": "support_agent",
    },
    ("cs-301", "resolved"): {
        "case_id": "CS-301",
        "status": "resolved",
        "updated_at": "2024-03-15T11:00:00Z",
        "updated_by": "support_agent",
    },
    ("cs-302", "resolved"): {
        "case_id": "CS-302",
        "status": "resolved",
        "updated_at": "2024-03-15T12:00:00Z",
        "updated_by": "support_agent",
    },
    ("cs-400", "resolved"): {
        "case_id": "CS-400",
        "status": "resolved",
        "updated_at": "2024-03-15T13:00:00Z",
        "updated_by": "support_agent",
    },
}


@tool()
def update_case(case_id: str, status: str, resolution: str, internal_notes: str):
    """
    Updates the status and resolution of a support case.

    Args:
        case_id: The unique case identifier (e.g. "CS-200").
        status: The new case status ("open", "in_progress", "resolved", "escalated", "closed").
        resolution: The resolution description or summary of actions taken.
        internal_notes: Internal notes not visible to the customer.

    Returns:
        Update confirmation including case_id and new status, or None if update failed.
    """
    key = (
        str(case_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
