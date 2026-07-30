from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("p-100", 100): {
        "product_id": "P-100",
        "requested_quantity": 100,
        "available_quantity": 1200,
        "is_available": True,
        "warehouse_id": "W-1",
    },
    ("p-200", 500): {
        "product_id": "P-200",
        "requested_quantity": 500,
        "available_quantity": 3500,
        "is_available": True,
        "warehouse_id": "W-1",
    },
    ("p-300", 200): {
        "product_id": "P-300",
        "requested_quantity": 200,
        "available_quantity": 30,
        "is_available": False,
        "warehouse_id": "W-2",
        "shortfall": 170,
    },
    ("p-400", 50): {
        "product_id": "P-400",
        "requested_quantity": 50,
        "available_quantity": 550,
        "is_available": True,
        "warehouse_id": "W-2",
    },
    ("p-500", 300): {
        "product_id": "P-500",
        "requested_quantity": 300,
        "available_quantity": 750,
        "is_available": True,
        "warehouse_id": "W-1",
    },
    ("p-100", 50): {
        "product_id": "P-100",
        "requested_quantity": 50,
        "available_quantity": 1200,
        "is_available": True,
        "warehouse_id": "W-1",
    },
    ("p-200", 1000): {
        "product_id": "P-200",
        "requested_quantity": 1000,
        "available_quantity": 800,
        "is_available": False,
        "warehouse_id": "W-3",
        "shortfall": 200,
    },
    ("p-500", 100): {
        "product_id": "P-500",
        "requested_quantity": 100,
        "available_quantity": 750,
        "is_available": True,
        "warehouse_id": "W-1",
    },
}


@tool()
def check_item_availability(product_id: str, quantity: int):
    """
    Checks whether the requested quantity of a product is available in stock.

    Args:
        product_id: The product identifier (e.g. "P-100").
        quantity: The quantity needed.

    Returns:
        Availability details including whether stock is sufficient and any shortfall, or None if product not found.
    """
    key = (
        str(product_id).lower().strip(),
        int(quantity),
    )
    return STUB_RESPONSES.get(key)
