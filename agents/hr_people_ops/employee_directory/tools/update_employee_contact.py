from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-200", "phone", "555-0199"): {
        "status": "success",
        "employee_id": "E-200",
        "field": "phone",
        "old_value": "555-0200",
        "new_value": "555-0199",
    },
    ("e-100", "phone", "555-0150"): {
        "status": "success",
        "employee_id": "E-100",
        "field": "phone",
        "old_value": "555-0100",
        "new_value": "555-0150",
    },
    ("e-101", "email", "jane.d@company.com"): {
        "status": "success",
        "employee_id": "E-101",
        "field": "email",
        "old_value": "jane.doe@company.com",
        "new_value": "jane.d@company.com",
    },
}


@tool()
def update_employee_contact(employee_id: str, field: str, value: str):
    """
    Updates a contact field for an employee.

    Args:
        employee_id: The employee's ID (e.g. "E-200"), returned by the lookup_employee tool.
        field: The contact field to update (e.g. "phone", "email").
        value: The new value for the field.

    Returns:
        The update result with old and new values, or None if the employee or field is not found.
    """
    key = (
        str(employee_id).lower().strip(),
        str(field).lower().strip(),
        str(value).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
