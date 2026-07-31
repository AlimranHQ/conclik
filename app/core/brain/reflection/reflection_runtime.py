from app.core.reflection_engine.reflection_runtime import reflection_runtime as core_reflection_runtime


class BrainReflectionRuntime:

    async def evaluate(self):

        result = {
            "score": 100,
            "status": "completed",
        }

        analysis = await core_reflection_runtime.run(result)

        return {
            "status": "reflection_ready",
            "reflection": analysis,
        }


reflection_runtime = BrainReflectionRuntime()
