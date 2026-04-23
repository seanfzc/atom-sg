# Diagram Reconstruction Framework

## Process Flow
```
1. Detect Issues (Vision Audit)
   ↓
2. Fix Code (Edit generate_renders.py)
   ↓
3. Regenerate Diagrams (Run script)
   ↓
4. Verify Fixes (Vision Check)
   ↓
5. Iterate OR Finalize
```

## Verification Rules

| Rule | Trigger | Action |
|-------|----------|---------|
| **Meaningful Change** | Only cosmetic tweaks (<10px shift) | Stop & escalate |
| **Vision Confidence** | Uncertain/conflicting feedback | Stop & escalate |
| **Time Budget** | >5 min per diagram | Stop & escalate |

## Agent Roles

| Phase | Agent Required? | Why |
|-------|----------------|-----|
| **Detect Issues** | ❌ No | Current agent + Vision LLM sufficient |
| **Fix Code** | ❌ No | Direct edit by current agent |
| **Regenerate** | ❌ No | Python script execution |
| **Verify Fixes** | ❌ No | Same Vision LLM, different prompt |

**Verdict:** No dedicated agents needed — all handled by current agent with Vision LLM.

## Instruction Format

```
/run-diagram-reconstruction [diagram_ids]

Examples:
/run-diagram-reconstruction G021 G022 G025
/run-diagram-reconstruction all
```

## Output Structure

```
RECONSTRUCTION REPORT: {DIAGRAM_IDS}

Diagram: G021
  Issues Found: {LIST}
  Code Fixed: {CHANGES}
  Verification: PASS/FAIL
  Attempts: N
  Status: COMPLETE/ESCALATED

Diagram: G022
  Issues Found: {LIST}
  Code Fixed: {CHANGES}
  Verification: PASS/FAIL
  Attempts: N
  Status: COMPLETE/ESCALATED
```

## Escalation Format

```
ESCALATION NEEDED: {DIAGRAM_ID}

Time: {X:Y elapsed}
Issues: {UNRESOLVED_ISSUES}

Last vision feedback:
{VISION_RESULT_RAW_TEXT}

Status: {TRIGGER_REASON}

Action required: MANUAL REVIEW
```

---

**Command:** `/run-diagram-reconstruction [diagram_ids]`
