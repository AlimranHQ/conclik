"""
Conclik Pilot AI
Version : 4.3.0
Module  : Context Engine
"""

from app.core.memory_engine import memory_engine


class ContextEngine:

    def build_context(
        self,
        user_prompt: str,
        project: str = "default",
    ):

        history = memory_engine.load(project)

        if history is None:
            history = []

        history.append(user_prompt)

        memory_engine.save(project, history)

        return "\n".join(history)


context_engine = ContextEngine()

