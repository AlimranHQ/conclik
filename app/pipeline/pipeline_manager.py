"""
Conclik v5.0
Pipeline Manager
"""

from app.pipeline.task_queue import add_task, get_task


class PipelineManager:

    def run(self, task: dict):
        add_task(task)
        current = get_task()
        return {
            "status": "success",
            "message": "Task executed",
            "task": current,
        }

    def status(self):
        return {
            "status": "ready"
        }


pipeline_manager = PipelineManager()
