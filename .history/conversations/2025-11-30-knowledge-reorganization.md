# Knowledge Reorganization - 2025-11-30

## Context

User requested analysis and execution of knowledge reorganization across the project's knowledge directories (`.context`, `content`, `docs`, `.history`), addressing four key questions:
1. What generic knowledge in `.context` should be moved to `content`
2. What project-specific knowledge in `content` should be moved to `.context`
3. What knowledge in `docs` should be consolidated
4. Why `.history` documents haven't been updated

## Key Decisions

### Decision 1: Generic Knowledge Migration (.context → content)

**Rationale**: `.context/intelligence/` contained reusable patterns mixed with project-specific data

**Actions**:
- Created `content/practices/engineering/common_pitfalls.md` (539 lines) - generic pitfalls guide
- Created `content/practices/ai_collaboration/interaction_patterns.md` (283 lines) - generic AI patterns
- Updated `.context/intelligence/common_pitfalls.md` to slim reference (88 lines) with SAGE-specific pitfalls only
- Updated `.context/intelligence/patterns.md` to slim reference (100 lines) with SAGE-specific calibration data only
- Kept `optimizations.md` and `performance_tuning.md` in `.context/` (SAGE-specific conventions)

### Decision 2: Project-Specific Content Migration (content → docs)

**Rationale**: `content/references/` contained SAGE-specific API documentation that doesn't belong in distributable content

**Actions**:
- Moved `content/references/mcp_api.md` → `docs/api/mcp_quick_ref.md`
- Moved `content/references/plugin_api.md` → `docs/api/plugin_quick_ref.md`
- Updated `docs/api/index.md` with new Quick References section

### Decision 3: Cross-References Between Design Docs and ADRs

**Rationale**: Design documents should reference their corresponding Architecture Decision Records

**Actions**:
- Updated `docs/design/01-architecture.md` with ADR references (0001, 0004, 0005, 0006)
- Updated `docs/design/02-sage-protocol.md` with ADR-0002 reference
- Updated `docs/design/04-timeout-loading.md` with ADR-0003 and timeout policy references

### Decision 4: Session History Activation

**Rationale**: `.history/` only contained example templates, no actual records were being created

**Actions**:
- Added Session History Management section to `.junie/guidelines.md` with:
  - Record type table
  - Session end checklist
  - Naming conventions
- Created `.history/_session-end-checklist.md` (143 lines) - detailed checklist template
- Created `.context/intelligence/session_automation_requirements.md` (247 lines) - long-term automation plan

## Outcomes

### Files Created
- `content/practices/engineering/common_pitfalls.md`
- `content/practices/ai_collaboration/interaction_patterns.md`
- `.history/_session-end-checklist.md`
- `.context/intelligence/session_automation_requirements.md`
- `.history/conversations/2025-11-30-knowledge-reorganization.md` (this file)

### Files Modified
- `.context/intelligence/common_pitfalls.md` (reduced from 541 to 88 lines)
- `.context/intelligence/patterns.md` (reduced from 277 to 100 lines)
- `docs/api/index.md` (added Quick References section)
- `docs/design/01-architecture.md` (added ADR references)
- `docs/design/02-sage-protocol.md` (added ADR reference)
- `docs/design/04-timeout-loading.md` (added ADR and policy references)
- `.junie/guidelines.md` (added Session History Management section)

### Files Moved
- `content/references/mcp_api.md` → `docs/api/mcp_quick_ref.md`
- `content/references/plugin_api.md` → `docs/api/plugin_quick_ref.md`

## Session Continuation: Configuration Verification

### Question 5: Configuration File Adjustments

**Analysis performed on configuration files:**

| Config File | Status | Notes |
|------------|--------|-------|
| `config/knowledge/content.yaml` | ✓ Valid | `references` directory still valid (2 files remain) |
| `config/knowledge/triggers.yaml` | ✓ Valid | No references to moved files |
| `config/knowledge/loading.yaml` | ✓ Valid | `always` list files exist |
| `config/sage.yaml` | ✓ Valid | Abstract paths, no direct file refs |

**Configuration Status**: All configuration files use abstract directory references (`content/references/`) rather than specific file paths. The `content/references/` directory still exists with `knowledge_quick_ref.md` and `performance_checklist.md`, so no configuration changes were needed.

### Broken Reference Fixes

**Found and fixed broken references to moved files:**

| File | Old Reference | New Reference |
|------|---------------|---------------|
| `content/scenarios/mcp_integration/context.md` | `content/references/mcp_api.md` | `docs/api/mcp_quick_ref.md` |
| `content/scenarios/plugin_development/context.md` | `content/references/plugin_api.md` | `docs/api/plugin_quick_ref.md` |

**Ignored references (historical/temporary):**
- `.history/conversations/2025-11-30-knowledge-reorganization.md` - Historical record
- `.outputs/*.py` - Temporary analysis scripts

---

## Learnings

1. **Knowledge Classification Principle**: 
   - `.context/` = Project-specific (ADRs, conventions, calibration data)
   - `content/` = Generic, distributable (patterns, practices, frameworks)
   - `docs/` = User-facing documentation (guides, API references)

2. **Session History Gap**: The `.history/` system was well-designed but lacked integration with AI collaboration workflows. Short-term solution is explicit instructions; long-term solution is automation via hooks and plugins.

3. **Cross-Reference Value**: Linking design docs to ADRs improves traceability and helps understand "why" behind designs.

## References

- `.junie/guidelines.md` — Updated AI collaboration guidelines
- `.history/index.md` — Session history structure
- `.context/intelligence/session_automation_requirements.md` — Automation roadmap
- `content/practices/ai_collaboration/interaction_patterns.md` — Generic AI patterns

---

*Session Duration: ~45 minutes*
*Part of SAGE Knowledge Base - Session History*
