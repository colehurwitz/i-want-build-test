from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("auth_system", "weekly", True): {
        "report_id": "AUD-6001",
        "system": "auth_system",
        "period": "weekly",
        "total_events": 15420,
        "findings_included": True,
        "findings_summary": {
            "critical": 2,
            "high": 0,
            "medium": 1,
            "low": 0,
        },
        "recommendations": [
            "Immediately investigate U-500 account — potential compromise via TOR access",
            "Review U-302 after-hours activity — verify business justification for bulk export",
            "Implement MFA requirement for admin role changes",
        ],
        "compliance_status": "NON-COMPLIANT — critical findings require immediate action",
        "generated_at": "2024-07-29",
    },
    ("auth_system", "weekly", False): {
        "report_id": "AUD-6002",
        "system": "auth_system",
        "period": "weekly",
        "total_events": 15420,
        "findings_included": False,
        "recommendations": [
            "Review access patterns for TOR-based connections",
            "Audit after-hours activity",
        ],
        "compliance_status": "REVIEW REQUIRED",
        "generated_at": "2024-07-29",
    },
    ("payment_system", "quarterly", True): {
        "report_id": "AUD-6003",
        "system": "payment_system",
        "period": "quarterly",
        "total_events": 8930,
        "findings_included": True,
        "findings_summary": {
            "critical": 0,
            "high": 0,
            "medium": 1,
            "low": 0,
        },
        "recommendations": [
            "Review U-401 refund pattern — verify each refund has valid business justification",
            "Implement refund threshold alerts for repeated same-day refunds",
        ],
        "compliance_status": "PARTIALLY COMPLIANT — medium findings under review",
        "generated_at": "2024-07-29",
    },
    ("hr_system", "quarterly", True): {
        "report_id": "AUD-6004",
        "system": "hr_system",
        "period": "quarterly",
        "total_events": 45200,
        "findings_included": True,
        "findings_summary": {
            "critical": 0,
            "high": 1,
            "medium": 1,
            "low": 0,
        },
        "recommendations": [
            "Restrict salary record access — U-600 viewed 57 records without documented business need",
            "Disable self-modification of performance reviews — U-700 modified own record",
            "Implement separation of duties for HR record changes",
        ],
        "compliance_status": "NON-COMPLIANT — access control violations detected",
        "generated_at": "2024-07-29",
    },
}


@tool()
def generate_audit_report(system: str, period: str, include_findings: bool):
    """
    Generates a comprehensive audit report for a system.

    Args:
        system: The system name to generate a report for (e.g. "auth_system").
        period: The reporting period — one of "daily", "weekly", "monthly", or "quarterly".
        include_findings: Whether to include detailed findings in the report.

    Returns:
        Audit report including total events, findings summary, recommendations, and compliance status, or None if generation failed.
    """
    key = (
        str(system).lower().strip(),
        str(period).lower().strip(),
        bool(include_findings),
    )
    return STUB_RESPONSES.get(key)
