import asyncio

from app.core.knowledge_engine.knowledge_registry import knowledge_registry
from app.core.knowledge_engine.knowledge_gateway import knowledge_gateway

print("=== Knowledge Engine Test ===")


class DemoKnowledge:

    async def run(self, topic):
        return f"Knowledge Engine executed: {topic}"


knowledge_registry.register(
    "demo",
    DemoKnowledge(),
)

result = asyncio.run(
    knowledge_gateway.run(
        "demo",
        "Artificial Intelligence"
    )
)

print(result)

assert result == "Knowledge Engine executed: Artificial Intelligence"

print("PASS | Knowledge Engine working")
