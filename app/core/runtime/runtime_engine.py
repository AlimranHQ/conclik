"""
Runtime Engine
"""

from app.core.runtime.runtime_manager import runtime_manager


class RuntimeEngine:

    async def run(self):

        pipeline = runtime_manager.pipeline()

        return {
            "status": "running",
            "steps": len(pipeline.steps),
        }


runtime_engine = RuntimeEngine()

