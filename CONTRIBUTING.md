# Contributing to SAGE Knowledge Base

Thank you for your interest in contributing to SAGE Knowledge Base! This document provides guidelines and instructions for contributing.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Documentation](#documentation)
- [Testing](#testing)
- [Review Process](#review-process)

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. We follow the principles of 信达雅 (Xin-Da-Ya):

- **信 (Faithfulness)**: Be honest, accurate, and reliable in your contributions
- **达 (Clarity)**: Communicate clearly and make your code accessible
- **雅 (Elegance)**: Strive for refined, balanced, and sustainable solutions

---

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git
- A GitHub account

### Finding Issues

- Check [Issues](https://github.com/HengYangDS/sage-kb/issues) for open tasks
- Look for issues labeled `good first issue` for beginner-friendly tasks
- Issues labeled `help wanted` are actively seeking contributors

### Types of Contributions

| Type | Description | Label |
|------|-------------|-------|
| Bug Fix | Fix existing issues | `bug` |
| Feature | Add new functionality | `enhancement` |
| Documentation | Improve docs | `documentation` |
| Knowledge Content | Add to knowledge base | `content` |
| Tests | Add or improve tests | `testing` |

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/sage-kb.git
cd sage-kb

# Add upstream remote
git remote add upstream https://github.com/HengYangDS/sage-kb.git
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Unix/macOS)
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Or use the setup script
python -m tools.dev_scripts.setup_dev
```

### 3. Verify Setup

```bash
# Run tests
pytest tests/ -v

# Run linting
ruff check .

# Run type checking
mypy src/
```

---

## Making Changes

### 1. Create a Branch

```bash
# Update your fork
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
# Or for bugs
git checkout -b fix/issue-description
```

### 2. Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/description` | `feature/add-search-filter` |
| Bug Fix | `fix/issue-description` | `fix/timeout-handling` |
| Documentation | `docs/description` | `docs/update-readme` |
| Refactor | `refactor/description` | `refactor/loader-module` |

### 3. Commit Messages

Follow conventional commits format:

```
type(scope): brief description

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:

```bash
feat(loader): add timeout configuration option

fix(cli): handle empty search results gracefully

docs(readme): update installation instructions

test(mcp): add integration tests for server
```

---

## Submitting Changes

### 1. Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Linting passes (`ruff check .`)
- [ ] Type checking passes (`mypy src/`)
- [ ] Documentation is updated if needed
- [ ] Commit messages follow convention

### 2. Create Pull Request

1. Push your branch to your fork
2. Open a Pull Request against `main`
3. Fill out the PR template
4. Link related issues

### 3. PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (describe)

## Related Issues
Fixes #123

## Testing
Describe testing performed

## Checklist
- [ ] Tests pass
- [ ] Linting passes
- [ ] Documentation updated
```

---

## Coding Standards

### Python Style

- **Formatter**: Ruff (line-length: 88)
- **Type Hints**: Required for all public functions
- **Docstrings**: Google style

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Files | `snake_case.py` | `timeout_manager.py` |
| Classes | `PascalCase` | `TimeoutLoader` |
| Functions | `snake_case` | `load_with_timeout` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT_MS` |
| Private | `_prefix` | `_internal_method` |

### Code Example

```python
"""Module description.

Detailed explanation if needed.
"""

from typing import Optional

from sage.core.protocols import LoaderProtocol


class ContentLoader:
    """Load content with timeout protection.
    
    Attributes:
        timeout_ms: Maximum time allowed for loading in milliseconds.
    """
    
    def __init__(self, timeout_ms: int = 5000) -> None:
        """Initialize loader.
        
        Args:
            timeout_ms: Timeout in milliseconds. Defaults to 5000.
        """
        self.timeout_ms = timeout_ms
    
    def load(self, path: str) -> Optional[str]:
        """Load content from path.
        
        Args:
            path: Path to content file.
            
        Returns:
            Content string if successful, None otherwise.
            
        Raises:
            TimeoutError: If loading exceeds timeout.
        """
        pass
```

---

## Documentation

### When to Update Documentation

- Adding new features
- Changing existing behavior
- Adding new configuration options
- Fixing documentation bugs

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
- Follow existing structure in target directory
- Include code examples where helpful
- Keep explanations concise but complete

---

## Testing

### Test Structure

```
tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
├── performance/    # Performance tests
└── fixtures/       # Test data
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Unit tests only
pytest tests/unit/ -v

# With coverage
pytest tests/ --cov=src/sage --cov-report=html

# Specific test file
pytest tests/unit/core/test_loader.py -v
```

### Writing Tests

```python
"""Tests for content loader."""

import pytest

from sage.core.loader import ContentLoader


class TestContentLoader:
    """Tests for ContentLoader class."""
    
    def test_load_valid_path(self, tmp_path):
        """Test loading content from valid path."""
        # Arrange
        content_file = tmp_path / "test.md"
        content_file.write_text("# Test Content")
        loader = ContentLoader()
        
        # Act
        result = loader.load(str(content_file))
        
        # Assert
        assert result == "# Test Content"
    
    def test_load_timeout(self):
        """Test timeout behavior."""
        loader = ContentLoader(timeout_ms=1)
        
        with pytest.raises(TimeoutError):
            loader.load("slow/path")
```

### Test Requirements

- All new features must have tests
- Bug fixes should include regression tests
- Maintain or improve test coverage
- Tests must pass in CI

---

## Review Process

### What Reviewers Look For

1. **Correctness**: Does the code work as intended?
2. **Style**: Does it follow project conventions?
3. **Testing**: Are there adequate tests?
4. **Documentation**: Is it properly documented?
5. **Performance**: Are there performance implications?

### Response Times

- Initial review: Within 3 business days
- Follow-up reviews: Within 2 business days

### Addressing Feedback

- Respond to all review comments
- Push fixes as new commits (don't force-push during review)
- Re-request review when ready

---

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues for similar questions

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

*Thank you for contributing to SAGE Knowledge Base!*
