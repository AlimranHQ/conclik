import asyncio

from app.bootstrap.application_bootstrap import initialize_application
initialize_application()

from app.core.pipeline_runtime.pipeline_registry import pipeline_registry
from app.core.agent_runtime.agent_runtime import agent_runtime
from app.agents.research_agent import research_agent
from app.core.project_runtime.project_runtime import project_runtime

print("=== Project Runtime Test ===")

class ResearchStep:

    async def run(self, topic):
        return await agent_runtime.run(
            research_agent,
            topic,
        )

pipeline_registry.register(ResearchStep())

result = asyncio.run(
    project_runtime.run(
        "Artificial Intelligence"
    )
)

assert result.success is True

print(result.data)

print("PASS | Project Runtime OK")
