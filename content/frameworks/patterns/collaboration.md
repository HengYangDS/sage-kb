# AI Collaboration Patterns

> Patterns for effective human-AI collaboration

---

## 💬 Communication Patterns

### Instruction Types

| Type            | Example                         | Best Practice                 |
|-----------------|---------------------------------|-------------------------------|
| **Direct**      | "Create user API endpoint"      | Clear, specific, actionable   |
| **Contextual**  | Fixing similar bugs             | Provide sufficient background |
| **Conditional** | "Refactor only if tests pass"   | State conditions clearly      |
| **Exploratory** | "Investigate performance issue" | Define scope and criteria     |
| **Batch**       | "Complete all TODO items"       | Group related tasks           |

### Response Patterns

| Pattern           | Format                       |
|-------------------|------------------------------|
| **Confirmation**  | "I will do X. Proceed?"      |
| **Progress**      | "Step 2/5: Implementing..."  |
| **Completion**    | "Done. Summary: ..."         |
| **Clarification** | "Did you mean A or B?"       |
| **Error**         | "Error: X. Suggested fix: Y" |

### Context Template

```
Project: [name] · Branch: [branch] · Recent: [changes]
Task: [objective] · Constraints: [limits] · Progress: [status]
```

---

## 🤝 Task Handoff

| Type         | Format                                                                         |
|--------------|--------------------------------------------------------------------------------|
| **Simple**   | Human: "Do X" → AI: Confirm → Execute → Report                                 |
| **Detailed** | Task · Requirements · Constraints · Acceptance · Autonomy: L[N]                |
| **Batch**    | Tasks: [prioritized list] · Order: Sequential/Parallel · Checkpoint: After [N] |

---

## 📝 Instruction Engineering

### CLEAR Framework

| C                    | L                 | E                | A                | R                 |
|----------------------|-------------------|------------------|------------------|-------------------|
| **C**ontext          | **L**imitations   | **E**xpectations | **A**ction       | **R**eview        |
| Background info      | Constraints       | Success criteria | What to do       | Checkpoints       |
| "In this FastAPI..." | "Don't modify DB" | "Tests pass"     | "Implement auth" | "Show plan first" |

### Quality Checklist

**Specific** · **Scoped** · **Measurable** · **Contextual** · **Prioritized**

### Anti-Patterns

| ❌ Anti-Pattern         | ✅ Better                      |
|------------------------|-------------------------------|
| "Make it better"       | Specific improvement criteria |
| "Do everything"        | Prioritized task list         |
| "You know what I mean" | Explicit requirements         |
| "ASAP"                 | Specific time constraint      |

---

## 🎭 Collaboration Modes

| Mode        | AI Behavior                   | When to Use         |
|-------------|-------------------------------|---------------------|
| **Plan**    | Create plan, await approval   | Complex new feature |
| **Execute** | Run with progress updates     | Clear task, bug fix |
| **Review**  | Analyze without changes       | Code quality check  |
| **Explain** | Explain concepts clearly      | Learning new tech   |
| **Debug**   | Diagnose with minimal changes | Unclear bug cause   |
| **Pair**    | Interactive back-and-forth    | Collaborative work  |

**Flow**: Complex feature → Plan → Execute | Unclear bug → Debug → Execute | Review → Refactor → Plan → Execute

---

## 🔄 Feedback & Calibration

### Calibration Signals

| Signal             | → Action               |
|--------------------|------------------------|
| "Let me see first" | L1-L2, verbose         |
| "You decide"       | L3-L4, autonomous      |
| "Just do it"       | Concise, execute       |
| "Stop"             | Checkpoint immediately |

### Feedback by Autonomy

| Level | Communication | Checkpoints       |
|-------|---------------|-------------------|
| L1-L2 | Every step    | After each action |
| L3-L4 | Milestones    | At decisions      |
| L5-L6 | Completion    | On issues only    |

---

## 🚨 Error Recovery

### Classification & Recovery

| Type         | Severity | Recovery         |
|--------------|----------|------------------|
| **Syntax**   | Low      | Auto-fix         |
| **Logic**    | Medium   | Report + suggest |
| **Data**     | High     | Stop + await     |
| **Security** | Critical | Stop immediately |

### Protocol

```
Detect → Classify → Stop (if High+) → Document → Analyze → Propose → Await (if needed) → Fix → Verify
```

### Error Report

```
Type: [class] · Severity: [L/M/H/C] · Location: [file:line]
What: [desc] · Why: [cause] · Fix: [solution]
```

---

## 🚀 Quick Reference

| Phase      | Actions                                                 |
|------------|---------------------------------------------------------|
| **Start**  | Context · Objective · Autonomy · Constraints · Priority |
| **During** | Monitor · Respond · Checkpoint · Adjust autonomy        |
| **End**    | Review · Feedback · Update calibration · Document       |

---

*Part of SAGE Knowledge Base*
