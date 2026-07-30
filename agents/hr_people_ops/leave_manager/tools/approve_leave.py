from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("lr-001", "m-100", "approved"): {
        "request_id": "LR-001",
        "status": "approved",
        "approved_by": "M-100",
        "approved_date": "2024-12-02",
        "effective_dates": "2024-12-23 to 2024-12-27",
    },
    ("lr-002", "m-100", "approved"): {
        "request_id": "LR-002",
        "status": "approved",
        "approved_by": "M-100",
        "approved_date": "2024-11-11",
        "effective_dates": "2024-11-18 to 2024-11-20",
    },
    ("lr-003", "m-200", "approved"): {
        "request_id": "LR-003",
        "status": "approved",
        "approved_by": "M-200",
        "approved_date": "2024-11-11",
        "effective_dates": "2024-11-12 to 2024-11-12",
    },
    ("lr-005", "m-100", "approved"): {
        "request_id": "LR-005",
        "status": "approved",
        "approved_by": "M-100",
        "approved_date": "2024-11-16",
        "effective_dates": "2024-11-22 to 2024-11-25",
    },
}


@tool()
def approve_leave(request_id: str, manager_id: str, decision: str, comments: str):
    """
    Approves or denies a leave request.

    Args:
        request_id: The leave request ID (e.g. "LR-001"), returned by the request_leave tool.
        manager_id: The approving manager's ID (e.g. "M-100").
        decision: The approval decision ("approved" or "denied").
        comments: Comments from the manager about the decision.

    Returns:
        The approval result with status and effective dates, or None if the request was not found.
    """
    key = (
        str(request_id).lower().strip(),
        str(manager_id).lower().strip(),
        str(decision).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
