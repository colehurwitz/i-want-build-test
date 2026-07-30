from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("eng-mgr-001", "ergonomic keyboards", 50, 7500.0, "standard"): {
        "req_id": "REQ-6001",
        "status": "approved",
        "budget_check_result": "within_budget",
        "estimated_total": 7500.00,
        "created_at": "2024-06-15",
    },
    ("ops-lead-001", "replacement servers", 5, 50000.0, "emergency"): {
        "req_id": "REQ-6002",
        "status": "approved",
        "budget_check_result": "within_budget",
        "estimated_total": 50000.00,
        "created_at": "2024-06-15",
        "urgency_note": "Emergency requisition — expedited processing",
    },
    ("admin-001", "monitors", 100, 45000.0, "standard"): {
        "req_id": "REQ-6003",
        "status": "approved",
        "budget_check_result": "within_budget",
        "estimated_total": 45000.00,
        "created_at": "2024-06-15",
    },
    ("pm-001", "headsets", 20, 3000.0, "standard"): {
        "req_id": "REQ-6004",
        "status": "approved",
        "budget_check_result": "within_budget",
        "estimated_total": 3000.00,
        "created_at": "2024-06-15",
    },
}


@tool()
def create_requisition(requester_id: str, item_description: str, quantity: int, estimated_cost: float, urgency: str):
    """
    Creates a purchase requisition with budget validation.

    Args:
        requester_id: The requester's employee ID (e.g. "ENG-MGR-001").
        item_description: Description of the item to purchase (e.g. "ergonomic keyboards").
        quantity: Number of items to purchase.
        estimated_cost: Estimated total cost in USD.
        urgency: Urgency level ("standard", "expedited", "emergency").

    Returns:
        Requisition details including req_id, status, and budget_check_result, or None if creation failed.
    """
    key = (
        str(requester_id).lower().strip(),
        str(item_description).lower().strip(),
        int(quantity),
        float(estimated_cost),
        str(urgency).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
