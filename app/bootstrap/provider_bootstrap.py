"""
Conclik Pilot AI
Provider Bootstrap
Version : 1.0.0
"""

from app.core.providers.provider_registry import provider_registry


def initialize_providers():

    """
    Register all AI providers here.

    Example:

    provider_registry.register(gemini_provider)

    provider_registry.register(openai_provider)

    provider_registry.register(claude_provider)
    """

    return provider_registry

