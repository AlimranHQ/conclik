from app.core.skill_engine.skill_registry import skill_registry
from app.core.skill_engine.skill_executor import skill_executor


class SkillGateway:

    async def run(self, skill_name, *args, **kwargs):

        skill = skill_registry.get(skill_name)

        if skill is None:
            raise RuntimeError(
                f"Unknown skill: {skill_name}"
            )

        return await skill_executor.execute(
            skill,
            *args,
            **kwargs,
        )


skill_gateway = SkillGateway()
