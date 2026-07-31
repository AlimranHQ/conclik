class PluginRegistry:

    def __init__(self):
        self._plugins = {}

    def register(self, name, plugin):
        self._plugins[name] = plugin

    def get(self, name):
        return self._plugins.get(name)

    def all(self):
        return self._plugins


plugin_registry = PluginRegistry()
