from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ord-100", "w-1", "standard"): {
        "fulfillment_id": "FUL-100",
        "order_id": "ORD-100",
        "warehouse_id": "W-1",
        "shipping_priority": "standard",
        "tracking_number": "TRK-FUL-100",
        "estimated_ship_date": "2026-07-31",
        "status": "created",
    },
    ("ord-300", "w-1", "standard"): {
        "fulfillment_id": "FUL-300",
        "order_id": "ORD-300",
        "warehouse_id": "W-1",
        "shipping_priority": "standard",
        "tracking_number": "TRK-FUL-300",
        "estimated_ship_date": "2026-07-31",
        "status": "created",
    },
    ("ord-400", "w-1", "standard"): {
        "fulfillment_id": "FUL-400",
        "order_id": "ORD-400",
        "warehouse_id": "W-1",
        "shipping_priority": "standard",
        "tracking_number": "TRK-FUL-400",
        "estimated_ship_date": "2026-07-31",
        "status": "created",
    },
    ("ord-600", "w-1", "next_day"): {
        "fulfillment_id": "FUL-600",
        "order_id": "ORD-600",
        "warehouse_id": "W-1",
        "shipping_priority": "next_day",
        "tracking_number": "TRK-FUL-600",
        "estimated_ship_date": "2026-07-30",
        "status": "created",
    },
}


@tool()
def create_fulfillment(order_id: str, warehouse_id: str, shipping_priority: str):
    """
    Creates a fulfillment record to trigger warehouse picking and shipping.

    Args:
        order_id: The order identifier (e.g. "ORD-100").
        warehouse_id: The warehouse to fulfill from (e.g. "W-1").
        shipping_priority: Shipping priority ("standard", "express", "next_day").

    Returns:
        Fulfillment details with tracking number and estimated ship date, or None if creation failed.
    """
    key = (
        str(order_id).lower().strip(),
        str(warehouse_id).lower().strip(),
        str(shipping_priority).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
