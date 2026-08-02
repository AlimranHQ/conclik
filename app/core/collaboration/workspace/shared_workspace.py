class SharedWorkspace:

    def __init__(self):
        self.data = {}

    async def write(self, agent, value):

        if agent not in self.data:
            self.data[agent] = []

        self.data[agent].append(value)

        return {
            "status": "written",
            "agent": agent,
            "entries": len(self.data[agent]),
        }

    async def latest(self, agent):

        history = self.data.get(agent, [])

        if not history:
            return {}

        return history[-1]

    async def history(self, agent):

        return self.data.get(agent, [])

    async def read(self):

        return {
            "status": "workspace_ready",
            "workspace": self.data,
        }

    async def clear(self):
        self.data = {}


shared_workspace = SharedWorkspace()
