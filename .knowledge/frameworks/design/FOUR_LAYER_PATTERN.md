# Four-Layer Architecture Pattern

> Universal pattern for organizing code into hierarchical layers with clear dependencies

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Layer Definitions](#2-layer-definitions)
- [3. Stability Levels](#3-stability-levels)
- [4. Dependency Rules](#4-dependency-rules)
- [5. Layer Characteristics](#5-layer-characteristics)
- [6. Implementation Guidelines](#6-implementation-guidelines)
- [7. Validation Checklist](#7-validation-checklist)

---

## 1. Overview

The Four-Layer Pattern organizes code into hierarchical layers from abstract to concrete:

```
Abstract ▲
         │  ┌─────────────────────────────────────────┐
         │  │ Extension Layer (plugins)               │
         │  │ · Extension mechanisms, lifecycle       │
         │  │ · Framework-level abstractions          │
         │  └─────────────────────────────────────────┘
         │                    │
         │                    ▼
         │  ┌─────────────────────────────────────────┐
         │  │ Interface Layer (capabilities)          │
         │  │ · Capability contracts and interfaces   │
         │  │ · Family-based organization             │
         │  └─────────────────────────────────────────┘
         │                    │
         │                    ▼
         │  ┌─────────────────────────────────────────┐
         │  │ Implementation Layer (tools)            │
         │  │ · Concrete implementations              │
         │  │ · User-facing functionality             │
         │  └─────────────────────────────────────────┘
         │                    │
         ▼                    ▼
Concrete   ┌─────────────────────────────────────────┐
           │ Auxiliary Layer (scripts)               │
           │ · Development utilities                 │
           │ · CI/CD, automation                     │
           └─────────────────────────────────────────┘
```

---

## 2. Layer Definitions

| Layer | Name | Definition | Key Question | Target User |
|-------|------|------------|--------------|-------------|
| **L1** | Extension | Extension mechanisms and lifecycle | How to extend? | Framework developers |
| **L2** | Interface | Capability contracts and interfaces | What can it do? | Capability developers |
| **L3** | Implementation | Concrete implementations | How to use? | End users |
| **L4** | Auxiliary | Development utilities | How to develop? | Project developers |

### 2.1 Extension Layer (L1)

- Defines how the system can be extended
- Provides plugin lifecycle management
- Contains framework-level abstractions
- Most stable, rarely changes

### 2.2 Interface Layer (L2)

- Defines capability contracts (protocols/interfaces)
- Organizes capabilities by family (analyzers, checkers, etc.)
- Decouples implementation from contract
- Changes infrequently

### 2.3 Implementation Layer (L3)

- Contains concrete tool implementations
- User-facing functionality
- May have multiple implementations per interface
- Changes regularly

### 2.4 Auxiliary Layer (L4)

- Development scripts and utilities
- CI/CD pipelines
- Git hooks and automation
- Changes frequently

---

## 3. Stability Levels

| Layer | Stability | Change Frequency | Impact of Change |
|-------|-----------|------------------|------------------|
| Extension (L1) | ★★★★★ | Rarely | High - affects all plugins |
| Interface (L2) | ★★★★☆ | Infrequent | Medium - affects implementations |
| Implementation (L3) | ★★★☆☆ | Regular | Low - isolated changes |
| Auxiliary (L4) | ★★☆☆☆ | Frequent | Minimal - development only |

**Principle**: Higher layers are more stable because changes cascade downward.

---

## 4. Dependency Rules

### 4.1 Allowed Dependencies

```
L4 (scripts) → L3 (tools) → L2 (capabilities) → L1 (plugins)
```

- Auxiliary may depend on Implementation
- Implementation may depend on Interface
- Interface may depend on Extension
- **Each layer may only depend on layers above it**

### 4.2 Forbidden Dependencies

```
L1 (plugins) ✗→ L2 (capabilities) ✗→ L3 (tools) ✗→ L4 (scripts)
```

- Extension must NOT depend on Interface
- Interface must NOT depend on Implementation
- Implementation must NOT depend on Auxiliary
- **No downward dependencies allowed**

### 4.3 Dependency Matrix

| From ↓ / To → | L1 Extension | L2 Interface | L3 Implementation | L4 Auxiliary |
|---------------|--------------|--------------|-------------------|--------------|
| L1 Extension | ✅ | ❌ | ❌ | ❌ |
| L2 Interface | ✅ | ✅ | ❌ | ❌ |
| L3 Implementation | ✅ | ✅ | ✅ | ❌ |
| L4 Auxiliary | ✅ | ✅ | ✅ | ✅ |

---

## 5. Layer Characteristics

### 5.1 Abstraction Level

| Layer | Abstraction | Example Content |
|-------|-------------|-----------------|
| Extension | Pure abstractions | Plugin protocols, lifecycle hooks |
| Interface | Contracts | Capability interfaces, type definitions |
| Implementation | Concrete | Actual tool implementations |
| Auxiliary | Utilities | Scripts, CI configs |

### 5.2 Testing Strategy

| Layer | Test Focus | Coverage Target |
|-------|------------|-----------------|
| Extension | Contract compliance | 90%+ |
| Interface | Interface validation | 85%+ |
| Implementation | Behavior verification | 80%+ |
| Auxiliary | Smoke tests | 60%+ |

---

## 6. Implementation Guidelines

### 6.1 When to Use This Pattern

- Projects with plugin/extension systems
- Systems requiring clear separation of concerns
- Codebases needing explicit dependency control
- Teams working on different abstraction levels

### 6.2 Naming Conventions

| Layer | Typical Directory Names |
|-------|------------------------|
| Extension | `plugins/`, `extensions/`, `core/plugins/` |
| Interface | `capabilities/`, `interfaces/`, `contracts/` |
| Implementation | `tools/`, `impl/`, `implementations/` |
| Auxiliary | `scripts/`, `dev/`, `ci/` |

### 6.3 Documentation Structure

Each layer should have:
- `INDEX.md` - Layer overview and navigation
- Per-component documentation
- Clear cross-references to related layers

---

## 7. Validation Checklist

- [ ] Each component belongs to exactly one layer
- [ ] No downward dependencies exist
- [ ] Layer boundaries are clearly documented
- [ ] Implementations are organized by capability family
- [ ] Auxiliary scripts are organized by category
- [ ] Documentation follows layer structure
- [ ] Tests exist for each layer with appropriate coverage

---

## Related

- `.knowledge/frameworks/design/INDEX.md` — Design framework index
- `.knowledge/frameworks/design/AXIOMS.md` — Design axioms
- `.knowledge/frameworks/design/LAYER_HIERARCHY.md` — Knowledge layer hierarchy (different concept)
- `.knowledge/practices/engineering/MECE.md` — MECE categorization principle

---

*AI Collaboration Knowledge Base*
