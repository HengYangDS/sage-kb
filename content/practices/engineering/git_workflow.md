# Git Workflow

> Best practices for version control with Git in SAGE projects

---

## Table of Contents

[1. Branch Strategy](#1-branch-strategy) · [2. Commit Conventions](#2-commit-conventions) · [3. Pull Request Process](#3-pull-request-process) · [4. Code Review Guidelines](#4-code-review-guidelines) · [5. Release Process](#5-release-process)

---

## 1. Branch Strategy

### 1.1 Branch Types

| Branch | Purpose | Naming | Lifetime |
|--------|---------|--------|----------|
| `main` | Production-ready code | - | Permanent |
| `develop` | Integration branch | - | Permanent |
| `feature/*` | New features | `feature/add-mcp-support` | Temporary |
| `bugfix/*` | Bug fixes | `bugfix/fix-timeout-issue` | Temporary |
| `hotfix/*` | Urgent production fixes | `hotfix/security-patch` | Temporary |
| `release/*` | Release preparation | `release/v1.2.0` | Temporary |

### 1.2 Branch Flow

```
main ─────●─────────────●─────────────●───────
          │             ↑             ↑
          │             │             │
develop ──●──●──●──●────●──●──●──●────●───────
             │  ↑  │       │  ↑
             │  │  │       │  │
feature/* ───●──●  │       ●──●
                   │
bugfix/* ──────────●
```

### 1.3 Branch Rules

- **main**: Protected, requires PR and review
- **develop**: Default branch for development
- **feature/bugfix**: Branch from `develop`, merge back to `develop`
- **hotfix**: Branch from `main`, merge to both `main` and `develop`

---

## 2. Commit Conventions

### 2.1 Conventional Commits

Format: `<type>(<scope>): <description>`

```
feat(mcp): add streaming response support
fix(cli): resolve timeout handling issue
docs(api): update MCP protocol documentation
refactor(core): simplify loader architecture
test(services): add integration tests for API
chore(deps): update dependencies
```

### 2.2 Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(cli): add export command` |
| `fix` | Bug fix | `fix(loader): handle empty files` |
| `docs` | Documentation | `docs: update README` |
| `style` | Formatting | `style: fix indentation` |
| `refactor` | Code restructure | `refactor: extract helper function` |
| `test` | Tests | `test: add unit tests for parser` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance | `perf: optimize file loading` |
| `ci` | CI/CD changes | `ci: add GitHub Actions workflow` |

### 2.3 Commit Message Guidelines

**Good commits**:
```
feat(mcp): implement tool registration protocol

- Add ToolRegistry class for managing tools
- Implement JSON-RPC message handling
- Add validation for tool schemas

Closes #123
```

**Bad commits**:
```
fix stuff
update
WIP
asdfgh
```

### 2.4 Commitizen Integration

```bash
# Install commitizen
pip install commitizen

# Interactive commit
cz commit

# Generate changelog
cz changelog
```

---

## 3. Pull Request Process

### 3.1 PR Checklist

- [ ] Branch is up-to-date with target branch
- [ ] All tests pass locally
- [ ] Code follows project style guidelines
- [ ] Documentation updated if needed
- [ ] Changelog entry added for user-facing changes
- [ ] No unresolved merge conflicts

### 3.2 PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

## Related Issues
Closes #(issue number)
```

### 3.3 PR Size Guidelines

| Size | Lines Changed | Review Time |
|------|---------------|-------------|
| XS | < 10 | Minutes |
| S | 10-50 | < 30 min |
| M | 50-200 | < 1 hour |
| L | 200-500 | < 2 hours |
| XL | > 500 | Split recommended |

---

## 4. Code Review Guidelines

### 4.1 Reviewer Responsibilities

- Understand the context and purpose
- Check for correctness and edge cases
- Verify test coverage
- Ensure code readability
- Suggest improvements constructively

### 4.2 Review Comments

**Good feedback**:
```
Consider using a context manager here to ensure the file is properly closed:

with open(path) as f:
    return f.read()
```

**Bad feedback**:
```
This is wrong.
```

### 4.3 Approval Criteria

- All CI checks pass
- At least one approval from maintainer
- No unresolved conversations
- No merge conflicts

---

## 5. Release Process

### 5.1 Semantic Versioning

Format: `MAJOR.MINOR.PATCH`

| Change | Version Bump | Example |
|--------|--------------|---------|
| Breaking changes | MAJOR | 1.0.0 → 2.0.0 |
| New features | MINOR | 1.0.0 → 1.1.0 |
| Bug fixes | PATCH | 1.0.0 → 1.0.1 |

### 5.2 Release Checklist

1. Create release branch: `release/vX.Y.Z`
2. Update version in `pyproject.toml`
3. Generate/update `CHANGELOG.md`
4. Run full test suite
5. Create PR to `main`
6. After merge, tag release: `git tag vX.Y.Z`
7. Push tag: `git push origin vX.Y.Z`

### 5.3 Changelog Format

```markdown
## [1.2.0] - 2025-11-29

### Added
- MCP streaming support (#123)
- New CLI export command (#124)

### Changed
- Improved timeout handling (#125)

### Fixed
- Memory leak in loader (#126)

### Deprecated
- Old configuration format (will be removed in 2.0)
```

---

## Quick Reference

```bash
# Start new feature
git checkout develop
git pull origin develop
git checkout -b feature/my-feature

# Commit changes
git add .
cz commit  # or: git commit -m "feat: description"

# Push and create PR
git push -u origin feature/my-feature

# Update branch with latest develop
git fetch origin
git rebase origin/develop

# After PR merged, cleanup
git checkout develop
git pull origin develop
git branch -d feature/my-feature
```

---

## Related

- `practices/engineering/code_review.md` — Code review practices
- `practices/engineering/ci_cd.md` — CI/CD pipeline configuration
- `templates/release_notes.md` — Release notes template

---

*Part of SAGE Knowledge Base*
