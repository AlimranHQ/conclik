import asyncio

from app.bootstrap.application_bootstrap import initialize_application
initialize_application()

from app.core.ai_gateway.ai_gateway import ai_gateway

print("=== AI Gateway Test ===")

result = asyncio.run(
    ai_gateway.generate(
        "Explain Artificial Intelligence"
    )
)

print(result)

assert result is not None

print("PASS | AI Gateway working")
