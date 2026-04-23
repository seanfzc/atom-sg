# Visual Errors & Learnings by Diagram Type

**Date:** 2026-04-19  
**Purpose:** Document common visual errors to prevent recurrence

---

## 1. PROTRACTOR DIAGRAMS (G001)

### Errors Found:
- Missing degree labels on scale markings
- Angle arcs too close together (overlapping)
- No clear "0°" reference point indicated

### Root Cause:
- Focused on aesthetic colors rather than measurement clarity
- Did not verify if a student could actually read the protractor

### Fix Required:
- Add degree labels (0°, 30°, 60°, 90°, etc.) at major markings
- Space angle arcs further apart (different radii)
- Clearly mark 0° baseline

### Learning:
**For measurement tools: Clarity > Aesthetics. A student must be able to take actual measurements from the diagram.**

---

## 2. COMPOSITE SHAPES (G011 - L-Shape)

### Errors Found:
- Missing internal dimension (the "step")
- Ambiguous 2cm label (could mean height or width)
- No visual indication of component rectangles

### Root Cause:
- Did not include ALL dimensions needed to solve
- Assumed student would infer missing measurements

### Fix Required:
- Add ALL dimensions including internal edges
- Use leader lines to clearly associate labels with edges
- Optionally show dashed lines dividing into component rectangles

### Learning:
**For composite shapes: Every edge that affects calculation must have a dimension. Never assume inference.**

---

## 3. 3D DIAGRAMS (G017 - Cuboid)

### Errors Found:
- Rotated text hard to read ("4 cm" on right face)
- Missing hidden edges (dashed lines)
- Different colors on faces may confuse dimension association

### Root Cause:
- Did not follow technical drawing conventions
- Prioritized color coding over clarity

### Fix Required:
- Keep dimension labels horizontal (readable)
- Add dashed lines for hidden edges
- Use consistent coloring or remove color differentiation

### Learning:
**For 3D diagrams: Follow technical drawing standards. Hidden edges = dashed. Labels must be readable without rotation.**

---

## 4. RADIUS/DIMENSION LABELS (Q21)

### Errors Found:
- "10 cm" label overlaps with line OA
- Arrow placement cluttered
- Not clear that ALL radii are 10 cm

### Root Cause:
- Poor placement of dimension annotation
- Did not verify label doesn't obscure geometry

### Fix Required:
- Move label outside the shape
- Use clearer arrow placement
- Consider labeling one radius clearly, then noting "all radii = 10 cm"

### Learning:
**For dimension labels: Must not overlap with lines or points. When in doubt, place outside with leader line.**

---

## General Principles by Visual Type

### Protractors
- [ ] Degree markings at 10° intervals, labels at 30° intervals
- [ ] Clear 0° baseline indicated
- [ ] Angle arcs at different radii to prevent overlap
- [ ] Center point clearly marked

### Composite Shapes
- [ ] Every outer edge labeled
- [ ] Internal edges that affect calculation labeled
- [ ] Component shapes visually indicated (optional dashed lines)
- [ ] Leader lines connect labels to correct edges

### 3D Solids
- [ ] Hidden edges shown as dashed lines
- [ ] All dimension labels horizontal/readable
- [ ] Consistent coloring (avoid face-color confusion)
- [ ] Isometric projection angles consistent

### Circles/Arcs
- [ ] Radius labels outside the circle
- [ ] Center point clearly marked
- [ ] Arc direction indicated if not full circle
- [ ] No label overlap with radius lines

### Charts/Graphs
- [ ] Axes clearly labeled with units
- [ ] Data values shown on bars/points
- [ ] Legend if multiple data series
- [ ] Grid lines subtle but visible

---

## Verification Checklist (Before Committing)

For each diagram type:

**Protractor:**
- [ ] Can I read the angle measurement without guessing?
- [ ] Are 0°, 90°, 180° clearly marked?

**Composite Shape:**
- [ ] Do I have all dimensions needed to calculate area/perimeter?
- [ ] Are internal edges dimensioned if needed?

**3D Solid:**
- [ ] Are hidden edges shown dashed?
- [ ] Can I read all dimension labels without tilting my head?

**Circle/Sector:**
- [ ] Is radius label clear and not overlapping?
- [ ] Is center point obvious?

**Chart:**
- [ ] Can I read all values directly from the chart?
- [ ] Are axes labeled with units?

---

## HISTORICAL VISUAL FIXES (Earlier Iterations)

### Q21 v1-v3: Overlapping Quarter Circles Evolution

**v1 Error:**
- Had two quarter circles with DIFFERENT centers (O and A)
- Shaded OBC was a triangle, not a sector
- Completely wrong geometry

**Root Cause:**
- Worked from text description only ("two overlapping quarter circles")
- Did not extract actual diagram from exam PDF
- Made assumptions about geometry

**Fix Applied:**
- Extracted actual ACS Junior Q15 diagram
- Discovered both quarter circles share center O
- Shaded OBC is a sector (pie slice), not triangle
- All points A, B, C, D on outer arc

**Learning:**
**Never reconstruct from text alone. Always extract and analyze the actual source diagram.**

---

### Q21 v4: Radius Label Placement

**v4 Error:**
- "10 cm" label overlapped with line OA
- Arrow placement cluttered

**Fix Applied (Current):**
- Moved radius label outside the shape
- Used leader line with clear arrow
- Added "radius" annotation for clarity

---

### DI Charts v1: Shared Diagrams

**v1 Error:**
- Q33-Q34 shared same line graph
- Q35-Q36 shared same bar chart
- Q37-Q38 shared same pie chart
- Q39-Q40 shared same line graph

**Root Cause:**
- Lazy duplication to save time
- Did not create unique data sets for each question

**Fix Applied:**
- Created 8 unique charts with different data:
  - Q33: T-shirt sales over week
  - Q34: Temperature readings (different data)
  - Q35: Books read by students
  - Q36: Test scores by subject (different data)
  - Q37: Spending distribution
  - Q38: Fruit distribution (different data)
  - Q39: Website traffic by hour
  - Q40: Plant growth over weeks (different data)

**Learning:**
**Each question must have its own unique visual. Never share diagrams between questions.**

---

### Geometry Questions v1: Missing Diagrams

**v1 Error:**
- 6 out of 12 geometry questions had NO diagrams
- Q25, Q27, Q28, Q29, Q31, Q32 were text-only

**Root Cause:**
- Assumed simple geometry questions didn't need diagrams
- Did not verify each question had required visual

**Fix Applied:**
- Added diagrams to ALL 12 geometry questions
- Each diagram VRS-compliant with coordinate specs

**Learning:**
**Every geometry question must have a diagram. No exceptions.**

---

### Linguistic Complexity v1: Too Simple

**v1 Error:**
- Word problems averaged 29 words
- Missing context, temporal density, nested fractions
- Complexity score 5.2/10 vs ACS Junior 10-12/10

**Root Cause:**
- Focused on mathematical correctness over linguistic complexity
- Did not analyze ACS Junior language patterns

**Fix Applied:**
- Increased average word count to 53
- Added contextual embedding (setting, actors, purpose)
- Increased temporal density ("at first... then... later...")
- Added nested fractions and supposition language
- Complexity score improved to 8.1/10

**Learning:**
**Exam-quality = mathematical correctness + linguistic complexity. Both must match source standard.**

---

## Pattern Summary: Why Errors Occurred

| Pattern | Root Cause | Prevention |
|---------|-----------|------------|
| Wrong geometry | Text-only reconstruction | Always extract source image |
| Missing diagrams | Assumption that text was enough | Every geometry Q needs diagram |
| Shared visuals | Laziness/efficiency | Each Q gets unique visual |
| Overlapping labels | Poor annotation placement | Place outside with leader lines |
| Missing dimensions | Assumed inference | Every edge labeled |
| Simple language | Focused only on math | Match source linguistic complexity |

---

*Document created from Q21, G001, G011, G017 error analysis*
*Historical fixes added: Q21 evolution, DI charts, missing diagrams, linguistic complexity*
