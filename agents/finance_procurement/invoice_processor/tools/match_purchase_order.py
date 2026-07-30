from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "po-2001": {
        "po_number": "PO-2001",
        "po_amount": 12500.00,
        "items": [
            {"item": "Office chairs", "quantity": 50, "unit_price": 250.00},
        ],
        "approved_by": "VP Operations",
        "remaining_amount": 12500.00,
        "status": "open",
    },
    "po-2002": {
        "po_number": "PO-2002",
        "po_amount": 7500.00,
        "items": [
            {"item": "Monitors", "quantity": 25, "unit_price": 300.00},
        ],
        "approved_by": "IT Director",
        "remaining_amount": 7500.00,
        "status": "open",
    },
    "po-2003": {
        "po_number": "PO-2003",
        "po_amount": 4500.00,
        "items": [
            {"item": "Cloud hosting", "quantity": 1, "unit_price": 4500.00},
        ],
        "approved_by": "CTO",
        "remaining_amount": 4500.00,
        "status": "open",
    },
    "po-2004": {
        "po_number": "PO-2004",
        "po_amount": 3200.00,
        "items": [
            {"item": "Standing desks", "quantity": 8, "unit_price": 400.00},
        ],
        "approved_by": "Facilities Manager",
        "remaining_amount": 3200.00,
        "status": "open",
    },
    "po-2005": {
        "po_number": "PO-2005",
        "po_amount": 14000.00,
        "items": [
            {"item": "Laptops", "quantity": 10, "unit_price": 1400.00},
        ],
        "approved_by": "IT Director",
        "remaining_amount": 14000.00,
        "status": "open",
    },
}


@tool()
def match_purchase_order(po_number: str):
    """
    Retrieves purchase order details for matching against an invoice.

    Args:
        po_number: The purchase order number (e.g. "PO-2001").

    Returns:
        PO details including po_amount, items, approved_by, and remaining_amount, or None if PO not found.
    """
    normalized = str(po_number).lower().strip()
    return STUB_RESPONSES.get(normalized)
