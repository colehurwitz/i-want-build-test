from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "2024"): {
        "employee_id": "E-100",
        "year": "2024",
        "federal_rate": 22.0,
        "state_rate": 8.0,
        "additional_withholding": 0.0,
        "filing_status": "single",
        "ytd_federal": 10200.00,
        "ytd_state": 4080.00,
    },
    ("e-101", "2024"): {
        "employee_id": "E-101",
        "year": "2024",
        "federal_rate": 18.0,
        "state_rate": 6.5,
        "additional_withholding": 50.0,
        "filing_status": "married_joint",
        "ytd_federal": 7776.00,
        "ytd_state": 3456.00,
    },
    ("e-102", "2024"): {
        "employee_id": "E-102",
        "year": "2024",
        "federal_rate": 24.0,
        "state_rate": 9.0,
        "additional_withholding": 100.0,
        "filing_status": "single",
        "ytd_federal": 12540.00,
        "ytd_state": 4560.00,
    },
}


@tool()
def get_tax_withholdings(employee_id: str, year: str):
    """
    Gets an employee's current tax withholding information for a given year.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        year: The tax year (e.g. "2024").

    Returns:
        The tax withholding details including federal/state rates, additional withholding, filing status, and year-to-date amounts, or None if not found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(year).strip(),
    )
    return STUB_RESPONSES.get(key)
