from app.core.runtime_integration.runtime_router import runtime_router
from app.core.runtime_integration.runtime_executor import runtime_executor

class RuntimeDispatcher:

    async def dispatch(
        self,
        runtime_name,
        *args,
        **kwargs,
    ):

        runtime = runtime_router.resolve(runtime_name)

        return await runtime_executor.execute(
            runtime,
            *args,
            **kwargs,
        )

runtime_dispatcher = RuntimeDispatcher()
