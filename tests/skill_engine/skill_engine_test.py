import asyncio

from app.core.skill_engine.skill_registry import skill_registry
from app.core.skill_engine.skill_gateway import skill_gateway

print("=== Skill Engine Test ===")


class DemoSkill:

    async def run(self, value):
        return f"Skill executed: {value}"


skill_registry.register(
    "demo",
    DemoSkill(),
)

result = asyncio.run(
    skill_gateway.run(
        "demo",
        "Conclik Skill Engine"
    )
)

print(result)

assert result == "Skill executed: Conclik Skill Engine"

print("PASS | Skill Engine working")
