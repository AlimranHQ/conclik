"""
Kernel Manager
"""

from app.kernel.kernel_state import kernel_state


class KernelManager:

    async def initialize(self):

        kernel_state.running = True

    async def shutdown(self):

        kernel_state.running = False


kernel_manager = KernelManager()

