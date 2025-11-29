# Troubleshooting Guide

> Common issues, debugging techniques, and solutions for SAGE Knowledge Base

---

## Table of Contents

[1. Quick Diagnostics](#1-quick-diagnostics) · [2. Common Issues](#2-common-issues) · [3. Debugging Techniques](#3-debugging-techniques) · [4. Log Analysis](#4-log-analysis) · [5. Performance Issues](#5-performance-issues) · [6. Configuration Problems](#6-configuration-problems) · [7. MCP Issues](#7-mcp-issues) · [8. Recovery Procedures](#8-recovery-procedures)

---

## 1. Quick Diagnostics

### 1.1 Health Check Commands

```bash
# Check system health
sage info

# Verify configuration
sage config --validate

# Test MCP connection
sage serve --dry-run

# Check knowledge base integrity
sage check --all
```

### 1.2 Diagnostic Checklist

| Check | Command | Expected |
|-------|---------|----------|
| Python version | `python --version` | 3.12+ |
| Dependencies | `pip list \| grep sage` | sage-kb installed |
| Config exists | `ls config/sage.yaml` | File exists |
| Content accessible | `ls content/` | Directories present |

---

## 2. Common Issues

### 2.1 Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'sage'`

**Solutions**:
```bash
# Ensure package is installed
pip install -e .

# Or install with all dependencies
pip install -e ".[all]"

# Verify installation
python -c "import sage; print(sage.__version__)"
```

### 2.2 Configuration Not Found

**Symptom**: `FileNotFoundError: config/sage.yaml`

**Solutions**:
```bash
# Check current directory
pwd

# Run from project root
cd /path/to/sage-kb

# Or specify config path
sage --config /path/to/config/sage.yaml info
```

### 2.3 MCP Server Won't Start

**Symptom**: `ImportError: mcp package not available`

**Solutions**:
```bash
# Install MCP dependencies
pip install -e ".[mcp]"

# Verify MCP installation
python -c "from mcp.server.fastmcp import FastMCP; print('OK')"
```

### 2.4 Timeout Errors

**Symptom**: `TimeoutError: Operation exceeded T3 limit`

**Solutions**:
1. Check timeout configuration in `config/core/timeout.yaml`
2. Reduce content size or use lazy loading
3. Increase timeout for specific operations:
   ```yaml
   # config/core/timeout.yaml
   timeouts:
     T3_layer_load: 3000  # Increase from 2000ms
   ```

### 2.5 Permission Denied

**Symptom**: `PermissionError: [Errno 13]`

**Solutions**:
```bash
# Check file permissions
ls -la config/

# Fix permissions
chmod 644 config/*.yaml
chmod 755 content/
```

---

## 3. Debugging Techniques

### 3.1 Enable Debug Logging

```python
# In code
import logging
logging.getLogger("sage").setLevel(logging.DEBUG)

# Or via environment
export SAGE_LOG_LEVEL=DEBUG
```

### 3.2 Verbose Mode

```bash
# CLI verbose output
sage --verbose info

# MCP server debug mode
sage serve --debug
```

### 3.3 Interactive Debugging

```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# Or use IPython
from IPython import embed; embed()
```

### 3.4 Trace Loading

```python
from sage.core.loader import KnowledgeLoader

loader = KnowledgeLoader()
loader.enable_tracing()  # Log all loading operations
result = loader.load(layer=0)
print(loader.get_trace_log())
```

---

## 4. Log Analysis

### 4.1 Log Locations

| Log Type | Location | Purpose |
|----------|----------|---------|
| Application | `.logs/sage.log` | General operations |
| Error | `.logs/error.log` | Errors only |
| Performance | `.logs/perf.log` | Timing data |
| Debug | `.logs/debug.log` | Detailed trace |

### 4.2 Log Format

```
2024-01-15T10:30:45.123Z | INFO | sage.core.loader | Loading layer 0 | duration_ms=45
```

### 4.3 Common Log Patterns

| Pattern | Meaning | Action |
|---------|---------|--------|
| `TIMEOUT` | Operation timed out | Check timeout config |
| `FALLBACK` | Using fallback content | Check primary source |
| `CACHE_HIT` | Content from cache | Normal operation |
| `CACHE_MISS` | Fresh load required | May be slow |

### 4.4 Log Analysis Commands

```bash
# Find errors
grep "ERROR" .logs/sage.log

# Find timeouts
grep "TIMEOUT" .logs/sage.log | tail -20

# Performance analysis
grep "duration_ms" .logs/perf.log | awk -F'=' '{sum+=$2; count++} END {print sum/count}'
```

---

## 5. Performance Issues

### 5.1 Slow Loading

**Diagnosis**:
```bash
# Check loading time
time sage get --layer 0

# Profile loading
sage profile --operation load
```

**Solutions**:
1. Enable caching in `config/core/memory.yaml`
2. Use lazy loading for large content
3. Reduce content size per layer
4. Increase timeout limits if needed

### 5.2 High Memory Usage

**Diagnosis**:
```python
import tracemalloc
tracemalloc.start()

# Run operations
from sage.core.loader import KnowledgeLoader
loader = KnowledgeLoader()
loader.load(layer=2)

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.1f}MB, Peak: {peak / 1024 / 1024:.1f}MB")
```

**Solutions**:
1. Enable content streaming
2. Use smaller token budgets
3. Clear cache periodically

### 5.3 Token Budget Exceeded

**Symptom**: Content truncated or incomplete

**Solutions**:
```yaml
# config/knowledge/token_budget.yaml
budgets:
  layer_0: 2000   # Increase budget
  layer_1: 5000
  total: 20000
```

---

## 6. Configuration Problems

### 6.1 Config Validation

```bash
# Validate all configs
sage config --validate

# Check specific config
python -c "
import yaml
with open('config/sage.yaml') as f:
    config = yaml.safe_load(f)
    print('Valid YAML')
"
```

### 6.2 Common Config Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid YAML` | Syntax error | Check indentation |
| `Unknown key` | Typo in config | Check spelling |
| `Type error` | Wrong value type | Check expected type |
| `Missing required` | Required field absent | Add required field |

### 6.3 Config Override

```bash
# Override via environment
export SAGE_TIMEOUT_T1=200

# Override via CLI
sage --config-override "timeout.T1=200" info
```

---

## 7. MCP Issues

### 7.1 Connection Problems

**Symptom**: Client cannot connect to MCP server

**Diagnosis**:
```bash
# Check if server is running
ps aux | grep "sage serve"

# Test port
curl http://localhost:8000/health
```

**Solutions**:
1. Ensure server is started: `sage serve`
2. Check port availability
3. Verify firewall settings

### 7.2 Tool Execution Failures

**Symptom**: MCP tool returns error

**Diagnosis**:
```python
# Test tool directly
from sage.services.mcp_server import get_knowledge
import asyncio
result = asyncio.run(get_knowledge(layer=0))
print(result)
```

### 7.3 Timeout in MCP Calls

**Solutions**:
1. Increase client timeout
2. Use smaller requests
3. Enable streaming responses

---

## 8. Recovery Procedures

### 8.1 Reset Cache

```bash
# Clear all caches
rm -rf .cache/

# Or programmatically
from sage.core.memory import MemoryManager
MemoryManager().clear_all()
```

### 8.2 Restore from Backup

```bash
# List available backups
sage backup --list

# Restore specific backup
sage backup --restore backup-2024-01-15
```

### 8.3 Rebuild Index

```bash
# Rebuild search index
sage index --rebuild

# Rebuild knowledge graph
sage graph --rebuild
```

### 8.4 Factory Reset

```bash
# Reset all configuration to defaults
sage config --reset

# Full reset (careful!)
rm -rf .cache/ .logs/ .outputs/
sage init
```

---

## Quick Reference

### Error Code Reference

| Code | Category | Description |
|------|----------|-------------|
| E001 | Config | Configuration error |
| E002 | Load | Loading failure |
| E003 | Timeout | Operation timeout |
| E004 | Memory | Memory limit exceeded |
| E005 | MCP | MCP communication error |

### Support Resources

- **Documentation**: `docs/guides/`
- **Design Docs**: `docs/design/`
- **Issues**: GitHub Issues
- **Logs**: `.logs/` directory

---

## Related

- `practices/engineering/logging.md` — Logging practices
- `practices/engineering/error_handling.md` — Error handling
- `frameworks/resilience/timeout_patterns.md` — Timeout patterns
- `.context/configurations/timeout_hierarchy.md` — Timeout configuration

---

*Part of SAGE Knowledge Base — Engineering Practices*
