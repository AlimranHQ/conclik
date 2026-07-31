from app.core.execution_coordinator.execution_executor import execution_executor


class ExecutionRuntime:

    async def run(self, assignments):

        executed = await execution_executor.execute(assignments)

        return {
            "executed": executed,
            "completed": len(executed),
        }


execution_runtime = ExecutionRuntime()
