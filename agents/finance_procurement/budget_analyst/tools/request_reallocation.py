from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("marketing", "engineering", 75000.0): {
        "request_id": "REALLOC-001",
        "status": "pending_cfo_approval",
        "requires_cfo_approval": True,
        "from_dept_remaining_after": -25000.00,
        "to_dept_remaining_after": 875000.00,
        "submitted_at": "2024-06-15",
    },
    ("sales", "engineering", 50000.0): {
        "request_id": "REALLOC-002",
        "status": "pending_cfo_approval",
        "requires_cfo_approval": True,
        "from_dept_remaining_after": 850000.00,
        "to_dept_remaining_after": 850000.00,
        "submitted_at": "2024-06-15",
    },
    ("sales", "marketing", 30000.0): {
        "request_id": "REALLOC-003",
        "status": "approved",
        "requires_cfo_approval": False,
        "from_dept_remaining_after": 870000.00,
        "to_dept_remaining_after": 80000.00,
        "submitted_at": "2024-06-15",
    },
}


@tool()
def request_reallocation(from_dept: str, to_dept: str, amount: float, justification: str):
    """
    Requests a budget reallocation between departments.

    Args:
        from_dept: The source department to transfer budget from.
        to_dept: The destination department to receive budget.
        amount: The amount in USD to reallocate.
        justification: The business justification for the reallocation.

    Returns:
        Reallocation request details including request_id, status, and whether CFO approval is required, or None if request failed.
    """
    key = (
        str(from_dept).lower().strip(),
        str(to_dept).lower().strip(),
        float(amount),
    )
    return STUB_RESPONSES.get(key)
