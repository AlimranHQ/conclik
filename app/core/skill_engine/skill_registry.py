class SkillRegistry:

    def __init__(self):
        self._skills = {}

    def register(self, name, skill):
        self._skills[name] = skill

    def get(self, name):
        return self._skills.get(name)

    def all(self):
        return self._skills


skill_registry = SkillRegistry()
