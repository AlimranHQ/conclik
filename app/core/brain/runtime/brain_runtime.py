from app.core.brain.goal_engine import goal_engine
from app.core.brain.planner_engine import planner_engine
from app.core.brain.task_planner_engine import task_planner_engine
from app.core.brain.decision.decision_engine import decision_engine

from app.core.workflow_engine.workflow_engine import workflow_engine

from app.core.collaboration.pipeline.agent_pipeline import (
    agent_pipeline,
)

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

        workflow = await workflow_engine.execute(goal)

        pipeline = await agent_pipeline.run(goal)

        reflection = await reflection_runtime.run(
            workflow["results"]
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
                "workflow": workflow,
                "pipeline": pipeline,
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

            "workflow": workflow,
            "pipeline": pipeline,

            "reflection": reflection,
            "learning": learning,
            "adaptive": adaptive,

            "memory": memory,
            "memory_updated": True,

            "personality": personality,
            "conversation": conversation,
        }


brain_runtime = BrainRuntime()
