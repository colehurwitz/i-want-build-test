from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "ord-100": {
        "order_id": "ORD-100",
        "customer": "Acme Corp",
        "items": ["Widget A", "Widget B", "Widget C"],
        "destination": "New York",
        "weight_kg": 15.0,
        "shipping_priority": "express",
    },
    "ord-200": {
        "order_id": "ORD-200",
        "customer": "BuildRight Inc",
        "items": ["Copper Wiring Spool", "Aluminum Sheet Pack"],
        "destination": "Los Angeles",
        "weight_kg": 30.0,
        "shipping_priority": "express",
    },
    "ord-300": {
        "order_id": "ORD-300",
        "customer": "TechParts Ltd",
        "items": ["Heavy Equipment Part"],
        "destination": "Los Angeles",
        "weight_kg": 25.0,
        "shipping_priority": "express",
    },
    "ord-400": {
        "order_id": "ORD-400",
        "customer": "MegaBuild Co",
        "items": ["Office Supplies", "Printer Paper"],
        "destination": "Boston",
        "weight_kg": 10.0,
        "shipping_priority": "ground",
    },
    "ord-500": {
        "order_id": "ORD-500",
        "customer": "QuickFix Supply",
        "items": ["Urgent Medical Supply"],
        "destination": "Miami",
        "weight_kg": 8.0,
        "shipping_priority": "overnight",
    },
}


@tool()
def get_order_details(order_id: str):
    """
    Retrieves full details for a customer order including items, destination, and shipping requirements.

    Args:
        order_id: The order identifier (e.g. "ORD-100").

    Returns:
        Order details including customer, items, destination, weight, and shipping priority, or None if not found.
    """
    normalized = str(order_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
