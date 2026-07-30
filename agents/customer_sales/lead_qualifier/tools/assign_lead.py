from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("l-100", "sr-100", "west"): {
        "assignment_id": "ASN-1001",
        "status": "assigned",
        "assigned_at": "2024-03-15T10:00:00Z",
        "rep_name": "Sarah Palmer",
    },
    ("l-100", "sr-200", "west"): {
        "assignment_id": "ASN-1002",
        "status": "assigned",
        "assigned_at": "2024-03-15T10:30:00Z",
        "rep_name": "James Rivera",
    },
    ("l-400", "sr-100", "east"): {
        "assignment_id": "ASN-1003",
        "status": "assigned",
        "assigned_at": "2024-03-15T11:00:00Z",
        "rep_name": "Sarah Palmer",
    },
    ("l-400", "sr-200", "west"): {
        "assignment_id": "ASN-1004",
        "status": "assigned",
        "assigned_at": "2024-03-15T11:30:00Z",
        "rep_name": "James Rivera",
    },
    ("l-500", "sr-300", "east"): {
        "assignment_id": "ASN-1005",
        "status": "assigned",
        "assigned_at": "2024-03-15T12:00:00Z",
        "rep_name": "Mike Torres",
    },
}


@tool()
def assign_lead(lead_id: str, sales_rep_id: str, territory: str):
    """
    Assigns a lead to a sales representative in a specific territory.

    Args:
        lead_id: The unique lead identifier (e.g. "L-100").
        sales_rep_id: The sales representative's ID (e.g. "SR-100").
        territory: The sales territory (e.g. "west", "east", "north").

    Returns:
        Assignment confirmation including assignment_id and status, or None if assignment failed.
    """
    key = (
        str(lead_id).lower().strip(),
        str(sales_rep_id).lower().strip(),
        str(territory).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
