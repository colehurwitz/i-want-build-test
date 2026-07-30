from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("inv-1001", "po-2001"): {
        "matched_items": [
            {"item": "Office chairs", "invoice_qty": 50, "po_qty": 50, "invoice_price": 250.00, "po_price": 250.00},
        ],
        "discrepancies": [],
        "match_percentage": 100.0,
    },
    ("inv-1002", "po-2002"): {
        "matched_items": [
            {"item": "Monitors", "invoice_qty": 25, "po_qty": 25, "invoice_price": 350.00, "po_price": 300.00},
        ],
        "discrepancies": [
            {"item": "Monitors", "type": "price_mismatch", "invoice_value": 350.00, "po_value": 300.00, "difference": 50.00},
        ],
        "match_percentage": 71.4,
    },
    ("inv-1003", "po-2003"): {
        "matched_items": [
            {"item": "Cloud hosting", "invoice_qty": 1, "po_qty": 1, "invoice_price": 4500.00, "po_price": 4500.00},
        ],
        "discrepancies": [],
        "match_percentage": 100.0,
    },
    ("inv-1004", "po-2004"): {
        "matched_items": [
            {"item": "Standing desks", "invoice_qty": 8, "po_qty": 8, "invoice_price": 400.00, "po_price": 400.00},
        ],
        "discrepancies": [],
        "match_percentage": 100.0,
    },
    ("inv-1005", "po-2005"): {
        "matched_items": [
            {"item": "Laptops", "invoice_qty": 10, "po_qty": 10, "invoice_price": 1500.00, "po_price": 1400.00},
        ],
        "discrepancies": [
            {"item": "Laptops", "type": "price_mismatch", "invoice_value": 1500.00, "po_value": 1400.00, "difference": 100.00},
        ],
        "match_percentage": 93.3,
    },
}


@tool()
def verify_line_items(invoice_id: str, po_number: str):
    """
    Verifies that invoice line items match the corresponding purchase order.

    Args:
        invoice_id: The invoice identifier (e.g. "INV-1001").
        po_number: The purchase order number to compare against (e.g. "PO-2001").

    Returns:
        Verification results including matched_items, discrepancies list, and match_percentage, or None if verification failed.
    """
    key = (
        str(invoice_id).lower().strip(),
        str(po_number).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
