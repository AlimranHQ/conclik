from app.core.memory.schema.memory_schema import MemoryRecord
from app.core.memory.index.memory_index import memory_index


class MemoryRuntime:

    def __init__(self):
        self._memory = {}

    async def remember(self, goal, data):

        record = MemoryRecord(
            goal=goal,
            workflow=data.get("workflow", {}),
            reflection=data.get("reflection", {}),
            learning=data.get("learning", {}),
            adaptive=data.get("adaptive", {}),
            metadata=data.get("metadata", {}),
        )

        self._memory[goal] = record

        memory_index.add(goal, record.__dict__)

        return {
            "status": "memory_saved",
            "goal": goal,
        }

    async def recall(self, goal):

        record = self._memory.get(goal)

        if record is None:
            return {
                "status": "memory_ready",
                "memory": {},
                "goal": goal,
            }

        return {
            "status": "memory_ready",
            "memory": record.__dict__,
            "goal": goal,
        }

    async def search(self, query):
        return memory_index.search(query)


memory_runtime = MemoryRuntime()
