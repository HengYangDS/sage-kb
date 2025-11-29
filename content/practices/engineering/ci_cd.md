# CI/CD Practices

> Continuous Integration and Continuous Deployment configuration and best practices

---

## Table of Contents

[1. Overview](#1-overview) · [2. GitHub Actions](#2-github-actions) · [3. Pipeline Stages](#3-pipeline-stages) · [4. Testing Strategy](#4-testing-strategy) · [5. Deployment](#5-deployment) · [6. Best Practices](#6-best-practices)

---

## 1. Overview

### 1.1 CI/CD Philosophy

| Principle | Description |
|-----------|-------------|
| **Automate Everything** | Manual steps are error-prone |
| **Fail Fast** | Catch issues early in pipeline |
| **Keep It Fast** | Target < 10 min for CI pipeline |
| **Reproducible** | Same input = same output |
| **Secure** | Never expose secrets in logs |

### 1.2 Pipeline Overview

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Lint   │ → │  Test   │ → │  Build  │ → │ Deploy  │ → │ Monitor │
│         │    │         │    │         │    │ Staging │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                  │
                                                  ↓
                                            ┌─────────┐
                                            │ Deploy  │
                                            │  Prod   │
                                            └─────────┘
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
    branches: [main, develop]

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
      
      - name: Run ruff
        run: ruff check src/
      
      - name: Run mypy
        run: mypy src/sage/

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/ -v --cov=src/sage --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: coverage.xml
```

### 2.2 Matrix Testing

```yaml
# .github/workflows/test-matrix.yml
name: Test Matrix

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.11', '3.12', '3.13']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: pip install -e ".[dev]"
      
      - name: Run tests
        run: pytest tests/ -v
```

### 2.3 Release Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Install build tools
        run: pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_TOKEN }}
        run: twine upload dist/*

  docker:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
      
      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.ref_name }}
            ghcr.io/${{ github.repository }}:latest
```

---

## 3. Pipeline Stages

### 3.1 Lint Stage

| Check | Tool | Purpose |
|-------|------|---------|
| Code style | `ruff check` | Enforce style guidelines |
| Formatting | `ruff format --check` | Verify formatting |
| Type hints | `mypy` | Static type checking |
| Security | `bandit` | Security vulnerability scan |
| Dependencies | `safety` | Check for vulnerable packages |

```yaml
lint:
  steps:
    - run: ruff check src/ tests/
    - run: ruff format --check src/ tests/
    - run: mypy src/sage/
    - run: bandit -r src/
    - run: safety check
```

### 3.2 Test Stage

| Test Type | Scope | Timeout |
|-----------|-------|---------|
| Unit | Individual functions | 5 min |
| Integration | Component interactions | 10 min |
| E2E | Full system | 15 min |
| Performance | Benchmarks | 10 min |

```yaml
test:
  steps:
    # Unit tests (fast, run first)
    - name: Unit tests
      run: pytest tests/unit/ -v --timeout=300
    
    # Integration tests
    - name: Integration tests
      run: pytest tests/integration/ -v --timeout=600
    
    # Performance tests (optional)
    - name: Performance tests
      if: github.ref == 'refs/heads/main'
      run: pytest tests/performance/ -v --benchmark-only
```

### 3.3 Build Stage

```yaml
build:
  steps:
    - name: Build Python package
      run: python -m build
    
    - name: Build documentation
      run: mkdocs build
    
    - name: Build Docker image
      run: docker build -t sage-kb .
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v4
      with:
        name: dist
        path: dist/
```

### 3.4 Deploy Stage

```yaml
deploy-staging:
  environment: staging
  steps:
    - name: Deploy to staging
      run: |
        # Deploy commands
        echo "Deploying to staging..."

deploy-production:
  environment: production
  needs: deploy-staging
  if: github.ref == 'refs/heads/main'
  steps:
    - name: Deploy to production
      run: |
        # Production deploy commands
        echo "Deploying to production..."
```

---

## 4. Testing Strategy

### 4.1 Test Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
addopts = """
    -v
    --strict-markers
    --cov=src/sage
    --cov-report=term-missing
    --cov-report=xml
"""
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
```

### 4.2 Coverage Requirements

| Layer | Minimum | Target |
|-------|---------|--------|
| Core | 90% | 95% |
| Services | 80% | 90% |
| Capabilities | 80% | 85% |
| Overall | 85% | 90% |

```yaml
- name: Check coverage
  run: |
    coverage report --fail-under=85
```

### 4.3 Test Parallelization

```yaml
test:
  strategy:
    matrix:
      test-group: [unit, integration, e2e]
  steps:
    - name: Run ${{ matrix.test-group }} tests
      run: pytest tests/${{ matrix.test-group }}/ -v
```

---

## 5. Deployment

### 5.1 Environment Configuration

| Environment | Branch | Auto-Deploy | Approval |
|-------------|--------|-------------|----------|
| Development | Any PR | Yes | No |
| Staging | `develop` | Yes | No |
| Production | `main` | No | Required |

### 5.2 Secrets Management

```yaml
# Use GitHub secrets
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}

# Use environment-specific secrets
jobs:
  deploy:
    environment: production
    env:
      API_KEY: ${{ secrets.PROD_API_KEY }}
```

### 5.3 Rollback Strategy

```yaml
deploy:
  steps:
    - name: Deploy with rollback capability
      run: |
        # Save current version for rollback
        CURRENT_VERSION=$(get-current-version)
        
        # Deploy new version
        deploy-new-version || {
          echo "Deploy failed, rolling back..."
          rollback-to $CURRENT_VERSION
          exit 1
        }
```

---

## 6. Best Practices

### 6.1 Pipeline Optimization

| Technique | Benefit |
|-----------|---------|
| **Caching** | Faster dependency installation |
| **Parallelization** | Reduced total time |
| **Fail fast** | Quick feedback on failures |
| **Incremental builds** | Only rebuild changed parts |
| **Artifact reuse** | Don't rebuild between stages |

```yaml
# Caching example
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

### 6.2 Security Practices

| Practice | Implementation |
|----------|----------------|
| **Secret scanning** | Enable GitHub secret scanning |
| **Dependency audit** | Run `pip-audit` in CI |
| **SAST** | Use `bandit` for Python |
| **Container scanning** | Scan Docker images |
| **Least privilege** | Minimal permissions for tokens |

### 6.3 Monitoring and Alerting

```yaml
# Notify on failure
- name: Notify Slack on failure
  if: failure()
  uses: slackapi/slack-github-action@v1
  with:
    channel-id: 'ci-alerts'
    slack-message: 'CI failed on ${{ github.ref }}'
  env:
    SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
```

### 6.4 Documentation

| Document | Content |
|----------|---------|
| `CONTRIBUTING.md` | How to contribute |
| `RELEASING.md` | Release process |
| `.github/CODEOWNERS` | Review assignments |
| `.github/pull_request_template.md` | PR checklist |

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Flaky tests | Add retries, fix race conditions |
| Slow pipeline | Add caching, parallelize |
| Secret exposure | Use secret masking, audit logs |
| Build failures | Check dependencies, pin versions |
| Deploy failures | Add health checks, rollback |

### Debugging CI

```yaml
# Enable debug logging
- name: Debug step
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
  env:
    ACTIONS_STEP_DEBUG: true
```

---

## Related

- `practices/engineering/git_workflow.md` — Git workflow
- `practices/engineering/testing_strategy.md` — Testing strategy
- `content/scenarios/devops/context.md` — DevOps scenario

---

*Part of SAGE Knowledge Base*
