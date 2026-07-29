from app.core.memory.memory_manager import memory_manager

print("=== Memory Integration Test ===")

memory_manager.save("project", "Conclik")

assert memory_manager.load("project") == "Conclik"

print("PASS | Memory Engine working")
