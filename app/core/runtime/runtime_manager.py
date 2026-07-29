"""
Runtime Manager
"""

from app.core.runtime.runtime_pipeline import runtime_pipeline


class RuntimeManager:

    def pipeline(self):
        return runtime_pipeline


runtime_manager = RuntimeManager()

