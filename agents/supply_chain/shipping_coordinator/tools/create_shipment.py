from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import List

STUB_RESPONSES = {
    ("ord-100", "express"): {
        "shipment_id": "SHP-100",
        "order_id": "ORD-100",
        "tracking_number": "TRK-100-EXP",
        "carrier": "FastFreight",
        "service_level": "express",
        "status": "pending",
        "estimated_delivery": "2026-08-02",
        "items_count": 3,
    },
    ("ord-300", "express"): {
        "shipment_id": "SHP-300",
        "order_id": "ORD-300",
        "tracking_number": "TRK-300-EXP",
        "carrier": "FastFreight",
        "service_level": "express",
        "status": "pending",
        "estimated_delivery": "2026-08-03",
        "items_count": 1,
    },
    ("ord-400", "ground"): {
        "shipment_id": "SHP-400",
        "order_id": "ORD-400",
        "tracking_number": "TRK-400-GND",
        "carrier": "GroundShip Co",
        "service_level": "ground",
        "status": "pending",
        "estimated_delivery": "2026-08-08",
        "items_count": 2,
    },
    ("ord-500", "overnight"): {
        "shipment_id": "SHP-500",
        "order_id": "ORD-500",
        "tracking_number": "TRK-500-OVN",
        "carrier": "AirExpress",
        "service_level": "overnight",
        "status": "pending",
        "estimated_delivery": "2026-07-31",
        "items_count": 1,
    },
}


@tool()
def create_shipment(order_id: str, items: List[str], destination: str, priority: str):
    """
    Creates a new shipment for a customer order.

    Args:
        order_id: The order identifier (e.g. "ORD-100").
        items: List of item descriptions being shipped.
        destination: The shipping destination address or city.
        priority: Shipping priority level ("ground", "express", or "overnight").

    Returns:
        Shipment details including tracking number, carrier, and estimated delivery, or None if creation failed.
    """
    key = (
        str(order_id).lower().strip(),
        str(priority).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
