"""
Kernel Health Monitor
"""

from app.kernel.kernel_state import kernel_state


class KernelHealth:

    def status(self):

        return {
            "running": kernel_state.running,
            "version": kernel_state.version,
        }


kernel_health = KernelHealth()

