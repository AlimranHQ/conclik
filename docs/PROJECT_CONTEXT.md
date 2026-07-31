# Conclik Project Context

## Project
Conclik is an AI Operating System.

## Current Version
Conclik Core v1.0 Stable

## Architecture

Conclik Runtime
↓
Runtime Orchestrator
↓
Brain Runtime
↓
Goal Engine
Planner Engine
Task Planner
Decision Engine
Assignment Runtime
↓
Agent Runtime
↓
Tool Router
├── Terminal Runtime
├── Python Runtime
├── File Runtime

Reflection Runtime
Learning Runtime
Adaptive Runtime
Memory Runtime
Conversation Runtime

## Kernel ABI

Every Runtime / Engine must implement:

- run()
- status()
- validate()
- reset()

BrainRuntime ONLY calls run().

## Stable Modules

- Kernel
- Brain Runtime
- Runtime Orchestrator
- Tool Router
- Agent Runtime
- Reflection
- Learning
- Adaptive
- Memory
- Conversation

## Git

Branch:
integration/runtime-v1

Stable Tag:
conclik-core-v1.0

## Current Phase

Phase 5

Current Goal:
Build Multi-Agent Kernel.

## Next Roadmap

1. Multi-Agent Runtime
2. Workflow Engine
3. Parallel Agent Execution
4. Autonomous AI
5. Cloud Runtime
6. Production Release

## Rules

Never break Kernel ABI.

Always run:

python tools/kernel_audit/kernel_abi_audit.py

before commit.

If ABI fails,
fix ABI first.

Never modify stable Kernel without reason.

