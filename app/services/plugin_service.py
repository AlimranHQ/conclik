"""
Conclik Pilot AI
Version : 4.6.0
Module : Plugin Service
"""

from app.core.plugin_loader import plugin_loader


class PluginService:

    def plugins(self):
        return plugin_loader.load()


plugin_service = PluginService()
