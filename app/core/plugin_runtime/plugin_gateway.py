from app.core.plugin_runtime.plugin_registry import plugin_registry
from app.core.plugin_runtime.plugin_executor import plugin_executor


class PluginGateway:

    async def run(self, plugin_name, *args, **kwargs):

        plugin = plugin_registry.get(plugin_name)

        if plugin is None:
            raise RuntimeError(
                f"Unknown plugin: {plugin_name}"
            )

        return await plugin_executor.execute(
            plugin,
            *args,
            **kwargs,
        )


plugin_gateway = PluginGateway()
