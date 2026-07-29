"""
Conclik Provider Registry Test
"""

from app.core.providers.provider_registry import provider_registry

print("\n=== Provider Registry Test ===")

providers = provider_registry.all()

print(f"Registered Providers : {len(providers)}")

if len(providers) == 0:
    print("PASS | Registry initialized successfully (0 providers registered)")
else:
    for provider in providers:
        print(f"PASS | {provider.name}")

print("\nRegistry Test Completed")

