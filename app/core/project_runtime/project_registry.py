class ProjectRegistry:

    def __init__(self):
        self._projects = {}

    def register(self, project_id, project):
        self._projects[project_id] = project

    def get(self, project_id):
        return self._projects.get(project_id)

    def all(self):
        return self._projects


project_registry = ProjectRegistry()
