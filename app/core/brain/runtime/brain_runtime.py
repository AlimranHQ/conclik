from app.core.brain.goal_engine import goal_engine
from app.core.brain.planner_engine import planner_engine
from app.core.brain.task_planner_engine import task_planner_engine
from app.core.brain.decision.decision_engine import decision_engine

from app.core.brain.assignment.assignment_runtime import assignment_runtime

from app.core.brain.personality.personality_runtime import personality_runtime
from app.core.brain.conversation.conversation_engine import conversation_engine

from app.core.brain.reflection.reflection_runtime import reflection_runtime
from app.core.brain.learning.learning_runtime import learning_runtime
from app.core.brain.adaptive.adaptive_runtime import adaptive_runtime
from app.core.brain.memory.memory_runtime import memory_runtime


class BrainRuntime:

    async def run(self, goal):

        goal_result = await goal_engine.run(goal)

        plan = await planner_engine.run(goal)

        graph = await task_planner_engine.run(goal)

        decision = await decision_engine.run(goal)

        assignment = await assignment_runtime.run(goal)

        reflection = await reflection_runtime.run(
            assignment["results"]
        )

        learning = await learning_runtime.run(reflection)

        adaptive = await adaptive_runtime.run(
            learning["learning"]
        )

        personality = await personality_runtime.run(goal)

        conversation = await conversation_engine.run(goal)

        memory = await memory_runtime.recall(goal)

        await memory_runtime.remember(
            goal,
            {
                "assignment": assignment,
                "reflection": reflection,
                "learning": learning,
                "adaptive": adaptive,
            }
        )

        return {
            "status": "brain_ready",

            "goal": goal_result,
            "plan": plan,
            "graph": graph,
            "decision": decision,

            "assignment": assignment,

            "reflection": reflection,
            "learning": learning,
            "adaptive": adaptive,

            "memory": memory,
            "memory_updated": True,

            "personality": personality,
            "conversation": conversation,
        }


brain_runtime = BrainRuntime()
