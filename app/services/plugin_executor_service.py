"""
Conclik Pilot AI
Version : 4.6.1
Module : Plugin Executor Service
"""

from app.core.plugin_executor import plugin_executor


class PluginExecutorService:

    def execute(
        self,
        plugin_name,
        *args,
        **kwargs
    ):

        return plugin_executor.execute(
            plugin_name,
            *args,
            **kwargs
        )


plugin_executor_service = PluginExecutorService()
