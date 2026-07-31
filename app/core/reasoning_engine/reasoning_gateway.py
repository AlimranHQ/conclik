from app.core.reasoning_engine.reasoning_registry import reasoning_registry
from app.core.reasoning_engine.reasoning_executor import reasoning_executor


class ReasoningGateway:

    async def run(self, engine_name, *args, **kwargs):

        engine = reasoning_registry.get(engine_name)

        if engine is None:
            raise RuntimeError(
                f"Unknown reasoning engine: {engine_name}"
            )

        return await reasoning_executor.execute(
            engine,
            *args,
            **kwargs,
        )


reasoning_gateway = ReasoningGateway()
