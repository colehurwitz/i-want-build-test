from ibm_watsonx_orchestrate.agent_builder.tools import tool

STUB_RESPONSES = {
    ("email_client", "application"): {
        "test_result": "fail",
        "details": "Application process consuming excessive memory (2.1GB). Likely memory leak in attachment renderer.",
        "recommendation": "Restart the email client application. If issue persists, reinstall.",
    },
    ("vpn", "connectivity"): {
        "test_result": "fail",
        "details": "VPN tunnel drops after idle timeout. DNS resolution for internal domains failing intermittently.",
        "recommendation": "Reconfigure VPN idle timeout settings. Check DNS resolver configuration.",
    },
    ("internal_wiki", "connectivity"): {
        "test_result": "fail",
        "details": "Cannot reach internal wiki server. Depends on VPN connection which is currently unstable.",
        "recommendation": "Fix VPN connectivity first, then retry wiki access.",
    },
    ("monitor", "performance"): {
        "test_result": "fail",
        "details": "Hardware diagnostic detected: monitor not receiving signal. Display adapter may be failing.",
        "recommendation": "Check cable connections. If cables are secure, the display adapter likely needs replacement.",
    },
    ("build_system", "application"): {
        "test_result": "fail",
        "details": "Build system experiencing intermittent compilation failures. Build queue backed up with 15 pending jobs.",
        "recommendation": "Clear build cache and retry. If failures persist, contact infrastructure team.",
    },
    ("two_factor_auth", "security"): {
        "test_result": "pass",
        "details": "Two-factor authentication system is functioning normally. No anomalies detected.",
        "recommendation": "No action required. System is healthy.",
    },
    ("build_system", "connectivity"): {
        "test_result": "pass",
        "details": "Network connectivity to build servers is stable. Latency is within normal range.",
        "recommendation": "Network is not the issue. Check application-level diagnostics.",
    },
    ("monitor", "connectivity"): {
        "test_result": "pass",
        "details": "Network connectivity test not applicable to hardware display issue.",
        "recommendation": "Run performance diagnostic for hardware-related issues.",
    },
}


@tool()
def run_diagnostic(system_name: str, test_type: str):
    """
    Runs a diagnostic test on a specific system.

    Args:
        system_name: The system to diagnose (e.g. "email_client", "vpn", "monitor").
        test_type: The type of diagnostic to run ("connectivity", "performance", "security", "application").

    Returns:
        Diagnostic results including test_result (pass/fail), details, and recommendation, or None if not found.
    """
    key = (
        str(system_name).lower().strip(),
        str(test_type).lower().strip(),
    )
    return STUB_RESPONSES.get(key)
