# AI Autonomy Levels Framework

> 6-level autonomy spectrum for human-AI collaboration

---

## Table of Contents

- [1. Level Spectrum](#1-level-spectrum)
- [2. Level Details](#2-level-details)
- [3. Level Selection](#3-level-selection)
- [4. Calibration](#4-calibration)
- [5. Override Conditions](#5-override-conditions)
- [6. Emergency Handling](#6-emergency-handling)
- [7. Audit & Observability](#7-audit--observability)
- [8. Testing & Validation](#8-testing--validation)
- [9. Adoption Path](#9-adoption-path)
- [10. Implementation](#10-implementation)

---

## 1. Level Spectrum

| Level  | Name        | Range   | Behavior                       |
|--------|-------------|---------|--------------------------------|
| **L1** | Minimal     | 0-20%   | Ask before all changes         |
| **L2** | Low         | 20-40%  | Ask before significant changes |
| **L3** | Medium      | 40-60%  | Proceed routine, ask novel     |
| **L4** | Medium-High | 60-80%  | Proceed, report after          |
| **L5** | High        | 80-95%  | High autonomy, minimal checks  |
| **L6** | Full        | 95-100% | Full autonomy                  |

---

## 2. Level Details

### 2.1 L1-L2: Low Autonomy

| Aspect   | L1                | L2              |
|----------|-------------------|-----------------|
| Changes  | Ask all           | Ask significant |
| Scope    | Minimal           | Small           |
| Use case | New collaboration | Sensitive tasks |

### 2.2 L3-L4: Medium Autonomy

| Aspect    | L3                       | L4              |
|-----------|--------------------------|-----------------|
| Changes   | Routine proceed          | Most proceed    |
| Reporting | Ask novel                | Report after    |
| Use case  | Established relationship | Trusted routine |

#### L3 vs L4 Decision Tree

```
Is the task routine AND well-understood?
├─ NO  → L3: Ask before proceeding
└─ YES → Has similar task succeeded 3+ times?
         ├─ NO  → L3: Ask before proceeding
         └─ YES → Is outcome easily reversible?
                  ├─ NO  → L3: Ask before proceeding
                  └─ YES → Does it affect shared/critical code?
                           ├─ YES → L3: Ask before proceeding
                           └─ NO  → Is there existing test coverage?
                                    ├─ NO  → L3: Ask before proceeding
                                    └─ YES → L4: Proceed, report after
```

#### Extended Decision Matrix

| Factor | L3 (Ask Novel) | L4 (Report After) |
|--------|----------------|-------------------|
| **Familiarity** | First time or rare | Done 3+ times successfully |
| **Reversibility** | Hard to undo | Easy to revert |
| **Scope** | Multiple files/modules | Single file/localized |
| **Impact** | Affects shared code | Isolated changes |
| **Coverage** | No/low test coverage | Good test coverage |
| **Environment** | Production/staging | Development/sandbox |
| **Complexity** | Novel logic/pattern | Known pattern |

#### Concrete Examples

| Scenario      | L3 (Ask Novel)                 | L4 (Report After)              |
|---------------|--------------------------------|--------------------------------|
| Code refactor | New pattern, unfamiliar module | Same pattern, familiar module  |
| Config change | New service, production        | Known service, dev/staging     |
| Documentation | New structure, API docs        | Typo fix, existing format      |
| Testing       | New test framework             | Adding tests to existing suite |
| Dependencies  | Major version upgrade          | Patch version update           |
| Bug fix       | Root cause unclear             | Clear fix, known issue type    |
| Feature       | New user-facing behavior       | Internal improvement           |
| Database      | Schema change                  | Query optimization (read-only) |

#### Boundary Cases (Gray Zone)

These cases require judgment—default to L3 when uncertain:

| Situation | Factors Favoring L3 | Factors Favoring L4 | Recommendation |
|-----------|---------------------|---------------------|----------------|
| Familiar pattern, unfamiliar codebase | New context risk | Pattern confidence | **L3** |
| Known codebase, new pattern | Pattern unfamiliarity | Context familiarity | **L3** |
| Minor change to critical path | Critical impact | Small change | **L3** |
| Large change to non-critical code | Change size | Low risk area | **L4** with detailed report |
| Refactor with good tests | Complexity | Safety net | **L4** |
| Simple change, no tests | Low complexity | No safety net | **L3** |

#### Quick Reference: L3 or L4?

```
L3 if ANY of these are true:
□ First time doing this type of task
□ Involves production environment
□ Changes shared/core code
□ No test coverage for affected area
□ Outcome hard to reverse
□ Uncertain about approach

L4 if ALL of these are true:
□ Done similar task 3+ times successfully
□ Development/sandbox environment OR well-tested
□ Changes are localized
□ Good test coverage exists
□ Easy to revert if needed
□ Confident in approach
```

### 2.3 L5-L6: High Autonomy

| Aspect   | L5              | L6               |
|----------|-----------------|------------------|
| Changes  | Most autonomous | Fully autonomous |
| Checks   | Minimal         | None             |
| Use case | Expert tasks    | Full delegation  |

---

## 3. Level Selection

| Context              | Recommended Level |
|----------------------|-------------------|
| New collaboration    | L2-L3             |
| Established trust    | L4-L5             |
| Production/sensitive | L1-L2             |
| Routine tasks        | L4-L5             |
| Sandbox/dev          | L5-L6             |
| Critical systems     | L1-L2             |

---

## 4. Calibration

### 4.1 Adjustment Rules

| Success Rate | Action               |
|--------------|----------------------|
| > 95%        | Upgrade +1 (max L5)  |
| 85-95%       | Maintain current     |
| 70-85%       | Downgrade -1         |
| < 70%        | Downgrade -2, review |

### 4.2 Reset Triggers

- Major errors or failures
- New problem domain
- Team composition change
- Extended absence (> 2 weeks)

---

## 5. Override Conditions

| Force Lower (L1-L2)    | Allow Higher (L5-L6)    |
|------------------------|-------------------------|
| Production deployments | Explicitly granted      |
| Database migrations    | Routine + well-tested   |
| Security-sensitive ops | Sandbox environments    |
| Irreversible actions   | Pipelines with rollback |
| Regulatory compliance  |                         |

---

## 6. Emergency Handling

### 6.1 Emergency Triggers

| Trigger              | Description                            | Action   |
|----------------------|----------------------------------------|----------|
| Security incident    | Detected breach, vulnerability exploit | Force L1 |
| Production outage    | Service down, critical errors          | Force L1 |
| Data breach          | Unauthorized data access/leak          | Force L1 |
| Compliance violation | Regulatory requirement breach          | Force L1 |
| Safety concern       | Risk to users or systems               | Force L1 |

### 6.2 Emergency Protocol

```yaml
emergency:
  triggers:
    - security_incident
    - production_outage
    - data_breach
    - compliance_violation
    - safety_concern
  action: force_L1
  notification: immediate
  escalation:
    - notify_human_immediately
    - halt_autonomous_actions
    - await_explicit_approval
  recovery:
    - incident_resolved: return_to_previous_level
    - require_review: downgrade_one_level
```

### 6.3 Post-Emergency Review

| Step | Action                                | Timeline        |
|------|---------------------------------------|-----------------|
| 1    | Document incident and AI actions      | Within 1 hour   |
| 2    | Review autonomy level appropriateness | Within 24 hours |
| 3    | Adjust calibration if needed          | Within 48 hours |
| 4    | Update override conditions            | Within 1 week   |

---

## 7. Audit & Observability

### 7.1 Audit Log Requirements

| Level | Logging Required    | Retention |
|-------|---------------------|-----------|
| L1-L3 | Optional            | 30 days   |
| L4    | Required            | 60 days   |
| L5-L6 | Required + detailed | 90 days   |

### 7.2 Audit Log Schema

```yaml
audit_log:
  required_fields:
    - timestamp: ISO 8601 datetime
    - autonomy_level: L1-L6
    - action_type: create|modify|delete|execute
    - action_description: string
    - outcome: success|failure|partial
    - user_override: boolean
    - override_reason: string (if applicable)
  optional_fields:
    - affected_files: list
    - risk_assessment: low|medium|high
    - rollback_available: boolean
```

### 7.3 Observability Metrics

| Metric                        | Description                  | Alert Threshold     |
|-------------------------------|------------------------------|---------------------|
| `autonomy_level_distribution` | Current level usage          | N/A (informational) |
| `override_frequency`          | User overrides per day       | > 5/day             |
| `calibration_accuracy`        | Predicted vs actual success  | < 80%               |
| `decision_reversal_rate`      | Decisions requiring rollback | > 10%               |
| `emergency_trigger_count`     | Emergency events             | Any occurrence      |

### 7.4 Dashboard Recommendations

```
┌─────────────────────────────────────────────────────┐
│  AUTONOMY DASHBOARD                                 │
├─────────────────────────────────────────────────────┤
│  Current Level: L4 (Medium-High)                    │
│  Success Rate (30d): 92%                            │
│  Override Count (7d): 2                             │
│  Last Emergency: None                               │
├─────────────────────────────────────────────────────┤
│  Level Distribution   │  Calibration Trend          │
│  L1: ██ 5%            │  ────────────────           │
│  L2: ███ 10%          │       ╱‾‾‾‾‾‾               │
│  L3: █████ 20%        │      ╱                      │
│  L4: ██████████ 45%   │  ───╱─────────────          │
│  L5: █████ 18%        │  Target: 85%                │
│  L6: ██ 2%            │  Current: 92%               │
└─────────────────────────────────────────────────────┘
```

### 7.5 Dashboard Components Specification

| Component | Data Source | Update Frequency | Visualization |
|-----------|-------------|------------------|---------------|
| Current Level | Session state | Real-time | Badge/indicator |
| Success Rate | Audit logs | Hourly | Percentage + trend |
| Override Count | Audit logs | Daily | Counter + sparkline |
| Level Distribution | Audit logs | Daily | Bar chart |
| Calibration Trend | Calibration events | Per calibration | Line chart |
| Emergency Status | Emergency logs | Real-time | Alert banner |

### 7.6 Data Collection Requirements

```yaml
data_collection:
  events:
    - type: autonomy_decision
      fields: [timestamp, level, action, outcome, duration_ms]
      retention: 90_days
      
    - type: level_change
      fields: [timestamp, from_level, to_level, reason, trigger]
      retention: 180_days
      
    - type: user_override
      fields: [timestamp, original_level, override_level, reason]
      retention: 180_days
      
    - type: emergency_trigger
      fields: [timestamp, trigger_type, previous_level, actions_halted]
      retention: 365_days

  aggregations:
    - name: daily_success_rate
      formula: successful_decisions / total_decisions
      granularity: daily
      
    - name: level_distribution
      formula: count_by_level / total_count
      granularity: daily
      
    - name: calibration_accuracy
      formula: correct_predictions / total_predictions
      granularity: weekly
```

### 7.7 Alert Configuration

| Alert | Condition | Severity | Action |
|-------|-----------|----------|--------|
| High Override Rate | > 5 overrides/day for 3 consecutive days | Warning | Review level settings |
| Low Success Rate | < 80% success rate (7-day rolling) | Warning | Consider downgrade |
| Calibration Drift | Accuracy dropped > 10% from baseline | Warning | Recalibrate |
| Emergency Triggered | Any emergency event | Critical | Immediate notification |
| Prolonged L1 | L1 for > 24 hours non-emergency | Info | Review if upgrade possible |

```yaml
alerts:
  high_override_rate:
    condition: "override_count_3d > 15"
    severity: warning
    channels: [dashboard, email]
    
  low_success_rate:
    condition: "success_rate_7d < 0.80"
    severity: warning
    channels: [dashboard, email]
    
  emergency_triggered:
    condition: "emergency_event == true"
    severity: critical
    channels: [dashboard, email, slack]
    escalation: immediate
```

---

## 8. Testing & Validation

### 8.1 Validation Methods

| Method                   | Purpose                         | Frequency |
|--------------------------|---------------------------------|-----------|
| Level selection accuracy | Verify correct level assignment | Weekly    |
| Calibration convergence  | Confirm calibration stabilizes  | Monthly   |
| Override effectiveness   | Assess override rule quality    | Quarterly |
| A/B testing              | Compare autonomy configurations | As needed |

### 8.2 Acceptance Criteria

| Criteria                 |     Target     |    Minimum     |
|--------------------------|:--------------:|:--------------:|
| Level selection accuracy |     > 90%      |     > 85%      |
| Calibration convergence  | < 10 decisions | < 20 decisions |
| False positive overrides |      < 5%      |     < 10%      |
| User satisfaction        |    > 4.0/5     |    > 3.5/5     |

### 8.3 Test Scenarios

```yaml
test_scenarios:
  level_selection:
    - scenario: "New collaboration, routine task"
      expected: L2-L3
    - scenario: "Established trust, sensitive data"
      expected: L2-L3
    - scenario: "Expert task, sandbox environment"
      expected: L5-L6

  calibration:
    - scenario: "5 consecutive successes"
      expected: upgrade_considered
    - scenario: "2 failures in 5 attempts"
      expected: downgrade_one_level

  emergency:
    - scenario: "Security alert triggered"
      expected: immediate_L1_enforcement
```

### 8.4 Validation Checklist

- [ ] Level definitions match actual behavior
- [ ] Calibration rules converge within expected decisions
- [ ] Override conditions trigger correctly
- [ ] Emergency handling activates immediately
- [ ] Audit logs capture required fields
- [ ] Metrics dashboard displays accurately

---

## 9. Adoption Path

### 9.1 Team Maturity Assessment

| Maturity Level | Characteristics                    | Max Autonomy |
|----------------|------------------------------------|:------------:|
| **Novice**     | New to AI collaboration, < 1 month |      L3      |
| **Developing** | Some experience, 1-3 months        |      L4      |
| **Proficient** | Established patterns, 3-6 months   |      L5      |
| **Expert**     | Deep trust, > 6 months             |      L6      |

### 9.2 Progressive Adoption

| Phase       | Duration | Starting Level | Target Level | Focus                |
|-------------|----------|:--------------:|:------------:|----------------------|
| **Phase 1** | Week 1-2 |       L2       |      L2      | Build understanding  |
| **Phase 2** | Week 3-4 |       L2       |      L3      | Establish patterns   |
| **Phase 3** | Month 2  |       L3       |    L3-L4     | Validate calibration |
| **Phase 4** | Month 3+ |       L4       |    L4-L5     | Optimize efficiency  |

### 9.3 Adoption Checklist

| Milestone        | Criteria                       | Action                |
|------------------|--------------------------------|-----------------------|
| Week 1 complete  | 10+ successful L2 interactions | Review patterns       |
| Month 1 complete | Success rate > 85%             | Consider L3 upgrade   |
| Month 2 complete | Calibration stable             | Enable L4 for routine |
| Quarter complete | Full validation passed         | Enable L5 for trusted |

### 9.4 Team Configuration Template

```yaml
team_autonomy:
  team_name: "Example Team"
  maturity: developing
  default_level: L3
  max_level: L4

  member_overrides:
    - member: "senior_dev"
      max_level: L5
      reason: "6+ months experience"

  domain_limits:
    - domain: "production"
      max_level: L2
    - domain: "security"
      max_level: L2
    - domain: "development"
      max_level: L5
```

---

## 10. Implementation

### 10.1 Setting Level

```yaml
# In task context
autonomy:
  level: L4
  reason: "Established trust, routine refactoring"
```

### 10.2 Reporting Format

| Level | Report Style            |
|-------|-------------------------|
| L1-L2 | Detailed, before action |
| L3-L4 | Summary, after action   |
| L5-L6 | Minimal, on completion  |

---

**Golden Rule**: Start conservative (L2-L3), increase gradually based on demonstrated success.

---

## Related

- `.knowledge/core/QUICK_REFERENCE.md` — Quick autonomy reference
- `.knowledge/practices/decisions/AUTONOMY_CASES.md` — Concrete examples
- `.knowledge/guidelines/AI_COLLABORATION.md` — Collaboration guidelines
- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Expert Committee Framework (review method)

---

*AI Autonomy Levels Framework v2.1*
*Updated: 2025-12-01 - Added observability specs (§7.5-7.7), L3-L4 boundary refinement*
*Last reviewed: 2025-12-01 by Expert Committee (L3, Conditional Approve)*

---

*AI Collaboration Knowledge Base*
