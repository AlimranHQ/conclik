"""
Kernel Events
"""

class KernelEvents:

    def emit(self, event: str):

        return {
            "event": event,
        }


kernel_events = KernelEvents()

