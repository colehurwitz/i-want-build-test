from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "po-8001": {
        "po_id": "PO-8001",
        "status": "in_transit",
        "current_location": "Distribution Center, Chicago IL",
        "estimated_arrival": "2024-06-28",
        "carrier": "FedEx Ground",
        "shipped_date": "2024-06-18",
    },
    "po-8002": {
        "po_id": "PO-8002",
        "status": "delivered",
        "current_location": "Receiving Dock, HQ Building",
        "estimated_arrival": "2024-06-22",
        "carrier": "UPS Express",
        "shipped_date": "2024-06-17",
        "delivered_date": "2024-06-21",
    },
    "po-5001": {
        "po_id": "PO-5001",
        "status": "partially_delivered",
        "current_location": "Warehouse, Dallas TX",
        "estimated_arrival": "2024-06-25",
        "carrier": "FedEx Freight",
        "shipped_date": "2024-06-15",
        "items_shipped": 10,
        "items_delivered": 8,
    },
}


@tool()
def track_delivery(po_id: str):
    """
    Tracks the delivery status of a purchase order.

    Args:
        po_id: The purchase order ID (e.g. "PO-8001").

    Returns:
        Delivery tracking details including status, current_location, estimated_arrival, and carrier, or None if PO not found.
    """
    normalized = str(po_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
