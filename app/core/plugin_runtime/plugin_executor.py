class PluginExecutor:

    async def execute(self, plugin, *args, **kwargs):
        return await plugin.run(*args, **kwargs)


plugin_executor = PluginExecutor()
