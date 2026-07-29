import asyncio

from app.bootstrap.application_bootstrap import initialize_application
from app.agents.research_agent import research_agent
from app.core.agent_runtime.agent_manager import agent_manager
from app.core.agent_runtime.agent_runtime import agent_runtime

print("=== Research Runtime Test ===")

# Boot the application (register providers)
initialize_application()

agent_manager.register(
    research_agent.name,
    research_agent,
)

result = asyncio.run(
    agent_runtime.run(
        "research",
        "Artificial Intelligence"
    )
)

assert result is not None

print("PASS | Research Agent Runtime OK")
