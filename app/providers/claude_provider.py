"""
Conclik Pilot AI
Version : 4.4.0
Module : Claude Provider
"""

from app.providers.base_provider import BaseProvider


class ClaudeProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Claude",
            "prompt": prompt,
            "status": "ready"
        }


claude_provider = ClaudeProvider()
