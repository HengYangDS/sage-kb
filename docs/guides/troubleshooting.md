# Troubleshooting Guide

> Solutions for common issues with SAGE Knowledge Base

---

## Table of Contents

[1. Quick Diagnostics](#1-quick-diagnostics) · [2. Installation Issues](#2-installation-issues) · [3. CLI Issues](#3-cli-issues) · [4. MCP Server Issues](#4-mcp-server-issues) · [5. Loading Issues](#5-loading-issues) · [6. Performance Issues](#6-performance-issues) · [7. Configuration Issues](#7-configuration-issues) · [8. Log Analysis](#8-log-analysis) · [9. Getting Help](#9-getting-help)

---

## 1. Quick Diagnostics

### 1.1 Health Check Command

```bash
# Run comprehensive health check
sage info --verbose

# Check specific components
sage info --component loader
sage info --component mcp
sage info --component config
```

### 1.2 Common Error Categories

| Error Type | Symptoms | First Check |
|------------|----------|-------------|
| **Installation** | Import errors, missing commands | Python version, dependencies |
| **Configuration** | Invalid config, missing files | Config file syntax |
| **Loading** | Timeout, empty results | Content paths, permissions |
| **Performance** | Slow responses | Token budgets, cache |
| **MCP** | Connection refused | Server status, ports |

### 1.3 Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Command not found | `pip install -e .` |
| Config error | `sage info --validate-config` |
| Timeout | Increase timeout in `config/core/timeout.yaml` |
| Empty results | Check content path in `config/sage.yaml` |

---

## 2. Installation Issues

### 2.1 Python Version Errors

**Symptom**: `Python version X.X is not supported`

**Solution**:
```bash
# Check Python version
python --version

# SAGE requires Python 3.12+
# Install correct version
pyenv install 3.12.0
pyenv local 3.12.0
```

### 2.2 Dependency Conflicts

**Symptom**: `pip` reports conflicting dependencies

**Solution**:
```bash
# Create fresh virtual environment
python -m venv .venv --clear
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows

# Install with fresh dependencies
pip install -e ".[dev]"
```

### 2.3 Missing Optional Dependencies

**Symptom**: `ModuleNotFoundError: No module named 'mcp'`

**Solution**:
```bash
# Install with MCP support
pip install -e ".[mcp]"

# Or install all optional dependencies
pip install -e ".[all]"
```

### 2.4 Permission Errors

**Symptom**: `PermissionError` during installation

**Solution**:
```bash
# Don't use sudo with pip in venv
# Instead, ensure venv is activated
which python  # Should show .venv path

# If global install needed (not recommended)
pip install --user sage-kb
```

---

## 3. CLI Issues

### 3.1 Command Not Found

**Symptom**: `sage: command not found`

**Solution**:
```bash
# Verify installation
pip show sage-kb

# Check if scripts directory is in PATH
python -c "import sage; print(sage.__file__)"

# Run as module if command not found
python -m sage.services.cli --help
```

### 3.2 No Output from Commands

**Symptom**: Commands complete but show nothing

**Diagnosis**:
```bash
# Enable verbose output
sage get --layer core --verbose

# Check if content exists
ls -la content/core/

# Validate configuration
sage info --validate-config
```

### 3.3 Search Returns No Results

**Symptom**: `sage search "term"` returns empty

**Possible Causes**:

| Cause | Check | Fix |
|-------|-------|-----|
| Wrong path | `config/sage.yaml` content_root | Update path |
| No matching content | Manual search | Verify search term exists |
| Index not built | N/A | Rebuild index (if applicable) |

**Solution**:
```bash
# Check content root
cat config/sage.yaml | grep content_root

# Manual verification
grep -r "search_term" content/

# Try broader search
sage search "*" --layer core
```

---

## 4. MCP Server Issues

### 4.1 Server Won't Start

**Symptom**: `sage serve` fails immediately

**Diagnosis**:
```bash
# Check for port conflicts
netstat -an | grep 8080  # Unix
netstat -an | findstr 8080  # Windows

# Check MCP dependencies
python -c "import mcp; print(mcp.__version__)"
```

**Solutions**:
```bash
# Use different port
sage serve --port 8081

# Check for existing processes
ps aux | grep sage  # Unix
tasklist | findstr sage  # Windows

# Kill existing process
kill <PID>  # Unix
taskkill /PID <PID>  # Windows
```

### 4.2 Connection Refused

**Symptom**: Client can't connect to MCP server

**Checklist**:
- [ ] Server is running (`sage serve` active)
- [ ] Correct port being used
- [ ] No firewall blocking connection
- [ ] Client using correct endpoint

**Verification**:
```bash
# Test server is responding
curl http://localhost:8080/health

# Check server logs
tail -f .logs/sage.log
```

### 4.3 MCP Protocol Errors

**Symptom**: `MCP protocol error` or malformed responses

**Solution**:
```bash
# Verify MCP version compatibility
pip show mcp

# Update to latest
pip install --upgrade mcp

# Check server configuration
cat config/services/mcp.yaml
```

---

## 5. Loading Issues

### 5.1 Content Not Found

**Symptom**: `FileNotFoundError` or `Content not found for layer`

**Diagnosis**:
```bash
# Check content directory exists
ls -la content/

# Verify structure
tree content/ -L 2

# Check configuration
cat config/sage.yaml | grep -A5 content
```

**Solution**:
```yaml
# config/sage.yaml - ensure correct path
content:
  root: "./content"  # Relative to project root
  # Or absolute path
  root: "/path/to/sage-kb/content"
```

### 5.2 Timeout Errors

**Symptom**: `TimeoutError` during content loading

**Diagnosis**:
```bash
# Check current timeout settings
cat config/core/timeout.yaml

# Test with increased timeout
sage get --layer core --timeout 10000
```

**Solutions**:

```yaml
# config/core/timeout.yaml - increase timeouts
timeouts:
  t1_cache_ms: 200      # Was 100
  t2_single_file_ms: 1000  # Was 500
  t3_layer_ms: 5000     # Was 2000
  t4_full_load_ms: 15000   # Was 5000
```

### 5.3 Partial Loading

**Symptom**: Only some content loads, warnings about skipped files

**Cause**: Token budget exceeded or individual file timeouts

**Solution**:
```yaml
# config/knowledge/token_budget.yaml - increase budget
token_budget:
  total: 10000  # Increase from default
  per_layer:
    core: 2000
    guidelines: 3000
    frameworks: 3000
    practices: 2000
```

---

## 6. Performance Issues

### 6.1 Slow Startup

**Symptom**: SAGE takes long time to initialize

**Diagnosis**:
```bash
# Profile startup time
time sage info

# Check what's loading
sage info --verbose --timing
```

**Solutions**:

| Cause | Solution |
|-------|----------|
| Large content | Enable lazy loading |
| No cache | Enable caching |
| Many plugins | Disable unused plugins |

```yaml
# config/knowledge/loading.yaml
loading:
  lazy: true
  cache_enabled: true
  preload_layers: [core]  # Only preload essentials
```

### 6.2 Slow Searches

**Symptom**: Search takes several seconds

**Solutions**:
```yaml
# config/knowledge/search.yaml
search:
  max_results: 50  # Limit results
  timeout_ms: 2000
  use_index: true  # Enable search index
```

### 6.3 Memory Issues

**Symptom**: High memory usage or `MemoryError`

**Diagnosis**:
```bash
# Monitor memory
watch -n 1 'ps aux | grep sage'

# Check loaded content size
sage info --memory
```

**Solution**:
```yaml
# config/core/memory.yaml
memory:
  max_content_mb: 100
  eviction_policy: lru
  gc_threshold: 0.8
```

---

## 7. Configuration Issues

### 7.1 Invalid YAML Syntax

**Symptom**: `yaml.YAMLError` or `Invalid configuration`

**Diagnosis**:
```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('config/sage.yaml'))"

# Use online validator
# https://yamlvalidator.com
```

**Common Mistakes**:

| Mistake | Wrong | Correct |
|---------|-------|---------|
| Tab indentation | `\t` | `  ` (2 spaces) |
| Missing quotes | `pattern: *.md` | `pattern: "*.md"` |
| Wrong type | `timeout: "100"` | `timeout: 100` |

### 7.2 Missing Configuration

**Symptom**: `KeyError` or `Configuration key not found`

**Solution**:
```bash
# Check for required config files
ls config/

# Expected files:
# - sage.yaml (main)
# - core/*.yaml
# - knowledge/*.yaml
# - services/*.yaml

# Restore defaults
python -m tools.migration_toolkit restore-defaults
```

### 7.3 Environment Variable Issues

**Symptom**: Environment variables not being read

**Diagnosis**:
```bash
# Check if variable is set
echo $SAGE_CONFIG_PATH  # Unix
echo %SAGE_CONFIG_PATH%  # Windows

# Verify in Python
python -c "import os; print(os.environ.get('SAGE_CONFIG_PATH'))"
```

**Solution**:
```bash
# Set environment variable
export SAGE_CONFIG_PATH=/path/to/config  # Unix
set SAGE_CONFIG_PATH=C:\path\to\config   # Windows

# Or use .env file (with python-dotenv)
echo "SAGE_CONFIG_PATH=/path/to/config" >> .env
```

---

## 8. Log Analysis

### 8.1 Log Locations

| Log Type | Location | Purpose |
|----------|----------|---------|
| Application | `.logs/sage.log` | General operations |
| Error | `.logs/error.log` | Errors only |
| Debug | `.logs/debug.log` | Detailed debugging |
| Audit | `.logs/audit.log` | Security events |

### 8.2 Log Levels

```yaml
# config/core/logging.yaml
logging:
  level: INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
  format: json  # or text
```

### 8.3 Common Log Patterns

**Timeout Warning**:
```
WARN - Timeout loading file: content/large_file.md (T2: 500ms exceeded)
```
→ Increase T2 timeout or optimize file

**Circuit Breaker**:
```
WARN - Circuit breaker opened for loader after 3 failures
```
→ Check content source, may have persistent issues

**Token Budget**:
```
INFO - Token budget exhausted, loaded 8/12 files
```
→ Increase token budget or prioritize content

### 8.4 Debug Mode

```bash
# Enable debug logging temporarily
SAGE_LOG_LEVEL=DEBUG sage get --layer core

# Or in configuration
# config/core/logging.yaml
logging:
  level: DEBUG
  include_timestamps: true
  include_caller: true
```

---

## 9. Getting Help

### 9.1 Information to Gather

Before reporting an issue, collect:

```bash
# System information
python --version
pip show sage-kb
uname -a  # Unix
systeminfo  # Windows

# SAGE information
sage info --verbose

# Configuration
cat config/sage.yaml

# Relevant logs
tail -100 .logs/sage.log
```

### 9.2 Reporting Issues

**GitHub Issues**: https://github.com/HengYangDS/sage-kb/issues

**Issue Template**:
```markdown
## Description
Brief description of the issue

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Python version:
- SAGE version:
- OS:

## Logs
```
[paste relevant logs]
```
```

### 9.3 Quick Reference

| Problem | Solution |
|---------|----------|
| Can't install | Check Python 3.12+, use venv |
| Command not found | `pip install -e .` |
| No results | Check content path in config |
| Timeout | Increase timeout values |
| Server won't start | Check port conflicts |
| Slow performance | Enable caching, reduce content |

---

## Related

- `docs/guides/quickstart.md` — Getting started
- `docs/guides/advanced.md` — Advanced configuration
- `config/index.md` — Configuration reference
- `.context/configurations/` — Configuration details

---

*Part of SAGE Knowledge Base*
