"""
Task Executor
"""

class TaskExecutor:

    async def execute(self, task):
        return {
            "status": "completed",
            "task": task.name,
        }


task_executor = TaskExecutor()

