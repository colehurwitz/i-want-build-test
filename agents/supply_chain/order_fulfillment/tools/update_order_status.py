from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ord-100", "processing"): {
        "status": "success",
        "order_id": "ORD-100",
        "previous_status": "received",
        "new_status": "processing",
        "notes": "Order confirmed and being processed",
        "updated_at": "2026-07-29T10:00:00Z",
    },
    ("ord-100", "shipped"): {
        "status": "success",
        "order_id": "ORD-100",
        "previous_status": "processing",
        "new_status": "shipped",
        "notes": "Order shipped",
        "updated_at": "2026-07-29T14:00:00Z",
    },
    ("ord-200", "confirmed"): {
        "status": "success",
        "order_id": "ORD-200",
        "previous_status": "received",
        "new_status": "confirmed",
        "notes": "Partial availability — awaiting restock for remaining items",
        "updated_at": "2026-07-29T10:00:00Z",
    },
    ("ord-300", "processing"): {
        "status": "success",
        "order_id": "ORD-300",
        "previous_status": "confirmed",
        "new_status": "processing",
        "notes": "Payment processed, fulfillment created",
        "updated_at": "2026-07-29T11:00:00Z",
    },
    ("ord-300", "shipped"): {
        "status": "success",
        "order_id": "ORD-300",
        "previous_status": "processing",
        "new_status": "shipped",
        "notes": "Order shipped",
        "updated_at": "2026-07-29T15:00:00Z",
    },
    ("ord-400", "processing"): {
        "status": "success",
        "order_id": "ORD-400",
        "previous_status": "received",
        "new_status": "processing",
        "notes": "Payment and fulfillment in progress",
        "updated_at": "2026-07-29T10:00:00Z",
    },
    ("ord-600", "processing"): {
        "status": "success",
        "order_id": "ORD-600",
        "previous_status": "received",
        "new_status": "processing",
        "notes": "Express fulfillment — next day shipping",
        "updated_at": "2026-07-29T09:00:00Z",
    },
    ("ord-600", "shipped"): {
        "status": "success",
        "order_id": "ORD-600",
        "previous_status": "processing",
        "new_status": "shipped",
        "notes": "Express order shipped for next-day delivery",
        "updated_at": "2026-07-29T12:00:00Z",
    },
}


@tool()
def update_order_status(order_id: str, status: str, notes: str):
    """
    Updates the status of a customer order.

    Args:
        order_id: The order identifier (e.g. "ORD-100").
        status: The new status ("received", "confirmed", "processing", "shipped", "delivered", "completed").
        notes: Notes about the status change.

    Returns:
        Update result with previous and new status, or None if the order is not found.
    """
    key = (
        str(order_id).lower().strip(),
        str(status).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
