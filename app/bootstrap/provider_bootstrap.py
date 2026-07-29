"""
Provider Bootstrap
Version : 2.1.0
"""

from app.core.providers.provider_registry import provider_registry
from app.core.providers.adapters.gemini_provider import gemini_provider


def initialize_providers():

    provider_registry.register(gemini_provider)

    return {
        "providers": provider_registry,
        "status": "initialized",
    }
