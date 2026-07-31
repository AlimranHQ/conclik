from app.core.brain.goal_engine import goal_engine
from app.core.brain.planner_engine import planner_engine
from app.core.brain.task_planner_engine import task_planner_engine
from app.core.brain.decision.decision_engine import decision_engine
from app.core.brain.assignment.assignment_engine import assignment_engine

from app.core.brain.learning.learning_engine import learning_engine
from app.core.brain.adaptive.adaptive_engine import adaptive_engine

from app.core.brain.personality.personality_engine import personality_engine
from app.core.brain.conversation.conversation_engine import conversation_engine

ENGINES = {
    "goal": goal_engine,
    "planner": planner_engine,
    "task_planner": task_planner_engine,
    "decision": decision_engine,
    "assignment": assignment_engine,
    "learning": learning_engine,
    "adaptive": adaptive_engine,
    "personality": personality_engine,
    "conversation": conversation_engine,
}

print("=== Kernel Contract Audit ===")

for name, engine in ENGINES.items():

    print(name)

    print("run:", hasattr(engine, "run"))
    print("status:", hasattr(engine, "status"))
    print("validate:", hasattr(engine, "validate"))
    print("reset:", hasattr(engine, "reset"))
    print()
