# Conclik Layer Rules

Version: 1.0
Status: Official

---

## Architecture Layers

Foundation

↓

Core

↓

Intelligence

↓

Providers

↓

Agents

↓

Services

↓

Routers

---

## Rules

Layers communicate downward.

Never upward.

Routers never call Providers directly.

Services never bypass Intelligence.

Agents never bypass Provider Manager.

Providers never contain business logic.

Every layer has one responsibility.

