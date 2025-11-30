# Secrets Management Framework

> Conceptual framework for secure handling of sensitive data and credentials

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Secret Types](#2-secret-types)
- [3. Threat Model](#3-threat-model)
- [4. Storage Solutions](#4-storage-solutions)
- [5. Lifecycle Management](#5-lifecycle-management)
- [6. Integration Examples](#6-integration-examples)
- [7. Best Practices](#7-best-practices)

---

## 1. Overview

### What Are Secrets?

Secrets are sensitive data that must be protected from unauthorized access:

| Category               | Examples                                    |
|------------------------|---------------------------------------------|
| **Credentials**        | Passwords, API keys, tokens                 |
| **Keys**               | Encryption keys, SSH keys, TLS certificates |
| **Connection Strings** | Database URLs, service endpoints            |
| **Configuration**      | Sensitive settings, feature flags           |

---

## 2. Secret Types

### Classification

| Type                     | Sensitivity | Rotation Frequency | Example                  |
|--------------------------|-------------|--------------------|--------------------------|
| **API Keys**             | Medium      | Monthly-Quarterly  | Third-party service keys |
| **Database Credentials** | High        | Quarterly          | PostgreSQL password      |
| **Encryption Keys**      | Critical    | Annually           | AES master key           |
| **OAuth Secrets**        | High        | Quarterly          | Client secret            |
| **TLS Certificates**     | High        | Annually           | Server certificates      |
| **SSH Keys**             | High        | Annually           | Deployment keys          |
| **Tokens**               | Medium      | Short-lived        | JWT, session tokens      |

---

## 3. Threat Model

### Exposure Risks

| Vector          | Risk                                    |
|-----------------|-----------------------------------------|
| **Source Code** | Git history, public repos               |
| **Logs**        | Log files, monitoring systems           |
| **Environment** | Process dumps, container inspection     |
| **Memory**      | Core dumps, debugging                   |
| **Network**     | Man-in-the-middle, sniffing             |
| **Storage**     | Unencrypted disks, backups              |
| **Humans**      | Social engineering, shoulder surfing    |

---

## 4. Storage Solutions

### Comparison

| Solution                | Security | Ease of Use | Cost | Best For        |
|-------------------------|----------|-------------|------|-----------------|
| **Env Variables**       | Low      | High        | Free | Development     |
| **Config Files**        | Low      | High        | Free | Development     |
| **HashiCorp Vault**     | High     | Medium      | $$   | Enterprise      |
| **AWS Secrets Manager** | High     | High        | $    | AWS workloads   |
| **Azure Key Vault**     | High     | High        | $    | Azure workloads |
| **GCP Secret Manager**  | High     | High        | $    | GCP workloads   |

### Selection Criteria

| Environment  | Recommended Solution      |
|--------------|---------------------------|
| Development  | Environment variables     |
| CI/CD        | Platform secrets (GitHub, GitLab) |
| Production   | Secret manager (Vault, AWS SM) |

---

## 5. Lifecycle Management

### Secret Lifecycle

```
Generate → Store → Use → Rotate → Revoke
```
| Phase        | Requirements                          |
|--------------|---------------------------------------|
| **Generate** | Cryptographically secure random       |
| **Store**    | Encrypted at rest, access controlled  |
| **Use**      | Minimal exposure, short-lived access  |
| **Rotate**   | Automated, zero-downtime              |
| **Revoke**   | Immediate, audit logged               |

### Rotation Schedule

| Secret Type        | Frequency   | Automation |
|--------------------|-------------|------------|
| API Keys           | 90 days     | Required   |
| Database Passwords | 60 days     | Required   |
| Service Tokens     | 30 days     | Required   |
| Session Keys       | 24 hours    | Automatic  |
| Encryption Keys    | 1 year      | Planned    |

### Rotation Process

**Standard Rotation Flow**:

```
1. GENERATE    → Create new secret (cryptographically secure)
2. DEPLOY      → Push to secret manager (versioned)
3. UPDATE      → Update consuming services (rolling)
4. VERIFY      → Confirm services using new secret
5. DEPRECATE   → Mark old secret as deprecated
6. REVOKE      → Remove old secret after grace period
7. AUDIT       → Log rotation event with metadata
```

**Zero-Downtime Rotation Pattern**:

| Step | Action | Duration |
|------|--------|----------|
| 1 | Generate new secret, keep old active | Immediate |
| 2 | Deploy new secret to consumers | 5-15 min |
| 3 | Verify all consumers switched | 5 min |
| 4 | Revoke old secret | Immediate |

**Emergency Rotation Procedure**:

| Trigger | Action | Timeline |
|---------|--------|----------|
| Suspected compromise | Immediate rotation + revoke | < 15 min |
| Confirmed breach | Rotate all related secrets | < 1 hour |
| Routine rotation | Standard flow | Scheduled |

---

## 6. Integration Examples

### HashiCorp Vault Integration

```yaml
# vault-config.yaml
vault:
  address: "https://vault.example.com:8200"
  auth_method: kubernetes
  role: app-role
  secret_path: "secret/data/myapp"
  
  rotation:
    enabled: true
    schedule: "0 0 * * 0"  # Weekly
    notification: slack://alerts
```

### AWS Secrets Manager Integration

```yaml
# aws-secrets.yaml
secrets_manager:
  region: us-east-1
  secret_id: "prod/myapp/db-credentials"
  
  rotation:
    enabled: true
    rotation_lambda_arn: "arn:aws:lambda:..."
    automatically_after_days: 30
    
  retrieval:
    cache_ttl: 300  # 5 minutes
    version_stage: AWSCURRENT
```

### Kubernetes Secrets Integration

```yaml
# external-secrets.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: app-secrets
  data:
    - secretKey: DB_PASSWORD
      remoteRef:
        key: secret/data/myapp
        property: db_password
```

### CI/CD Integration Pattern

| Platform | Secret Source | Rotation Support |
|----------|---------------|------------------|
| GitHub Actions | GitHub Secrets, OIDC | Manual + Dependabot |
| GitLab CI | GitLab Variables, Vault | Manual + Scheduled |
| Jenkins | Credentials Plugin, Vault | Plugin-based |
| ArgoCD | External Secrets Operator | Automatic refresh |

---

## 7. Best Practices

### DO's and DON'Ts

| ✅ DO                       | ❌ DON'T                    |
|----------------------------|----------------------------|
| Use secrets manager        | Hardcode secrets           |
| Encrypt at rest            | Store in plain text        |
| Rotate regularly           | Use same secret forever    |
| Audit access               | Ignore access logs         |
| Use short-lived tokens     | Use long-lived credentials |
| Principle of least privilege | Grant broad access       |

### Access Control

| Principle                | Implementation              |
|--------------------------|-----------------------------|
| Least privilege          | Minimal necessary access    |
| Separation of duties     | Different secrets per role  |
| Need-to-know             | Access only when required   |
| Audit trail              | Log all secret access       |

---

## Related

- `.knowledge/practices/engineering/security/SECRETS_IMPLEMENTATION.md` — Implementation patterns and code
- `.knowledge/guidelines/SECURITY.md` — Security guidelines
- `.knowledge/frameworks/security/AUTHENTICATION.md` — Authentication patterns

---

*Secrets Management Framework v1.1*
*Updated: 2025-12-01 - Added rotation process details (§5.3) and integration examples (§6)*

---

*AI Collaboration Knowledge Base*
