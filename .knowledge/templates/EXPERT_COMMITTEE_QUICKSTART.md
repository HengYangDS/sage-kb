# Expert Committee Quick-Start Guide

> Get started in 5-10 minutes. No prior knowledge required. **AI completes all calculations.**

---

## 🎯 Core Concept (30 seconds)

**What**: A structured way to make decisions using multiple expert perspectives.

**Why**: Avoid blind spots, reduce bias, increase confidence.

**How**: Collect independent scores → AI calculates result → Make decision.

```
┌─────────────────────────────────────────────────────────┐
│  YOU: Provide scores     AI: Calculates everything      │
│  ─────────────────────   ───────────────────────────    │
│  • Select level          • Weighted average             │
│  • Choose experts        • Standard deviation           │
│  • Collect scores        • Confidence interval          │
│  • Record concerns       • Information sufficiency      │
│                          • Final recommendation         │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 5-Step Quick Start

### Step 1: Select Level (30 seconds)

| Decision Type | Level | Experts | Time |
|---------------|:-----:|:-------:|------|
| Bug fix, config change | **L1** | 2-3 | 15 min |
| Minor feature | **L2** | 4-6 | 30 min |
| Refactoring, new tech | **L3** | 7-10 | 1 hour |
| Architecture change | **L4** | 11-15 | 2-3 hours |
| Platform, security | **L5** | 16-23 | Half day |

**Quick Rule**: Easy to undo? → L1-L2. Cross-team? → L3+. Strategic? → L5.

### Step 2: Assemble Panel (1 minute)

| Level | Required Experts |
|:-----:|------------------|
| L1 | Engineer + QA |
| L2 | + Architect + PM |
| L3 | + DevOps + Security |
| L4 | + Data + Domain experts |
| L5 | Full 23-expert committee |

### Step 3: Collect Independent Scores (2-5 minutes)

**⚠️ CRITICAL**: Each expert scores **independently** (1-5). Do NOT show others' scores!

| Score | Meaning | Action |
|:-----:|---------|--------|
| 5 | Excellent | Proceed |
| 4 | Good | Minor improvements |
| 3 | Acceptable | Address concerns |
| 2 | Poor | Significant changes |
| 1 | Failing | Do not proceed |

### Step 4: Let AI Calculate (1 minute)

Simply provide your data to AI in this format:

```
Decision: [What you're deciding]
Level: [L1-L5]
Expert Scores:
- [Expert Role] ([High/Medium/Low] weight): [Score] - [Any concerns]
- [Expert Role] ([High/Medium/Low] weight): [Score] - [Any concerns]
...
Please calculate and recommend.
```

**AI will automatically**:
- Apply correct weight formula
- Calculate enhanced score with divergence penalty
- Compute 95% confidence interval
- Determine information sufficiency
- Provide recommendation

### Step 5: Review and Decide (1 minute)

AI provides recommendation. You confirm or discuss further.

| AI Says | You Do |
|:--------|:-------|
| ✅ Strong Approve | Proceed confidently |
| ⚠️ Conditional Approve | Proceed with noted conditions |
| 🔄 Revise | Address concerns, re-score |
| ❌ Reject | Do not proceed |
| ℹ️ Need More Info | Add experts or discuss divergence |

---

## 🤖 AI Calculation Examples

### Example 1: L1 Bug Fix (Complete Walkthrough)

**Your Input to AI**:
```
Decision: Fix login button not responding on mobile
Level: L1
Expert Scores:
- Engineer (High): 5 - Clean fix, tested locally
- QA (Medium): 4 - Passed regression, minor edge case concern

Please calculate and recommend.
```

**AI Calculation** (shown for transparency):
```
Step 1: Assign weights
  Engineer: High = 3
  QA: Medium = 2
  Total weight = 5

Step 2: Calculate weighted average
  S = (3×5 + 2×4) / 5 = (15 + 8) / 5 = 23 / 5 = 4.6

Step 3: Calculate divergence penalty
  Range = 5 - 4 = 1
  n = 2 experts → λ = 1.2
  Penalty = 1.2 × 1 / 4 = 0.3

Step 4: Enhanced score
  S_enhanced = 4.6 - 0.3 = 4.3

Step 5: Decision check
  S_enhanced = 4.3 ≥ 4.0 ✓
  Range = 1 ≤ 1 ✓

Result: ✅ STRONG APPROVE
Confidence: High (low divergence, sufficient experts for L1)
```

---

### Example 2: L2 New Feature

**Your Input to AI**:
```
Decision: Add dark mode to user settings
Level: L2
Expert Scores:
- Architect (High): 4 - Clean implementation pattern
- Engineer (Medium): 4 - Straightforward to implement
- QA (Medium): 3 - Need to test all color combinations
- PM (Low): 5 - Users have requested this frequently

Please calculate and recommend.
```

**AI Calculation**:
```
Step 1: Weights
  Architect: 3, Engineer: 2, QA: 2, PM: 1
  Total = 8

Step 2: Weighted average
  S = (3×4 + 2×4 + 2×3 + 1×5) / 8
    = (12 + 8 + 6 + 5) / 8 = 31 / 8 = 3.875

Step 3: Divergence penalty
  Range = 5 - 3 = 2
  n = 4 → λ = 0.9
  Penalty = 0.9 × 2 / 4 = 0.45

Step 4: Enhanced score
  S_enhanced = 3.875 - 0.45 = 3.425

Step 5: Confidence interval (simplified)
  σ ≈ Range/2.5 = 0.8
  SE = σ/√n = 0.8/2 = 0.4
  CI_95% ≈ [3.425 - 0.8, 3.425 + 0.8] = [2.6, 4.2]
  IS = 1 - 1.6/4 = 0.6 (sufficient)

Step 6: Decision check
  S_enhanced = 3.425 < 3.5 (below conditional threshold)
  BUT Range = 2 (moderate divergence)

Result: 🔄 REVISE
Reason: QA concern (score 3) needs addressing before approval.
Recommendation: Discuss testing strategy with QA, then re-score.
```

---

### Example 3: L3 Technology Decision

**Your Input to AI**:
```
Decision: Migrate from REST to GraphQL for mobile API
Level: L3
Expert Scores:
- Architect (High): 4 - Good fit for mobile data needs
- Backend Engineer (High): 3 - Learning curve, but manageable
- Frontend Engineer (Medium): 5 - Will simplify our mobile code significantly
- QA (Medium): 3 - Need new testing approach
- DevOps (Medium): 4 - Deployment is similar
- Security (Medium): 4 - Can implement same auth patterns
- PM (Low): 4 - Aligns with mobile-first strategy
- Tech Lead (High): 4 - Strategic investment worth making

Please calculate and recommend.
```

**AI Calculation**:
```
Step 1: Weights (High=3, Medium=2, Low=1)
  Architect: 3, Backend: 3, Frontend: 2, QA: 2
  DevOps: 2, Security: 2, PM: 1, Tech Lead: 3
  Total = 18

Step 2: Weighted average
  S = (3×4 + 3×3 + 2×5 + 2×3 + 2×4 + 2×4 + 1×4 + 3×4) / 18
    = (12 + 9 + 10 + 6 + 8 + 8 + 4 + 12) / 18
    = 69 / 18 = 3.83

Step 3: Divergence penalty
  Range = 5 - 3 = 2
  n = 8 → λ = 0.7
  Penalty = 0.7 × 2 / 4 = 0.35

Step 4: Enhanced score
  S_enhanced = 3.83 - 0.35 = 3.48

Step 5: Confidence interval
  Scores: [4,3,5,3,4,4,4,4], mean=3.83
  σ ≈ 0.65
  SE = 0.65/√8 × 1.3 (correlation factor) = 0.30
  t(7) = 2.4
  CI_95% = [3.48 - 2.4×0.30, 3.48 + 2.4×0.30] = [2.76, 4.20]
  IS = 1 - 1.44/4 = 0.64 (sufficient)

Step 6: Decision check
  S_enhanced = 3.48 (just below 3.5)
  CI includes 3.5 ✓
  IS = 0.64 > 0.5 ✓

Result: ⚠️ CONDITIONAL APPROVE
Conditions:
1. Address Backend Engineer's learning curve concern (training plan)
2. Address QA's testing concern (define new test strategy)
Confidence: Medium (score borderline, but majority support)
```

---

## ❓ Common Errors FAQ

### Q1: "I forgot to collect scores independently"

**Problem**: Experts saw each other's scores → anchoring bias.

**Solution**: 
- Discard biased scores
- Re-collect independently (use separate forms/messages)
- Prevention: Always collect via private channel first

---

### Q2: "My experts gave very different scores (Range ≥ 3)"

**Problem**: Range of 3-4 indicates severe divergence.

**Solution**:
1. **Don't average and proceed** - this hides real disagreement
2. Identify which experts diverge most
3. Facilitate discussion to understand perspectives
4. Either reach consensus or escalate to higher level
5. Document the disagreement regardless of outcome

---

### Q3: "I don't know what weight to assign"

**Problem**: Unsure if expert is High/Medium/Low weight.

**Solution - Quick Rule**:
| Expert's Relation to Decision | Weight |
|-------------------------------|:------:|
| Primary domain expert | **High (3)** |
| Related expertise | **Medium (2)** |
| General stakeholder | **Low (1)** |

**Examples**:
- Architecture decision → Architect: High, PM: Low
- UX change → UX Designer: High, Backend: Low
- Security issue → Security: High, Frontend: Low

---

### Q4: "AI gave 'Need More Info' - what do I do?"

**Problem**: Information Sufficiency < 0.5 or CI too wide.

**Solution**:
1. Add more experts (especially from underrepresented domains)
2. If experts are uncertain, gather more data first
3. Break the decision into smaller, more specific questions
4. Consider if the question is well-defined enough

---

### Q5: "Score is borderline (around 3.5)"

**Problem**: S_enhanced ≈ 3.5, unclear approve or revise.

**Solution**:
1. Check CI - does it include both >3.5 and <3.5?
2. If yes → decision is genuinely uncertain
3. Options:
   - Add experts for more confidence
   - Accept with conditions (monitoring plan)
   - Address specific concerns and re-score
4. Document the borderline nature of the decision

---

### Q6: "One expert's score seems like an outlier"

**Problem**: One score of 2 when others are 4-5.

**Solution**:
1. **Do NOT discard** - outliers often catch real issues
2. Ask the dissenting expert to elaborate
3. If concern is valid → address it
4. If concern is based on misunderstanding → clarify and allow re-score
5. Document dissent even if overruled (Devil's Advocate requirement)

---

### Q7: "We're in a hurry - can we skip steps?"

**Problem**: Time pressure to decide quickly.

**Solution**:
| What to Skip | Safe? |
|--------------|:-----:|
| Independent scoring | ❌ Never skip |
| Devil's advocate | ❌ Never skip |
| Documentation | ⚠️ Minimal OK |
| Full calculation | ✅ Use AI |
| Extended discussion | ✅ If consensus |

**Minimum viable process**:
1. ✓ Independent scores
2. ✓ AI calculation
3. ✓ One dissenting view
4. ✓ Brief documentation

---

## 📋 Copy-Paste Templates

### Template A: Minimal (L1)

```markdown
## L1 Quick Check
**Decision**: [What]
**Panel**: Engineer, QA

| Expert | Weight | Score | Concern |
|--------|:------:|:-----:|---------|
| Engineer | High | | |
| QA | Medium | | |

**AI Result**: [Paste AI calculation]
**Verdict**: [Approve/Conditional/Revise/Reject]
```

### Template B: Standard (L2)

```markdown
## L2 Standard Review
**Decision**: [What]
**Context**: [Why this decision now]

| Expert | Weight | Score | Concern |
|--------|:------:|:-----:|---------|
| Architect | High | | |
| Engineer | Medium | | |
| QA | Medium | | |
| PM | Low | | |

**AI Result**: [Paste AI calculation]
**Devil's Advocate**: [One dissenting view]
**Verdict**: [Decision]
**Conditions**: [If any]
**Next Steps**: [Actions]
```

### Template C: Complex (L3+)

```markdown
## L[3/4/5] Deep Review
**Decision**: [Detailed description]
**Impact**: [Who/what is affected]
**Urgency**: [Timeline]

### Expert Scores
| Expert | Domain | Weight | Score | Key Concern |
|--------|--------|:------:|:-----:|-------------|
| | | | | |

### AI Analysis
[Paste full AI calculation including CI and IS]

### Divergence Points
| Issue | Experts | Resolution |
|-------|---------|------------|
| | | |

### Devil's Advocate
**Dissenter**: [Role]
**Objection**: [Main concern]
**Risk if ignored**: [What could go wrong]

### Final Decision
**Verdict**: [Decision]
**S_enhanced**: [Score]
**CI_95%**: [Range]
**Confidence**: [High/Medium/Low]
**Binding Conditions**: [Must-do items]
```

---

## ⚡ One-Page Cheat Sheet

```
┌─────────────────────────────────────────────────────────┐
│       EXPERT COMMITTEE CHEAT SHEET v2.2                 │
├─────────────────────────────────────────────────────────┤
│  STEP 1 - SELECT LEVEL:                                 │
│  • Easy to undo? → L1-L2                                │
│  • Cross-team? → L3+                                    │
│  • Strategic? → L5                                      │
├─────────────────────────────────────────────────────────┤
│  STEP 2 - COLLECT SCORES:                               │
│  • MUST be independent (no peeking!)                    │
│  • Scale: 1=Fail, 2=Poor, 3=OK, 4=Good, 5=Excellent    │
│  • Record concerns alongside scores                     │
├─────────────────────────────────────────────────────────┤
│  STEP 3 - ASSIGN WEIGHTS:                               │
│  • Primary expert → High (3)                            │
│  • Related expert → Medium (2)                          │
│  • General input → Low (1)                              │
├─────────────────────────────────────────────────────────┤
│  STEP 4 - LET AI CALCULATE:                             │
│  • Provide: Level, Experts, Weights, Scores, Concerns   │
│  • AI returns: S_enhanced, CI, IS, Recommendation       │
├─────────────────────────────────────────────────────────┤
│  STEP 5 - DECIDE:                                       │
│  • ✅ Strong Approve: CI_lower > 3.5                    │
│  • ⚠️ Conditional: S > 3.5, CI_lower > 2.5              │
│  • 🔄 Revise: S < 3.5 or Range ≥ 3                      │
│  • ❌ Reject: CI_upper < 2.5                            │
├─────────────────────────────────────────────────────────┤
│  NEVER SKIP:                                            │
│  □ Independent scoring                                  │
│  □ Devil's advocate (1+ dissenting view)                │
│  □ Brief documentation                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 Learn More

| Topic | Reference |
|-------|-----------|
| Full framework | `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` |
| Detailed templates | `.knowledge/templates/EXPERT_COMMITTEE.md` |
| Weight matrices | `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` |
| Expert roles (23) | `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` |
| Quality angles (37) | `.knowledge/frameworks/patterns/DECISION.md` |

---

## ✅ Pre-Decision Checklist

```markdown
□ Level selected based on risk/reversibility?
□ Right experts assembled for the domain?
□ Scores collected INDEPENDENTLY?
□ Weights assigned (High/Medium/Low)?
□ AI calculation completed?
□ Confidence interval acceptable?
□ Information sufficiency > 0.5?
□ Devil's advocate opinion recorded?
□ Decision documented?
```

---

## Related

- `.knowledge/frameworks/cognitive/EXPERT_COMMITTEE.md` — Full framework (SSOT)
- `.knowledge/templates/EXPERT_COMMITTEE.md` — Detailed templates
- `.knowledge/frameworks/cognitive/CONFLICT_RESOLUTION.md` — Conflict resolution
- `.knowledge/frameworks/cognitive/ROLE_PERSONA.md` — Expert roles (23)
- `.knowledge/frameworks/patterns/DECISION.md` — Quality angles (37)

---

*Expert Committee Quick-Start Guide v2.2*
