from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("software", "fail"): [
        {"step_num": 1, "action": "Close all instances of the application", "expected_outcome": "All processes terminated"},
        {"step_num": 2, "action": "Clear the application cache folder", "expected_outcome": "Cache directory emptied"},
        {"step_num": 3, "action": "Restart the application", "expected_outcome": "Application starts without errors"},
        {"step_num": 4, "action": "If issue persists, uninstall and reinstall the application", "expected_outcome": "Fresh installation resolves the issue"},
    ],
    ("network", "fail"): [
        {"step_num": 1, "action": "Disconnect and reconnect the VPN client", "expected_outcome": "VPN reconnects successfully"},
        {"step_num": 2, "action": "Flush DNS cache (ipconfig /flushdns or sudo dscacheutil -flushcache)", "expected_outcome": "DNS cache cleared"},
        {"step_num": 3, "action": "Restart network adapter", "expected_outcome": "Network adapter reinitialized"},
        {"step_num": 4, "action": "If still failing, try a different VPN server endpoint", "expected_outcome": "Connection established on alternate endpoint"},
    ],
    ("hardware", "fail"): [
        {"step_num": 1, "action": "Check all cable connections (power, display, peripherals)", "expected_outcome": "Cables are securely connected"},
        {"step_num": 2, "action": "Try connecting to a different port or using a different cable", "expected_outcome": "Determine if cable or port is faulty"},
        {"step_num": 3, "action": "If display adapter failure suspected, request hardware replacement", "expected_outcome": "Replacement order submitted"},
    ],
    ("access", "pass"): [
        {"step_num": 1, "action": "Navigate to the company security portal at security.company.com", "expected_outcome": "Security portal loads"},
        {"step_num": 2, "action": "Click 'Set up two-factor authentication' under Account Security", "expected_outcome": "2FA setup wizard begins"},
        {"step_num": 3, "action": "Scan the QR code with your authenticator app (Google Authenticator or Authy)", "expected_outcome": "App displays 6-digit code"},
        {"step_num": 4, "action": "Enter the 6-digit code to verify setup", "expected_outcome": "2FA is activated for your account"},
    ],
}


@tool()
def get_resolution_steps(category: str, diagnostic_result: str):
    """
    Retrieves resolution steps based on ticket category and diagnostic outcome.

    Args:
        category: The issue category ("software", "network", "hardware", "access").
        diagnostic_result: The diagnostic result ("pass" or "fail").

    Returns:
        A list of resolution steps with step number, action, and expected outcome, or None if not found.
    """
    key = (
        str(category).lower().strip(),
        str(diagnostic_result).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
