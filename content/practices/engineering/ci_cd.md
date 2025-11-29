# CI/CD Practices

> Continuous Integration and Continuous Deployment best practices for SAGE projects

---

## Table of Contents

[1. Overview](#1-overview) · [2. GitHub Actions](#2-github-actions) · [3. Pipeline Stages](#3-pipeline-stages) · [4. Testing Strategy](#4-testing-strategy) · [5. Deployment](#5-deployment) · [6. Monitoring](#6-monitoring)

---

## 1. Overview

### 1.1 CI/CD Principles

| Principle | Description |
|-----------|-------------|
| **Automate Everything** | Manual steps introduce errors and delays |
| **Fail Fast** | Catch issues early in the pipeline |
| **Build Once, Deploy Many** | Same artifact across environments |
| **Version Everything** | Code, configs, infrastructure |
| **Keep Pipelines Fast** | Target < 10 minutes for CI |

### 1.2 Pipeline Overview

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Lint   │───▶│  Test   │───▶│  Build  │───▶│ Publish │───▶│ Deploy  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  Ruff/MyPy    pytest        wheel/docker    PyPI/GHCR     staging/prod
```

---

## 2. GitHub Actions

### 2.1 Basic CI Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install ruff mypy
      
      - name: Run Ruff
        run: ruff check src/
      
      - name: Run MyPy
        run: mypy src/

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: coverage.xml

  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Build package
        run: |
          pip install build
          python -m build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/
```

### 2.2 Release Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Build package
        run: |
          pip install build
          python -m build
      
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
      
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
          generate_release_notes: true
```

### 2.3 Docker Build Workflow

```yaml
# .github/workflows/docker.yml
name: Docker

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=semver,pattern={{version}}
            type=sha
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## 3. Pipeline Stages

### 3.1 Lint Stage

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Ruff** | Linting & formatting | `pyproject.toml` |
| **MyPy** | Type checking | `pyproject.toml` |
| **Pre-commit** | Git hooks | `.pre-commit-config.yaml` |

```yaml
# Pre-commit configuration
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        additional_dependencies: [types-PyYAML]
```

### 3.2 Test Stage

| Test Type | Tools | Target |
|-----------|-------|--------|
| **Unit** | pytest | > 80% coverage |
| **Integration** | pytest-asyncio | Critical paths |
| **E2E** | pytest | User workflows |
| **Performance** | pytest-benchmark | Regression detection |

```yaml
# pytest configuration in pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
addopts = [
    "--strict-markers",
    "--cov=src",
    "--cov-report=term-missing",
]
```

### 3.3 Build Stage

**Python Package**:
```bash
pip install build
python -m build
# Creates dist/sage-kb-*.whl and dist/sage-kb-*.tar.gz
```

**Docker Image**:
```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY pyproject.toml .
COPY src/ src/
RUN pip install build && python -m build --wheel

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/dist/*.whl .
RUN pip install *.whl && rm *.whl
EXPOSE 8000
CMD ["sage", "serve"]
```

---

## 4. Testing Strategy

### 4.1 Test Pyramid

```
        ┌───────────┐
        │    E2E    │  Few, slow, high confidence
        ├───────────┤
        │Integration│  Some, medium speed
        ├───────────┤
        │   Unit    │  Many, fast, isolated
        └───────────┘
```

### 4.2 Test Organization

```
tests/
├── unit/              # Fast, isolated tests
│   ├── core/
│   ├── services/
│   └── conftest.py
├── integration/       # Component interaction tests
│   ├── test_mcp_server.py
│   └── test_api.py
├── e2e/              # End-to-end workflows
│   └── test_cli.py
├── performance/      # Benchmarks
│   └── benchmarks/
└── conftest.py       # Shared fixtures
```

### 4.3 Test Markers

```python
import pytest

@pytest.mark.unit
def test_parser_basic():
    """Fast unit test."""
    pass

@pytest.mark.integration
def test_mcp_connection():
    """Integration test requiring setup."""
    pass

@pytest.mark.slow
def test_full_kb_load():
    """Slow test, skip in CI fast mode."""
    pass

@pytest.mark.asyncio
async def test_async_handler():
    """Async test with pytest-asyncio."""
    pass
```

---

## 5. Deployment

### 5.1 Environment Strategy

| Environment | Purpose | Trigger |
|-------------|---------|---------|
| **Development** | Local testing | Manual |
| **Staging** | Pre-production validation | Push to `develop` |
| **Production** | Live system | Tag `v*` |

### 5.2 Deployment Checklist

- [ ] All tests pass
- [ ] Security scan completed
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Rollback plan ready

### 5.3 Rollback Strategy

```yaml
# Quick rollback via tags
jobs:
  rollback:
    runs-on: ubuntu-latest
    steps:
      - name: Rollback to previous version
        run: |
          # Get previous tag
          PREV_TAG=$(git describe --abbrev=0 --tags HEAD^)
          # Deploy previous version
          kubectl set image deployment/app app=ghcr.io/org/app:$PREV_TAG
```

---

## 6. Monitoring

### 6.1 Pipeline Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| CI Duration | < 10 min | > 15 min |
| Test Coverage | > 80% | < 75% |
| Build Success Rate | > 95% | < 90% |
| Deploy Frequency | Daily | < Weekly |

### 6.2 Notifications

```yaml
# Slack notification on failure
- name: Notify Slack
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "CI Failed: ${{ github.repository }}",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Build Failed*\n${{ github.event.head_commit.message }}"
            }
          }
        ]
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

---

## Quick Commands

```bash
# Run CI locally
make lint test build

# Test specific stage
pytest tests/unit -v
pytest tests/integration -v --slow

# Build package
python -m build

# Build Docker image
docker build -t sage-kb .

# Run pre-commit hooks
pre-commit run --all-files
```

---

## Related

- `practices/engineering/git_workflow.md` — Git workflow
- `practices/engineering/testing_strategy.md` — Testing practices
- `scenarios/devops/context.md` — DevOps scenario context
- `templates/runbook.md` — Operational runbook template

---

*Part of SAGE Knowledge Base*
