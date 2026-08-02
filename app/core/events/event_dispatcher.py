"""
Conclik Event Dispatcher V2
Parallel Collaboration Engine
"""

import asyncio

from app.core.agent_runtime.agent_runtime import agent_runtime


class EventDispatcher:

    def __init__(self):

        self.routes = {}


    def register(self, event_name: str, agents: list):

        self.routes[event_name] = agents


    async def dispatch(self, event):

        agents = self.routes.get(
            event.name,
            []
        )

        if not agents:

            return {
                "status": "no_agents",
                "event": event.name,
            }


        tasks = []

        for agent in agents:

            tasks.append(
                agent_runtime.execute(
                    agent,
                    event.payload.get("task", "")
                )
            )


        results = await asyncio.gather(*tasks)


        return {
            "status": "parallel_completed",
            "event": event.name,
            "agents": agents,
            "results": results,
        }


event_dispatcher = EventDispatcher()
