from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("q-7002", "req-6001", "mgr-eng-001"): {
        "po_id": "PO-8001",
        "status": "issued",
        "vendor": "ErgoSupply Co",
        "total_amount": 6750.00,
        "estimated_delivery": "2024-06-28",
        "payment_terms": "Net 30",
    },
    ("q-7004", "req-6002", "dir-ops-001"): {
        "po_id": "PO-8002",
        "status": "issued",
        "vendor": "ServerMax",
        "total_amount": 47500.00,
        "estimated_delivery": "2024-06-22",
        "payment_terms": "Net 15",
    },
    ("q-7007", "req-6003", "vp-it-001"): {
        "po_id": "PO-8003",
        "status": "issued",
        "vendor": "ScreenPro Global",
        "total_amount": 38000.00,
        "estimated_delivery": "2024-07-10",
        "payment_terms": "Net 30",
    },
    ("q-7009", "req-6004", "mgr-pm-001"): {
        "po_id": "PO-8004",
        "status": "issued",
        "vendor": "SoundGear Inc",
        "total_amount": 1500.00,
        "estimated_delivery": "2024-06-30",
        "payment_terms": "Net 30",
    },
}


@tool()
def issue_purchase_order(quote_id: str, req_id: str, approver_id: str):
    """
    Issues a purchase order based on a selected quote.

    Args:
        quote_id: The selected quote ID (e.g. "Q-7002").
        req_id: The associated requisition ID (e.g. "REQ-6001").
        approver_id: The approver's ID — must be the requester's manager or VP for large orders.

    Returns:
        PO details including po_id, status, vendor, total_amount, and estimated_delivery, or None if PO creation failed.
    """
    key = (
        str(quote_id).lower().strip(),
        str(req_id).lower().strip(),
        str(approver_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
