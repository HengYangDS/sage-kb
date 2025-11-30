---
version: "1.0"
last_updated: "2025-11-30"
status: published
tokens: ~500
---

# Documentation Navigation

> User-facing documentation for SAGE Knowledge Base

---

## Table of Contents

- [1. Directory Structure](#1-directory-structure)
- [2. Design Documents](#2-design-documents)
- [3. API Reference](#3-api-reference)
- [4. User Guides](#4-user-guides)
- [5. Quick Access](#5-quick-access)

---

## 1. Directory Structure

| Directory | Purpose                               | Files |
|-----------|---------------------------------------|-------|
| `design/` | Architecture and design documentation | 10    |
| `api/`    | API reference documentation           | 6     |
| `guides/` | User guides and tutorials             | 9     |

---

## 2. Design Documents

Comprehensive design documentation for SAGE architecture and implementation:

| Document                         | Description                           |
|----------------------------------|---------------------------------------|
| `design/00-OVERVIEW.MD`          | Project overview and introduction     |
| `design/01-ARCHITECTURE.MD`      | Three-layer architecture design       |
| `design/02-SAGE-PROTOCOL.MD`     | SAGE protocol specification           |
| `design/03-SERVICES.MD`          | Service layer design (CLI, MCP, API)  |
| `design/04-TIMEOUT-LOADING.MD`   | Timeout hierarchy and smart loading   |
| `design/05-PLUGIN-MEMORY.MD`     | Plugin system and memory persistence  |
| `design/06-CONTENT-STRUCTURE.MD` | Knowledge content organization        |
| `design/07-ROADMAP.MD`           | Implementation roadmap and milestones |
| `design/08-EVALUATION.MD`        | Evaluation criteria and metrics       |
| `design/09-CONFIGURATION.MD`     | Configuration management design       |

---

## 3. API Reference

API documentation for different interfaces:

| Document                  | Description                      |
|---------------------------|----------------------------------|
| `api/INDEX.MD`            | API overview and quick reference |
| `api/CLI.MD`              | Command-line interface reference |
| `api/MCP.MD`              | MCP (Model Context Protocol) API |
| `api/MCP_QUICK_REF.MD`    | MCP quick reference guide        |
| `api/PLUGIN_QUICK_REF.MD` | Plugin API quick reference       |
| `api/PYTHON.MD`           | Python SDK reference             |

---

## 4. User Guides

Tutorials and guides for users and developers:

| Document                       | Description                        |
|--------------------------------|------------------------------------|
| `guides/INDEX.MD`              | Guides overview and navigation     |
| `guides/QUICKSTART.MD`         | Quick start guide (5 minutes)      |
| `guides/CONFIGURATION.MD`      | Configuration guide                |
| `guides/MCP_TOOLS.MD`          | MCP tools usage guide              |
| `guides/PLUGIN_DEVELOPMENT.MD` | Plugin development guide           |
| `guides/ADVANCED.MD`           | Advanced usage and customization   |
| `guides/MIGRATION.MD`          | Migration guide from other systems |
| `guides/TROUBLESHOOTING.MD`    | Troubleshooting common issues      |
| `guides/FAQ.MD`                | Frequently asked questions         |

---

## 5. Quick Access

### 5.1 Getting Started

1. Start with `guides/QUICKSTART.MD` for a 5-minute introduction
2. Read `design/00-OVERVIEW.MD` for project overview
3. Check `api/CLI.MD` for command-line usage

### 5.2 For Developers

1. Review `design/01-ARCHITECTURE.MD` for system design
2. See `guides/PLUGIN_DEVELOPMENT.MD` for extending SAGE
3. Reference `api/PYTHON.MD` for programmatic access

### 5.3 For Configuration

1. Check `guides/CONFIGURATION.MD` for setup options
2. See `design/09-CONFIGURATION.MD` for design details

---

## Related

- `.knowledge/` — Knowledge base content
- `.context/` — Project-specific context
- `config/` — Runtime configuration files
- `README.md` — Project overview

---

*Part of SAGE Knowledge Base*
