from app.core.autonomous_core.autonomous_registry import autonomous_registry
from app.core.autonomous_core.autonomous_executor import autonomous_executor


class AutonomousGateway:

    async def run(self, core_name, *args, **kwargs):

        core = autonomous_registry.get(core_name)

        if core is None:
            raise RuntimeError(
                f"Unknown autonomous core: {core_name}"
            )

        return await autonomous_executor.execute(
            core,
            *args,
            **kwargs,
        )


autonomous_gateway = AutonomousGateway()
