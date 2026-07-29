from app.core.execution.task import Task
from app.core.workflow_engine.workflow import Workflow
from app.core.workflow_engine.workflow_manager import workflow_manager
from app.core.workflow_engine.workflow_executor import workflow_executor

print("=== Workflow Test ===")

workflow = Workflow(
    name="demo",
    tasks=[
        Task("research", {}),
        Task("script", {}),
    ],
)

workflow_manager.register(workflow)

loaded = workflow_manager.load("demo")

assert loaded is not None

workflow_executor.execute(loaded)

print("PASS | Workflow Engine working")
