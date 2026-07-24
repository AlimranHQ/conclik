"""
Conclik Pilot AI
Version : 4.6.0
Module : Plugin Manager
"""

class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def get(self, name):
        return self.plugins.get(name)

    def list(self):
        return list(self.plugins.keys())


plugin_manager = PluginManager()
