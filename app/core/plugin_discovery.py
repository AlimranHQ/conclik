"""
Conclik Pilot AI
Version : 4.6.1
Module : Plugin Discovery
"""

from app.core.plugin_manager import plugin_manager


class PluginDiscovery:

    def discover(self):

        return {
            "count": len(plugin_manager.list()),
            "plugins": plugin_manager.list()
        }


plugin_discovery = PluginDiscovery()
