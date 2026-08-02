"""
Conclik Built-in Agents
"""

from app.core.agent_runtime.agent_manager import agent_manager

from app.core.agents.research_agent import research_agent
from app.core.agents.script_agent import script_agent
from app.core.agents.seo_agent import seo_agent
from app.core.agents.thumbnail_agent import thumbnail_agent
from app.core.agents.voice_agent import voice_agent
from app.core.agents.video_agent import video_agent
from app.core.agents.qa_agent import qa_agent


agent_manager.register(research_agent.name, research_agent)
agent_manager.register(script_agent.name, script_agent)
agent_manager.register(seo_agent.name, seo_agent)
agent_manager.register(thumbnail_agent.name, thumbnail_agent)
agent_manager.register(voice_agent.name, voice_agent)
agent_manager.register(video_agent.name, video_agent)
agent_manager.register(qa_agent.name, qa_agent)


__all__ = [
    "research_agent",
    "script_agent",
    "seo_agent",
    "thumbnail_agent",
    "voice_agent",
    "video_agent",
    "qa_agent",
]
