from app.core.agents.research_agent import research_agent

try:
    from app.core.agents.script_agent import script_agent
except Exception:
    script_agent = None

try:
    from app.core.agents.seo_agent import seo_agent
except Exception:
    seo_agent = None

try:
    from app.core.agents.thumbnail_agent import thumbnail_agent
except Exception:
    thumbnail_agent = None

try:
    from app.core.agents.voice_agent import voice_agent
except Exception:
    voice_agent = None

try:
    from app.core.agents.video_agent import video_agent
except Exception:
    video_agent = None

try:
    from app.core.agents.qa_agent import qa_agent
except Exception:
    qa_agent = None


AGENT_REGISTRY = {
    "research_agent": research_agent,
    "script_agent": script_agent,
    "seo_agent": seo_agent,
    "thumbnail_agent": thumbnail_agent,
    "voice_agent": voice_agent,
    "video_agent": video_agent,
    "qa_agent": qa_agent,
}


def get_agent(name: str):
    return AGENT_REGISTRY.get(name)


def list_agents():
    return list(AGENT_REGISTRY.keys())
