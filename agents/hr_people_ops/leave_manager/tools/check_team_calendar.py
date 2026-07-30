from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("engineering", "2024-12-23 to 2024-12-27"): {
        "department": "Engineering",
        "date_range": "2024-12-23 to 2024-12-27",
        "scheduled_off": [
            {"name": "Alice Johnson", "dates": "Dec 23-24"},
            {"name": "Bob Chen", "dates": "Dec 26-27"},
        ],
        "team_size": 8,
        "available_count": 5,
        "coverage_warning": True,
    },
    ("engineering", "2024-11-18 to 2024-11-20"): {
        "department": "Engineering",
        "date_range": "2024-11-18 to 2024-11-20",
        "scheduled_off": [],
        "team_size": 8,
        "available_count": 8,
        "coverage_warning": False,
    },
    ("sales", "2024-11-12 to 2024-11-12"): {
        "department": "Sales",
        "date_range": "2024-11-12 to 2024-11-12",
        "scheduled_off": [
            {"name": "Tom Green", "dates": "Nov 12"},
        ],
        "team_size": 6,
        "available_count": 5,
        "coverage_warning": False,
    },
    ("engineering", "2024-11-22 to 2024-11-25"): {
        "department": "Engineering",
        "date_range": "2024-11-22 to 2024-11-25",
        "scheduled_off": [
            {"name": "Carlos Ruiz", "dates": "Nov 22"},
        ],
        "team_size": 8,
        "available_count": 7,
        "coverage_warning": False,
    },
}


@tool()
def check_team_calendar(department: str, date_range: str):
    """
    Checks the team calendar for a department to see who is scheduled off during a date range.

    Args:
        department: The department name (e.g. "Engineering", "Sales").
        date_range: The date range to check (e.g. "2024-12-23 to 2024-12-27").

    Returns:
        Team calendar details including who is off, team size, available count, and coverage warnings, or None if not found.
    """
    key = (
        str(department).lower().strip(),
        str(date_range).strip(),
    )
    return STUB_RESPONSES.get(key)
