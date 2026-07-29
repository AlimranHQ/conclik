class PipelineRegistry:

    def __init__(self):
        self._steps = []

    def register(self, step):
        self._steps.append(step)

    def all(self):
        return self._steps


pipeline_registry = PipelineRegistry()
