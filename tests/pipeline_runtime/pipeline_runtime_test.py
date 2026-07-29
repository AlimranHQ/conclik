import asyncio

from app.bootstrap.application_bootstrap import initialize_application

# Boot Conclik before running pipeline
initialize_application()

from app.core.pipeline_runtime.pipeline_registry import pipeline_registry
from app.core.pipeline_runtime.pipeline_runtime import pipeline_runtime
from app.core.agent_runtime.agent_runtime import agent_runtime

from app.agents.research_agent import research_agent

print("=== Pipeline Runtime Test ===")


class ResearchStep:

    async def run(self, topic):
        return await agent_runtime.run(
            research_agent,
            topic,
        )


pipeline_registry.register(ResearchStep())

result = asyncio.run(
    pipeline_runtime.run(
        "Artificial Intelligence"
    )
)

print(result)

print("PASS | Pipeline Runtime working")
