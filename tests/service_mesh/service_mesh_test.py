import asyncio

from app.core.service_mesh.service_registry import service_registry
from app.core.service_mesh.service_gateway import service_gateway

print("=== Service Mesh Test ===")


class DemoService:

    async def run(self, value):
        return f"Service Mesh executed: {value}"


service_registry.register(
    "demo",
    DemoService(),
)

result = asyncio.run(
    service_gateway.run(
        "demo",
        "Conclik Service Mesh"
    )
)

print(result)

assert result == "Service Mesh executed: Conclik Service Mesh"

print("PASS | Service Mesh working")
