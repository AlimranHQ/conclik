"""
Multi Agent State V5
"""


class MultiAgentState:

    def __init__(self):

        self.status = "idle"

        self.running = []

        self.completed = []

        self.failed = []


    def start(self, agent):

        self.running.append(agent)


    def complete(self, agent):

        self.completed.append(agent)

        if agent in self.running:
            self.running.remove(agent)


    def fail(self, agent):

        self.failed.append(agent)

        if agent in self.running:
            self.running.remove(agent)


multi_agent_state = MultiAgentState()
