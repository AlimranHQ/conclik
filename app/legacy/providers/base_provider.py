"""
Conclik Pilot AI
Version : 4.4.0
Module : Base Provider
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str):
        pass
