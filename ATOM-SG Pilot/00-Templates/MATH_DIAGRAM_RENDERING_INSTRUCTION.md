# Math Diagram Rendering — Agent Instruction

Before drawing anything, run these four gates in order. Each can reject your approach.

---

## CRITICAL REQUIREMENT: Diagram vs Question Data Separation

**Fix 1 (Stage 0 Finding):** Separate diagram data from question data.

The renderer MUST:
1. **Only read `diagram_data:` section** — Ignore `question:`, `solution:`, `answer_key:` sections
2. **Validate diagram structure** — Check all required fields present
3. **Render visual elements ONLY** — No question text, no solutions, no answers
4. **Test solvability** — Given diagram + question text (from separate input), can student solve?

**Reference:** [YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md](YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md)

**Why:** If solutions or answers leak into diagram rendering, students see answers before solving. This violates the solvability test.

---

## Gate 0 — Solve First

Solve the problem to completion before choosing a visual. If you cannot solve it, you cannot draw it. Stop and say so.

## Gate 1 — Audience Constraint Check

Identify what the target learner **cannot** use:

| Level | Cannot use | Use instead |
|-------|-----------|-------------|
| P1–P2 | Multiplication, division, variables | Counting, grouping, concrete objects |
| P3–P4 | Algebra, ratios, negative numbers | Bar models, suppose heuristic, guess-and-check |
| P5–P6 | Simultaneous equations, formal algebra | Unitary method, suppose heuristic, bar models |

**Read every planned label and annotation. If any require a concept the learner has not learned, redesign.** This is the most important gate. Common violations: writing `3(n−1) = 27` for primary students, drawing "n units" when n is unknown, using "∴" or "deficit" or "surplus" instead of "so" or "left over" or "short by."

## Gate 2 — Map the Reasoning Chain

Write the step-by-step reasoning a student at the target level would use, using only their tools. Your diagram must make **each step** visible. If a step has no visual anchor, the learner skips it.

## Gate 3 — Plan Scale

Choose a pixels-per-unit scale for all bars that will be compared. Write it down. If two quantities use different scales, they must appear in visually separated panels (whitespace + header between them). Within a panel, a 25-unit segment must be 5× the width of a 5-unit segment — no exceptions.

---

## Visual Strategies

Pick based on the reasoning chain, not the problem type.

**Direct comparison** — Two bars, same start, different lengths. For known quantities where the difference is the focus.

**Part-whole** — One bar split into labelled segments. For a total broken into components.

**Transformation / Suppose** — Show what changes between two scenarios. For problems with two conditions on the same unknown total, especially when you cannot draw the unknowns directly. See "Suppose Method" below.

**Grouping** — A bar divided into equal groups with a count. For when the solve step is a division.

**Stacked multi-step** — Multiple panels building on each other. For problems where no single bar captures the full logic. Most non-trivial problems use this.

---

## The Suppose Method (Excess-and-Shortage)

Use when: two conditions on the same total, number of groups unknown, so you cannot draw the groups.

**Panel 1 — Establish facts.** Show both scenarios as statements with visual annotations. For "shortage" show a bar split into [what they get] + [shortfall]. For "excess" label the surplus.

**Panel 2 — Per-unit comparison.** Two bars (one per scenario), same scale, left-aligned. Highlight the difference: "each needs X more."

**Panel 3 — Total adjustment.** Single bar: [excess] + [shortage] side by side. Bracket labelled with the sum. This converts two abstract conditions into one concrete number.

**Panel 4 — Grouping solve.** Divide the total bar into equal groups of [per-unit difference]. Count them. That is the answer.

**Panel 5 — Answer + check.** Verify against both original conditions.

Scale: Panels 2 uses one scale. Panels 3–4 share a second scale. Separate them visually.

---

## 3D and Isometric Diagrams

Three distinct sub-types. Each requires a different rendering approach.

### Sub-type A — 3D Solids with Dimensions (Cuboids, Prisms, Cylinders)

Example: a cuboid container with water level, labelled height/width/length, and a "?" on the unknown dimension.

**Isometric projection rules:**
- Use 30° isometric: x-axis at +30° from horizontal (right), y-axis at -30° (left), z-axis vertical.
- Conversion: for a point (x, y, z) in 3D space →
  ```
  screen_x = origin_x + (x - y) × cos(30°)
  screen_y = origin_y - z + (x + y) × sin(30°) × 0.5
  ```
- Visible faces: top, right, front. Back edges drawn as dashed lines or omitted.
- All parallel edges in 3D remain parallel on screen. No perspective convergence.

**Dimension lines on 3D solids:**
- Place dimension arrows along the **front-facing edges only** — never along a receding (depth) edge, as foreshortening distorts the measurement.
- If a depth dimension must be labelled, extend a leader line to clear space and label it there.
- The dimension line sits **outside the shape**, offset 10–15px from the nearest edge, parallel to the edge it measures.
- For height labels (vertical), place to the right of the front face. For width (horizontal), place below the front face. For depth (receding), place along the top face edge.

**Water level / partial fill rendering:**
- The water surface is a horizontal plane cutting through the solid. Draw it as a filled rectangle matching the cross-section at that height.
- Visible water edges: front face water line (solid), right face water line (solid), top water surface (solid outline with light fill or hatching).
- The fill/shading (hatching, stipple, or light grey) applies only to the visible faces below the water line — front face and right face portions below the water surface.
- Air gap above water: no fill — just the outline of the container.

**When variables change:**
- Dimension labels update. Dimension arrow lengths update.
- Water level height recomputes from new volume / base area.
- Visible face fill region resizes.

### Sub-type B — Cube Nets (2D Flat Patterns)

Example: four net options, student identifies which fold into a valid cube.

**These are 2D diagrams, not 3D renders.** Render on a unit grid.

**Grid rules:**
- Every face is a square of identical size (e.g., 40×40px). All squares snap to the grid.
- Adjacent faces share exactly one full edge — no partial overlaps, no gaps.
- All edges aligned to grid axes (no rotated squares).
- Edge lines between adjacent faces: thin (0.5px) internal, medium (1.5px) external outline.

**Layout for multiple net options:**
- Space nets horizontally with at least 1.5× face-width gap between them.
- Label each net (A, B, C, D) below or above.
- If a reference cube is shown, draw it as a simple isometric wireframe above the nets, centered.

**Parametric approach:**
```yaml
net:
  face_size: 40           # px per face
  layout: [[0,0], [0,1], [0,2], [0,3], [1,1], [-1,1]]  # grid positions
  # Each [col, row] places one face. Change layout to show different nets.
```

**When variables change:**
- For variant generation, swap the `layout` array. Face size stays constant.
- Optionally shade specific faces to test "which face is opposite which" questions.

### Sub-type C — Isometric Stacked Cubes (Multi-View Problems)

Example: an L-shaped solid made of 10 unit cubes, with "Front view," "Side view," "Top view" labels.

**This is the hardest sub-type.** The isometric view must be geometrically correct so the student can count cubes and deduce views.

**Cube-grid approach:**
- Define the solid as a 3D occupancy grid: a list of (x, y, z) positions where a unit cube exists.
  ```yaml
  cubes: [[0,0,0], [1,0,0], [2,0,0], [0,1,0], [0,0,1], ...]
  ```
- Render using the isometric projection from Sub-type A. Each cube = 6 faces projected.

**Visible face computation (critical for correctness):**
- For each cube face, check if the adjacent cell in that face's normal direction is occupied. If occupied, the face is hidden (interior). If empty, the face is visible.
- Visible faces only: top (z+1 empty), right (x+1 empty), front (y-1 empty, depending on orientation convention).
- Hidden edges between adjacent cubes on the same face: omit or draw as very light lines.
- Outline edges (where the solid meets air): draw solid, 1.5px.
- Internal grid edges (between cubes on the same visible face): draw thin, 0.5px.

**View labels:**
- "Top view," "Front view," "Side view" placed outside the solid with flow arrows indicating viewing direction.
- Arrows point toward the solid from the labelled viewing direction.
- Labels positioned to not overlap the solid or each other.

**Shading for depth (optional but recommended):**
- Top faces: lightest shade.
- Front faces: medium shade.
- Right/side faces: darkest shade.
- This gives the illusion of a light source from top-left, helping the student perceive the 3D form.

**When variables change:**
- Adding or removing a cube from the occupancy grid recomputes all visible faces.
- View projection diagrams (2D front/side/top views) recompute as grid squares shaded where cubes are present at that row/column.

---

## Rendering Anti-Patterns

- **Algebra in disguise.** `3(n−1) = 27` inside a rectangle is an equation, not a bar model.
- **Unknown block counts.** Drawing "n parts" when n is the unknown. If you cannot count it, do not draw it.
- **Decorative brackets.** A bracket labelled "30" must span content that sums to exactly 30 at the diagram's scale.
- **Scale betrayal.** Two segments meant to show 5:1 drawn at 2:1.
- **Reasoning leaps.** Jumping from "3 more per girl" to "10 girls" without showing the 30 in between.
- **Adult vocabulary.** "Hence," "deficit," "∴" → use "so," "short by," plain language.
- **Orphaned elements.** Any unlabelled, unreferenced segment — delete it.
- **Inverted comparison.** Smaller quantity drawn as the longer bar.
- **Perspective on isometric.** Converging lines on a diagram that should use parallel projection. Isometric = all parallel edges stay parallel.
- **Wrong visible faces.** Drawing the back face of a 3D solid as visible, or omitting a front face. Apply the painter's algorithm: render far cubes first, near cubes last.
- **Net with wrong adjacency.** Two net faces sharing a partial edge, or separated by a gap. Every shared edge must be a full face-width.
- **Inconsistent cube shading.** All top faces must share the same shade. All front faces must share the same shade. Mixed shading destroys depth perception.
