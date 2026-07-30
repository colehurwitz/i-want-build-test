from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("p-200", "w-1", "w-3", 50): {
        "status": "success",
        "product_id": "P-200",
        "from_warehouse": "W-1",
        "to_warehouse": "W-3",
        "quantity_transferred": 50,
        "from_new_quantity": 3450,
        "to_new_quantity": 850,
        "transfer_id": "TRF-001",
    },
    ("p-400", "w-1", "w-3", 500): {
        "status": "success",
        "product_id": "P-400",
        "from_warehouse": "W-1",
        "to_warehouse": "W-3",
        "quantity_transferred": 500,
        "from_new_quantity": 2300,
        "to_new_quantity": 620,
        "transfer_id": "TRF-002",
    },
    ("p-100", "w-1", "w-2", 200): {
        "status": "success",
        "product_id": "P-100",
        "from_warehouse": "W-1",
        "to_warehouse": "W-2",
        "quantity_transferred": 200,
        "from_new_quantity": 1000,
        "to_new_quantity": 245,
        "transfer_id": "TRF-003",
    },
}


@tool()
def transfer_stock(product_id: str, from_warehouse: str, to_warehouse: str, quantity: int):
    """
    Transfers stock of a product between warehouses.

    Args:
        product_id: The product identifier (e.g. "P-200").
        from_warehouse: The source warehouse identifier (e.g. "W-1").
        to_warehouse: The destination warehouse identifier (e.g. "W-3").
        quantity: The number of units to transfer.

    Returns:
        Transfer result with new quantities at both warehouses, or None if the transfer failed.
    """
    key = (
        str(product_id).lower().strip(),
        str(from_warehouse).lower().strip(),
        str(to_warehouse).lower().strip(),
        int(quantity),
    )
    return STUB_RESPONSES.get(key)
