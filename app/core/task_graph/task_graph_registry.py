class TaskGraphRegistry:

    def __init__(self):
        self._graphs = {}

    def register(self, name, graph):
        self._graphs[name] = graph

    def get(self, name):
        return self._graphs.get(name)

    def all(self):
        return self._graphs


task_graph_registry = TaskGraphRegistry()
