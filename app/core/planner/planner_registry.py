class PlannerRegistry:

    def __init__(self):
        self._planners = {}

    def register(self, name, planner):
        self._planners[name] = planner

    def get(self, name):
        return self._planners.get(name)

    def all(self):
        return self._planners


planner_registry = PlannerRegistry()
