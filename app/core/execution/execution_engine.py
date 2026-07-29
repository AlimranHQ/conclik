"""
Execution Engine
"""

from app.core.execution.task_manager import task_manager
from app.core.execution.task_executor import task_executor


class ExecutionEngine:

    async def run(self):

        task = task_manager.next()

        if task is None:
            return None

        return await task_executor.execute(task)


execution_engine = ExecutionEngine()

