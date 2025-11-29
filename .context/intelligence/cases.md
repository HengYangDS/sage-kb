# Technical Cases Repository

> Collection of problem-solving cases and lessons learned

---

## Overview

This document records technical cases encountered during project development. Each case follows the structure defined in `content/templates/case_study.md`.

---

## Case Index

| ID | Title | Category | Date | Status |
|----|-------|----------|------|--------|
| CASE-2025-11-29-001 | Output files in wrong directory | Bug Fix | 2025-11-29 | Resolved |
| CASE-2025-11-29-002 | Knowledge consolidation initiative | Documentation | 2025-11-29 | Resolved |

---

## CASE-2025-11-29-001

### Summary

| Field | Value |
|-------|-------|
| **Case ID** | CASE-2025-11-29-001 |
| **Title** | Output files created in wrong directory |
| **Date** | 2025-11-29 |
| **Category** | Bug Fix |
| **Difficulty** | Simple |
| **Time Spent** | 15 minutes |
| **Status** | Resolved |

### Problem Description

The `build_knowledge_graph` MCP tool was creating output files (e.g., `test_graph.json`) in the current working directory or user-specified path instead of the designated `.outputs/` directory.

**Expected Behavior**: Output files should be saved to `.outputs/` directory.

**Actual Behavior**: Files were saved to the path provided by the user directly.

### Root Cause

The `build_knowledge_graph` function in `mcp_server.py` directly used the `output_file` parameter without normalizing the path to the `.outputs/` directory.

```python
# Original code
if output_file:
    builder.export_to_json(Path(output_file))
```

### Solution

Modified `src/sage/services/mcp_server.py` to:
1. Create `.outputs/` directory if it doesn't exist
2. Extract only the filename from user-provided path
3. Construct output path as `.outputs/{filename}`

```python
# Fixed code
if output_file:
    project_root = Path(__file__).parent.parent.parent.parent
    outputs_dir = project_root / ".outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    
    output_filename = Path(output_file).name
    output_path = outputs_dir / output_filename
    builder.export_to_json(output_path)
```

### Verification

- Ran unit tests: `pytest tests/unit/services/test_mcp_server.py::TestKnowledgeGraphTool -v`
- Verified `test_graph.json` was created in `.outputs/` directory

### Lessons Learned

| Takeaway | Action |
|----------|--------|
| Output paths should be normalized | Always use designated output directories |
| Create directories programmatically | Use `mkdir(parents=True, exist_ok=True)` |
| Document output locations | Update docstrings with file locations |

### Tags

`bug-fix` `mcp-tools` `file-output` `path-normalization`

---

## CASE-2025-11-29-002

### Summary

| Field | Value |
|-------|-------|
| **Case ID** | CASE-2025-11-29-002 |
| **Title** | Knowledge consolidation initiative |
| **Date** | 2025-11-29 |
| **Category** | Documentation |
| **Difficulty** | Medium |
| **Time Spent** | ~60 minutes |
| **Status** | Resolved |

### Problem Description

User requested analysis of knowledge gaps in the SAGE Knowledge Base and implementation of recommended improvements.

**Request**: "有哪些知识可以沉淀或补充" (What knowledge can be consolidated or supplemented)

### Analysis Results

After analyzing the project structure, identified the following areas for improvement:

| Category | Gap | Priority |
|----------|-----|----------|
| Troubleshooting | No dedicated troubleshooting guide | High |
| Integration | No integration patterns document | High |
| Security | No security practices document | Medium |
| Migration | No version migration guide | Medium |
| FAQ | No FAQ document | Medium |
| Configuration | No comprehensive config guide | Medium |
| Tools | No MCP tools guide | Medium |
| Tools | No Knowledge Graph guide | Medium |
| Cases | No case study template or repository | Medium |

### Solution

Created 10 new documentation files:

| File | Lines | Purpose |
|------|-------|---------|
| `content/practices/engineering/troubleshooting.md` | 451 | Troubleshooting guide |
| `content/frameworks/patterns/integration.md` | 574 | Integration patterns |
| `content/practices/engineering/security.md` | 592 | Security practices |
| `docs/guides/migration.md` | 477 | Version migration |
| `docs/guides/faq.md` | 472 | FAQ |
| `content/templates/case_study.md` | 231 | Case study template |
| `docs/guides/configuration.md` | 756 | Configuration guide |
| `content/practices/engineering/knowledge_graph.md` | 562 | Knowledge graph guide |
| `docs/guides/mcp_tools.md` | 861 | MCP tools guide |
| `.context/intelligence/cases.md` | This file | Cases repository |

**Total**: ~5,000 lines of documentation added

### Lessons Learned

| Takeaway | Action |
|----------|--------|
| Regular knowledge audits are valuable | Schedule periodic KB reviews |
| Documentation gaps accumulate | Address gaps proactively |
| Templates accelerate documentation | Create templates for common doc types |
| Case studies capture institutional knowledge | Record significant problem-solving experiences |

### Tags

`documentation` `knowledge-management` `knowledge-gaps` `best-practices`

---

## Case Categories Reference

| Category | Description |
|----------|-------------|
| Bug Fix | Fixing incorrect behavior |
| Performance | Optimization issues |
| Architecture | Design-level issues |
| Integration | External system issues |
| Configuration | Config-related issues |
| Security | Security vulnerabilities |
| Documentation | Doc-related improvements |

---

## How to Add New Cases

1. Copy the case template structure from this file or `content/templates/case_study.md`
2. Fill in all sections with details
3. Add entry to the Case Index table at the top
4. Add relevant tags for searchability
5. Update this file via PR or direct edit

---

## Related

- `content/templates/case_study.md` — Case study template
- `.context/intelligence/patterns.md` — Learned patterns
- `.context/intelligence/optimizations.md` — Optimization history
- `content/practices/engineering/troubleshooting.md` — Troubleshooting guide

---

*Part of SAGE Knowledge Base — 信达雅 (Xin-Da-Ya)*
