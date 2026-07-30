from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("auth_system", "2024-07-22", "2024-07-29"): {
        "system": "auth_system",
        "period": "2024-07-22 to 2024-07-29",
        "total_events": 15420,
        "log_entries": [
            {"timestamp": "2024-07-23T03:14:00Z", "user": "U-500", "action": "login", "ip": "185.220.101.42", "status": "success", "location": "TOR exit node"},
            {"timestamp": "2024-07-23T03:15:00Z", "user": "U-500", "action": "privilege_change", "ip": "185.220.101.42", "status": "success", "details": "role changed to admin"},
            {"timestamp": "2024-07-24T22:45:00Z", "user": "U-302", "action": "login", "ip": "10.0.1.55", "status": "success", "location": "office"},
            {"timestamp": "2024-07-25T02:30:00Z", "user": "U-302", "action": "bulk_export", "ip": "10.0.1.55", "status": "success", "details": "exported 5000 records"},
            {"timestamp": "2024-07-26T09:00:00Z", "user": "U-100", "action": "login", "ip": "10.0.1.10", "status": "success", "location": "office"},
        ],
        "summary": "15420 events across 7 days. 2 suspicious patterns detected: TOR-based admin access, after-hours bulk export.",
    },
    ("payment_system", "2024-07-22", "2024-07-29"): {
        "system": "payment_system",
        "period": "2024-07-22 to 2024-07-29",
        "total_events": 8930,
        "log_entries": [
            {"timestamp": "2024-07-23T14:00:00Z", "user": "U-401", "action": "refund_processed", "ip": "10.0.2.20", "status": "success", "amount": "$150.00"},
            {"timestamp": "2024-07-24T14:05:00Z", "user": "U-401", "action": "refund_processed", "ip": "10.0.2.20", "status": "success", "amount": "$200.00"},
            {"timestamp": "2024-07-25T14:10:00Z", "user": "U-401", "action": "refund_processed", "ip": "10.0.2.20", "status": "success", "amount": "$175.00"},
            {"timestamp": "2024-07-26T10:00:00Z", "user": "U-200", "action": "payment_processed", "ip": "10.0.2.15", "status": "success", "amount": "$5000.00"},
        ],
        "summary": "8930 events across 7 days. Pattern of daily refunds from same user noted.",
    },
    ("hr_system", "2024-04-01", "2024-06-30"): {
        "system": "hr_system",
        "period": "2024-04-01 to 2024-06-30",
        "total_events": 45200,
        "log_entries": [
            {"timestamp": "2024-04-15T08:00:00Z", "user": "U-600", "action": "salary_view", "ip": "10.0.3.30", "status": "success", "details": "viewed 12 salary records"},
            {"timestamp": "2024-05-20T11:00:00Z", "user": "U-600", "action": "salary_view", "ip": "10.0.3.30", "status": "success", "details": "viewed 45 salary records"},
            {"timestamp": "2024-06-10T16:00:00Z", "user": "U-700", "action": "record_modification", "ip": "10.0.3.35", "status": "success", "details": "modified own performance review"},
        ],
        "summary": "45200 events across Q2. Unusual salary record access pattern from U-600. Self-modification of performance data by U-700.",
    },
}


@tool()
def get_audit_logs(system: str, start_date: str, end_date: str):
    """
    Retrieves audit logs for a system within a specified date range.

    Args:
        system: The system name to retrieve logs for (e.g. "auth_system", "payment_system", "hr_system").
        start_date: The start date in YYYY-MM-DD format.
        end_date: The end date in YYYY-MM-DD format.

    Returns:
        Audit log data including total events, log entries with timestamps/users/actions/IPs, and a summary, or None if not found.
    """
    key = (
        str(system).lower().strip(),
        str(start_date).strip(),
        str(end_date).strip(),
    )
    return STUB_RESPONSES.get(key)
