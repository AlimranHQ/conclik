from pathlib import Path
import importlib

ROOT = Path("app/core")

REQUIRED = [
    "run",
    "status",
    "validate",
    "reset",
]

print("=== Conclik Kernel ABI Audit ===\n")

errors = []

for py in ROOT.rglob("*.py"):

    if py.name == "__init__.py":
        continue

    module = (
        str(py)
        .replace("/", ".")
        .replace("\\", ".")
        .replace(".py", "")
    )

    try:

        mod = importlib.import_module(module)

    except Exception:
        continue

    for name in dir(mod):

        obj = getattr(mod, name)

        if not isinstance(obj, type):
            continue

        if name.endswith("Engine") or name.endswith("Runtime"):

            print(f"{name}")

            for method in REQUIRED:

                ok = hasattr(obj(), method)

                print(f"  {method}: {ok}")

                if not ok:
                    errors.append(
                        f"{name} missing {method}"
                    )

            print()

print("=" * 40)

if errors:

    print("ABI FAILED\n")

    for e in errors:
        print(e)

else:

    print("ABI PASSED")

