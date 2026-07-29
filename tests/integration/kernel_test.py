from app.kernel.kernel_state import kernel_state

print("=== Kernel Integration Test ===")

assert kernel_state.version == "1.0.0"

print("PASS | Kernel version detected")
