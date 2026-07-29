"""
Lazy Gemini Loader
"""

from app.core.providers.mock.mock_registry import MOCK_PROVIDERS

_gemini_client = None


def load_gemini():
    global _gemini_client

    if _gemini_client is not None:
        return _gemini_client

    try:
        from app.providers.gemini_client import gemini_client
        _gemini_client = gemini_client
    except Exception:
        _gemini_client = MOCK_PROVIDERS["gemini"]

    return _gemini_client
