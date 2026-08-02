"""
Conclik Workflow V4
"""

from dataclasses import dataclass, field


@dataclass
class WorkflowTask:

    id: int

    name: str

    agent: str = None

    mode: str = "sequential"

    depends_on: list = field(default_factory=list)

    status: str = "pending"


@dataclass
class Workflow:

    name: str

    tasks: list = field(default_factory=list)

    mode: str = "sequential"

    metadata: dict = field(default_factory=dict)

    def add_task(self, task: WorkflowTask):

        self.tasks.append(task)

        return task
