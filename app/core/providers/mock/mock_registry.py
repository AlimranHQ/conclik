"""
Mock Provider Registry
"""

from app.core.providers.mock.mock_gemini import mock_gemini

MOCK_PROVIDERS = {
    "gemini": mock_gemini,
}
