"""
Conclik Pilot AI
Version : 4.6.0
Module : Plugin Loader
"""

from app.core.plugin_manager import plugin_manager


class PluginLoader:

    def load(self):
        return plugin_manager.list()


plugin_loader = PluginLoader()
