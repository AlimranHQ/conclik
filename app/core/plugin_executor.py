"""
Conclik Pilot AI
Version : 4.6.1
Module : Plugin Executor
"""

from app.core.plugin_manager import plugin_manager


class PluginExecutor:

    def execute(
        self,
        plugin_name,
        *args,
        **kwargs
    ):

        plugin = plugin_manager.get(plugin_name)

        if plugin is None:

            return {
                "success": False,
                "message": "Plugin not found"
            }

        return plugin(*args, **kwargs)


plugin_executor = PluginExecutor()
