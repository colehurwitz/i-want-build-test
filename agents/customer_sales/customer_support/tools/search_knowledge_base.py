from ibm_watsonx_orchestrate.agent_builder.tools import tool

_KB_ACCOUNT_ACCESS = {
    "results": [
        {
            "article_id": "KB-101",
            "title": "Troubleshooting Account Access Issues",
            "summary": "Common solutions for account lockouts and access problems",
            "solution": "1. Clear browser cache and cookies. 2. Try incognito mode. 3. Reset password via forgot password link. 4. Check if account is suspended.",
            "relevance_score": 0.92,
        },
        {
            "article_id": "KB-102",
            "title": "SSO Login Failures",
            "summary": "Resolving Single Sign-On authentication issues",
            "solution": "Verify SSO configuration in admin panel. Check SAML certificate expiry.",
            "relevance_score": 0.75,
        },
    ],
    "total_results": 2,
}
_KB_BILLING_DISPUTE = {
    "results": [
        {
            "article_id": "KB-201",
            "title": "Handling Billing Disputes",
            "summary": "Process for reviewing and resolving billing discrepancies",
            "solution": "1. Review invoice details in billing portal. 2. Compare with subscription plan. 3. If overcharge confirmed, issue credit memo. 4. Update billing records.",
            "relevance_score": 0.95,
        },
    ],
    "total_results": 1,
}
_KB_APP_CRASHES = {
    "results": [
        {
            "article_id": "KB-301",
            "title": "Application Crash Troubleshooting",
            "summary": "Steps to diagnose and resolve application crashes",
            "solution": "1. Check system requirements. 2. Update to latest version. 3. Clear app cache. 4. Reinstall if persistent.",
            "relevance_score": 0.88,
        },
    ],
    "total_results": 1,
}
_KB_BILLING_QUESTION = {
    "results": [
        {
            "article_id": "KB-202",
            "title": "Understanding Your Invoice",
            "summary": "Guide to reading and understanding billing statements",
            "solution": "Review the billing FAQ at support.company.com/billing. Contact billing team for specific charge questions.",
            "relevance_score": 0.80,
        },
    ],
    "total_results": 1,
}
_KB_API_ERRORS = {
    "results": [
        {
            "article_id": "KB-302",
            "title": "API Error Code Reference",
            "summary": "Common API error codes and their resolutions",
            "solution": "500 errors: Check service status page. 429 errors: Reduce request rate. 401 errors: Regenerate API key.",
            "relevance_score": 0.90,
        },
    ],
    "total_results": 1,
}

STUB_RESPONSES = {
    ("account access", "account"): _KB_ACCOUNT_ACCESS,
    ("cannot access account login issues", "account"): _KB_ACCOUNT_ACCESS,
    ("cannot access account", "account"): _KB_ACCOUNT_ACCESS,
    ("account access issues", "account"): _KB_ACCOUNT_ACCESS,
    ("account access troubleshooting", "account"): _KB_ACCOUNT_ACCESS,
    ("login issues", "account"): _KB_ACCOUNT_ACCESS,
    ("unable to login", "account"): _KB_ACCOUNT_ACCESS,
    ("account lockout", "account"): _KB_ACCOUNT_ACCESS,
    ("account login", "account"): _KB_ACCOUNT_ACCESS,
    ("login problem", "account"): _KB_ACCOUNT_ACCESS,
    ("access issue", "account"): _KB_ACCOUNT_ACCESS,
    ("account access issue", "account"): _KB_ACCOUNT_ACCESS,
    ("billing dispute", "billing"): _KB_BILLING_DISPUTE,
    ("billing dispute recent charges resolution", "billing"): _KB_BILLING_DISPUTE,
    ("billing dispute resolution", "billing"): _KB_BILLING_DISPUTE,
    ("charge dispute", "billing"): _KB_BILLING_DISPUTE,
    ("invoice dispute", "billing"): _KB_BILLING_DISPUTE,
    ("billing discrepancy", "billing"): _KB_BILLING_DISPUTE,
    ("disputed charge", "billing"): _KB_BILLING_DISPUTE,
    ("overcharge", "billing"): _KB_BILLING_DISPUTE,
    ("billing dispute charges", "billing"): _KB_BILLING_DISPUTE,
    ("app crashes", "technical"): _KB_APP_CRASHES,
    ("application crash", "technical"): _KB_APP_CRASHES,
    ("app crash", "technical"): _KB_APP_CRASHES,
    ("crash", "technical"): _KB_APP_CRASHES,
    ("dashboard crash", "technical"): _KB_APP_CRASHES,
    ("application crashes when loading", "technical"): _KB_APP_CRASHES,
    ("exportfailedexception unable to write file export crash report", "technical"): _KB_APP_CRASHES,
    ("export crash", "technical"): _KB_APP_CRASHES,
    ("exportfailedexception", "technical"): _KB_APP_CRASHES,
    ("unable to write file", "technical"): _KB_APP_CRASHES,
    ("technical issue app crash", "technical"): _KB_APP_CRASHES,
    ("billing question", "billing"): _KB_BILLING_QUESTION,
    ("invoice question", "billing"): _KB_BILLING_QUESTION,
    ("billing inquiry", "billing"): _KB_BILLING_QUESTION,
    ("billing charges", "billing"): _KB_BILLING_QUESTION,
    ("charged wrong plan pro plus standard invoice", "billing"): _KB_BILLING_QUESTION,
    ("wrong plan charge", "billing"): _KB_BILLING_QUESTION,
    ("plan charges", "billing"): _KB_BILLING_QUESTION,
    ("invoice charges", "billing"): _KB_BILLING_QUESTION,
    ("understanding charges", "billing"): _KB_BILLING_QUESTION,
    ("api errors", "technical"): _KB_API_ERRORS,
    ("api error", "technical"): _KB_API_ERRORS,
    ("api error codes", "technical"): _KB_API_ERRORS,
}


@tool()
def search_knowledge_base(query: str, category: str):
    """
    Searches the knowledge base for articles matching a query and category.

    Args:
        query: The search query describing the issue (e.g. "account access").
        category: The category to search within ("billing", "technical", "account", "product", "general").

    Returns:
        Search results including matching articles with titles, summaries, and solutions, or None if no results found.
    """
    key = (
        str(query).lower().strip(),
        str(category).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
