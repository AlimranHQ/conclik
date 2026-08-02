"""
Master Registry V1
"""


class MasterRegistry:

    def __init__(self):
        self.components = {}


    def register(self, name, component):

        self.components[name] = component


    def get(self, name):

        return self.components.get(name)


    def all(self):

        return self.components


master_registry = MasterRegistry()
