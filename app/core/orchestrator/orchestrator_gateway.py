from app.core.orchestrator.orchestrator_registry import orchestrator_registry
from app.core.orchestrator.orchestrator_executor import orchestrator_executor


class OrchestratorGateway:

    async def run(self, runtime_name, *args, **kwargs):

        runtime = orchestrator_registry.get(runtime_name)

        if runtime is None:
            raise RuntimeError(
                f"Unknown orchestrator runtime: {runtime_name}"
            )

        return await orchestrator_executor.execute(
            runtime,
            *args,
            **kwargs,
        )


orchestrator_gateway = OrchestratorGateway()
