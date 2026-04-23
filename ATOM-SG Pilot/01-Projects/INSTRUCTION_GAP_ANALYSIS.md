# Gap Analysis: Why Issues Weren't Caught
## Evaluation of Documentation vs. Actual Errors

**Date:** 2026-04-20  
**Purpose:** Identify why Q15, Q12, Q19 issues escaped detection despite comprehensive instructions

---

## Issues Discovered vs. Instructions Available

### Issue 1: Q15 - Dimension Line Overshot Radius

**What Happened:**
- Arrow representing 10cm extended beyond the actual radius line
- Created visual confusion suggesting radius < 10cm

**Why Instructions Didn't Catch It:**

| Instruction Section | What It Says | Gap |
|--------------------|--------------|-----|
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - Dimension Lines | "Both arrow tips must touch the exact boundaries" | ✅ Covered |
| PARAMETRIC_VISUAL_RENDERING_GUIDE.md - Dimension Lines | "Arrow tip x/y must equal the extension line x/y to the pixel" | ✅ Covered |
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - T8 | "Do both arrow tips touch the exact edge boundaries?" | ✅ Covered |

**Root Cause:** 
- **The instructions ARE correct and comprehensive**
- **The issue:** Implementation didn't follow the instructions
- The rendering code used a simple `annotate` arrow instead of computing exact endpoints

**Gap Identified:** 
- ❌ **No code review/verification step** in the rendering process
- ❌ **No automated measurement validation** to verify dimension line accuracy
- Instructions exist but weren't enforced in code

---

### Issue 2: Q12 - Unable to Solve with Existing Info

**What Happened:**
- Only Square X = 4cm labeled
- No visible relationships between squares
- Student cannot deduce Y, Z, W, V sizes

**Why Instructions Didn't Catch It:**

| Instruction Section | What It Says | Gap |
|--------------------|--------------|-----|
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - T4 | "Solve the problem at the target level... Flag any step with no anchor" | ✅ Covered |
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - Stage 4 | "Does the diagram teach the claimed concept?" | ✅ Covered |
| MATH_DIAGRAM_RENDERING_INSTRUCTION.md - Gate 2 | "Your diagram must make each step visible" | ✅ Covered |

**Root Cause:**
- **The instructions ARE correct**
- **The issue:** "Establish Intent" was incomplete
- Intent stated: "show 5 squares with X=4cm"
- Intent should have stated: "show 5 squares with solvable relationships"

**Gap Identified:**
- ❌ **No requirement to verify solvability** before rendering
- ❌ **Intent statement doesn't require "student can solve from diagram"**
- The audit checked "labels match" but not "information is sufficient"

---

### Issue 3: Q19 - Not True Isometric, Cubes Misrepresented

**What Happened:**
- Previous render didn't use true 30° isometric projection
- Cubes appeared distorted
- No view labels or grid

**Why Instructions Didn't Catch It:**

| Instruction Section | What It Says | Gap |
|--------------------|--------------|-----|
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - 3D Solids | "Receding edges must be at exactly 30° from horizontal. Measure." | ✅ Covered |
| MATH_DIAGRAM_AUDIT_INSTRUCTION.md - 3D Solids | "Flag >2° deviation" | ✅ Covered |
| PARAMETRIC_VISUAL_RENDERING_GUIDE.md - 3D | "Use 30° isometric: x-axis at +30°, y-axis at -30°" | ✅ Covered |
| PARAMETRIC_VISUAL_RENDERING_GUIDE.md - 3D | "Conversion: screen_x = origin_x + (x - y) × cos(30°)" | ✅ Covered |

**Root Cause:**
- **The instructions ARE correct and detailed**
- **The issue:** Implementation used approximate/manual coordinates instead of parametric formulas
- Previous code: `iso_angle = math.radians(30)` but then used manual positioning

**Gap Identified:**
- ❌ **No enforcement of parametric approach** in code
- ❌ **No angle measurement verification** in audit
- Instructions say "measure" but no tool/procedure provided for measurement

---

## Systemic Gaps Identified

### Gap 1: Instructions vs. Implementation Disconnect

**Problem:** Instructions are comprehensive but not enforced

**Evidence:**
- All three issues were covered in existing docs
- But rendering code didn't follow the instructions
- Audit checked "presence of labels" not "accuracy of geometry"

**Solution:**
Add to MATH_DIAGRAM_AUDIT_INSTRUCTION.md:
```markdown
### T9 — Implementation Verification
For every dimension line, arrow, or geometric element:
- [ ] Verify the code uses the parametric formulas from PARAMETRIC_VISUAL_RENDERING_GUIDE.md
- [ ] Do not accept "looks correct" — verify the math in the code matches the specification
- [ ] Check that isometric projections use exact 30° formulas, not approximations
- [ ] Verify dimension lines compute endpoints from geometry, not hardcoded coordinates
```

---

### Gap 2: Missing "Solvability Verification"

**Problem:** Audit checks if diagram matches problem, but not if problem is solvable from diagram

**Evidence:**
- Q12 passed all checks (labels correct, alignment good)
- But student couldn't solve it from the diagram alone

**Solution:**
Add to MATH_DIAGRAM_AUDIT_INSTRUCTION.md - Stage 0:
```markdown
### Stage 0b — Solvability Check
After establishing intent, verify:
- Can a student at the target level solve this problem using ONLY the diagram + question text?
- Are all necessary constraints visible in the diagram?
- Are relationships between elements visually apparent?
- If the answer is "no" to any of these, flag INTENT INCOMPLETE.
```

---

### Gap 3: No Automated Measurement Tools

**Problem:** Instructions say "measure" but provide no procedure

**Evidence:**
- "Measure pixel widths" — how?
- "Flag >2° deviation" — with what tool?
- "Verify exact 30°" — how to verify?

**Solution:**
Add to PARAMETRIC_VISUAL_RENDERING_GUIDE.md:
```markdown
## Automated Verification Procedures

### Verifying Isometric Angles
```python
# For any line segment in the diagram:
angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
if abs(angle - 30) > 2 and abs(angle + 30) > 2 and abs(angle - 90) > 2:
    flag_deviation(angle)
```

### Verifying Dimension Line Accuracy
```python
# For a dimension line claiming to measure edge from A to B:
expected_length = distance(A, B)
actual_length = distance(dim_start, dim_end)
if abs(expected_length - actual_length) > 1:  # 1px tolerance
    flag_inaccuracy(expected_length, actual_length)
```

### Verifying Solvability
```python
# For geometry problems:
unknowns = count_unknowns_in_diagram()
constraints = count_visible_constraints()
if constraints < unknowns:
    flag_not_solvable(unknowns, constraints)
```
```

---

### Gap 4: No Code Review Requirements

**Problem:** Instructions for auditors but not for implementers

**Evidence:**
- Rendering code didn't follow the 4-gates
- No checklist for implementers

**Solution:**
Create new file: **MATH_DIAGRAM_IMPLEMENTATION_CHECKLIST.md**
```markdown
# Implementation Checklist

Before generating any diagram:

## Pre-Implementation
- [ ] Gate 0: Solved the problem completely?
- [ ] Gate 1: Verified all labels use age-appropriate language?
- [ ] Gate 2: Written out reasoning chain with visual anchors?
- [ ] Gate 3: Defined px_per_unit scale?

## During Implementation
- [ ] Using parametric formulas from RENDERING_GUIDE.md?
- [ ] Labels anchored to elements, not hardcoded?
- [ ] Collision detection implemented?
- [ ] Dimension lines use exact endpoint calculation?
- [ ] Isometric uses exact 30° formulas?

## Post-Implementation
- [ ] Run AUDIT_INSTRUCTION.md T1-T9
- [ ] Verify solvability from diagram alone
- [ ] Check all measurements with automated tools
- [ ] Review against this checklist
```

---

## Summary: Instructions Are Good, Enforcement Is Missing

| Aspect | Status | Issue |
|--------|--------|-------|
| Rendering instructions | ✅ Comprehensive | Not followed in code |
| Audit instructions | ✅ Comprehensive | No measurement tools |
| 3D guidelines | ✅ Detailed | Not enforced |
| Solvability check | ❌ Missing | Added above |
| Implementation checklist | ❌ Missing | Added above |
| Automated verification | ❌ Missing | Added above |

## Recommended Actions

1. **Add T9 — Implementation Verification** to audit instructions
2. **Add Stage 0b — Solvability Check** to audit pipeline
3. **Add Automated Verification Procedures** to rendering guide
4. **Create MATH_DIAGRAM_IMPLEMENTATION_CHECKLIST.md**
5. **Require checklist completion** before any diagram is approved

The instructions were correct. The gaps were in:
- Enforcement mechanisms
- Automated verification tools
- Solvability verification
- Implementation accountability
