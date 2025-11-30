---
version: "1.0"
last_updated: "2025-11-30"
status: published
tokens: ~500
---

# .junie Configuration

> JetBrains Junie AI collaboration configuration directory

---

## Table of Contents

- [1. Directory Structure](#1-directory-structure)
- [2. Usage](#2-usage)
- [3. Customization Guidelines](#3-customization-guidelines)
- [4. Version Information](#4-version-information)

---

## 1. Directory Structure

```
.junie/
├── GUIDELINES.MD           # 🔄 Main entry point (generic AI rules)
├── README.md               # 🔄 This file - directory documentation
│
├── generic/                # 🔄 Generic settings (reusable)
│   ├── config.yaml         # Junie settings
│   └── QUICKREF.MD         # Quick reference card
│
├── mcp/                    # 🔄 MCP server configuration
│   └── mcp.json            # MCP servers definition
│
├── schema/                 # 🔄 JSON Schema validation
│   ├── config.schema.json  # Config file schema
│   └── mcp.schema.json     # MCP config schema
│
├── docs/                   # 🔄 Junie documentation
│   ├── README.md           # Documentation index
│   ├── guides/             # User guides
│   │   ├── QUICK-START.MD
│   │   └── ACTION-ALLOWLIST.MD
│   ├── mcp/                # MCP integration
│   │   ├── OVERVIEW.MD
│   │   ├── CONFIGURATION.MD
│   │   ├── SERVERS.MD
│   │   ├── MEMORY.MD
│   │   └── TROUBLESHOOTING.MD
│   ├── operations/         # Operations guides
│   │   ├── MAINTENANCE.MD
│   │   ├── MIGRATION.MD
│   │   ├── METRICS.MD
│   │   └── RECOVERY.MD
│   ├── reference/          # Reference materials
│   │   ├── GLOSSARY.MD
│   │   ├── REGEX.MD
│   │   ├── RULES-WINDOWS.MD
│   │   └── RULES-UNIX.MD
│   └── vision/             # Future vision
│       └── FUTURE-PROTOCOLS.MD
│
└── project/                # 📌 Project-specific files (must customize)
    ├── config.yaml         # Project variables definition
    └── QUICKREF.MD         # Project-specific quick reference
```

### Legend

- 🔄 **Generic**: Reusable across projects with minimal or no changes
- 📌 **Project**: Must be customized for each project

---

## 2. Usage

### New Project Setup

1. **Copy the entire `.junie/` directory** to your project

2. **Keep generic files unchanged**:
    - `GUIDELINES.MD` (root)
    - `generic/` directory
    - `mcp/` directory
    - `docs/` directory

3. **Customize project-specific files**:
    - `project/config.yaml` — Define your project variables
    - `project/QUICKREF.MD` — Add project-specific quick reference

### File Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                     .junie/ Directory                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐                                       │
│  │  GUIDELINES.MD   │  ◄── Main entry point                 │
│  │  (Generic Rules) │                                       │
│  └────────┬─────────┘                                       │
│           │                                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Generic Directories (Reusable)              │    │
│  │  ┌────────────┐  ┌────────────┐  ┌──────────────┐   │    │
│  │  │ generic/   │  │ mcp/       │  │ docs/        │   │    │
│  │  │ (Settings) │  │ (MCP)      │  │ (Docs)       │   │    │
│  │  └────────────┘  └────────────┘  └──────────────┘   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              project/ (Customize)                   │    │
│  │  ┌────────────────┐  ┌────────────────┐             │    │
│  │  │ config.yaml    │  │ QUICKREF.MD    │             │    │
│  │  │ (Variables)    │  │ (Project Ref)  │             │    │
│  │  └────────────────┘  └────────────────┘             │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Customization Guidelines

| Directory/File         | When to Modify                                       |
|------------------------|------------------------------------------------------|
| `GUIDELINES.MD` (root) | Only when changing generic AI collaboration patterns |
| `generic/*`            | Only when adding new generic features                |
| `mcp/*`                | Only when changing MCP server configuration          |
| `docs/*`               | Only when updating documentation                     |
| `project/*`            | Freely customize for your specific project           |

---

## 4. Version Information

- **Schema Version**: 1.0
- **Compatibility**: JetBrains Junie v2024.3+, MCP v1.0+

---

*Part of the Junie Configuration Template System*
