---
version: "1.0"
last_updated: "2025-11-30"
status: published
tokens: ~500
---
# Project Context Navigation

> Project-specific knowledge base for SAGE Knowledge Base

---

## Table of Contents

- [1. Directory Structure](#1-directory-structure)
- [2. Content Categories](#2-content-categories)
- [3. Quick Access](#3-quick-access)
- [4. Usage Guide](#4-usage-guide)

---

## 1. Directory Structure

| Directory       | Purpose                              | Contents |
|:----------------|:-------------------------------------|:---------|
| `overview/`     | Project introduction and quick start | 1 file   |
| `policies/`     | Project-specific policies            | 6 files  |
| `conventions/`  | Project-specific coding conventions  | 3 files  |
| `decisions/`    | Architecture Decision Records (ADRs) | 8 files  |
| `intelligence/` | AI collaboration (4 subdirectories)  | 8 files  |

---

## 2. Content Categories

### 2.0 Overview

Quick introduction to the project:

| Document              | Description                                      |
|:----------------------|:-------------------------------------------------|
| `PROJECT_OVERVIEW.MD` | Project introduction, architecture, key concepts |

### 2.1 Policies

Project-specific policy documentation:

| Document                    | Description                                   |
|:----------------------------|:----------------------------------------------|
| `TIMEOUT_HIERARCHY.MD`      | T1-T5 timeout levels and fallback strategies  |
| `LOADING_CONFIGURATIONS.MD` | Knowledge loading strategies and layer config |
| `RUNTIME_SETTINGS.MD`       | Environment variables, logging, services      |
| `MEMORY_SETTINGS.MD`        | Memory persistence and caching configuration  |
| `PLUGIN_SETTINGS.MD`        | Plugin system settings and extension points   |
| `SERVICE_SETTINGS.MD`       | Service layer configuration (CLI, MCP, API)   |

### 2.2 Conventions

Project-specific rules and standards:

| Document            | Description                              |
|:--------------------|:-----------------------------------------|
| `NAMING.MD`         | Naming conventions for all code elements |
| `CODE_PATTERNS.MD`  | DI, EventBus, timeout, async patterns    |
| `FILE_STRUCTURE.MD` | Directory layout, module organization    |

### 2.3 Decisions

Architecture Decision Records (ADRs) documenting significant technical decisions.

**ADR Format**: All ADRs follow the standard ADR template structure:

- **Status** → **Context** → **Decision** → **Alternatives Considered** → **Consequences** → **Implementation** → *
  *Related**

This format is an industry-standard pattern for documenting architecture decisions, providing consistent structure for
decision rationale and traceability.

| ADR      | Title                           | Status   |
|:---------|:--------------------------------|:---------|
| ADR-0001 | Three-Layer Architecture        | Accepted |
| ADR-0002 | SAGE Protocol Design            | Accepted |
| ADR-0003 | Timeout Hierarchy Design        | Accepted |
| ADR-0004 | Dependency Injection Container  | Accepted |
| ADR-0005 | Event Bus Architecture          | Accepted |
| ADR-0006 | Protocol-First Interface Design | Accepted |
| ADR-0007 | Configuration Management        | Accepted |
| ADR-0008 | Plugin System Design            | Accepted |

### 2.4 Intelligence

AI collaboration patterns, learned behaviors, and project-specific calibration data.

**Purpose**: This directory contains knowledge that helps AI assistants collaborate effectively with the project:

- **Calibration**: Autonomy levels and decision boundaries for this project
- **Patterns**: Successful interaction templates and workflows
- **Learning**: Cases, lessons, and pitfalls from actual development
- **Optimization**: Performance tuning and efficiency improvements

#### Subdirectory Structure

| Subdirectory    | Purpose                       | Files |
|:----------------|:------------------------------|:------|
| `calibration/`  | Autonomy levels and patterns  | 2     |
| `learning/`     | Cases, lessons, pitfalls      | 3     |
| `optimization/` | Performance and optimizations | 2     |
| `automation/`   | Session automation planning   | 1     |

#### Files by Subdirectory

**calibration/** — Autonomy and patterns:

| Document         | Description                                   |
|:-----------------|:----------------------------------------------|
| `CALIBRATION.MD` | Autonomy level calibration (L1-L6)            |
| `PATTERNS.MD`    | Successful interaction patterns and templates |

**learning/** — Cases and lessons:

| Document             | Description                            |
|:---------------------|:---------------------------------------|
| `CASES.MD`           | Case studies and real-world examples   |
| `LESSONS_LEARNED.MD` | Key learnings from project development |
| `COMMON_PITFALLS.MD` | Common mistakes and how to avoid them  |

**optimization/** — Performance:

| Document                | Description                          |
|:------------------------|:-------------------------------------|
| `OPTIMIZATIONS.MD`      | Code generation preferences, testing |
| `PERFORMANCE_TUNING.MD` | Performance optimization strategies  |

**automation/** — Session management:

| Document                             | Description                                   |
|:-------------------------------------|:----------------------------------------------|
| `SESSION_AUTOMATION_REQUIREMENTS.MD` | Long-term automation plan for session history |

---

## 3. Quick Access

### 3.1 By Topic

| Topic                | Documents                                                                         |
|:---------------------|:----------------------------------------------------------------------------------|
| **Getting Started**  | `overview/PROJECT_OVERVIEW.MD`, `conventions/NAMING.MD`                           |
| **Architecture**     | `decisions/ADR-0001-ARCHITECTURE.MD`, `decisions/ADR-0002-SAGE-PROTOCOL.MD`       |
| **Configuration**    | `policies/RUNTIME_SETTINGS.MD`, `policies/LOADING_CONFIGURATIONS.MD`              |
| **Timeouts**         | `policies/TIMEOUT_HIERARCHY.MD`, `decisions/ADR-0003-TIMEOUT-HIERARCHY.MD`        |
| **DI & Events**      | `decisions/ADR-0004-DEPENDENCY-INJECTION.MD`, `decisions/ADR-0005-EVENT-BUS.MD`   |
| **AI Collaboration** | `intelligence/calibration/CALIBRATION.MD`, `intelligence/calibration/PATTERNS.MD` |

### 3.2 All Documents

#### Overview

- `overview/PROJECT_OVERVIEW.MD` — Project introduction and quick start

#### Policies

- `policies/TIMEOUT_HIERARCHY.MD` — SAGE T1-T5 timeout levels
- `policies/LOADING_CONFIGURATIONS.MD` — Loading strategies and layers
- `policies/RUNTIME_SETTINGS.MD` — Environment and runtime config
- `policies/MEMORY_SETTINGS.MD` — Memory persistence and caching
- `policies/PLUGIN_SETTINGS.MD` — Plugin system settings
- `policies/SERVICE_SETTINGS.MD` — Service layer configuration

#### Conventions

- `conventions/NAMING.MD` — Naming conventions
- `conventions/CODE_PATTERNS.MD` — Code patterns (DI, EventBus, etc.)
- `conventions/FILE_STRUCTURE.MD` — File and directory organization

#### Decisions (ADRs)

- `decisions/ADR-0001-ARCHITECTURE.MD` — Three-layer architecture
- `decisions/ADR-0002-SAGE-PROTOCOL.MD` — SAGE protocol design
- `decisions/ADR-0003-TIMEOUT-HIERARCHY.MD` — Timeout hierarchy
- `decisions/ADR-0004-DEPENDENCY-INJECTION.MD` — DI container
- `decisions/ADR-0005-EVENT-BUS.MD` — Event bus
- `decisions/ADR-0006-PROTOCOL-FIRST.MD` — Protocol-first design
- `decisions/ADR-0007-CONFIGURATION.MD` — Configuration management
- `decisions/ADR-0008-PLUGIN-SYSTEM.MD` — Plugin system

#### Intelligence

**calibration/**

- `intelligence/calibration/CALIBRATION.MD` — Autonomy calibration (L1-L6)
- `intelligence/calibration/PATTERNS.MD` — AI interaction patterns

**learning/**

- `intelligence/learning/CASES.MD` — Case studies and examples
- `intelligence/learning/LESSONS_LEARNED.MD` — Key project learnings
- `intelligence/learning/COMMON_PITFALLS.MD` — Common mistakes to avoid

**optimization/**

- `intelligence/optimization/OPTIMIZATIONS.MD` — Project optimizations
- `intelligence/optimization/PERFORMANCE_TUNING.MD` — Performance optimization

**automation/**

- `intelligence/automation/SESSION_AUTOMATION_REQUIREMENTS.MD` — Session history automation

---

## 4. Usage Guide

### 4.1 For New Contributors

1. Start with `overview/PROJECT_OVERVIEW.MD` for quick introduction
2. Read `conventions/NAMING.MD` and `conventions/FILE_STRUCTURE.MD`
3. Review key ADRs: ADR-0001 (architecture), ADR-0002 (SAGE protocol)

### 4.2 For AI Assistants

1. Check `intelligence/calibration/CALIBRATION.MD` for autonomy levels
2. Follow patterns in `intelligence/calibration/PATTERNS.MD`
3. Use optimizations from `intelligence/optimization/OPTIMIZATIONS.MD`
4. Learn from `intelligence/learning/` (cases, lessons, pitfalls)

### 4.3 For Policies

1. Timeout settings: `policies/TIMEOUT_HIERARCHY.MD`
2. Loading behavior: `policies/LOADING_CONFIGURATIONS.MD`
3. Runtime/environment: `policies/RUNTIME_SETTINGS.MD`

---

## Related

- `.knowledge/` — Generic, reusable knowledge
- `.junie/GUIDELINES.MD` — AI collaboration guidelines
- `docs/design/` — Design documents
- `README.md` — Project overview

---

*Part of SAGE Knowledge Base - Project Context*
