from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    "ord-100": {
        "status": "reserved",
        "order_id": "ORD-100",
        "reservation_id": "RES-100",
        "items_reserved": [
            {"product_id": "P-100", "quantity": 100, "warehouse_id": "W-1"},
            {"product_id": "P-200", "quantity": 500, "warehouse_id": "W-1"},
        ],
        "expires_at": "2026-08-01T00:00:00Z",
    },
    "ord-200": {
        "status": "partial",
        "order_id": "ORD-200",
        "reservation_id": "RES-200",
        "items_reserved": [
            {"product_id": "P-400", "quantity": 50, "warehouse_id": "W-2"},
        ],
        "items_failed": [
            {"product_id": "P-300", "quantity": 200, "reason": "insufficient_stock"},
        ],
        "expires_at": "2026-08-01T00:00:00Z",
    },
    "ord-300": {
        "status": "reserved",
        "order_id": "ORD-300",
        "reservation_id": "RES-300",
        "items_reserved": [
            {"product_id": "P-500", "quantity": 300, "warehouse_id": "W-1"},
        ],
        "expires_at": "2026-08-01T00:00:00Z",
    },
    "ord-400": {
        "status": "reserved",
        "order_id": "ORD-400",
        "reservation_id": "RES-400",
        "items_reserved": [
            {"product_id": "P-100", "quantity": 50, "warehouse_id": "W-1"},
        ],
        "expires_at": "2026-08-01T00:00:00Z",
    },
    "ord-600": {
        "status": "reserved",
        "order_id": "ORD-600",
        "reservation_id": "RES-600",
        "items_reserved": [
            {"product_id": "P-500", "quantity": 100, "warehouse_id": "W-1"},
        ],
        "expires_at": "2026-07-30T00:00:00Z",
    },
}


@tool()
def reserve_inventory(order_id: str, items: List[str]):
    """
    Reserves inventory for an order's items to prevent overselling.

    Args:
        order_id: The order identifier (e.g. "ORD-100").
        items: List of product IDs to reserve (e.g. ["P-100", "P-200"]).

    Returns:
        Reservation result with reserved items and expiration, or None if reservation failed.
    """
    normalized = str(order_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
