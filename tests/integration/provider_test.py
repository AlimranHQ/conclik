from app.core.providers.provider_registry import provider_registry

print("=== Provider Registry Test ===")

assert provider_registry is not None

print("PASS | Provider Registry available")
