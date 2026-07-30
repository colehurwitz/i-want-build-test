from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "west": [
        {"rep_id": "SR-100", "name": "Sarah Palmer", "current_leads": 5, "specialty": "enterprise"},
        {"rep_id": "SR-200", "name": "James Rivera", "current_leads": 8, "specialty": "mid_market"},
    ],
    "east": [
        {"rep_id": "SR-100", "name": "Sarah Palmer", "current_leads": 5, "specialty": "enterprise"},
        {"rep_id": "SR-300", "name": "Mike Torres", "current_leads": 3, "specialty": "smb"},
    ],
    "north": [],
    "south": [
        {"rep_id": "SR-400", "name": "Lisa Chen", "current_leads": 12, "specialty": "enterprise"},
    ],
}


@tool()
def get_available_sales_reps(territory: str):
    """
    Returns the list of available sales representatives for a given territory.

    Args:
        territory: The sales territory to look up (e.g. "west", "east", "north", "south").

    Returns:
        A list of available sales reps with their IDs, names, current lead counts, and specialties, or an empty list if no reps cover that territory.
    """
    normalized = str(territory).lower().strip()
    return STUB_RESPONSES.get(normalized, [])
