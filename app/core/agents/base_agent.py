"""
Conclik Base Agent
"""

from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def run(self, *args, **kwargs):
        ...
