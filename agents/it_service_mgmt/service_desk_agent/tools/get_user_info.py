from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "vip.exec@company.com": {
        "user_id": "USR-VIP-001",
        "name": "Victoria Patel",
        "department": "Executive",
        "vip_status": True,
        "open_tickets": 1,
    },
    "dev@company.com": {
        "user_id": "USR-DEV-100",
        "name": "Derek Chen",
        "department": "Engineering",
        "vip_status": False,
        "open_tickets": 2,
    },
    "user@company.com": {
        "user_id": "USR-STD-200",
        "name": "Uma Rodriguez",
        "department": "Marketing",
        "vip_status": False,
        "open_tickets": 0,
    },
    "manager@company.com": {
        "user_id": "USR-MGR-300",
        "name": "Marcus Johnson",
        "department": "Engineering",
        "vip_status": False,
        "open_tickets": 3,
    },
    "newuser@company.com": {
        "user_id": "USR-NEW-400",
        "name": "Nina Kowalski",
        "department": "Sales",
        "vip_status": False,
        "open_tickets": 0,
    },
    "poweruser@company.com": {
        "user_id": "USR-PWR-500",
        "name": "Peter Walsh",
        "department": "Finance",
        "vip_status": False,
        "open_tickets": 10,
    },
}


@tool()
def get_user_info(email: str):
    """
    Looks up user information by their email address.

    Args:
        email: The user's email address.

    Returns:
        User details including user_id, name, department, VIP status, and open ticket count, or None if not found.
    """
    normalized = str(email).lower().strip()
    return STUB_RESPONSES.get(normalized)
