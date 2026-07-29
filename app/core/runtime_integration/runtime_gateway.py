from app.core.runtime_integration.runtime_dispatcher import runtime_dispatcher

class RuntimeGateway:

    async def run(
        self,
        runtime_name,
        *args,
        **kwargs,
    ):
        return await runtime_dispatcher.dispatch(
            runtime_name,
            *args,
            **kwargs,
        )

runtime_gateway = RuntimeGateway()
