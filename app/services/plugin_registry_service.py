"""
Conclik Pilot AI
Version : 4.6.1
Module : Plugin Registry Service
"""

from app.core.plugin_registry import plugin_registry


class PluginRegistryService:

    def register(
        self,
        name,
        plugin
    ):

        plugin_registry.register(
            name,
            plugin
        )


plugin_registry_service = PluginRegistryService()
