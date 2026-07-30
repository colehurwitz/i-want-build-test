from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "user@eu-company.com": {
        "subject_id": "DS-101",
        "name": "Hans Mueller",
        "email": "user@eu-company.com",
        "jurisdiction": "EU",
        "data_categories": ["personal", "financial", "behavioral"],
        "registration_date": "2022-03-15",
        "last_activity": "2024-07-20",
    },
    "ds-101": {
        "subject_id": "DS-101",
        "name": "Hans Mueller",
        "email": "user@eu-company.com",
        "jurisdiction": "EU",
        "data_categories": ["personal", "financial", "behavioral"],
        "registration_date": "2022-03-15",
        "last_activity": "2024-07-20",
    },
    "gdpr@company.eu": {
        "subject_id": "DS-102",
        "name": "Marie Dupont",
        "email": "gdpr@company.eu",
        "jurisdiction": "EU",
        "data_categories": ["personal", "behavioral"],
        "registration_date": "2021-08-01",
        "last_activity": "2024-07-15",
    },
    "ds-102": {
        "subject_id": "DS-102",
        "name": "Marie Dupont",
        "email": "gdpr@company.eu",
        "jurisdiction": "EU",
        "data_categories": ["personal", "behavioral"],
        "registration_date": "2021-08-01",
        "last_activity": "2024-07-15",
    },
    "user@company.com": {
        "subject_id": "DS-103",
        "name": "Alex Johnson",
        "email": "user@company.com",
        "jurisdiction": "US",
        "data_categories": ["personal", "financial", "behavioral", "health"],
        "registration_date": "2023-01-10",
        "last_activity": "2024-07-28",
    },
    "ds-103": {
        "subject_id": "DS-103",
        "name": "Alex Johnson",
        "email": "user@company.com",
        "jurisdiction": "US",
        "data_categories": ["personal", "financial", "behavioral", "health"],
        "registration_date": "2023-01-10",
        "last_activity": "2024-07-28",
    },
    "user@uk-company.co.uk": {
        "subject_id": "DS-104",
        "name": "James Wright",
        "email": "user@uk-company.co.uk",
        "jurisdiction": "UK",
        "data_categories": ["personal", "financial"],
        "registration_date": "2023-06-20",
        "last_activity": "2024-07-25",
    },
    "ds-104": {
        "subject_id": "DS-104",
        "name": "James Wright",
        "email": "user@uk-company.co.uk",
        "jurisdiction": "UK",
        "data_categories": ["personal", "financial"],
        "registration_date": "2023-06-20",
        "last_activity": "2024-07-25",
    },
    "user@partner.de": {
        "subject_id": "DS-105",
        "name": "Lena Schmidt",
        "email": "user@partner.de",
        "jurisdiction": "EU",
        "data_categories": ["personal"],
        "registration_date": "2024-01-05",
        "last_activity": "2024-04-10",
    },
    "ds-105": {
        "subject_id": "DS-105",
        "name": "Lena Schmidt",
        "email": "user@partner.de",
        "jurisdiction": "EU",
        "data_categories": ["personal"],
        "registration_date": "2024-01-05",
        "last_activity": "2024-04-10",
    },
}


@tool()
def lookup_data_subject(identifier: str, identifier_type: str):
    """
    Looks up a data subject by email address or subject ID.

    Args:
        identifier: The data subject's email address or subject ID (e.g. "user@company.com" or "DS-101").
        identifier_type: The type of identifier provided — either "email" or "subject_id".

    Returns:
        The data subject's profile including subject_id, name, email, jurisdiction, data_categories, and registration_date, or None if not found.
    """
    normalized = str(identifier).lower().strip()
    return STUB_RESPONSES.get(normalized)
