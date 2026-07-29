"""
Conclik Pilot AI
Base Agent
Version : 1.0.0
"""

from abc import ABC, abstractmethod

from app.core.intelligence.intelligence_engine import intelligence_engine


class BaseAgent(ABC):

    def __init__(
        self,
        provider: str = "gemini",
    ):
        self.provider = provider

    async def ask_ai(
        self,
        prompt: str,
        category: str = "general",
        **kwargs,
    ):

        return await intelligence_engine.generate(
            prompt=prompt,
            category=category,
            preferred_provider=self.provider,
            **kwargs,
        )

    @abstractmethod
    async def run(
        self,
        *args,
        **kwargs,
    ):
        """
        Every agent must implement this.
        """
        raise NotImplementedError

