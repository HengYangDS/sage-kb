# Development Tools

> Utility tools for SAGE Knowledge Base development and operations

---

## Table of Contents

[1. Overview](#1-overview) · [2. Tool Reference](#2-tool-reference) · [3. Usage Examples](#3-usage-examples) · [4. Development](#4-development)

---

## 1. Overview

This directory contains development and operational tools for the SAGE Knowledge Base project.

### 1.1 Tool Categories

| Category | Directory | Purpose |
|----------|-----------|---------|
| **Core Tools** | `tools/` | Main utility scripts |
| **Dev Scripts** | `tools/dev_scripts/` | Development environment setup |
| **Knowledge Graph** | `tools/knowledge_graph/` | Knowledge structure analysis |
| **Monitors** | `tools/monitors/` | Runtime monitoring |

### 1.2 Quick Reference

| Tool | Command | Purpose |
|------|---------|---------|
| Timeout Manager | `python -m tools.timeout_manager` | Manage timeout configurations |
| Migration Toolkit | `python -m tools.migration_toolkit` | Migrate content and configs |
| Knowledge Graph | `python -m tools.knowledge_graph` | Build knowledge graphs |
| Timeout Monitor | `python -m tools.monitors.timeout_monitor` | Monitor timeout events |
| Dev Setup | `python -m tools.dev_scripts.setup_dev` | Set up development environment |

---

## 2. Tool Reference

### 2.1 timeout_manager.py

**Purpose**: Manage and configure timeout settings across the application.

**Features**:
- Configure timeout levels (T1-T5)
- Test timeout behavior
- Generate timeout reports

**Usage**:

```python
from tools.timeout_manager import TimeoutManager

manager = TimeoutManager()
manager.configure(level="T3", timeout_ms=2000)
manager.test_timeout("loader")
```

**CLI**:

```bash
# Configure timeout
python -m tools.timeout_manager configure --level T3 --timeout 2000

# Test timeout
python -m tools.timeout_manager test --component loader

# Generate report
python -m tools.timeout_manager report
```

---

### 2.2 migration_toolkit.py

**Purpose**: Migrate content, configurations, and data between versions.

**Features**:
- Content migration between directory structures
- Configuration format upgrades
- Backup and restore functionality

**Usage**:

```python
from tools.migration_toolkit import MigrationToolkit

toolkit = MigrationToolkit()
toolkit.migrate_content(source="old/content", target="new/content")
toolkit.upgrade_config(config_path="config/sage.yaml")
```

**CLI**:

```bash
# Migrate content
python -m tools.migration_toolkit migrate --source old/ --target new/

# Upgrade configuration
python -m tools.migration_toolkit upgrade --config config/sage.yaml

# Create backup
python -m tools.migration_toolkit backup --output .backups/
```

---

### 2.3 knowledge_graph/knowledge_graph_builder.py

**Purpose**: Build and analyze knowledge graph structures from content.

**Features**:
- Parse markdown files for relationships
- Generate graph visualization data
- Identify orphan nodes and missing links

**Usage**:

```python
from tools.knowledge_graph import KnowledgeGraphBuilder

builder = KnowledgeGraphBuilder(content_dir="content/")
graph = builder.build()
builder.export_json("knowledge_graph.json")
builder.find_orphans()
```

**CLI**:

```bash
# Build graph
python -m tools.knowledge_graph build --content content/

# Export to JSON
python -m tools.knowledge_graph export --format json --output graph.json

# Find orphan nodes
python -m tools.knowledge_graph analyze --check orphans
```

---

### 2.4 monitors/timeout_monitor.py

**Purpose**: Monitor timeout events and performance in real-time.

**Features**:
- Real-time timeout event tracking
- Performance metrics collection
- Alert on threshold breaches

**Usage**:

```python
from tools.monitors import TimeoutMonitor

monitor = TimeoutMonitor()
monitor.start()
monitor.on_timeout(callback=handle_timeout)
monitor.get_metrics()
```

**CLI**:

```bash
# Start monitoring
python -m tools.monitors.timeout_monitor start

# Get metrics
python -m tools.monitors.timeout_monitor metrics

# Set alert threshold
python -m tools.monitors.timeout_monitor alert --threshold 100
```

---

### 2.5 dev_scripts/setup_dev.py

**Purpose**: Set up development environment with all required dependencies and configurations.

**Features**:
- Install development dependencies
- Configure pre-commit hooks
- Set up local configuration files
- Verify environment setup

**Usage**:

```bash
# Full setup
python -m tools.dev_scripts.setup_dev

# Install dependencies only
python -m tools.dev_scripts.setup_dev --deps-only

# Configure hooks only
python -m tools.dev_scripts.setup_dev --hooks-only

# Verify setup
python -m tools.dev_scripts.setup_dev --verify
```

---

## 3. Usage Examples

### 3.1 Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/HengYangDS/sage-kb.git
cd sage-kb

# Run setup script
python -m tools.dev_scripts.setup_dev

# Verify installation
python -m tools.dev_scripts.setup_dev --verify
```

### 3.2 Migrating Content

```bash
# Create backup first
python -m tools.migration_toolkit backup --output .backups/pre-migration/

# Run migration
python -m tools.migration_toolkit migrate --source old/ --target content/

# Verify migration
python -m tools.knowledge_graph analyze --check orphans
```

### 3.3 Monitoring Performance

```bash
# Start timeout monitor in background
python -m tools.monitors.timeout_monitor start --daemon

# Run your application
sage serve

# Check metrics
python -m tools.monitors.timeout_monitor metrics
```

---

## 4. Development

### 4.1 Adding New Tools

1. Create tool module in appropriate directory
2. Add `__init__.py` exports
3. Update this README
4. Add tests in `tests/tools/`

### 4.2 Tool Structure

```python
"""
Tool Name

Purpose: Brief description
Author: Your Name
"""

from typing import Optional

class ToolName:
    """Main tool class."""
    
    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
    
    def run(self) -> None:
        """Execute main functionality."""
        pass

def main() -> None:
    """CLI entry point."""
    tool = ToolName()
    tool.run()

if __name__ == "__main__":
    main()
```

### 4.3 Testing Tools

```bash
# Run tool tests
pytest tests/tools/ -v

# Test specific tool
pytest tests/tools/test_timeout_manager.py -v
```

---

## Related

- `docs/guides/quickstart.md` — Getting started guide
- `docs/design/00-overview.md` — Architecture overview
- `.context/configurations/` — Configuration documentation

---

*Part of SAGE Knowledge Base*
