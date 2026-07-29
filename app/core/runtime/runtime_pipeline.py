"""
Runtime Pipeline
"""

class RuntimePipeline:

    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)


runtime_pipeline = RuntimePipeline()

