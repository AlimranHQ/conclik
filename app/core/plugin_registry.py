"""
Conclik Pilot AI
Version : 4.6.0
Module : Plugin Registry
"""

from app.core.plugin_manager import plugin_manager


class PluginRegistry:

    def register(self, name, plugin):
        plugin_manager.register(name, plugin)


plugin_registry = PluginRegistry()
