# Integration Patterns

> Patterns for integrating SAGE with AI tools, IDEs, and CI/CD systems

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. AI Tool Integration](#2-ai-tool-integration)
- [3. IDE Integration](#3-ide-integration)
- [4. CI/CD Integration](#4-cicd-integration)
- [5. API Integration](#5-api-integration)
- [6. Plugin Integration](#6-plugin-integration)
- [7. Data Integration](#7-data-integration)
- [8. Best Practices](#8-best-practices)

---

## 1. Overview

### 1.1 Integration Philosophy

| Principle                | Description                                   |
|--------------------------|-----------------------------------------------|
| **Loose Coupling**       | Minimize dependencies between systems         |
| **Protocol-First**       | Define clear interfaces before implementation |
| **Graceful Degradation** | Continue working when integrations fail       |
| **Observable**           | Make integration state visible and debuggable |

### 1.2 Integration Types

```mermaid
flowchart TB
    subgraph KB["AI Collaboration Knowledge Base"]
        MCP["MCP Server"]
        CLI["CLI Interface"]
        API["API Server"]
        Plugin["Plugin System"]
    end
    MCP --> AI["AI Clients"]
    CLI --> Terminal["Terminal Tools"]
    API --> External["External Apps"]
    Plugin --> Custom["Custom Plugins"]
```
---

## 2. AI Tool Integration

### 2.1 MCP Client Integration

**Supported Clients**:

| Client             | Integration Method | Status    |
|--------------------|--------------------|-----------|
| Claude Desktop     | MCP Protocol       | Native    |
| JetBrains Junie    | MCP Protocol       | Native    |
| Cursor             | MCP Protocol       | Supported |
| VS Code + Continue | MCP Protocol       | Supported |
| Custom Clients     | MCP SDK            | Manual    |

**Configuration Example**:

```json
{
  "mcpServers": {
    "knowledge-base": {
      "command": "sage",
      "args": [
        "serve",
        "--stdio"
      ],
      "env": {
        "SAGE_CONFIG": "/path/to/config"
      }
    }
  }
}
```
### 2.2 Multi-Client Pattern

```python
# Support multiple concurrent clients
from sage.services.mcp_server import create_app
app = create_app()
# Each client gets isolated session state
@app.tool()
async def get_knowledge(
    session_id: str,  # Client-provided session ID
    layer: int = 0
) -> dict:
    """Knowledge retrieval with session isolation."""
    session = get_or_create_session(session_id)
    return await session.load_knowledge(layer)
```
### 2.3 Context Synchronization

| Pattern    | Use Case          | Implementation                    |
|------------|-------------------|-----------------------------------|
| **Push**   | Real-time updates | WebSocket/SSE                     |
| **Pull**   | On-demand refresh | Periodic polling                  |
| **Hybrid** | Balanced approach | Push notifications + Pull details |

**Example: Hybrid Sync**:

```python
class ContextSync:
    def __init__(self, client):
        self.client = client
        self.last_sync = None
    async def on_change(self, change_event):
        """Push: Notify client of changes."""
        await self.client.notify(
            "context_changed", {
                "type": change_event.type,
                "path": change_event.path
            }
        )
    async def get_full_context(self):
        """Pull: Client requests full context."""
        self.last_sync = datetime.now()
        return await self.load_context()
```
---

## 3. IDE Integration

> **Full configuration details**: See `.knowledge/practices/engineering/workflow/IDE_INTEGRATION.md`

### 3.1 Supported IDEs

| IDE | Integration Method | Configuration |
|-----|-------------------|---------------|
| JetBrains (IntelliJ, PyCharm, etc.) | .junie/guidelines.md + File Watcher | See practices |
| VS Code | Extension settings + Tasks | See practices |
| Other editors | EditorBridge API | See practices |

### 3.2 Integration Pattern

```python
class EditorBridge:
    async def provide_context(self, file_path: str) -> dict:
        """Provide context for current file."""
        return {
            "file_context": await self.get_file_context(file_path),
            "project_context": await self.get_project_context(),
            "relevant_knowledge": await self.search_relevant(file_path)
        }
```

---

## 4. CI/CD Integration

> **Configuration templates**: See `.knowledge/templates/CI_CD_KNOWLEDGE_CHECK.yaml`

### 4.1 Supported Systems

| System | Template Available | Key Features |
|--------|-------------------|--------------|
| GitHub Actions | ✓ | Path-based triggers, validation steps |
| GitLab CI | ✓ | Multi-stage pipeline, artifacts |
| Pre-commit | ✓ | Local validation hooks |

### 4.2 Pipeline Stages

| Stage | Action | On Failure |
|-------|--------|------------|
| **Lint** | Check formatting, links | Block merge |
| **Validate** | Structure, content validation | Block merge |
| **Build** | Generate outputs | Block deploy |
| **Deploy** | Update production KB | Rollback |

---

## 5. API Integration

### 5.1 REST API Pattern

```python
from fastapi import FastAPI, HTTPException
from sage.core.loader import KnowledgeLoader
app = FastAPI()
loader = KnowledgeLoader()
@app.get("/api/v1/knowledge/{layer}")
async def get_knowledge(layer: int, timeout_ms: int = 5000):
    """REST endpoint for knowledge retrieval."""
    try:
        result = await loader.load_layer(layer, timeout_ms=timeout_ms)
        return {"status": "success", "data": result}
    except TimeoutError:
        raise HTTPException(504, "Knowledge loading timed out")
@app.get("/api/v1/search")
async def search(q: str, max_results: int = 10):
    """Search knowledge base."""
    results = await loader.search(q, max_results=max_results)
    return {"status": "success", "results": results}
```
### 5.2 GraphQL Pattern

```python
import strawberry
from sage.core.loader import KnowledgeLoader
@strawberry.type
class KnowledgeNode:
    id: str
    title: str
    content: str
    layer: int
@strawberry.type
class Query:
    @strawberry.field
    async def knowledge(self, layer: int = 0) -> list[KnowledgeNode]:
        loader = KnowledgeLoader()
        return await loader.load_layer(layer)
    @strawberry.field
    async def search(self, query: str) -> list[KnowledgeNode]:
        loader = KnowledgeLoader()
        return await loader.search(query)
```
### 5.3 Webhook Pattern

```python
from sage.core.events import EventBus
class WebhookIntegration:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        EventBus.subscribe("knowledge.updated", self.on_update)
    async def on_update(self, event):
        """Send webhook on knowledge update."""
        await httpx.post(
            self.webhook_url, json={
                "event"    : "knowledge.updated",
                "timestamp": event.timestamp,
                "changes"  : event.changes
            }
        )
```
---

## 6. Plugin Integration

### 6.1 Plugin Discovery

```python
from sage.plugins import PluginManager
class IntegrationPlugin:
    """Base class for integration plugins."""
    name: str = "base-integration"
    version: str = "1.0.0"
    async def initialize(self, context: dict) -> None:
        """Called when plugin is loaded."""
        pass
    async def on_knowledge_load(self, knowledge: dict) -> dict:
        """Hook for knowledge loading."""
        return knowledge
    async def on_search(self, query: str, results: list) -> list:
        """Hook for search results."""
        return results
```
### 6.2 Plugin Communication

```mermaid
flowchart TB
    A["Plugin A"] -->|Event Bus| B["Plugin B"]
    A --> Core["Core"]
    B --> Core
```
**Event-Based Communication**:

```python
from sage.core.events import EventBus
class AnalyticsPlugin:
    async def initialize(self, context):
        EventBus.subscribe("tool.invoked", self.track_usage)
    async def track_usage(self, event):
        # Track tool usage for analytics
        await self.analytics.track(event.tool_name, event.duration)
```
---

## 7. Data Integration

### 7.1 Import Patterns

| Source     | Format        | Handler               |
|------------|---------------|-----------------------|
| Confluence | HTML/Markdown | `confluence_importer` |
| Notion     | Markdown      | `notion_importer`     |
| Git Wiki   | Markdown      | `git_importer`        |
| Docusaurus | MDX           | `mdx_importer`        |

**Import Example**:

```python
from sage.integrations import ConfluenceImporter
importer = ConfluenceImporter(
    base_url="https://company.atlassian.net",
    space_key="KB"
)
# Import with transformation
await importer.import_space(
    target_path=".knowledge/imported/",
    transform=lambda doc: doc.to_sage_format()
)
```
### 7.2 Export Patterns

```python
from sage.integrations import Exporter
exporter = Exporter(kb_path=".knowledge/")
# Export to different formats
await exporter.to_docusaurus("dist/docusaurus/")
await exporter.to_mkdocs("dist/mkdocs/")
await exporter.to_json("dist/knowledge.json")
```
### 7.3 Sync Patterns

| Pattern     | Use Case               | Complexity |
|-------------|------------------------|------------|
| **One-way** | KB as source of truth  | Low        |
| **Two-way** | Bidirectional edits    | High       |
| **Merge**   | Periodic consolidation | Medium     |

---

## 8. Best Practices

### 8.1 Integration Checklist

| Category       | Checklist Item                         |
|----------------|----------------------------------------|
| **Setup**      | □ Define clear interface contract      |
|                | □ Document authentication requirements |
|                | □ Set up error handling                |
| **Testing**    | □ Unit tests for integration points    |
|                | □ Integration tests with mocks         |
|                | □ End-to-end tests in staging          |
| **Operations** | □ Monitor integration health           |
|                | □ Set up alerts for failures           |
|                | □ Document troubleshooting steps       |

### 8.2 Error Handling

```python
from sage.integrations import IntegrationError
class ResilientIntegration:
    async def call_external(self, request):
        retries = 3
        for attempt in range(retries):
            try:
                return await self._do_call(request)
            except IntegrationError as e:
                if attempt == retries - 1:
                    # Log and return fallback
                    logger.error(f"Integration failed: {e}")
                    return self.fallback_response()
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
```
### 8.3 Security Considerations

| Aspect             | Recommendation                               |
|--------------------|----------------------------------------------|
| **Authentication** | Use API keys or OAuth2                       |
| **Authorization**  | Implement RBAC for sensitive knowledge       |
| **Data Transit**   | Always use TLS                               |
| **Secrets**        | Use environment variables or secret managers |

### 8.4 Performance Optimization

| Technique              | When to Use               |
|------------------------|---------------------------|
| **Caching**            | Frequently accessed data  |
| **Batching**           | Multiple small requests   |
| **Async**              | I/O-bound operations      |
| **Connection Pooling** | Database/HTTP connections |

---

## Quick Reference

### Integration URLs

| Service     | Endpoint                        |
|-------------|---------------------------------|
| MCP (stdio) | `sage serve --stdio`            |
| MCP (SSE)   | `http://localhost:8080/sse`     |
| REST API    | `http://localhost:8080/api/v1/` |
| Health      | `http://localhost:8080/health`  |

### Environment Variables

```bash
SAGE_MCP_PORT=8080
SAGE_API_KEY=your-api-key
SAGE_WEBHOOK_SECRET=webhook-secret
SAGE_EXTERNAL_URL=https://api.example.com
```
---

## Related

- `.knowledge/frameworks/patterns/COLLABORATION.md` — Collaboration patterns
- `.knowledge/practices/engineering/design/API_DESIGN.md` — API design guidelines
- `.context/decisions/ADR_0008_PLUGIN_SYSTEM.md` — Plugin architecture
- `docs/api/MCP.md` — MCP API reference

---

*Patterns Framework v1.0*
*Last reviewed: 2025-12-01 by Expert Committee (L2, Strong Approve, 4.42/5)*

