from app.core.container.service_container import service_container

print("=== Service Container Test ===")

service_container.register("demo", {"status": "ok"})

assert service_container.resolve("demo")["status"] == "ok"

print("PASS | Service Container working")
