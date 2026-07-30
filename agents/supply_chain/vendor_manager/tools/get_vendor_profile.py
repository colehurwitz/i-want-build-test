from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "v-100": {
        "vendor_id": "V-100",
        "name": "PrecisionParts Ltd",
        "tier": "strategic",
        "categories": ["bearings", "fasteners", "gaskets"],
        "location": "Detroit, MI",
        "contact": "procurement@precisionparts.com",
        "since": "2020-03-15",
        "annual_spend": 1250000.00,
        "payment_terms": "Net-30",
    },
    "v-200": {
        "vendor_id": "V-200",
        "name": "MetalWorks Global",
        "tier": "preferred",
        "categories": ["aluminum", "steel", "copper"],
        "location": "Pittsburgh, PA",
        "contact": "sales@metalworksglobal.com",
        "since": "2021-06-01",
        "annual_spend": 850000.00,
        "payment_terms": "Net-30",
    },
    "v-300": {
        "vendor_id": "V-300",
        "name": "QuickSupply Co",
        "tier": "standard",
        "categories": ["fasteners", "wiring", "gaskets"],
        "location": "Columbus, OH",
        "contact": "orders@quicksupply.com",
        "since": "2023-01-10",
        "annual_spend": 320000.00,
        "payment_terms": "Net-30",
    },
    "v-400": {
        "vendor_id": "V-400",
        "name": "IndustrialDirect Inc",
        "tier": "standard",
        "categories": ["bearings", "aluminum"],
        "location": "Cleveland, OH",
        "contact": "vendor@industrialdirect.com",
        "since": "2022-09-01",
        "annual_spend": 480000.00,
        "payment_terms": "Net-30",
    },
    "v-500": {
        "vendor_id": "V-500",
        "name": "BudgetParts Warehouse",
        "tier": "probationary",
        "categories": ["fasteners", "gaskets"],
        "location": "Toledo, OH",
        "contact": "sales@budgetparts.com",
        "since": "2024-02-15",
        "annual_spend": 150000.00,
        "payment_terms": "Net-15",
    },
}


@tool()
def get_vendor_profile(vendor_id: str):
    """
    Retrieves the profile for a vendor including tier, categories, and contact information.

    Args:
        vendor_id: The vendor identifier (e.g. "V-100").

    Returns:
        Vendor profile with tier, categories, location, contact, and annual spend, or None if not found.
    """
    normalized = str(vendor_id).lower().strip()
    return STUB_RESPONSES.get(normalized)
