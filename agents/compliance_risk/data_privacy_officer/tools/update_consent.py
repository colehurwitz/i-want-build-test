from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("ds-102", "marketing", False): {
        "subject_id": "DS-102",
        "purpose": "marketing",
        "consent_given": False,
        "previous_status": "expired",
        "new_status": "withdrawn",
        "updated_at": "2024-07-29T10:00:00Z",
        "confirmation": "Marketing consent withdrawn for DS-102",
    },
    ("ds-103", "analytics", False): {
        "subject_id": "DS-103",
        "purpose": "analytics",
        "consent_given": False,
        "previous_status": "active",
        "new_status": "withdrawn",
        "updated_at": "2024-07-29T10:05:00Z",
        "confirmation": "Analytics consent withdrawn for DS-103",
    },
    ("ds-103", "marketing", True): {
        "subject_id": "DS-103",
        "purpose": "marketing",
        "consent_given": True,
        "previous_status": "active",
        "new_status": "active",
        "updated_at": "2024-07-29T10:06:00Z",
        "confirmation": "Marketing consent confirmed for DS-103",
    },
    ("ds-101", "third_party_sharing", True): {
        "subject_id": "DS-101",
        "purpose": "third_party_sharing",
        "consent_given": True,
        "previous_status": "not_given",
        "new_status": "active",
        "updated_at": "2024-07-29T10:10:00Z",
        "confirmation": "Third-party sharing consent granted for DS-101",
    },
    ("ds-104", "marketing", False): {
        "subject_id": "DS-104",
        "purpose": "marketing",
        "consent_given": False,
        "previous_status": "active",
        "new_status": "withdrawn",
        "updated_at": "2024-07-29T10:15:00Z",
        "confirmation": "Marketing consent withdrawn for DS-104",
    },
    ("ds-104", "analytics", True): {
        "subject_id": "DS-104",
        "purpose": "analytics",
        "consent_given": True,
        "previous_status": "not_given",
        "new_status": "active",
        "updated_at": "2024-07-29T10:16:00Z",
        "confirmation": "Analytics consent granted for DS-104",
    },
}


@tool()
def update_consent(subject_id: str, purpose: str, consent_given: bool):
    """
    Updates a data subject's consent for a specific processing purpose.

    Args:
        subject_id: The data subject's ID (e.g. "DS-101").
        purpose: The processing purpose — one of "marketing", "analytics", "third_party_sharing", or "essential_services".
        consent_given: Whether consent is being granted (true) or withdrawn (false).

    Returns:
        Updated consent record including previous_status, new_status, and confirmation message, or None if update failed.
    """
    key = (
        str(subject_id).lower().strip(),
        str(purpose).lower().strip(),
        bool(consent_given),
    )
    return STUB_RESPONSES.get(key)
