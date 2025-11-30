# IDE Integration Guide

> Configuration and setup for integrating SAGE with various IDEs

---

## Table of Contents

- [1. JetBrains IDE Integration](#1-jetbrains-ide-integration)
- [2. VS Code Integration](#2-vs-code-integration)
- [3. Editor-Agnostic Pattern](#3-editor-agnostic-pattern)

---

## 1. JetBrains IDE Integration

### 1.1 Setup via .junie/guidelines.md

```markdown
# Project Guidelines

## Knowledge Base
- Use `sage get` for context loading
- Follow timeout hierarchy (T1-T5)
- Reference `.context/` for project-specific knowledge

## Autonomy Level
Default: L4 (Medium-High)
```

### 1.2 File Watcher Integration

```yaml
# .idea/sage-watcher.xml
<component name="SageWatcher">
  <watch path=".context/" />
  <watch path=".knowledge/" />
  <on-change action="sage rebuild --incremental" />
</component>
```

---

## 2. VS Code Integration

### 2.1 Extension Settings

`.vscode/settings.json`:

```json
{
  "sage.enable": true,
  "sage.configPath": "./config/app.yaml",
  "sage.autoLoad": true,
  "sage.timeout": 5000,
  "sage.layers": [
    "core",
    "guidelines"
  ]
}
```

### 2.2 Tasks Configuration

`.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "SAGE: Reload Knowledge",
      "type": "shell",
      "command": "sage",
      "args": ["reload"],
      "problemMatcher": []
    },
    {
      "label": "SAGE: Check Links",
      "type": "shell",
      "command": "sage",
      "args": ["check", "--links"],
      "problemMatcher": []
    }
  ]
}
```

---

## 3. Editor-Agnostic Pattern

### 3.1 Bridge Implementation

```python
class EditorBridge:
    """Bridge between SAGE and any editor."""
    
    def __init__(self, editor_type: str):
        self.editor = self._detect_editor(editor_type)
    
    async def provide_context(self, file_path: str) -> dict:
        """Provide context for current file."""
        return {
            "file_context": await self.get_file_context(file_path),
            "project_context": await self.get_project_context(),
            "relevant_knowledge": await self.search_relevant(file_path)
        }
    
    async def on_file_save(self, file_path: str):
        """Hook for file save events."""
        if self._is_knowledge_file(file_path):
            await self.trigger_rebuild()
```

### 3.2 Integration Points

| Event | Action | Implementation |
|-------|--------|----------------|
| File Open | Load relevant context | `provide_context()` |
| File Save | Trigger rebuild if KB file | `on_file_save()` |
| Project Open | Load full knowledge base | `load_knowledge()` |
| Search | Query knowledge base | `search()` |

---

## Related

- `.knowledge/frameworks/patterns/INTEGRATION.md` — Integration patterns overview
- `.knowledge/practices/engineering/operations/CI_CD.md` — CI/CD configuration

---

*IDE Integration Guide v1.0*
*Extracted from Integration Patterns Framework*

---

*AI Collaboration Knowledge Base*
