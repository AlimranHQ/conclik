from app.core.runtime_integration.runtime_registry import runtime_registry

class RuntimeRouter:

    def resolve(self, runtime_name: str):

        runtime = runtime_registry.get(runtime_name)

        if runtime is None:
            raise RuntimeError(
                f"Runtime '{runtime_name}' not registered."
            )

        return runtime

runtime_router = RuntimeRouter()
