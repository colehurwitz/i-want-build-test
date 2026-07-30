from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ds-101", "marketing"): {
        "subject_id": "DS-101",
        "purpose": "marketing",
        "consent_given": True,
        "consent_date": "2022-03-15",
        "expiry_date": "2025-03-15",
        "status": "active",
    },
    ("ds-101", "analytics"): {
        "subject_id": "DS-101",
        "purpose": "analytics",
        "consent_given": True,
        "consent_date": "2022-03-15",
        "expiry_date": "2025-03-15",
        "status": "active",
    },
    ("ds-101", "third_party_sharing"): {
        "subject_id": "DS-101",
        "purpose": "third_party_sharing",
        "consent_given": False,
        "consent_date": None,
        "expiry_date": None,
        "status": "not_given",
    },
    ("ds-101", "essential_services"): {
        "subject_id": "DS-101",
        "purpose": "essential_services",
        "consent_given": True,
        "consent_date": "2022-03-15",
        "expiry_date": None,
        "status": "active",
    },
    ("ds-102", "marketing"): {
        "subject_id": "DS-102",
        "purpose": "marketing",
        "consent_given": True,
        "consent_date": "2021-08-01",
        "expiry_date": "2023-08-01",
        "status": "expired",
    },
    ("ds-102", "analytics"): {
        "subject_id": "DS-102",
        "purpose": "analytics",
        "consent_given": False,
        "consent_date": None,
        "expiry_date": None,
        "status": "not_given",
    },
    ("ds-102", "essential_services"): {
        "subject_id": "DS-102",
        "purpose": "essential_services",
        "consent_given": True,
        "consent_date": "2021-08-01",
        "expiry_date": None,
        "status": "active",
    },
    ("ds-103", "marketing"): {
        "subject_id": "DS-103",
        "purpose": "marketing",
        "consent_given": True,
        "consent_date": "2023-01-10",
        "expiry_date": "2026-01-10",
        "status": "active",
    },
    ("ds-103", "analytics"): {
        "subject_id": "DS-103",
        "purpose": "analytics",
        "consent_given": True,
        "consent_date": "2023-01-10",
        "expiry_date": "2026-01-10",
        "status": "active",
    },
    ("ds-103", "third_party_sharing"): {
        "subject_id": "DS-103",
        "purpose": "third_party_sharing",
        "consent_given": True,
        "consent_date": "2023-01-10",
        "expiry_date": "2026-01-10",
        "status": "active",
    },
    ("ds-103", "essential_services"): {
        "subject_id": "DS-103",
        "purpose": "essential_services",
        "consent_given": True,
        "consent_date": "2023-01-10",
        "expiry_date": None,
        "status": "active",
    },
    ("ds-104", "marketing"): {
        "subject_id": "DS-104",
        "purpose": "marketing",
        "consent_given": True,
        "consent_date": "2023-06-20",
        "expiry_date": "2025-06-20",
        "status": "active",
    },
    ("ds-104", "analytics"): {
        "subject_id": "DS-104",
        "purpose": "analytics",
        "consent_given": False,
        "consent_date": None,
        "expiry_date": None,
        "status": "not_given",
    },
    ("ds-104", "essential_services"): {
        "subject_id": "DS-104",
        "purpose": "essential_services",
        "consent_given": True,
        "consent_date": "2023-06-20",
        "expiry_date": None,
        "status": "active",
    },
    ("ds-105", "marketing"): {
        "subject_id": "DS-105",
        "purpose": "marketing",
        "consent_given": False,
        "consent_date": None,
        "expiry_date": None,
        "status": "not_given",
    },
    ("ds-105", "essential_services"): {
        "subject_id": "DS-105",
        "purpose": "essential_services",
        "consent_given": True,
        "consent_date": "2024-01-05",
        "expiry_date": None,
        "status": "active",
    },
}


@tool()
def check_consent_status(subject_id: str, purpose: str):
    """
    Checks the consent status of a data subject for a specific processing purpose.

    Args:
        subject_id: The data subject's ID (e.g. "DS-101").
        purpose: The processing purpose to check — one of "marketing", "analytics", "third_party_sharing", or "essential_services".

    Returns:
        Consent record including subject_id, purpose, consent_given, consent_date, expiry_date, and status ("active", "expired", or "not_given"), or None if not found.
    """
    key = (str(subject_id).lower().strip(), str(purpose).lower().strip())
    return STUB_RESPONSES.get(key)
