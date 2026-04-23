# Geometry Taxonomy: Nano‑Nodes for P5–P6
*Derived from ATOM‑SG schema v4.1 and Singapore MOE syllabus*

## Scope
- **Grade levels:** Primary 5 and Primary 6 only (Singapore Maths)
- **Focus:** Geometry‑specific skills; no algebra, data, or other strands
- **Schema alignment:** Maps to `geometry_measurement` and `geometry_properties` logic families in ATOM‑SG v4.1
- **Format:** Each “nano‑node” is a granular, assessable skill that can be:
  - Described in a rubric (`Geometry‑Rubrics.md` template)
  - Linked to an equation shadow (algebraic/arithmetic representation)
  - Mapped to starter problems (P5‑Problem‑* or DI‑Problem‑*)

## Nano‑Node List
*Each entry is a value for the `subpathway` field in `Geometry‑Rubrics.md`*

### Geometry Measurement (`geometry_measurement`)
1. **Identify and measure angles using a protractor**  
   - Recognizes acute, right, obtuse, straight, reflex angles  
   - Measures to nearest degree (0–180°, 180–360° for reflex)

2. **Calculate perimeter of rectilinear figures**  
   - Sums side lengths of polygons (including missing lengths)  
   - Handles composite shapes made of rectangles

3. **Calculate area of composite rectangular figures**  
   - Breaks L‑shapes, U‑shapes into rectangles  
   - Applies area formula (length × breadth) and sums

4. **Calculate volume of cubes and cuboids**  
   - Uses formula (length × breadth × height)  
   - Converts between cm³, m³, litres where applicable

5. **Convert between units of measurement (length, area, volume)**  
   - cm ↔ m, cm² ↔ m², cm³ ↔ m³ ↔ litres  
   - Understands squared/cubed unit relationships

6. **Draw triangles/quadrilaterals given dimensions**  
   - Uses ruler, protractor, set‑square appropriately  
   - Achieves specified side lengths and angles

7. **Identify line(s) of symmetry in 2D shapes**  
   - Recognizes reflective symmetry  
   - Draws symmetry lines for regular polygons

8. **Complete symmetrical figures given mirror line**  
   - Reflects points across vertical/horizontal/diagonal lines  
   - Maintains shape and proportions

### Geometry Properties (`geometry_properties`)
9. **Classify triangles by sides (equilateral, isosceles, scalene)**  
   - Recognizes equal‑side patterns  
   - Uses geometric notation (dashes for equal sides)

10. **Classify triangles by angles (acute, right, obtuse)**  
    - Applies angle‑sum property (180°)  
    - Identifies right angles (90°) in diagrams

11. **Classify quadrilaterals (square, rectangle, parallelogram, rhombus, trapezium)**  
    - Knows defining properties (parallel sides, equal sides, angles)  
    - Distinguishes between similar types (rectangle vs. square)

12. **Use angle properties to find unknown angles**  
    - Angles on a straight line sum to 180°  
    - Angles at a point sum to 360°  
    - Vertically opposite angles are equal

13. **Apply angle sum of triangle (180°) to find missing angles**  
    - Solves for third angle given two angles  
    - Handles isosceles triangles (base angles equal)

14. **Identify perpendicular and parallel lines in diagrams**  
    - Recognizes right‑angle notation  
    - Uses arrow notation for parallel lines

15. **Understand circle vocabulary (radius, diameter, circumference)**  
    - Knows relationships: diameter = 2 × radius  
    - Distinguishes between circumference (perimeter) and area

16. **Calculate circumference/area of circle using π**  
    - Uses formulas C = πd or C = 2πr, A = πr²  
    - Approximates π as 3.14 or 22/7 as appropriate

17. **Interpret pie charts as fractions of a circle**  
    - Relates sector angle to proportion (angle/360°)  
    - Extracts data from pie‑chart questions

18. **Visualize nets of cubes/cuboids and identify 3D shapes from nets**  
    - Recognises folding patterns  
    - Counts faces, edges, vertices

## Baseline Test Framework Integration
*Aligned with Geometry Baseline Test Framework (Telegram thread topic 55) and GeoBot's Problem‑Pack Plan*

### Four Sub‑Pathways (G1–G4)
1. **G1 Angle Reasoning** – Angle measurement, properties, angle sums, perpendicular/parallel lines.
2. **G2 Area & Perimeter** – Rectilinear figures, composite rectangles, unit conversion, symmetry.
3. **G3 Volume & 3D** – Volume of cubes/cuboids, nets, spatial visualization.
4. **G4 Properties & Classification** – Triangle/quadrilateral classification, circle properties, pie‑chart interpretation.

### 25‑Item Distribution (Difficulty Zones A–D)
- **G1:** 8 items (A‑D)
- **G2:** 8 items (A‑D)  
- **G3:** 4 items (A‑D)
- **G4:** 5 items (A‑D)

### Enhanced Diagnostic Rubric (4 dimensions, 5 points max per item)
1. **Pathway Identification** – Correctly identifies sub‑pathway (G1–G4).
2. **Equation‑Shadow Setup** – Translates geometry problem into appropriate algebraic skeleton.
3. **Algebraic Execution** – Solves the equation shadow accurately.
4. **Explanation & Justification** – Provides clear reasoning for steps.

### Complexity Scoring Integration (4‑axis profile per item)
- **Cognitive Load** – Number of steps, working‑memory demand.
- **Visual‑Linguistic Integration** – Diagram complexity, text‑to‑visual mapping.
- **Conceptual Abstraction** – Level of abstraction (concrete → abstract).
- **Contextual Load** – Real‑world knowledge required.

### Mapping to Nano‑Nodes
Each of the 25 items in GeoBot's Problem‑Pack Plan (`ATOM‑SG Pilot/02‑Geometry/Problem‑Pack‑Plan.md`) maps to a specific nano‑node from this taxonomy, ensuring alignment between skill definitions and baseline assessment items.

## Equation Shadows
*Each nano‑node can be represented by a symbolic “shadow” that captures its core arithmetic/algebraic structure.*

| Nano‑Node | Equation Shadow | Notes |
|-----------|----------------|-------|
| Measure angles | `angle = protractor_reading` (0–180°) | Direct measurement, no calculation |
| Area of composite rectangles | `total_area = Σ(area_of_rectangle_i)` | Summation of rectangular areas |
| Angles on straight line | `∠A + ∠B = 180°` | Linear pair property |
| Angle sum of triangle | `∠A + ∠B + ∠C = 180°` | Interior angles |
| Circumference of circle | `C = π × d` or `C = 2 × π × r` | π ≈ 3.14 or 22/7 |
| Volume of cuboid | `V = l × b × h` | Consistent units required |
| Unit conversion (length) | `1 m = 100 cm` | Multiplication/division by powers of 10 |
| Symmetry completion | `(x, y) → (x, −y)` (vertical reflection) | Coordinate‑transformation view |

## Articulation Rubric Template
*Use the three‑level rubric in `Geometry‑Rubrics.md` to define proficiency for each nano‑node.*

**Level 1 (Basic):** Can perform skill with scaffolding, simple cases, or high error tolerance.  
**Level 2 (Proficient):** Executes skill accurately in standard P5/P6 contexts.  
**Level 3 (Advanced):** Applies skill flexibly in novel or multi‑step problems; explains reasoning.

Example for *“Calculate area of composite rectangular figures”*:
- **Level 1:** Identifies rectangles in composite figure; adds areas of visible rectangles.
- **Level 2:** Breaks composite figure into non‑overlapping rectangles; calculates total area correctly.
- **Level 3:** Handles figures with missing sections (L‑shapes); applies formula efficiently; checks units.

## Starter Problem Mapping
*Link each nano‑node to existing or new starter problems.*

| Nano‑Node | Suggested Problem ID | Problem Sketch |
|-----------|---------------------|----------------|
| Identify/measure angles | P5‑Problem‑ANG01 | Diagram with angles marked; measure ∠A, ∠B, ∠C |
| Area of composite rectangles | P5‑Problem‑AREA01 | L‑shape figure with given side lengths; find area |
| Angles on straight line | P6‑Problem‑ANG01 | Two angles on line; one given, find the other |
| Circle circumference | P6‑Problem‑CIRC01 | Circle with radius 7 cm; find circumference (π = 22/7) |
| Volume of cuboid | P5‑Problem‑VOL01 | Box dimensions 5 cm × 8 cm × 10 cm; find volume |

**Problem‑naming convention:**
- `P5‑Problem‑<TOPIC><NN>` for Primary 5
- `P6‑Problem‑<TOPIC><NN>` for Primary 6
- Store in `ATOM‑SG Pilot/01‑Projects/` or relevant problem bank.

## Integration with ATOM‑SG Schema
- **Logic families:** All nano‑nodes map to `geometry_measurement` or `geometry_properties`.
- **Vertical evolution:** P5 nodes can link forward to P6 refinements (e.g., P5 angle measurement → P6 angle properties).
- **Paper 1 alignment:** Flag nano‑nodes that appear in non‑calculator papers (`calculator_required: false`).
- **Game‑design hooks:** Each nano‑node suggests a game mechanic (e.g., “Angle Measurer” protractor mini‑game, “Area Builder” rectangle‑assembly game).

## Next Steps
1. **Review nano‑node list** – confirm completeness for P5–P6 geometry.
2. **Populate `Geometry‑Rubrics.md`** with 3–5 detailed examples (using the template).
3. **Create starter problems** for high‑priority nano‑nodes (2–3 problems each).
4. **Engage PM** for owner assignment and timeline.
5. **Link to existing ATOM‑SG pilot data** (e.g., Rosyth P6 questions that test geometry).

---
*Created: 2026‑04‑12 | Owner: [PM to assign] | Due: [TBD] | Status: Draft*