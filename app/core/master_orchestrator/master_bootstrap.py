"""
Master Bootstrap V1
"""

from app.core.master_orchestrator.master_registry import master_registry
from app.core.master_orchestrator.master_runtime import master_runtime


class MasterBootstrap:

    def boot(self):

        master_registry.register(
            "master_runtime",
            master_runtime
        )

        return {
            "status": "boot_completed",
            "components": list(
                master_registry.all().keys()
            )
        }


master_bootstrap = MasterBootstrap()
