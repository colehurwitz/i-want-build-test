from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ds-101", "data_inventory", True): {
        "report_id": "PRV-4001",
        "subject_id": "DS-101",
        "report_type": "data_inventory",
        "data_categories": ["personal", "financial", "behavioral"],
        "total_records": 359,
        "storage_locations": ["primary-db-eu", "analytics-warehouse", "backup-eu-west"],
        "processing_activities": [
            {"purpose": "service_delivery", "legal_basis": "contract", "retention": "account_lifetime"},
            {"purpose": "marketing", "legal_basis": "consent", "retention": "until_withdrawal"},
            {"purpose": "analytics", "legal_basis": "consent", "retention": "24_months"},
        ],
        "third_party_recipients": ["payment-processor.com"],
        "generated_at": "2024-07-29",
    },
    ("ds-101", "data_inventory", False): {
        "report_id": "PRV-4002",
        "subject_id": "DS-101",
        "report_type": "data_inventory",
        "data_categories": ["personal", "financial", "behavioral"],
        "total_records": 359,
        "storage_locations": ["primary-db-eu", "analytics-warehouse", "backup-eu-west"],
        "generated_at": "2024-07-29",
    },
    ("ds-102", "consent_audit", True): {
        "report_id": "PRV-4003",
        "subject_id": "DS-102",
        "report_type": "consent_audit",
        "consent_summary": {
            "marketing": "expired",
            "analytics": "not_given",
            "third_party_sharing": "not_given",
            "essential_services": "active",
        },
        "processing_activities": [
            {"purpose": "essential_services", "legal_basis": "contract", "retention": "account_lifetime"},
        ],
        "issues_found": ["Marketing consent expired on 2023-08-01 — processing must stop"],
        "generated_at": "2024-07-29",
    },
    ("ds-103", "data_inventory", True): {
        "report_id": "PRV-4004",
        "subject_id": "DS-103",
        "report_type": "data_inventory",
        "data_categories": ["personal", "financial", "behavioral", "health"],
        "total_records": 614,
        "storage_locations": ["primary-db-us", "analytics-warehouse", "health-records-vault"],
        "processing_activities": [
            {"purpose": "service_delivery", "legal_basis": "contract", "retention": "account_lifetime"},
            {"purpose": "marketing", "legal_basis": "consent", "retention": "until_withdrawal"},
            {"purpose": "analytics", "legal_basis": "consent", "retention": "24_months"},
            {"purpose": "health_services", "legal_basis": "explicit_consent", "retention": "10_years"},
        ],
        "third_party_recipients": ["payment-processor.com", "health-partner.com"],
        "generated_at": "2024-07-29",
    },
    ("ds-104", "processing_activities", True): {
        "report_id": "PRV-4005",
        "subject_id": "DS-104",
        "report_type": "processing_activities",
        "processing_activities": [
            {"purpose": "service_delivery", "legal_basis": "contract", "retention": "account_lifetime"},
            {"purpose": "marketing", "legal_basis": "consent", "retention": "until_withdrawal"},
            {"purpose": "fraud_detection", "legal_basis": "legitimate_interest", "retention": "36_months"},
        ],
        "data_flows": [
            {"from": "primary-db-uk", "to": "analytics-warehouse", "purpose": "reporting"},
            {"from": "primary-db-uk", "to": "fraud-detection-service", "purpose": "fraud_prevention"},
        ],
        "generated_at": "2024-07-29",
    },
}


@tool()
def generate_privacy_report(subject_id: str, report_type: str, include_processing_activities: bool):
    """
    Generates a privacy compliance report for a data subject.

    Args:
        subject_id: The data subject's ID (e.g. "DS-101").
        report_type: The type of report — one of "data_inventory", "processing_activities", "consent_audit", or "breach_notification".
        include_processing_activities: Whether to include detailed processing activity records in the report.

    Returns:
        Privacy report including report_id, data categories, storage locations, and optionally processing activities, or None if generation failed.
    """
    key = (
        str(subject_id).lower().strip(),
        str(report_type).lower().strip(),
        bool(include_processing_activities),
    )
    return STUB_RESPONSES.get(key)
