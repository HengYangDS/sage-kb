
# MCP API Quick Reference

> Essential MCP tools and resources for SAGE integration

---

## Tools

| Tool                 | Purpose               | Required Params |
|----------------------|-----------------------|-----------------|
| `sage_get_knowledge` | Retrieve knowledge    | `layer`         |
| `sage_search`        | Search KB             | `query`         |
| `sage_get_context`   | Task-specific context | `task_type`     |
| `sage_info`          | System status         | (none)          |

## Table of Contents

- [Tools](#tools)
- [Tool Parameters](#tool-parameters)
- [Resources](#resources)
- [Timeout Levels](#timeout-levels)
- [Error Codes](#error-codes)
- [Quick Start](#quick-start)
- [Related](#related)

---

## Tool Parameters

### sage_get_knowledge

```json
{ "layer": "core|guidelines|frameworks|practices|all", "topic": "optional", "timeout_ms": 2000 }
```
### sage_search

```json
{ "query": "search text", "limit": 10, "layer": "all" }
```
### sage_get_context

```json
{ "task_type": "coding|debugging|reviewing|planning|documenting", "language": "python", "token_budget": 4000 }
```
---

## Resources

| URI Pattern                           | Content           |
|---------------------------------------|-------------------|
| `knowledge://core/{topic?}`           | Core principles   |
| `knowledge://guidelines/{category?}`  | Coding standards  |
| `knowledge://frameworks/{framework?}` | Conceptual models |
| `knowledge://practices/{category?}`   | Best practices    |

---

## Timeout Levels

| Level | Timeout | Use Case         |
|-------|---------|------------------|
| T1    | 100ms   | Cache-only       |
| T2    | 500ms   | Single file      |
| T3    | 2s      | Standard calls   |
| T4    | 5s      | Full KB load     |
| T5    | 10s     | Complex analysis |

---

## Error Codes

| Code            | Description                |
|-----------------|----------------------------|
| `TIMEOUT`       | Operation exceeded timeout |
| `NOT_FOUND`     | Resource not found         |
| `INVALID_INPUT` | Invalid parameters         |
| `INTERNAL`      | Server error               |

---

## Quick Start

```bash
# Start server
sage serve --host localhost --port 8000
```
```python
# Client usage
result = await client.call_tool("sage_get_knowledge", {"layer": "core"})
results = await client.call_tool("sage_search", {"query": "timeout"})
```
---

## Related

- `docs/api/MCP.md` — Full MCP protocol reference
- `docs/api/MCP_TOOLS_REF.md` — Detailed tool schemas
- `docs/api/MCP_RESOURCES.md` — Resources and prompts
- `docs/design/services/MCP_SERVICE.md` — MCP service design

---

*AI Collaboration Knowledge Base*
