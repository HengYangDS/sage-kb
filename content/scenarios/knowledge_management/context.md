# Knowledge Management Scenario Context

> Pre-configured context for building knowledge management systems

---

## Table of Contents

[1. Scenario Profile](#1-scenario-profile) · [2. Relevant Knowledge](#2-relevant-knowledge) · [3. Project Structure](#3-project-structure) · [4. Knowledge Architecture](#4-knowledge-architecture) · [5. Content Patterns](#5-content-patterns) · [6. Search & Retrieval](#6-search--retrieval) · [7. Common Tasks](#7-common-tasks) · [8. Autonomy Calibration](#8-autonomy-calibration)

---

## 1. Scenario Profile

```yaml
scenario: knowledge_management
languages: [ python, markdown, yaml ]
tools: [ sage, fastapi, elasticsearch, vector-db ]
focus: [ knowledge-organization, search, retrieval, taxonomy ]
autonomy_default: L3
```

---

## 2. Relevant Knowledge

| Priority | Files |
|----------|-------|
| **Auto-Load** | `core/principles.md` · `practices/documentation/knowledge_organization.md` · `frameworks/cognitive/knowledge_layers.md` |
| **On-Demand** | `practices/documentation/standards.md` · `practices/ai_collaboration/knowledge_extraction.md` |

---

## 3. Project Structure

| Directory | Purpose |
|-----------|---------|
| `content/` | Knowledge content repository |
| `config/knowledge/` | Knowledge loading configuration |
| `src/knowledge/` | Knowledge processing logic |
| `src/search/` | Search and retrieval services |
| `src/indexing/` | Content indexing |
| `taxonomies/` | Category and tag definitions |
| `schemas/` | Content schemas and validation |

---

## 4. Knowledge Architecture

### 4.1 Layer Model

```
┌─────────────────────────────────────────┐
│              Presentation               │
│    (CLI, API, MCP, Web Interface)       │
├─────────────────────────────────────────┤
│              Services                   │
│   (Search, Retrieval, Transformation)   │
├─────────────────────────────────────────┤
│              Core                       │
│   (Loading, Indexing, Caching)          │
├─────────────────────────────────────────┤
│              Storage                    │
│   (Files, Database, Vector Store)       │
└─────────────────────────────────────────┘
```

### 4.2 Content Hierarchy

```
knowledge_base/
├── core/              # Foundational concepts (highest priority)
│   ├── principles.md
│   └── concepts.md
├── guidelines/        # Standards and conventions
│   ├── writing.md
│   └── formatting.md
├── frameworks/        # Reusable structures
│   ├── taxonomy/
│   └── templates/
├── practices/         # Implementation guides
│   ├── workflows/
│   └── processes/
└── reference/         # Reference materials
    ├── glossary.md
    └── index.md
```

### 4.3 Metadata Schema

```yaml
# Document metadata structure
metadata:
  title: string           # Document title
  description: string     # Brief description
  layer: enum             # core|guidelines|frameworks|practices|reference
  tags: list[string]      # Searchable tags
  priority: int           # Loading priority (1-5)
  auto_load: bool         # Load on startup
  tokens: int             # Estimated token count
  updated: date           # Last modification date
  author: string          # Content author
  version: string         # Content version
```

---

## 5. Content Patterns

### 5.1 Document Template

```markdown
# Document Title

> Brief one-line description

---

## Table of Contents

[Section 1](#section-1) · [Section 2](#section-2)

---

## Section 1

### 1.1 Subsection

Content with structure...

---

## Related

- Related document links

---

*Part of Knowledge Base - Category*
```

### 5.2 Knowledge Extraction Pattern

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class KnowledgeItem:
    """Extracted knowledge item."""
    id: str
    title: str
    content: str
    layer: str
    tags: List[str]
    metadata: dict
    embeddings: Optional[List[float]] = None

class KnowledgeExtractor:
    """Extract structured knowledge from documents."""
    
    async def extract(self, path: str) -> KnowledgeItem:
        content = await self.load_content(path)
        metadata = self.parse_frontmatter(content)
        
        return KnowledgeItem(
            id=self.generate_id(path),
            title=metadata.get("title", self.extract_title(content)),
            content=self.clean_content(content),
            layer=metadata.get("layer", "practices"),
            tags=metadata.get("tags", []),
            metadata=metadata
        )
```

### 5.3 Indexing Pattern

```python
from typing import Protocol, List

class IndexProtocol(Protocol):
    """Knowledge index protocol."""
    
    async def add(self, item: KnowledgeItem) -> None:
        """Add item to index."""
        ...
    
    async def search(self, query: str, limit: int = 10) -> List[KnowledgeItem]:
        """Search index."""
        ...
    
    async def get_by_layer(self, layer: str) -> List[KnowledgeItem]:
        """Get all items in layer."""
        ...

class InMemoryIndex:
    """Simple in-memory index implementation."""
    
    def __init__(self):
        self._items: dict[str, KnowledgeItem] = {}
        self._by_layer: dict[str, list[str]] = {}
    
    async def add(self, item: KnowledgeItem) -> None:
        self._items[item.id] = item
        self._by_layer.setdefault(item.layer, []).append(item.id)
    
    async def search(self, query: str, limit: int = 10) -> List[KnowledgeItem]:
        query_lower = query.lower()
        results = [
            item for item in self._items.values()
            if query_lower in item.title.lower() 
            or query_lower in item.content.lower()
        ]
        return results[:limit]
```

---

## 6. Search & Retrieval

### 6.1 Search Strategies

| Strategy | Use Case | Implementation |
|----------|----------|----------------|
| **Keyword** | Exact matches | Full-text search |
| **Semantic** | Conceptual similarity | Vector embeddings |
| **Hybrid** | Best of both | Combined scoring |
| **Faceted** | Filtered browsing | Metadata filters |

### 6.2 Vector Search Integration

```python
from typing import List
import numpy as np

class VectorSearch:
    """Vector-based semantic search."""
    
    def __init__(self, embedding_model):
        self.model = embedding_model
        self.vectors: List[np.ndarray] = []
        self.items: List[KnowledgeItem] = []
    
    async def add(self, item: KnowledgeItem) -> None:
        embedding = await self.model.embed(item.content)
        self.vectors.append(embedding)
        self.items.append(item)
    
    async def search(self, query: str, k: int = 5) -> List[KnowledgeItem]:
        query_vec = await self.model.embed(query)
        similarities = [
            np.dot(query_vec, vec) / (np.linalg.norm(query_vec) * np.linalg.norm(vec))
            for vec in self.vectors
        ]
        top_indices = np.argsort(similarities)[-k:][::-1]
        return [self.items[i] for i in top_indices]
```

### 6.3 Query Processing

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SearchQuery:
    """Structured search query."""
    text: str
    layers: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    limit: int = 10
    offset: int = 0

class QueryProcessor:
    """Process and optimize search queries."""
    
    def parse(self, raw_query: str) -> SearchQuery:
        """Parse raw query string into structured query."""
        # Extract layer filters: layer:core
        layers = self._extract_filter(raw_query, "layer")
        
        # Extract tag filters: tag:python
        tags = self._extract_filter(raw_query, "tag")
        
        # Clean query text
        text = self._clean_query(raw_query)
        
        return SearchQuery(text=text, layers=layers, tags=tags)
    
    def _extract_filter(self, query: str, prefix: str) -> List[str]:
        import re
        pattern = f"{prefix}:(\\w+)"
        return re.findall(pattern, query)
```

---

## 7. Common Tasks

| Task | Steps |
|------|-------|
| **Add knowledge** | Create document → Add metadata → Index → Verify search |
| **Update taxonomy** | Define categories → Update schemas → Reindex → Test |
| **Build search** | Choose strategy → Implement index → Add ranking → Optimize |
| **Export knowledge** | Select scope → Transform format → Validate → Package |
| **Migrate content** | Map structure → Transform → Validate → Import |

---

## 8. Autonomy Calibration

| Task Type | Level | Notes |
|-----------|-------|-------|
| Add new document | L4 | Follow templates |
| Update metadata | L5 | Low risk |
| Modify taxonomy | L2 | Affects organization |
| Change search algorithm | L2 | Affects retrieval quality |
| Update templates | L3 | Verify consistency |
| Bulk import | L2 | Review before commit |
| Schema changes | L1-L2 | Breaking change potential |

---

## 9. Quality Checklist

| Area | Check |
|------|-------|
| **Structure** | Consistent hierarchy, clear navigation |
| **Metadata** | Complete, accurate, up-to-date |
| **Content** | Clear, concise, actionable |
| **Links** | Valid references, no broken links |
| **Search** | Relevant results, good ranking |
| **Performance** | Fast loading, efficient indexing |

---

## Related

- `practices/documentation/knowledge_organization.md` — Organization principles
- `practices/documentation/standards.md` — Documentation standards
- `frameworks/cognitive/knowledge_layers.md` — Layer definitions
- `templates/` — Document templates

---

*Part of SAGE Knowledge Base - Scenarios*
