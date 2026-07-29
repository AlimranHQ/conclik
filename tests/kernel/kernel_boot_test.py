from app.kernel.kernel_state import kernel_state
from app.bootstrap.application_bootstrap import initialize_application

print("=== Conclik Kernel Boot Test ===")

initialize_application()

assert kernel_state.running is True

print("PASS | Kernel started successfully")
print(f"Kernel Version : {kernel_state.version}")
print("Boot Test Completed")
