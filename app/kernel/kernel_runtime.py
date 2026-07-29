"""
Conclik Kernel Runtime

Version : 1.0.0
"""

from app.core.intelligence.intelligence_engine import intelligence_engine


class KernelRuntime:

    async def initialize(self):

        return True

    async def start(self):

        return intelligence_engine

    async def stop(self):

        return True


kernel_runtime = KernelRuntime()

