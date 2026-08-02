"""
Multi Agent Context V5
"""


class MultiAgentContext:

    def __init__(self, goal=None):

        self.goal = goal
        self.data = {}
        self.events = []


    def set(self, key, value):

        self.data[key] = value


    def get(self, key, default=None):

        return self.data.get(key, default)


    def add_event(self, event):

        self.events.append(event)


multi_agent_context = MultiAgentContext()
