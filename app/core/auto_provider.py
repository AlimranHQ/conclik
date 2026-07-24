"""
Conclik Pilot AI
Version : 4.4.0
Module : Auto Provider
"""

from app.core.provider_health import provider_health


class AutoProvider:

    PRIORITY = [
        "gemini",
        "openai",
        "claude",
        "deepseek",
        "grok",
        "mistral",
        "ollama",
    ]

    def select(self):

        health = provider_health.check()

        for provider in self.PRIORITY:
            if health.get(provider):
                return provider

        return None


auto_provider = AutoProvider()
