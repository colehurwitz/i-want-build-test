from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    "email_client": [
        {
            "issue_id": "KI-101",
            "title": "Email client crashes on large attachments",
            "status": "active",
            "workaround": "Remove attachments over 25MB. Use cloud file sharing for large files instead.",
            "affected_systems": ["email_client", "outlook"],
        },
    ],
    "vpn": [
        {
            "issue_id": "KI-201",
            "title": "VPN disconnects after 2 hours",
            "status": "active",
            "workaround": "Reconnect the VPN client. Engineering is working on a permanent fix.",
            "affected_systems": ["vpn", "internal_wiki"],
        },
    ],
    "internal_wiki": [
        {
            "issue_id": "KI-201",
            "title": "VPN disconnects after 2 hours",
            "status": "active",
            "workaround": "Reconnect the VPN client. Engineering is working on a permanent fix.",
            "affected_systems": ["vpn", "internal_wiki"],
        },
    ],
    "monitor": [],
    "build_system": [
        {
            "issue_id": "KI-301",
            "title": "Build system intermittent failures since morning maintenance",
            "status": "active",
            "workaround": "Retry the build. If it fails 3 times, escalate to the infrastructure team.",
            "affected_systems": ["build_system", "ci_cd"],
        },
    ],
    "two_factor_auth": [],
}


@tool()
def check_known_issues(system_name: str):
    """
    Checks for known issues affecting a specific system.

    Args:
        system_name: The name of the system to check (e.g. "email_client", "vpn", "monitor").

    Returns:
        A list of known issues with issue_id, title, status, workaround, and affected systems, or None if system not found.
    """
    normalized = str(system_name).lower().strip()
    return STUB_RESPONSES.get(normalized)
