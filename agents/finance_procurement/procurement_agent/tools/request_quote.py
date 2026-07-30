from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("v-100", "req-6001", 50): {
        "quote_id": "Q-7001",
        "vendor_name": "KeyTech Pro",
        "unit_price": 145.00,
        "total": 7250.00,
        "delivery_date": "2024-07-01",
        "valid_until": "2024-07-15",
    },
    ("v-101", "req-6001", 50): {
        "quote_id": "Q-7002",
        "vendor_name": "ErgoSupply Co",
        "unit_price": 135.00,
        "total": 6750.00,
        "delivery_date": "2024-06-28",
        "valid_until": "2024-07-10",
    },
    ("v-102", "req-6001", 50): {
        "quote_id": "Q-7003",
        "vendor_name": "Office Gear Direct",
        "unit_price": 155.00,
        "total": 7750.00,
        "delivery_date": "2024-07-08",
        "valid_until": "2024-07-20",
    },
    ("v-200", "req-6002", 5): {
        "quote_id": "Q-7004",
        "vendor_name": "ServerMax",
        "unit_price": 9500.00,
        "total": 47500.00,
        "delivery_date": "2024-06-22",
        "valid_until": "2024-07-05",
    },
    ("v-201", "req-6002", 5): {
        "quote_id": "Q-7005",
        "vendor_name": "CloudHardware Inc",
        "unit_price": 9800.00,
        "total": 49000.00,
        "delivery_date": "2024-06-20",
        "valid_until": "2024-07-01",
    },
    ("v-300", "req-6003", 100): {
        "quote_id": "Q-7006",
        "vendor_name": "DisplayTech",
        "unit_price": 420.00,
        "total": 42000.00,
        "delivery_date": "2024-07-01",
        "valid_until": "2024-07-15",
    },
    ("v-301", "req-6003", 100): {
        "quote_id": "Q-7007",
        "vendor_name": "ScreenPro Global",
        "unit_price": 380.00,
        "total": 38000.00,
        "delivery_date": "2024-07-10",
        "valid_until": "2024-07-20",
    },
    ("v-400", "req-6004", 20): {
        "quote_id": "Q-7008",
        "vendor_name": "AudioPro",
        "unit_price": 89.00,
        "total": 1780.00,
        "delivery_date": "2024-06-25",
        "valid_until": "2024-07-10",
    },
    ("v-401", "req-6004", 20): {
        "quote_id": "Q-7009",
        "vendor_name": "SoundGear Inc",
        "unit_price": 75.00,
        "total": 1500.00,
        "delivery_date": "2024-06-30",
        "valid_until": "2024-07-15",
    },
}


@tool()
def request_quote(vendor_id: str, req_id: str, quantity: int):
    """
    Requests a price quote from a vendor for a specific requisition.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").
        req_id: The requisition ID to quote against (e.g. "REQ-6001").
        quantity: The quantity of items to quote.

    Returns:
        Quote details including quote_id, unit_price, total, delivery_date, and validity period, or None if quote request failed.
    """
    key = (
        str(vendor_id).lower().strip(),
        str(req_id).lower().strip(),
        int(quantity),
    )
    return STUB_RESPONSES.get(key)
