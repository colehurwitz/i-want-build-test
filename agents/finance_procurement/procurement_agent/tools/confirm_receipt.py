from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("po-8002", 5, "new"): {
        "receipt_id": "REC-9001",
        "status": "complete",
        "discrepancy_flag": False,
        "received_quantity": 5,
        "expected_quantity": 5,
        "condition_report": "All items received in new condition",
    },
    ("po-5001", 8, "good"): {
        "receipt_id": "REC-9002",
        "status": "partial",
        "discrepancy_flag": True,
        "received_quantity": 8,
        "expected_quantity": 10,
        "condition_report": "8 of 10 items received in good condition. 2 items still pending delivery.",
    },
    ("po-8001", 50, "new"): {
        "receipt_id": "REC-9003",
        "status": "complete",
        "discrepancy_flag": False,
        "received_quantity": 50,
        "expected_quantity": 50,
        "condition_report": "All 50 ergonomic keyboards received in new condition",
    },
}


@tool()
def confirm_receipt(po_id: str, received_quantity: int, condition: str):
    """
    Confirms receipt of goods for a purchase order.

    Args:
        po_id: The purchase order ID (e.g. "PO-8001").
        received_quantity: Number of items actually received.
        condition: Condition of received items ("new", "good", "damaged", "mixed").

    Returns:
        Receipt confirmation including receipt_id, status, discrepancy_flag, and condition_report, or None if confirmation failed.
    """
    key = (
        str(po_id).lower().strip(),
        int(received_quantity),
        str(condition).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
