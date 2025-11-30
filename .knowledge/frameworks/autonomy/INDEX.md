# Autonomy Framework

> AI autonomy levels and decision-making guidelines

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Documents](#2-documents)
- [3. Quick Reference](#3-quick-reference)
- [4. Framework Components](#4-framework-components)

---

## 1. Overview

The Autonomy Framework defines 6 levels (L1-L6) of AI autonomy for human-AI collaboration, ranging from minimal
autonomy (always ask) to full autonomy (act independently).

**Version**: 2.0 (2025-12-01)
**Last Review**: Expert Committee L3 - Conditional Approve

---

## 2. Documents

| Document    | Description                                 |
|-------------|---------------------------------------------|
| `LEVELS.md` | Complete 6-level autonomy framework (L1-L6) |

---

## 3. Quick Reference

| Level | Name        | Autonomy | Description                    |
|-------|-------------|----------|--------------------------------|
| L1    | Minimal     | 0-20%    | Always ask before any action   |
| L2    | Low         | 20-40%   | Ask for most decisions         |
| L3    | Medium      | 40-60%   | Balance asking and acting      |
| L4    | Medium-High | 60-80%   | Act, report after (default)    |
| L5    | High        | 80-95%   | High autonomy, minimal asking  |
| L6    | Full        | 95-100%  | Full autonomy for trusted work |

**Default Level**: L4 (Medium-High) for mature collaboration.

---

## 4. Framework Components

| Component | Section | Description |
|-----------|---------|-------------|
| Level Spectrum | §1-2 | 6-level definitions and details |
| Level Selection | §3 | Context-based recommendations |
| Calibration | §4 | Success rate adjustment rules |
| Override Conditions | §5 | Force lower/allow higher rules |
| Emergency Handling | §6 | Crisis response protocol |
| Audit & Observability | §7 | Logging, metrics, dashboards |
| Testing & Validation | §8 | Acceptance criteria and scenarios |
| Adoption Path | §9 | Team maturity and progressive adoption |
| Implementation | §10 | Configuration and reporting |

---

## Related

- `.context/intelligence/calibration/CALIBRATION.md` — Autonomy calibration settings
- `config/capabilities/autonomy.yaml` — Autonomy configuration
- `.junie/GUIDELINES.md` — AI collaboration guidelines
- `.knowledge/practices/decisions/AUTONOMY_CASES.md` — Concrete decision examples
- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Review framework

---

*AI Autonomy Framework v2.0*
