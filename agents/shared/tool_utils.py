"""Shared utilities for agent tool development.

Provides helpers for building STUB_RESPONSES-based tools following
the watsonx Orchestrate ADK pattern (returning dicts/lists directly).
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool


def normalize_key(value):
    """Normalize a string key for STUB_RESPONSES lookup."""
    return str(value).lower().strip()


def normalize_compound_key(*values):
    """Normalize a compound tuple key for STUB_RESPONSES lookup."""
    return tuple(normalize_key(v) for v in values)


def lookup(stub_responses, key):
    """Look up a normalized key in STUB_RESPONSES, return None if not found."""
    if isinstance(key, tuple):
        normalized = normalize_compound_key(*key)
    else:
        normalized = normalize_key(key)
    return stub_responses.get(normalized)
