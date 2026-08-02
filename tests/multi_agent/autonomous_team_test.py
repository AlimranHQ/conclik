import asyncio

import app.core.agents

from app.core.multi_agent.multi_agent_runtime import multi_agent_runtime
from app.core.multi_agent.multi_agent_scheduler import multi_agent_scheduler


print("=== Autonomous Agent Team Test ===")


tasks = [
    "Research",
    "Script",
    "SEO",
    "Thumbnail",
    "Voice",
    "Video",
    "QA",
]


async def main():

    goal = "Build AI YouTube Automation"


    plan = await multi_agent_runtime.run(
        tasks
    )


    result = await multi_agent_scheduler.schedule(
        plan["assignments"],
        goal
    )


    print(result)


    assert result["status"] == "team_completed"

    assert result["total_agents"] == 7


    print("PASS | Autonomous Agent Team")


asyncio.run(main())
