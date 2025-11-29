# Documentation Standards Practice Guide

> **Load Time**: On-demand (~150 tokens)  
> **Purpose**: Practical standards for effective documentation

---

## 1. Document Structure

### File Naming

`[category]_[topic]_[qualifier].md` — e.g., `api_authentication_guide.md`, `architecture_decision_001.md`

### Standard Header

```
# Title
> **Load Time**: [timing] (~[tokens] tokens)  
> **Purpose**: [brief statement]  
> **Version**: [semver]
---
```

### Heading Hierarchy

`# Title (H1)` → `## Section (H2)` → `### Subsection (H3)` → `#### Detail (H4, sparingly)`

---

## 2. Content Types

| Type | Key Sections | Use For |
|------|--------------|---------|
| **API Reference** | Signature, Parameters, Returns, Raises, Example | Functions/Classes |
| **Tutorial/Guide** | Prerequisites, Steps, Verification, Troubleshooting | How-to content |
| **ADR** | Status, Context, Decision, Consequences (+/-/neutral) | Architecture decisions |
| **README** | Features, Quick Start, Documentation links, License | Project entry |
| **Changelog** | Added, Changed, Fixed, Removed (per version) | Release history |

### API Reference Format

`## [Name]` → `Signature` (code) → `Parameters` (table) → `Returns` → `Raises` → `Example` (code)

### ADR Format

`Status: Proposed|Accepted|Deprecated` → `Context` → `Decision` → `Consequences: +/-/neutral`

---

## 3. Writing Standards

| Guideline | ❌ Bad | ✓ Good |
|-----------|--------|--------|
| Be specific | "Configure the system" | "Set `MAX_CONNECTIONS=100` in config.yaml" |
| Active voice | "The file is read by the loader" | "The loader reads the file" |
| Present tense | "This will create a user" | "This creates a user" |
| Avoid jargon | "Utilize the endpoint" | "Use the endpoint" |

### Code Examples

**Good**: Complete · Minimal · Commented · Shows output · Handles errors

### Tables vs Lists

| Use Tables | Use Lists |
|------------|-----------|
| Comparing items | Sequential steps |
| Structured data | Simple enumerations |
| Reference info | Hierarchical info |

---

## 4. AI-Friendly Documentation

### Token Efficiency

| High Efficiency | Low Efficiency (Avoid) |
|-----------------|------------------------|
| Tables for structured data | Long paragraphs |
| Concise headers | Repeated information |
| Code blocks for examples | Excessive formatting |
| Bullet points for lists | Embedded images |

### Scannable Structure

`## Section` → `**Key Point**: summary` → `### Details` (bullets) → `### Example` (code)

### Cross-References

`See [Title](path)` or `Related: path/file.md (description)`

---

## 5. Maintenance

### Review Checklist

✓ Code examples tested · ✓ Links verified · ✓ Versions current · ✓ No outdated info · ✓ Consistent terms · ✓ Proper formatting

### Update Triggers

| Trigger | Action |
|---------|--------|
| Code change | Update affected docs |
| API change | Update reference + changelog |
| New feature | Add guide + reference |
| Bug found | Add troubleshooting |
| User question | Improve clarity |

### Deprecation Notice

`> ⚠️ **Deprecated**: [feature] deprecated in v[X]. Use [alternative]. Removed in v[Y].`

---

## 6. Documentation Types Matrix

| Type | Audience | Update Frequency | Token Priority |
|------|----------|------------------|----------------|
| README | All | Per release | High |
| API Reference | Developers | Per API change | Medium |
| Tutorials | New users | Quarterly | Low |
| ADRs | Team | Per decision | Low |
| Changelog | All | Per release | High |

---

## 7. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Completeness | 100% public API | API coverage check |
| Accuracy | 100% examples work | Automated testing |
| Freshness | < 1 month since code change | Git diff analysis |
| Readability | Grade 8 level | Readability score |
| Token Efficiency | < 500 tokens/section | Token counter |

---

## 8. Quick Reference

| ✓ Do | ❌ Don't |
|------|---------|
| Keep documents focused | Duplicate information |
| Use consistent formatting | Use screenshots for code |
| Include working examples | Leave TODOs in published docs |
| Update with code changes | Assume reader knowledge |
| Link to related documents | Use inconsistent terminology |

---

## Related

- `content/practices/ai_collaboration/token_optimization.md` — Token efficiency
- `content/guidelines/documentation.md` — Documentation guidelines
- `content/templates/` — Document templates

---

*Part of AI Collaboration Knowledge Base*
