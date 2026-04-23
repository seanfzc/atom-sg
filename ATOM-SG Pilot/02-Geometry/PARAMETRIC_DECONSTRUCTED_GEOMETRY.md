# Parametric Deconstructed Geometry Data
## 4-Gates + Parametric Approach

**Date:** 2026-04-19  
**Source:** ACS Junior, Nanyang, Henry Park, Nan Hua, Raffles Girls 2025 Prelims  
**Method:** Variable-driven, reasoning-first diagrams

---

## Q15 (ACS Junior): Overlapping Quarter Circles

### Gate 0 — Solve First

**Given Variables:**
- `radius = 10` cm (constant)
- `shaded_area = 30` cm²
- `perimeter_OBC = 26` cm

**Derived Variables:**
- `arc_BC = perimeter_OBC - 2*radius = 26 - 20 = 6` cm
- `arc_angle = (arc_BC * 360) / (2 * π * radius) = 34.4°`
- `area_quarter = 0.25 * π * radius² = 78.5` cm²
- `area_OABCD = 2*area_quarter - shaded_area = 127` cm²

**Solution:**
1. Perimeter OBC = OB + OC + arc_BC
2. 26 = 10 + 10 + arc_BC
3. arc_BC = 6 cm
4. Area OABCD = 78.5 + 78.5 - 30 = 127 cm²

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Use π = 3.14
- ✓ Fractions (¼)
- ✓ No algebra variables
- ✓ Plain language

**Labels:**
- "10 cm" (not "r = 10")
- "shaded area" (not "sector OBC")

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Multi-panel with parametric overlays

**Panel 1:** Establish Geometry
- Show two quarter circles with shared center O
- Radius = 10 cm (parametric: `radius`)
- Label points A, B, C, D

**Panel 2:** Find Arc BC
- Show: 26 - 10 - 10 = 6
- Arc BC = 6 cm
- Visual: Arc length indicator

**Panel 3:** Calculate Area
- Show: 78.5 + 78.5 - 30 = 127
- Visual: Two quarter circles minus overlap

**Panel 4:** Verify with Angle
- Show arc_angle = 34.4°
- Visual: Angle arc at center O

### Gate 3 — Parametric Scale

```yaml
variables:
  radius: 10
  arc_BC: 6
  arc_angle: 34.4
  scale_factor: 0.3  # cm to plot units

elements:
  center_O:
    x: 5
    y: 2
    
  points:
    A: [center_O.x + radius*scale*cos(90°), center_O.y + radius*scale*sin(90°)]
    B: [center_O.x + radius*scale*cos(90°), center_O.y + radius*scale*sin(90°)]
    C: [center_O.x + radius*scale*cos(90°-arc_angle), center_O.y + radius*scale*sin(90°-arc_angle)]
    D: [center_O.x + radius*scale*cos(90°-arc_angle-90°), center_O.y + radius*scale*sin(90°-arc_angle-90°)]
    
  quarter_circle_1:
    center: center_O
    radius: radius * scale
    start_angle: 90° - arc_angle
    end_angle: 90°
    
  quarter_circle_2:
    center: center_O
    radius: radius * scale
    start_angle: 90° - arc_angle - 90°
    end_angle: 90° - arc_angle
    
  shaded_sector:
    center: center_O
    radius: radius * scale
    start_angle: 90° - arc_angle
    end_angle: 90°
    fill: light_blue
```

---

## Q13 (ACS Junior): Rhombus + Trapezium Angle Chasing

### Gate 0 — Solve First

**Given Variables:**
- `angle_DFE = 21°`
- `angle_BCD = 108°`
- `angle_DAB_given = 33°`

**Rhombus Properties (Implicit):**
- `angle_BAD = angle_BCD = 108°` (opposite angles)
- `angle_ADC = 180° - 108° = 72°` (consecutive supplementary)
- `angle_ABC = 72°`

**Trapezium ADEF Properties:**
- `AF || DE` (given)
- Consecutive interior angles supplementary

**Find:** x and y

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Angle properties of rhombus
- ✓ Parallel line properties
- ✓ No algebra
- ✓ Plain geometric terms

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Step-by-step angle marking with color coding

**Step 1:** Mark rhombus angles
- Show: angle BAD = 108° (opposite BCD)
- Show: angle ADC = 72°

**Step 2:** Use trapezium parallel lines
- AF || DE
- Show angle relationships

**Step 3:** Calculate x and y
- Trace angle chasing path

### Gate 3 — Parametric Scale

```yaml
variables:
  angle_BCD: 108
  angle_DFE: 21
  angle_DAB_input: 33
  
  # Derived
  angle_BAD: 108  # opposite in rhombus
  angle_ADC: 72   # 180 - 108
  angle_ABC: 72

elements:
  rhombus_ABCD:
    type: polygon
    vertices: [A, B, C, D]
    properties:
      - AB = BC = CD = DA
      - angle_BAD = angle_BCD
      - angle_ADC = angle_ABC
      
  trapezium_ADEF:
    type: polygon
    vertices: [A, D, E, F]
    properties:
      - AF || DE
      
  angles:
    - vertex: BCD
      value: 108°
      color: red
    - vertex: DFE
      value: 21°
      color: blue
    - vertex: DAB_input
      value: 33°
      color: green
```

---

## Q12 (ACS Junior): Five Squares in Rectangle

### Gate 0 — Solve First

**Given Variables:**
- `square_X = 4` cm

**Arrangement Analysis:**
- 5 squares arranged in rectangle
- Square X = 4 cm (smallest)
- Need to deduce other square sizes from arrangement

**Typical Arrangement:**
- Squares arranged in 2 rows or specific pattern
- Let Y = side of square Y
- Relationships from adjacency

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Spatial reasoning
- ✓ Area calculation
- ✓ No algebra
- ✓ Visual deduction

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Show arrangement with dimension labels

**Step 1:** Show 5 squares in rectangle
- Label square X = 4 cm
- Show arrangement pattern

**Step 2:** Deduce sizes
- From adjacency relationships
- Show Y and other squares

**Step 3:** Calculate rectangle dimensions
- Length = sum of sides
- Width = max height

**Step 4:** Calculate cubes from 2cm squares
- Total area ÷ 4

### Gate 3 — Parametric Scale

```yaml
variables:
  square_X: 4
  # Deduce from arrangement
  square_Y: 6  # example - depends on actual arrangement
  square_Z: 10 # example
  
  rectangle:
    length: square_X + square_Y + square_Z  # depends on arrangement
    width: max([square_X, square_Y, square_Z])
    
  total_area: rectangle.length * rectangle.width
  num_2cm_cubes: total_area / 4

elements:
  squares:
    - id: X
      side: square_X
      position: [0, 0]
    - id: Y
      side: square_Y
      position: [square_X, 0]
    # ... etc
    
  rectangle_boundary:
    width: rectangle.length
    height: rectangle.width
    style: dashed
```

---

## Q19 (Nanyang): 3D Solid Views

### Gate 0 — Solve First

**Given Variables:**
- `total_cubes = 7`
- Given: top view, side view

**Find:** Front view on grid

**Constraint Satisfaction:**
- Front view must match visible heights
- Hidden cubes don't appear
- Top and side views constrain column heights

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Spatial visualization
- ✓ Orthographic projection
- ✓ Counting
- ✓ No algebra

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Multi-view with grid overlay

**Step 1:** Show isometric solid
- 7 cubes in arrangement
- Label views

**Step 2:** Show top view
- Grid with heights

**Step 3:** Show side view
- Grid with heights

**Step 4:** Derive front view
- Match constraints
- Draw on grid

### Gate 3 — Parametric Scale

```yaml
variables:
  total_cubes: 7
  grid_size: 1  # cm
  
  # Cube positions (x, y, z)
  cubes:
    - [0, 0, 0]
    - [0, 0, 1]
    - [1, 0, 0]
    - [1, 0, 1]
    - [1, 0, 2]
    - [2, 0, 0]
    - [2, 0, 1]
    
  # Views
  top_view:
    grid: 3x1
    heights: [[2, 3, 2]]  # max height at each position
    
  side_view:
    grid: 1x3
    heights: [[2, 3, 2]]
    
  front_view:
    grid: 3x3  # to be filled

elements:
  isometric_solid:
    cubes: cubes
    angle: 30°
    
  views:
    - type: top
      grid: top_view.grid
      heights: top_view.heights
    - type: side
      grid: side_view.grid
      heights: side_view.heights
    - type: front
      grid: front_view.grid
      fill: student_answer
```

---

## Q20 (Nanyang): Cuboid Completion

### Gate 0 — Solve First

**Given Variables:**
- `existing_cubes = 7`
- Arrangement: irregular solid

**Find:** Minimum cubes to add to form cuboid

**Bounding Box:**
- Find minimal enclosing rectangular prism
- `cuboid_volume = length × width × height`
- `additional_cubes = cuboid_volume - existing_cubes`

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Spatial reasoning
- ✓ Volume calculation
- ✓ No algebra
- ✓ Minimization concept

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Before/after with bounding box

**Step 1:** Show existing solid
- 7 cubes in arrangement
- Count and show dimensions

**Step 2:** Determine bounding box
- Show minimal enclosing cuboid
- Mark dimensions

**Step 3:** Calculate
- Total cubes needed
- Subtract existing

**Step 4:** Show answer
- Additional cubes highlighted

### Gate 3 — Parametric Scale

```yaml
variables:
  existing_cubes: 7
  
  # Bounding box dimensions
  bbox:
    length: 3  # max x extent
    width: 2   # max y extent
    height: 3  # max z extent
    
  cuboid_volume: bbox.length * bbox.width * bbox.height
  additional_cubes: cuboid_volume - existing_cubes

elements:
  existing_solid:
    cubes: [[0,0,0], [0,0,1], [1,0,0], [1,0,1], [1,0,2], [2,0,0], [2,0,1]]
    color: blue
    
  bounding_box:
    dimensions: [bbox.length, bbox.width, bbox.height]
    style: dashed_wireframe
    color: gray
    
  additional_positions:
    # Positions to fill
    - [0, 1, 0]
    - [0, 1, 1]
    # ... etc
    color: red_transparent
```

---

## Q18 (Nanyang): Grid Symmetry / Reflection

### Gate 0 — Solve First

**Given Variables:**
- `existing_shaded = 9`
- `to_add = 3`
- Mirror line: diagonal AB

**Constraint:**
- Every shaded square must have mirror image across AB
- Final figure symmetric

### Gate 1 — Audience Check

**P5-P6 Appropriate:**
- ✓ Reflection concept
- ✓ Grid counting
- ✓ No algebra
- ✓ Spatial reasoning

### Gate 2 — Map Reasoning Chain

**Visual Strategy:** Grid with mirror line and reflection indicators

**Step 1:** Show existing shaded squares
- 9 squares on grid
- Mark diagonal AB

**Step 2:** Identify mirror pairs
- Show which squares already have mirrors
- Identify 3 missing mirrors

**Step 3:** Shade additional squares
- Complete symmetry

### Gate 3 — Parametric Scale

```yaml
variables:
  grid_size: 6  # 6x6 grid
  existing_shaded:
    - [0, 0]
    - [0, 1]
    - [1, 0]
    - [1, 1]
    - [2, 2]
    - [3, 3]
    - [4, 4]
    - [4, 5]
    - [5, 4]
    
  mirror_line:
    type: diagonal
    from: [0, 5]
    to: [5, 0]
    
  to_add: 3
elements:
  grid:
    size: grid_size
    lines: true
    
  shaded_squares:
    positions: existing_shaded
    color: blue
    
  mirror_line:
    path: mirror_line
    style: dashed_red
    
  reflection_indicators:
    # Arrows showing mirror pairs
    - from: [0, 0]
      to: [5, 5]
      style: curved_arrow
```

---

## Implementation Notes

### Parametric Rendering Principles

1. **All positions derived from variables**
   - Never hardcode coordinates
   - Use expressions like `center.x + radius * cos(angle)`

2. **Labels anchored to elements**
   - Label position = anchor position + offset
   - Offset direction based on element geometry

3. **Collision detection**
   - Check all label bounding boxes
   - Adjust offsets if overlap detected

4. **Scale consistency**
   - Single scale factor for entire diagram
   - Proportions must be exact

### Audit Checklist per Question

- [ ] Unit equality (bars, segments)
- [ ] Label binding (unambiguous)
- [ ] Numeric consistency
- [ ] Scale consistency
- [ ] Pedagogical sanity
- [ ] Audience appropriateness

---

*Next: Generate parametric diagrams for all questions*
