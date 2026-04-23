# Math Diagram Implementation Checklist

**Purpose:** Ensure rendering code follows all guidelines before any diagram is generated

---

## Pre-Implementation (4 Gates)

### Gate 0 — Solve First
- [ ] Problem solved completely with target-level tools only
- [ ] All variables identified and documented
- [ ] Solution method verified (no algebra for P5-P6)

### Gate 1 — Audience Constraint Check
- [ ] All labels use age-appropriate language
- [ ] No variables like "n" for unknown counts
- [ ] No formal notation (∴, ∑, etc.)
- [ ] No adult vocabulary ("deficit", "hence")

### Gate 2 — Map Reasoning Chain
- [ ] Every solution step has a visual anchor
- [ ] No reasoning leaps
- [ ] Unknowns can be derived from visible elements

### Gate 3 — Plan Scale
- [ ] px_per_unit defined for all comparable elements
- [ ] Different scales separated by panels
- [ ] Scale written down before coding

---

## During Implementation

### Parametric Approach
- [ ] All positions computed from variables, not hardcoded
- [ ] Labels anchored to elements with offset calculation
- [ ] Collision detection implemented
- [ ] Canvas bounds checking implemented

### Dimension Lines (Critical)
- [ ] Arrow tips touch EXACT endpoints (not near, not past)
- [ ] Extension lines perpendicular to measured edge
- [ ] Label centered on dimension line with background break
- [ ] Multiple dimensions stacked at consistent offsets (12, 28, 44px)
- [ ] NO dimension lines cross each other

### Isometric 3D (Critical)
- [ ] Uses exact 30° formulas:
  ```python
  screen_x = origin_x + (x - y) * cos(30°) * scale
  screen_y = origin_y - z * scale + (x + y) * sin(30°) * scale * 0.5
  ```
- [ ] NOT using manual coordinate placement
- [ ] Visible faces computed (check adjacent cells)
- [ ] Face shading consistent (top=light, front=medium, side=dark)
- [ ] Cube count verified against problem statement

### Labels
- [ ] Font sizes follow hierarchy (title 14px, axis 12px, data 11px, tick 10px)
- [ ] Minimum 10px for primary school
- [ ] Labels on shaded regions have contrast ≥ 4.5:1 or opaque background
- [ ] Leader lines start at label edge, end on element boundary
- [ ] No label overlaps (2px minimum clearance)

---

## Post-Implementation Verification

### Automated Checks (Run These)

```python
# Check 1: Isometric angles
for line in isometric_lines:
    angle = degrees(atan2(y2-y1, x2-x1))
    assert abs(angle - 30) <= 2 or abs(angle + 30) <= 2 or abs(angle - 90) <= 2

# Check 2: Dimension line accuracy
for dim_line in dimension_lines:
    expected = distance(dim_line.measured_edge)
    actual = distance(dim_line.start, dim_line.end)
    assert abs(expected - actual) <= 1  # 1px tolerance

# Check 3: Bar model proportions
for bar in comparison_bars:
    actual_ratio = bar1.pixel_length / bar2.pixel_length
    expected_ratio = bar1.value / bar2.value
    assert abs(actual_ratio - expected_ratio) <= 0.03  # 3% tolerance

# Check 4: Solvability
unknowns = count_question_marks() + count_unknown_dimensions()
constraints = count_given_values() + count_visible_relationships()
assert constraints >= unknowns, "Problem not solvable from diagram"
```

### Manual Checks

- [ ] T1: Numeric recomputation — all numbers verified
- [ ] T2: Pixel ratio measurement — all proportions checked
- [ ] T3: Label binding trace — every label traced to element
- [ ] T4: Reasoning chain walk-through — every step anchored
- [ ] T5: Audience simulation — can student solve from diagram?
- [ ] T6: Scale audit — same scale within panels
- [ ] T7: Bracket span verification — endpoints on boundaries
- [ ] T8: Edge case stress tests — 3D, nets, dimension lines
- [ ] T9: Implementation verification — code follows formulas

---

## Solvability Verification (NEW)

### For Geometry Problems
- [ ] Can student measure all needed dimensions from diagram?
- [ ] Are unknowns marked with "?" (not blank)?
- [ ] Are relationships visible (e.g., X + Y = Z shown with brackets)?
- [ ] Can answer be derived without guessing?

### For 3D Problems
- [ ] Is cube count clearly labeled?
- [ ] Are view directions indicated (Front, Side, Top arrows)?
- [ ] Is grid provided for drawing views?
- [ ] Can front view be determined without ambiguity?

### For Bar Models
- [ ] Is "?" on the unknown quantity?
- [ ] Are all known values labeled?
- [ ] Do brackets span exactly what they claim?
- [ ] Is the comparison ratio visible?

---

## Final Sign-Off

Before committing any diagram:

```
I certify that:
- [ ] All 4 gates were completed
- [ ] All implementation checks passed
- [ ] All automated verification tests passed
- [ ] All manual T1-T9 checks passed
- [ ] Solvability verification passed
- [ ] Diagram has been reviewed against this checklist

Signed: _________________ Date: _______
```

---

## Common Failure Modes

| Failure | Prevention |
|---------|-----------|
| Dimension line overshoot | Use exact endpoint calculation, not approximate |
| Not solvable | Add "?" marks, show relationships, verify constraints ≥ unknowns |
| Not true isometric | Use cos(30°) and sin(30°) formulas, never manual placement |
| Label overlap | Implement collision detection, don't skip |
| Wrong visible faces | Compute occupancy grid, check adjacent cells |
| Scale betrayal | Define px_per_unit, compute all lengths from it |

---

*This checklist must be completed for every diagram before approval*
