"""
Conclik Kernel

Version : 1.0.0

The central runtime of Conclik OS.
"""

from app.kernel.kernel_manager import kernel_manager


class Kernel:

    async def start(self):

        await kernel_manager.initialize()

    async def shutdown(self):

        await kernel_manager.shutdown()


kernel = Kernel()

