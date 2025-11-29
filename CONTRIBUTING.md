# Contributing to SAGE Knowledge Base

> Guidelines for contributing to the SAGE Knowledge Base project

Thank you for your interest in contributing to SAGE! This document provides guidelines and instructions for contributing.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Commit Messages](#commit-messages)
- [Issue Reporting](#issue-reporting)

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git
- pip or conda for package management

### Quick Start

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/sage-kb.git
cd sage-kb

# Set up development environment
python -m tools.dev_scripts.setup_dev

# Verify setup
python -m tools.dev_scripts.setup_dev --verify

# Run tests to ensure everything works
pytest tests/ -v
```

---

## Development Setup

### 1. Create Virtual Environment

```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Using conda
conda create -n sage python=3.12
conda activate sage
```

### 2. Install Dependencies

```bash
# Install all dependencies including dev tools
pip install -e ".[dev,mcp]"

# Or using the setup script
python -m tools.dev_scripts.setup_dev
```

### 3. Configure Pre-commit Hooks

```bash
pre-commit install
```

### 4. Verify Installation

```bash
# Run linting
ruff check src/ tests/

# Run type checking
mypy src/

# Run tests
pytest tests/ -v
```

---

## Making Changes

### 1. Create a Branch

```bash
# Sync with upstream
git fetch origin
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-description
```

### Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/description` | `feature/add-search-api` |
| Bug fix | `fix/description` | `fix/timeout-race-condition` |
| Documentation | `docs/description` | `docs/update-api-reference` |
| Refactor | `refactor/description` | `refactor/loader-module` |

### 2. Make Your Changes

- Follow the [Coding Standards](#coding-standards)
- Write tests for new functionality
- Update documentation as needed
- Keep changes focused and atomic

### 3. Test Your Changes

```bash
# Run full test suite
pytest tests/ -v

# Run specific test categories
pytest tests/unit/ -v
pytest tests/integration/ -v

# Run with coverage
pytest tests/ --cov=src/sage --cov-report=html
```

---

## Pull Request Process

### 1. Before Submitting

- [ ] All tests pass locally
- [ ] Code follows project style guidelines
- [ ] Documentation is updated
- [ ] Commit messages follow convention
- [ ] Branch is up to date with main

### 2. PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
Describe testing performed

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (for significant changes)
```

### 3. Review Process

1. Submit PR against `main` branch
2. Automated checks must pass (CI/CD)
3. At least one maintainer review required
4. Address review feedback
5. Squash and merge when approved

---

## Coding Standards

### Python Style

| Aspect | Standard |
|--------|----------|
| Formatter | Ruff (line-length: 88) |
| Type hints | Required for all public functions |
| Docstrings | Google style |
| Imports | Sorted by ruff (isort compatible) |

### Example Code

```python
"""Module description.

Detailed module documentation.
"""

from typing import Optional

from sage.core.models import KnowledgeItem


def process_item(
    item: KnowledgeItem,
    *,
    validate: bool = True,
    timeout_ms: int = 5000,
) -> Optional[str]:
    """Process a knowledge item.

    Args:
        item: The knowledge item to process.
        validate: Whether to validate the item. Defaults to True.
        timeout_ms: Timeout in milliseconds. Defaults to 5000.

    Returns:
        Processed content string, or None if processing fails.

    Raises:
        ValueError: If item is invalid and validate is True.
        TimeoutError: If processing exceeds timeout_ms.
    """
    if validate and not item.is_valid():
        raise ValueError(f"Invalid item: {item.id}")
    
    return item.content
```

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Files | `snake_case.py` | `timeout_manager.py` |
| Classes | `PascalCase` | `TimeoutLoader` |
| Functions | `snake_case` | `load_with_timeout` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT_MS` |
| Private | `_leading_underscore` | `_internal_method` |

---

## Testing Requirements

### Test Categories

| Category | Location | Purpose |
|----------|----------|---------|
| Unit | `tests/unit/` | Test individual components |
| Integration | `tests/integration/` | Test component interactions |
| Performance | `tests/performance/` | Test performance characteristics |

### Test Requirements

1. **New features** must have corresponding tests
2. **Bug fixes** should include regression tests
3. **Minimum coverage** for new code: 80%

### Test Example

```python
"""Tests for timeout manager."""

import pytest

from sage.core.timeout import TimeoutManager


class TestTimeoutManager:
    """Test suite for TimeoutManager."""

    def test_configure_valid_level(self) -> None:
        """Test configuring a valid timeout level."""
        manager = TimeoutManager()
        manager.configure(level="T3", timeout_ms=2000)
        
        assert manager.current_level == "T3"
        assert manager.timeout_ms == 2000

    def test_configure_invalid_level_raises(self) -> None:
        """Test that invalid level raises ValueError."""
        manager = TimeoutManager()
        
        with pytest.raises(ValueError, match="Invalid timeout level"):
            manager.configure(level="T99", timeout_ms=1000)

    @pytest.mark.asyncio
    async def test_async_operation_with_timeout(self) -> None:
        """Test async operation respects timeout."""
        manager = TimeoutManager()
        
        result = await manager.execute_with_timeout(
            async_operation(),
            timeout_ms=100,
        )
        
        assert result is not None
```

---

## Documentation

### When to Update Documentation

- Adding new features
- Changing existing behavior
- Fixing documentation bugs
- Improving clarity

### Documentation Locations

| Type | Location |
|------|----------|
| API Reference | `docs/api/` |
| User Guides | `docs/guides/` |
| Design Docs | `docs/design/` |
| Knowledge Content | `content/` |
| Project Context | `.context/` |

### Documentation Style

- Use Markdown format
- Follow existing document structure
- Include code examples where helpful
- Keep language clear and concise

---

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding/updating tests |
| `chore` | Maintenance tasks |

### Examples

```bash
# Feature
feat(loader): add smart caching for knowledge items

# Bug fix
fix(timeout): resolve race condition in async handler

# Documentation
docs(api): update MCP endpoint documentation

# With body and footer
feat(search): implement fuzzy search capability

Add fuzzy matching algorithm for knowledge search.
Supports configurable similarity threshold.

Closes #123
```

---

## Issue Reporting

### Bug Reports

Include:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Relevant logs or error messages

### Feature Requests

Include:
- Clear description of the feature
- Use case and motivation
- Proposed implementation (if any)
- Alternatives considered

### Issue Labels

| Label | Description |
|-------|-------------|
| `bug` | Something isn't working |
| `enhancement` | New feature request |
| `documentation` | Documentation improvement |
| `good first issue` | Good for newcomers |
| `help wanted` | Extra attention needed |

---

## Questions?

- Check existing [documentation](docs/)
- Search [existing issues](https://github.com/HengYangDS/sage-kb/issues)
- Open a new issue for questions

---

## Recognition

Contributors are recognized in:
- GitHub contributors list
- CHANGELOG.md for significant contributions
- Release notes

Thank you for contributing to SAGE Knowledge Base! 🎉

---

*Part of SAGE Knowledge Base*
