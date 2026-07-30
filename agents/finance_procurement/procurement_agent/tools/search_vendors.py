from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("keyboards", 3.5): [
        {"vendor_id": "V-100", "name": "KeyTech Pro", "rating": 4.5, "lead_time_days": 14, "location": "US"},
        {"vendor_id": "V-101", "name": "ErgoSupply Co", "rating": 4.2, "lead_time_days": 10, "location": "US"},
        {"vendor_id": "V-102", "name": "Office Gear Direct", "rating": 3.8, "lead_time_days": 21, "location": "Canada"},
    ],
    ("servers", 3.5): [
        {"vendor_id": "V-200", "name": "ServerMax", "rating": 4.7, "lead_time_days": 7, "location": "US"},
        {"vendor_id": "V-201", "name": "CloudHardware Inc", "rating": 4.3, "lead_time_days": 5, "location": "US"},
        {"vendor_id": "V-202", "name": "DataCenter Supply", "rating": 3.9, "lead_time_days": 12, "location": "US"},
    ],
    ("monitors", 3.5): [
        {"vendor_id": "V-300", "name": "DisplayTech", "rating": 4.4, "lead_time_days": 10, "location": "US"},
        {"vendor_id": "V-301", "name": "ScreenPro Global", "rating": 4.1, "lead_time_days": 18, "location": "China"},
        {"vendor_id": "V-302", "name": "VisualEdge", "rating": 3.6, "lead_time_days": 15, "location": "US"},
    ],
    ("headsets", 3.5): [
        {"vendor_id": "V-400", "name": "AudioPro", "rating": 4.6, "lead_time_days": 7, "location": "US"},
        {"vendor_id": "V-401", "name": "SoundGear Inc", "rating": 4.0, "lead_time_days": 12, "location": "US"},
    ],
    ("headsets", 4.0): [
        {"vendor_id": "V-400", "name": "AudioPro", "rating": 4.6, "lead_time_days": 7, "location": "US"},
        {"vendor_id": "V-401", "name": "SoundGear Inc", "rating": 4.0, "lead_time_days": 12, "location": "US"},
    ],
}


@tool()
def search_vendors(item_category: str, min_rating: float):
    """
    Searches for qualified vendors that supply a given item category.

    Args:
        item_category: The category of items to search for (e.g. "keyboards", "servers", "monitors").
        min_rating: Minimum vendor rating required (0.0-5.0, recommended minimum 3.5).

    Returns:
        A list of vendor dicts with vendor_id, name, rating, lead_time_days, and location, or None if no vendors found.
    """
    key = (
        str(item_category).lower().strip(),
        float(min_rating),
    )
    return STUB_RESPONSES.get(key)
