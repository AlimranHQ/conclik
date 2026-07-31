import asyncio

from app.core.plugin_runtime.plugin_registry import plugin_registry
from app.core.plugin_runtime.plugin_gateway import plugin_gateway

print("=== Plugin Runtime Test ===")


class DemoPlugin:

    async def run(self, value):
        return f"Plugin executed: {value}"


plugin_registry.register(
    "demo",
    DemoPlugin(),
)

result = asyncio.run(
    plugin_gateway.run(
        "demo",
        "Conclik Plugin"
    )
)

print(result)

assert result == "Plugin executed: Conclik Plugin"

print("PASS | Plugin Runtime working")
