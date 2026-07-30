from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ds-101", "access", "full"): {
        "request_id": "REQ-3001",
        "subject_id": "DS-101",
        "request_type": "access",
        "scope": "full",
        "status": "completed",
        "data_provided": {
            "personal": {"name": "Hans Mueller", "email": "user@eu-company.com", "phone": "+49-555-0101"},
            "financial": {"payment_methods": 2, "transaction_count": 47},
            "behavioral": {"login_count": 312, "last_login": "2024-07-20"},
        },
        "processing_time_hours": 2,
        "regulatory_deadline": "30 days (GDPR Art. 15)",
    },
    ("ds-101", "access", "personal"): {
        "request_id": "REQ-3002",
        "subject_id": "DS-101",
        "request_type": "access",
        "scope": "personal",
        "status": "completed",
        "data_provided": {
            "personal": {"name": "Hans Mueller", "email": "user@eu-company.com", "phone": "+49-555-0101"},
        },
        "processing_time_hours": 1,
        "regulatory_deadline": "30 days (GDPR Art. 15)",
    },
    ("ds-102", "deletion", "full"): {
        "request_id": "REQ-3003",
        "subject_id": "DS-102",
        "request_type": "deletion",
        "scope": "full",
        "status": "completed",
        "records_deleted": 156,
        "retention_exceptions": ["invoice records retained for 7 years per tax law"],
        "third_parties_notified": ["analytics-partner.com", "ad-network.com"],
        "processing_time_hours": 24,
        "regulatory_deadline": "30 days (GDPR Art. 17)",
    },
    ("ds-103", "access", "full"): {
        "request_id": "REQ-3004",
        "subject_id": "DS-103",
        "request_type": "access",
        "scope": "full",
        "status": "completed",
        "data_provided": {
            "personal": {"name": "Alex Johnson", "email": "user@company.com", "phone": "555-0103"},
            "financial": {"payment_methods": 3, "transaction_count": 89},
            "behavioral": {"login_count": 520, "last_login": "2024-07-28"},
            "health": {"records_count": 5},
        },
        "processing_time_hours": 4,
        "regulatory_deadline": "45 days (CCPA)",
    },
    ("ds-104", "portability", "full"): {
        "request_id": "REQ-3005",
        "subject_id": "DS-104",
        "request_type": "portability",
        "scope": "full",
        "status": "completed",
        "export_format": "JSON",
        "file_size_mb": 12.5,
        "download_url": "https://secure.company.com/exports/REQ-3005",
        "download_expiry": "2024-08-05",
        "processing_time_hours": 6,
        "regulatory_deadline": "30 days (UK GDPR Art. 20)",
    },
    ("ds-103", "rectification", "personal"): {
        "request_id": "REQ-3006",
        "subject_id": "DS-103",
        "request_type": "rectification",
        "scope": "personal",
        "status": "completed",
        "fields_updated": ["phone", "address"],
        "processing_time_hours": 1,
        "regulatory_deadline": "30 days (CCPA)",
    },
}


@tool()
def process_data_request(subject_id: str, request_type: str, scope: str):
    """
    Processes a data subject request such as access, deletion, portability, or rectification.

    Args:
        subject_id: The data subject's ID (e.g. "DS-101").
        request_type: The type of request — one of "access", "deletion", "portability", "rectification", or "restriction".
        scope: The scope of the request — "full" for all data categories or a specific category like "personal".

    Returns:
        Request processing result including request_id, status, and details specific to the request type, or None if not found.
    """
    key = (
        str(subject_id).lower().strip(),
        str(request_type).lower().strip(),
        str(scope).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
