from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("e-100", "first national bank", "021000021", "****5678"): {
        "status": "success",
        "employee_id": "E-100",
        "bank_name": "First National Bank",
        "routing_number": "021000021",
        "account_last_four": "5678",
        "effective_date": "2024-02-01",
        "confirmation_number": "DD-1001",
    },
    ("e-101", "chase bank", "021000089", "****9012"): {
        "status": "success",
        "employee_id": "E-101",
        "bank_name": "Chase Bank",
        "routing_number": "021000089",
        "account_last_four": "9012",
        "effective_date": "2024-02-01",
        "confirmation_number": "DD-1002",
    },
}


@tool()
def update_direct_deposit(employee_id: str, bank_name: str, routing_number: str, account_number: str):
    """
    Updates an employee's direct deposit information.

    Args:
        employee_id: The employee's ID (e.g. "E-100").
        bank_name: The name of the bank (e.g. "First National Bank").
        routing_number: The bank's routing number.
        account_number: The bank account number.

    Returns:
        The update confirmation with effective date and confirmation number, or None if the update failed.
    """
    key = (
        str(employee_id).lower().strip(),
        str(bank_name).lower().strip(),
        str(routing_number).strip(),
        str(account_number).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
