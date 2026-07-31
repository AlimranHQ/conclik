from app.core.service_mesh.service_registry import service_registry
from app.core.service_mesh.service_executor import service_executor


class ServiceGateway:

    async def run(self, service_name, *args, **kwargs):

        service = service_registry.get(service_name)

        if service is None:
            raise RuntimeError(
                f"Unknown service: {service_name}"
            )

        return await service_executor.execute(
            service,
            *args,
            **kwargs,
        )


service_gateway = ServiceGateway()
