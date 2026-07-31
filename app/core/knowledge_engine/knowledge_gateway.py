from app.core.knowledge_engine.knowledge_registry import knowledge_registry
from app.core.knowledge_engine.knowledge_executor import knowledge_executor


class KnowledgeGateway:

    async def run(self, engine_name, *args, **kwargs):

        engine = knowledge_registry.get(engine_name)

        if engine is None:
            raise RuntimeError(
                f"Unknown knowledge engine: {engine_name}"
            )

        return await knowledge_executor.execute(
            engine,
            *args,
            **kwargs,
        )


knowledge_gateway = KnowledgeGateway()
