from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "p-100": {
        "product_id": "P-100",
        "product_name": "Industrial Bearings",
        "reorder_history": [
            {"date": "2026-06-01", "quantity": 500, "warehouse_id": "W-1", "supplier": "BearingCorp"},
            {"date": "2026-05-10", "quantity": 300, "warehouse_id": "W-2", "supplier": "BearingCorp"},
            {"date": "2026-04-15", "quantity": 800, "warehouse_id": "W-1", "supplier": "MetalParts Inc"},
        ],
    },
    "p-200": {
        "product_id": "P-200",
        "product_name": "Steel Fasteners",
        "reorder_history": [
            {"date": "2026-06-20", "quantity": 2000, "warehouse_id": "W-1", "supplier": "FastenAll"},
            {"date": "2026-05-05", "quantity": 1000, "warehouse_id": "W-3", "supplier": "FastenAll"},
        ],
    },
    "p-300": {
        "product_id": "P-300",
        "product_name": "Copper Wiring",
        "reorder_history": [
            {"date": "2026-06-10", "quantity": 200, "warehouse_id": "W-2", "supplier": "WireTech"},
            {"date": "2026-03-22", "quantity": 400, "warehouse_id": "W-2", "supplier": "CopperLine"},
        ],
    },
    "p-400": {
        "product_id": "P-400",
        "product_name": "Aluminum Sheets",
        "reorder_history": [
            {"date": "2026-07-01", "quantity": 600, "warehouse_id": "W-1", "supplier": "AluSupply"},
            {"date": "2026-06-15", "quantity": 300, "warehouse_id": "W-2", "supplier": "AluSupply"},
            {"date": "2026-05-20", "quantity": 200, "warehouse_id": "W-3", "supplier": "MetalParts Inc"},
        ],
    },
    "p-500": {
        "product_id": "P-500",
        "product_name": "Rubber Gaskets",
        "reorder_history": [
            {"date": "2026-06-25", "quantity": 400, "warehouse_id": "W-1", "supplier": "GasketWorld"},
        ],
    },
}


@tool()
def get_reorder_history(product_id: str):
    """
    Retrieves the reorder history for a product across all warehouses.

    Args:
        product_id: The product identifier (e.g. "P-100").

    Returns:
        Reorder history including dates, quantities, warehouses, and suppliers, or None if not found.
    """
    normalized = str(product_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
