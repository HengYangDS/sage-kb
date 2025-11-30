# Scripts Directory

> Development utilities and automation scripts organized by category

---

## Directory Structure

```
scripts/
├── dev/          # Development setup and utilities
├── check/        # Validation and verification scripts
├── hooks/        # Git hooks (pre-commit, pre-push, etc.)
└── ci/           # CI/CD pipeline scripts
```

---

## Categories

### dev/ - Development Scripts

| Script | Purpose |
|--------|---------|
| `setup_dev.py` | Development environment setup |
| `new_file.py` | Create new files from templates |
| `add_metadata.py` | Add metadata to files |
| `generate_index.py` | Generate index files |
| `check_architecture.py` | Architecture validation |
| `check_links.py` | Link validation |
| `validate_format.py` | Format validation |

### check/ - Validation Scripts

| Script | Purpose |
|--------|---------|
| `validate_knowledge.py` | Knowledge base validation |

### hooks/ - Git Hooks

| Script | Purpose |
|--------|---------|
| `pre_push.py` | Pre-push validation |
| `post_commit.py` | Post-commit actions |

### ci/ - CI/CD Scripts

| Script | Purpose |
|--------|---------|
| *(planned)* | Build, test, release automation |

---

## Usage

```bash
# Development setup
python scripts/dev/setup_dev.py

# Validate knowledge base
python scripts/check/validate_knowledge.py

# Install git hooks
cp scripts/hooks/*.py .git/hooks/
```

---

## Related

- `tools/` — Runtime tools (analyzers, checkers, converters, generators, monitors)
- `.knowledge/scripts/` — Knowledge base maintenance scripts
- `docs/design/architecture/DIRECTORY_LAYOUT.md` — Directory structure reference

---

*AI Collaboration Knowledge Base*
