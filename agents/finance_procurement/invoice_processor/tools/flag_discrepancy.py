from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inv-1002", "price_mismatch"): {
        "flag_id": "FLAG-4001",
        "review_assigned_to": "AP Supervisor",
        "priority": "medium",
        "status": "under_review",
    },
    ("inv-1005", "price_mismatch"): {
        "flag_id": "FLAG-4002",
        "review_assigned_to": "AP Manager",
        "priority": "high",
        "status": "under_review",
    },
    ("inv-1006", "missing_po"): {
        "flag_id": "FLAG-4003",
        "review_assigned_to": "Procurement Team",
        "priority": "medium",
        "status": "under_review",
    },
}


@tool()
def flag_discrepancy(invoice_id: str, discrepancy_type: str, details: str):
    """
    Flags an invoice discrepancy for review by the accounts payable team.

    Args:
        invoice_id: The invoice identifier (e.g. "INV-1002").
        discrepancy_type: The type of discrepancy ("price_mismatch", "quantity_mismatch", "missing_po", "duplicate_invoice", "invalid_vendor").
        details: A description of the specific discrepancy found.

    Returns:
        Flag details including flag_id, review_assigned_to, and priority, or None if flagging failed.
    """
    key = (
        str(invoice_id).lower().strip(),
        str(discrepancy_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
