from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inv-1001", "ap-mgr-001"): {
        "payment_id": "PAY-3001",
        "scheduled_date": "2024-04-12",
        "status": "approved",
        "amount": 12500.00,
    },
    ("inv-1003", "ap-mgr-001"): {
        "payment_id": "PAY-3003",
        "scheduled_date": "2024-04-18",
        "status": "approved",
        "amount": 4500.00,
    },
    ("inv-1004", "ap-mgr-001"): {
        "payment_id": "PAY-3004",
        "scheduled_date": "2024-04-22",
        "status": "approved",
        "amount": 3200.00,
    },
    ("inv-1005", "ap-mgr-001"): {
        "payment_id": "PAY-3005",
        "scheduled_date": "2024-04-02",
        "status": "approved",
        "amount": 15000.00,
    },
}


@tool()
def approve_payment(invoice_id: str, approver_id: str):
    """
    Approves an invoice for payment after verification.

    Args:
        invoice_id: The invoice identifier (e.g. "INV-1001").
        approver_id: The payment approver's ID (e.g. "AP-MGR-001").

    Returns:
        Payment approval details including payment_id, scheduled_date, and status, or None if approval failed.
    """
    key = (
        str(invoice_id).lower().strip(),
        str(approver_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
