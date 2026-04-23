# ATOM-SG YAML Schema — Diagram vs Question Data Separation

## Core Principle

**Fix 1: Separate diagram data from question data**

The YAML structure must have TWO CLEARLY SEPARATED sections:
1. **`diagram_data:`** — What to DRAW (shapes, labels, dimensions that appear visually ONLY)
2. **`question:` / `solution:` / `answer_key:`** — What to KEEP HIDDEN (text, solution steps, answers)

**Why this matters:**
- The renderer only sees `diagram_data:` section
- If solution or answer values leak into diagram data, the renderer may show them
- This violates the solvability test — student sees answers before solving

---

## Required YAML Structure

```yaml
problems:
  <QUESTION_ID>:
    id: "<question_identifier>"
    name: "<problem_name>"
    source:
      school: "<school_name>"
      year: <year>
      paper: "<paper>"
      page: <page>
      image_file: "<image_filename>"

    extraction:
      timestamp: "<ISO_8601>"
      tools_used: ["<tool1>", "<tool2>", ...]
      confidence: <0.0-1.0>

    # ========================================
    # SECTION 1: DIAGRAM DATA — VISIBLE ONLY
    # ========================================
    # ONLY what appears visually on the original diagram
    # NO solutions, NO derived values, NO answers
    # NO calculations shown on original image
    diagram_data:
      geometric_shape:
        type: "<shape_type>"
        appearance: "<visual_description>"

      # Add ALL visual elements from original diagram
      # Examples: labels, dimensions, arrows, annotations
      # Examples: vertices, edges, angles, points
      # Examples: axes, gridlines, data points

    # ========================================
    # SECTION 2: QUESTION DATA — NEVER RENDERED
    # ========================================
    # Question text, solution steps, answer key
    # These sections are NEVER shown to students
    question_text: |
      <full_question_text>

    solution: |
      <step_by_step_solution>

    answer_key:
      <answer_value_or_expression>
```

---

## What Goes In `diagram_data:`

✅ **INCLUDE:**
- Shapes (circles, triangles, rectangles, bar models, graphs, etc.)
- Labels visible on the original diagram
- Dimensions/angles/measurements visible on the original diagram
- Axes (for graphs)
- Gridlines (if visible on original)
- Data points (dots on graphs, values on axes)
- Arrow annotations
- Shading/hatching patterns
- Vertex labels (A, B, C, D for geometry)
- Color codes (if visible on original)

❌ **NEVER INCLUDE:**
- Solution steps
- Derived values (calculated dimensions, intermediate results)
- Final answers
- Calculations shown in working
- Mathematical reasoning
- "x = 147°" type annotations (unless actually on original)
- "Total = 240,000 cm³" type annotations (unless actually on original)

---

## What Goes In `question:` / `solution:` / `answer_key:`

✅ **INCLUDE:**
- Full question text exactly as appears in exam
- Solution steps (for verification, not rendering)
- Final answer(s) (for scoring, not rendering)
- Multiple-choice options (if any)
- Units for the answer

❌ **NEVER RENDER:**
- These sections are NEVER passed to the renderer
- Renderer should only access `diagram_data:` section
- Any answer visible to student violates solvability test

---

## Renderer Responsibilities

The rendering pipeline must:
1. **Only read `diagram_data:` section** — Ignore `question:` and `answer_key:`
2. **Validate diagram structure** — Check all required fields present
3. **Render visual elements only** — No text, no solutions, no answers
4. **Test solvability** — Given diagram + question text (from separate input), can student solve?

---

## Example: Valid YAML Structure

```yaml
problems:
  Q10:
    id: "Q10"
    name: "T-shirt Line Graph Data Interpretation"
    source:
      school: "ACS Junior"
      year: 2025
      paper: "Paper 2"
      page: 26
      image_file: "page-26.png"

    extraction:
      timestamp: "2026-04-22T10:35:00Z"
      tools_used: ["PyMuPDF", "Tesseract OCR", "Vision LLM (Gemini 3 Flash)"]
      confidence: 0.85

    # ========================================
    # DIAGRAM DATA — VISIBLE ONLY
    # ========================================
    diagram_data:
      geometric_shape:
        type: "line_graph"
        appearance: "coordinate_axes_with_data_line_and_points"

      axes:
        y_axis:
          label: "Number of T-shirts left unsold"
          direction: "vertical"
          orientation: "left"
          gridlines: [0, 20, 40, 60, 80, 100, 120]
          gridline_style: "horizontal_dashed"
          color: "#BDC3C7"

        x_axis:
          label: "Days"
          direction: "horizontal"
          orientation: "bottom"
          ticks: ["Start", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
          color: "#BDC3C7"

      data_line:
        type: "continuous_line"
        appearance: "solid"
        color: "#2980B9"
        marker_style: "solid_dots"

      data_points:
        start:
          x_label: "Start"
          y_value: 120
          point_style: "solid_dot"
        day_1:
          x_label: "Day 1"
          y_value: 96
          point_style: "solid_dot"
        day_2:
          x_label: "Day 2"
          y_value: 76
          point_style: "solid_dot"
        # ... (all 8 data points)

    # ========================================
    # QUESTION DATA — NEVER RENDERED
    # ========================================
    question_text: |
      The graph shows the number of T-shirts left unsold in a shop over 7 days.
      The shop started with 120 T-shirts.

      (a) How many T-shirts were sold on Day 3?

      (b) What percentage of T-shirts were sold in total?
      (Give your answer correct to 1 decimal place.)

    solution: |
      Step 1: Calculate T-shirts sold on each day
      Day 1: 120 - 96 = 24
      Day 2: 96 - 76 = 20
      Day 3: 76 - 60 = 16
      Day 4: 60 - 32 = 28
      Day 5: 32 - 20 = 12
      Day 6: 20 - 12 = 8
      Day 7: 12 - 4 = 8

      Step 2: Calculate total sold
      Total sold = 24 + 20 + 16 + 28 + 12 + 8 + 8 = 116

      Step 3: Calculate percentage
      Percentage = (116 ÷ 120) × 100 = 96.7%

    answer_key:
      a: "16 T-shirts"
      b: "96.7%"
```

---

## Common Violations (Stage 0 Finding 1)

### Violation 1: Answer in diagram_data

❌ **BAD:**
```yaml
diagram_data:
  angle_x:
    label: "x = 147°"  # ← WRONG: Answer visible!
```

✅ **GOOD:**
```yaml
diagram_data:
  angle_x:
    label: "∠ABC = x"  # ← CORRECT: Label only, no value
```

### Violation 2: Solution steps in diagram_data

❌ **BAD:**
```yaml
diagram_data:
  annotation:
    text: "Total = 120 - 4 = 116"  # ← WRONG: Calculation visible!
```

✅ **GOOD:**
```yaml
diagram_data:
  axis_label:
    text: "120"  # ← CORRECT: Only the value, no calculation
```

### Violation 3: Derived values in diagram_data

❌ **BAD:**
```yaml
diagram_data:
  volume:
    value: "240,000 cm³"  # ← WRONG: Calculated value!
```

✅ **GOOD:**
```yaml
diagram_data:
  tank_dimensions:
    label: "60 cm × 80 cm"  # ← CORRECT: Only dimensions shown on original
```

---

## Validation Checklist

Before committing a YAML file, verify:

- [ ] `diagram_data:` section exists and contains only visual elements
- [ ] `question_text:` section exists with full question
- [ ] `answer_key:` section exists with answer(s)
- [ ] NO values from `solution:` or `answer_key:` appear in `diagram_data:`
- [ ] NO calculations appear in `diagram_data:`
- [ ] NO solution steps appear in `diagram_data:`
- [ ] All labels in `diagram_data:` match original exactly
- [ ] All dimensions/angles in `diagram_data:` match original exactly
- [ ] Renderer only reads `diagram_data:` section (validation test)

---

## Impact on Stages

**Stage 1 (Deconstruction):**
- Vision LLM must extract diagram data → `diagram_data:`
- Vision LLM must extract question text → `question_text:`
- NO mixing between sections

**Stage 2 (Baseline PDF Generation):**
- Renderer reads `diagram_data:` only
- Renderer adds question text from separate input
- PDF shows diagram + question (no solutions)

**Stage 3-5 (Testing/Intervention):**
- Students see diagram + question (no solutions)
- Solvability test passes only if separation maintained

---

## Iterating and Improving Spirit (SOR v4.5)

**From Stage 0 Finding 1 — "Separate question data from diagram data"**

This schema enforces the separation by:
1. Clear structure with two distinct sections
2. Explicit rules for what goes in each
3. Validation checklist for compliance
4. Examples of common violations
5. Renderer responsibilities defined

**Apply this to all new YAML files created during Stage 1-5.**

---

*Created: 2026-04-22 based on Stage 0 Finding 1*
*Applies to: SOR v4.5 and all ATOM-SG Pilot work*
