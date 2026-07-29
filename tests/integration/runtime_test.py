import asyncio

from app.core.runtime.runtime_pipeline import runtime_pipeline
from app.core.runtime.runtime_engine import runtime_engine

print("=== Runtime Test ===")

runtime_pipeline.add("research")
runtime_pipeline.add("script")

result = asyncio.run(runtime_engine.run())

assert result["status"] == "running"
assert result["steps"] == 2

print("PASS | Runtime Engine working")
