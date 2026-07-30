from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "inv-1001": {
        "invoice_id": "INV-1001",
        "vendor": "Acme Supplies",
        "amount": 12500.00,
        "line_items": [
            {"item": "Office chairs", "quantity": 50, "unit_price": 250.00},
        ],
        "due_date": "2024-04-15",
        "status": "pending",
        "po_number": "PO-2001",
    },
    "inv-1002": {
        "invoice_id": "INV-1002",
        "vendor": "Tech Hardware Inc",
        "amount": 8750.00,
        "line_items": [
            {"item": "Monitors", "quantity": 25, "unit_price": 350.00},
        ],
        "due_date": "2024-04-10",
        "status": "pending",
        "po_number": "PO-2002",
    },
    "inv-1003": {
        "invoice_id": "INV-1003",
        "vendor": "Cloud Services Corp",
        "amount": 4500.00,
        "line_items": [
            {"item": "Cloud hosting", "quantity": 1, "unit_price": 4500.00},
        ],
        "due_date": "2024-04-20",
        "status": "pending",
        "po_number": "PO-2003",
    },
    "inv-1004": {
        "invoice_id": "INV-1004",
        "vendor": "Acme Supplies",
        "amount": 3200.00,
        "line_items": [
            {"item": "Standing desks", "quantity": 8, "unit_price": 400.00},
        ],
        "due_date": "2024-04-25",
        "status": "pending",
        "po_number": "PO-2004",
    },
    "inv-1005": {
        "invoice_id": "INV-1005",
        "vendor": "Tech Hardware Inc",
        "amount": 15000.00,
        "line_items": [
            {"item": "Laptops", "quantity": 10, "unit_price": 1500.00},
        ],
        "due_date": "2024-04-05",
        "status": "overdue",
        "po_number": "PO-2005",
    },
    "inv-1006": {
        "invoice_id": "INV-1006",
        "vendor": "Metro Utilities",
        "amount": 2200.00,
        "line_items": [
            {"item": "Electricity", "quantity": 1, "unit_price": 2200.00},
        ],
        "due_date": "2024-04-30",
        "status": "pending",
        "po_number": None,
    },
}


@tool()
def lookup_invoice(invoice_id: str):
    """
    Looks up an invoice by its ID and returns full details.

    Args:
        invoice_id: The invoice identifier (e.g. "INV-1001").

    Returns:
        Invoice details including vendor, amount, line_items, due_date, status, and po_number, or None if not found.
    """
    normalized = str(invoice_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
