class SkillExecutor:

    async def execute(self, skill, *args, **kwargs):
        return await skill.run(*args, **kwargs)


skill_executor = SkillExecutor()
