class ServiceExecutor:

    async def execute(self, service, *args, **kwargs):
        return await service.run(*args, **kwargs)


service_executor = ServiceExecutor()
