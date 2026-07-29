"""
Conclik Pilot AI
Core Provider Interface
Version : 2.0.0
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        category: str = "general",
        **kwargs,
    ) -> str:
        ...

    @abstractmethod
    async def health(self) -> bool:
        ...

