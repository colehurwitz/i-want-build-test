from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("p-300", "w-2", 200, "restock"): {
        "status": "success",
        "product_id": "P-300",
        "warehouse_id": "W-2",
        "previous_quantity": 30,
        "quantity_change": 200,
        "new_quantity": 230,
        "reason": "restock",
    },
    ("p-100", "w-2", 100, "restock"): {
        "status": "success",
        "product_id": "P-100",
        "warehouse_id": "W-2",
        "previous_quantity": 45,
        "quantity_change": 100,
        "new_quantity": 145,
        "reason": "restock",
    },
    ("p-400", "w-3", 200, "restock"): {
        "status": "success",
        "product_id": "P-400",
        "warehouse_id": "W-3",
        "previous_quantity": 120,
        "quantity_change": 200,
        "new_quantity": 320,
        "reason": "restock",
    },
    ("p-200", "w-1", -50, "transfer_out"): {
        "status": "success",
        "product_id": "P-200",
        "warehouse_id": "W-1",
        "previous_quantity": 3500,
        "quantity_change": -50,
        "new_quantity": 3450,
        "reason": "transfer_out",
    },
}


@tool()
def update_stock(product_id: str, warehouse_id: str, quantity_change: int, reason: str):
    """
    Updates stock quantity for a product in a warehouse.

    Args:
        product_id: The product identifier (e.g. "P-300").
        warehouse_id: The warehouse identifier (e.g. "W-2").
        quantity_change: The quantity to add (positive) or remove (negative).
        reason: The reason for the stock change (e.g. "restock", "damaged", "transfer_out", "sold").

    Returns:
        Update result with previous and new quantities, or None if the product/warehouse is not found.
    """
    key = (
        str(product_id).lower().strip(),
        str(warehouse_id).lower().strip(),
        int(quantity_change),
        str(reason).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
