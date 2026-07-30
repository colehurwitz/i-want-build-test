from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("p-100", "w-1"): {
        "product_id": "P-100",
        "warehouse_id": "W-1",
        "product_name": "Industrial Bearings",
        "quantity_on_hand": 1200,
        "reorder_point": 500,
        "status": "overstocked",
        "last_updated": "2026-07-15",
    },
    ("p-100", "w-2"): {
        "product_id": "P-100",
        "warehouse_id": "W-2",
        "product_name": "Industrial Bearings",
        "quantity_on_hand": 45,
        "reorder_point": 500,
        "status": "critically_low",
        "last_updated": "2026-07-14",
    },
    ("p-200", "w-1"): {
        "product_id": "P-200",
        "warehouse_id": "W-1",
        "product_name": "Steel Fasteners",
        "quantity_on_hand": 3500,
        "reorder_point": 1000,
        "status": "overstocked",
        "last_updated": "2026-07-16",
    },
    ("p-200", "w-3"): {
        "product_id": "P-200",
        "warehouse_id": "W-3",
        "product_name": "Steel Fasteners",
        "quantity_on_hand": 800,
        "reorder_point": 1000,
        "status": "normal",
        "last_updated": "2026-07-13",
    },
    ("p-300", "w-2"): {
        "product_id": "P-300",
        "warehouse_id": "W-2",
        "product_name": "Copper Wiring",
        "quantity_on_hand": 30,
        "reorder_point": 200,
        "status": "critically_low",
        "last_updated": "2026-07-12",
    },
    ("p-400", "w-1"): {
        "product_id": "P-400",
        "warehouse_id": "W-1",
        "product_name": "Aluminum Sheets",
        "quantity_on_hand": 2800,
        "reorder_point": 600,
        "status": "overstocked",
        "last_updated": "2026-07-15",
    },
    ("p-400", "w-2"): {
        "product_id": "P-400",
        "warehouse_id": "W-2",
        "product_name": "Aluminum Sheets",
        "quantity_on_hand": 550,
        "reorder_point": 600,
        "status": "normal",
        "last_updated": "2026-07-14",
    },
    ("p-400", "w-3"): {
        "product_id": "P-400",
        "warehouse_id": "W-3",
        "product_name": "Aluminum Sheets",
        "quantity_on_hand": 120,
        "reorder_point": 600,
        "status": "critically_low",
        "last_updated": "2026-07-13",
    },
    ("p-500", "w-1"): {
        "product_id": "P-500",
        "warehouse_id": "W-1",
        "product_name": "Rubber Gaskets",
        "quantity_on_hand": 750,
        "reorder_point": 400,
        "status": "normal",
        "last_updated": "2026-07-16",
    },
}


@tool()
def check_inventory(product_id: str, warehouse_id: str):
    """
    Checks current inventory levels for a product in a specific warehouse.

    Args:
        product_id: The product identifier (e.g. "P-100").
        warehouse_id: The warehouse identifier (e.g. "W-1").

    Returns:
        Inventory details including quantity on hand, reorder point, and stock status, or None if not found.
    """
    key = (
        str(product_id).lower().strip(),
        str(warehouse_id).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
