from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "ord-100": {
        "order_id": "ORD-100",
        "customer": "Acme Corp",
        "status": "received",
        "items": [
            {"product_id": "P-100", "name": "Industrial Bearings", "quantity": 100, "unit_price": 25.00},
            {"product_id": "P-200", "name": "Steel Fasteners", "quantity": 500, "unit_price": 2.50},
        ],
        "total": 3750.00,
        "payment_method": "credit_card",
        "shipping_priority": "standard",
        "warehouse_id": "W-1",
    },
    "ord-200": {
        "order_id": "ORD-200",
        "customer": "BuildRight Inc",
        "status": "received",
        "items": [
            {"product_id": "P-300", "name": "Copper Wiring", "quantity": 200, "unit_price": 15.00},
            {"product_id": "P-400", "name": "Aluminum Sheets", "quantity": 50, "unit_price": 45.00},
        ],
        "total": 5250.00,
        "payment_method": "purchase_order",
        "shipping_priority": "express",
        "warehouse_id": "W-2",
    },
    "ord-300": {
        "order_id": "ORD-300",
        "customer": "TechParts Ltd",
        "status": "confirmed",
        "items": [
            {"product_id": "P-500", "name": "Rubber Gaskets", "quantity": 300, "unit_price": 3.00},
        ],
        "total": 900.00,
        "payment_method": "credit_card",
        "shipping_priority": "standard",
        "warehouse_id": "W-1",
    },
    "ord-400": {
        "order_id": "ORD-400",
        "customer": "MegaBuild Co",
        "status": "received",
        "items": [
            {"product_id": "P-100", "name": "Industrial Bearings", "quantity": 50, "unit_price": 25.00},
        ],
        "total": 1250.00,
        "payment_method": "wire_transfer",
        "shipping_priority": "standard",
        "warehouse_id": "W-1",
    },
    "ord-500": {
        "order_id": "ORD-500",
        "customer": "QuickFix Supply",
        "status": "received",
        "items": [
            {"product_id": "P-200", "name": "Steel Fasteners", "quantity": 1000, "unit_price": 2.50},
        ],
        "total": 2500.00,
        "payment_method": "net_30",
        "shipping_priority": "express",
        "warehouse_id": "W-3",
    },
    "ord-600": {
        "order_id": "ORD-600",
        "customer": "Urgent Repairs LLC",
        "status": "received",
        "items": [
            {"product_id": "P-500", "name": "Rubber Gaskets", "quantity": 100, "unit_price": 3.00},
        ],
        "total": 300.00,
        "payment_method": "credit_card",
        "shipping_priority": "next_day",
        "warehouse_id": "W-1",
    },
}


@tool()
def get_order_details(order_id: str):
    """
    Retrieves full details for a customer order.

    Args:
        order_id: The order identifier (e.g. "ORD-100").

    Returns:
        Order details including customer, items, total, payment method, and shipping priority, or None if not found.
    """
    normalized = str(order_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
