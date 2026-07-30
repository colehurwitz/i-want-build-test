from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("shp-200", "in_transit"): {
        "status": "success",
        "shipment_id": "SHP-200",
        "previous_status": "in_transit",
        "new_status": "in_transit",
        "notes": "Status confirmed, no changes needed",
        "updated_at": "2026-07-29T12:00:00Z",
    },
    ("shp-202", "delayed"): {
        "status": "success",
        "shipment_id": "SHP-202",
        "previous_status": "delayed",
        "new_status": "delayed",
        "notes": "Customer notified of delay",
        "updated_at": "2026-07-29T12:00:00Z",
    },
    ("shp-203", "in_transit"): {
        "status": "success",
        "shipment_id": "SHP-203",
        "previous_status": "pending",
        "new_status": "in_transit",
        "notes": "Shipment picked up by carrier",
        "updated_at": "2026-07-29T14:00:00Z",
    },
}


@tool()
def update_shipment(shipment_id: str, status: str, notes: str):
    """
    Updates the status of an existing shipment.

    Args:
        shipment_id: The shipment identifier (e.g. "SHP-200").
        status: The new status ("pending", "in_transit", "delivered", "delayed", "cancelled").
        notes: Notes about the status update.

    Returns:
        Update result with previous and new status, or None if the shipment is not found.
    """
    key = (
        str(shipment_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
