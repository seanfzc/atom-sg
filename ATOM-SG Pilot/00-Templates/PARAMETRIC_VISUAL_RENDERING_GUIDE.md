# Parametric Math Visual Rendering Guide

## Core Principle

Every visual element is a **function of the question's variables**, not a fixed coordinate. When a variable changes, every dependent element — shapes, labels, arrows, shading, captions — recomputes automatically.

```python
# BAD: fixed coordinates
label_x = 150
label_y = 80

# GOOD: derived from what the label describes
label_x = edge_midpoint(A, B).x
label_y = edge_midpoint(A, B).y - LABEL_OFFSET
```

---

## The Parametric Data Model

Every question defines variables. Every visual element references those variables.

```yaml
question:
  variables:
    num_boys: 12
    num_girls: 18
    total: 30          # derived: num_boys + num_girls
    boy_fraction: 0.4  # derived: num_boys / total

  visual:
    type: pie_chart
    slices:
      - label: "Boys"
        value: $num_boys          # ← references variable
        start_angle: 0            # ← computed: 0
        sweep_angle: 144          # ← computed: $boy_fraction × 360
      - label: "Girls"
        value: $num_girls
        start_angle: 144          # ← computed: previous end
        sweep_angle: 216          # ← computed: (1 - $boy_fraction) × 360
```

Change `num_boys` to 15, and the pie redraws with correct angles, labels, leader lines — no manual adjustment.

---

## Universal Label Placement Rules

These apply to every chart type. Specific types add rules on top.

### Rule 1 — Labels are anchored to elements, never to coordinates

Every label has an **anchor** (the element it describes) and an **offset** (distance from that anchor). Store these, not the final position.

```yaml
label:
  text: "12 cm"
  anchor: edge(A, B)        # what it describes
  position: midpoint         # where on the anchor
  offset_direction: above    # which side
  offset_distance: 8px       # how far
  # final_x and final_y are COMPUTED from the above
```

### Rule 2 — Label collision detection is mandatory

After computing all label positions, check every pair for overlap. When two labels collide:
1. Move the less important one further from its anchor (increase offset).
2. If still colliding, shift it along the anchor's axis (slide along the edge).
3. As a last resort, use a leader line to place the label in clear space.

Never skip this step. Label overlap is the single most common visual error in AI-generated diagrams.

### Rule 3 — Labels stay within the canvas

After computing position, clamp to canvas bounds with padding:
```python
final_x = clamp(computed_x, PADDING, canvas_width - PADDING - text_width)
final_y = clamp(computed_y, PADDING, canvas_height - PADDING)
```

### Rule 4 — Labels never cross lines they don't describe

A label's bounding box (text extents + 2px padding on all sides) must not intersect any edge, axis, gridline, arrow, or shape boundary **except the one it is anchored to**. If it does, move the label to the other side of its anchor. If both sides collide, use a leader line to clear space.

### Rule 5 — Label proximity (as close as possible)

Labels must sit at the **minimum distance** from their anchor element that avoids collision with other elements. The offset is not a style choice — it is computed:

```python
offset = max(MIN_OFFSET, smallest_distance_without_collision)
```

Where `MIN_OFFSET` = 6px for inline labels, 8px for labels with leader lines.

A label 40px from its edge when 8px was achievable creates ambiguity about which element it describes. Flag this in audits.

### Rule 6 — Label bounding box clearance

After placing all labels, verify every pair:
```python
for each pair (label_A, label_B):
  if bounding_boxes_overlap(label_A, label_B):
    shift the less important label (smaller font / annotation > data label > axis label)
    re-route any attached leader line
```

Minimum clearance between any two label bounding boxes: 2px.

### Rule 7 — Labels on shaded or filled regions

If a label must sit on a shaded/hatched region:
- Verify contrast ratio ≥ 4.5:1 between text colour and background.
- If hatching, place a small opaque background rectangle (matching page background) behind the text — just large enough to cover the text + 2px padding. This prevents hatching lines from crossing through characters.

### Rule 8 — Font sizing hierarchy

| Element | Size | Weight |
|---------|------|--------|
| Chart title | 14px | bold |
| Axis labels | 12px | bold |
| Data labels (values on bars/slices) | 11–12px | normal |
| Tick labels (axis numbers) | 10–11px | normal |
| Annotations / captions | 10–11px | normal |
| Source / footnotes | 9–10px | normal |

Primary school materials: increase all by 1–2px. Never go below 10px.

---

## Chart-Specific Rendering Rules

---

### Bar Charts (Vertical and Horizontal)

**Parametric inputs:**
```yaml
data: [{label: "Mon", value: 12}, {label: "Tue", value: 8}, ...]
axis_max: auto          # computed: round_up(max(values), nice_number)
bar_gap_ratio: 0.3      # gap = bar_width × ratio
orientation: vertical
show_gridlines: true
```

**Bar sizing (computed):**
```python
plot_width = canvas_width - margin_left - margin_right
num_bars = len(data)
bar_width = plot_width / (num_bars + (num_bars + 1) × gap_ratio)
gap = bar_width × gap_ratio
bar_height(value) = (value / axis_max) × plot_height
```

**Label placement:**

| Label type | Position rule |
|-----------|--------------|
| Bar value label | Centered horizontally on bar. Vertically: **inside bar top** if bar is tall enough (value label height + 4px < bar height), otherwise **above bar** with 4px gap. |
| Category label (x-axis) | Centered below each bar, at fixed y below axis line. If text wider than bar, rotate 45° or truncate with ellipsis. |
| Axis title | Centered along axis, outside tick labels. Y-axis title rotated 90° counter-clockwise. |
| Axis tick labels | Right-aligned for y-axis (flush to tick mark with 4px gap). Centered for x-axis. |
| Gridlines | Horizontal lines at each y-axis tick. Extend full plot width. Light grey, 0.5px, behind bars. |

**When variables change:**
- Bar widths recompute from new data count.
- Axis max recomputes (use "nice numbers": 5, 10, 15, 20, 25, 50, 100...).
- Value labels reflow — a label that was inside a tall bar may need to move above a now-shorter bar.
- Category labels recheck for collision if text changed.

**Common errors to prevent:**
- Bar value labels overlapping the axis or other bars when values are close.
- Y-axis not starting at zero (always start at zero for primary math).
- Bars of different widths when they should be uniform.
- Gridlines drawn on top of bars instead of behind.

---

### Pie Charts

**Parametric inputs:**
```yaml
data: [{label: "Chicken", value: 45}, {label: "Fish", value: 30}, ...]
radius: auto             # computed from canvas size
start_angle: -90         # 12 o'clock
label_mode: auto         # auto | inside | outside | legend
```

**Slice computation (computed):**
```python
total = sum(values)
for each slice:
  fraction = value / total
  sweep = fraction × 360
  start = previous_end (or start_angle for first)
  midpoint_angle = start + sweep / 2
```

**Label placement — the hardest chart type for labels:**

**Step 1 — Decide inside vs outside per slice:**
```python
if sweep_angle > 40° AND label fits inside:
  place inside at (center + 0.6 × radius at midpoint_angle)
else:
  place outside with leader line
```

**Step 2 — Outside label layout (when needed):**
```python
# Place labels at radius × 1.15, at the slice's midpoint angle
raw_x = center_x + (radius × 1.15) × cos(midpoint_angle)
raw_y = center_y + (radius × 1.15) × sin(midpoint_angle)

# Leader line: two segments
# Segment 1: from slice edge (radius × 1.02) to elbow (radius × 1.10)
# Segment 2: horizontal from elbow to label

# Text anchor:
#   right half (angle 270°→90°): text-anchor = start, label to the right
#   left half (angle 90°→270°): text-anchor = end, label to the left
```

**Step 3 — Collision resolution for outside labels:**
Sort all outside labels by angle. Walk the sorted list. If two labels' y-positions are within `label_height + 4px`, push the lower one down. After pushing, re-route its leader line to the new position.

**Percentage labels:**
- Display as "45%" not "45.0%" (no decimal for whole percentages).
- Always verify displayed percentages sum to exactly 100%. If rounding causes 99% or 101%, adjust the largest slice's percentage by 1%.
- Place percentage next to or below the category label, never on a separate line across the chart.

**When variables change:**
- All angles recompute.
- Labels switch between inside/outside as slices grow or shrink.
- Leader lines re-route.
- Collision resolution re-runs.
- A slice that was large enough for an inside label may now need an outside one.

**Common errors to prevent:**
- Crossed leader lines (two lines crossing each other to reach their labels).
- Labels placed inside tiny slices where they're unreadable.
- Percentage rounding not summing to 100.
- Slices not starting from 12 o'clock.
- Legend colour swatches not matching actual slice colours.

---

### Bar Models (Singapore Math)

**Parametric inputs:**
```yaml
type: comparison          # comparison | part_whole
bars:
  - label: "Ali"
    value: $ali_amount    # from question variable
    segments: [{value: $known_part, label: "24"}, {value: $unknown, label: "?"}]
  - label: "Ben"
    value: $ben_amount
    segments: [{value: $ben_amount, label: "$ben_amount"}]
bracket:
  spans: [bar_1]          # which bar(s) the bracket covers
  label: "$total"
difference:
  label: "$diff"
  between: [bar_1, bar_2]
```

**Sizing (computed):**
```python
max_value = max(all bar values)
px_per_unit = plot_width / max_value
bar_length(value) = value × px_per_unit

# ALL bars start at the same x (left-aligned, mandatory)
bar_start_x = margin_left + name_label_width + gap
```

**Label placement:**

| Label type | Position rule |
|-----------|--------------|
| Bar name (e.g., "Ali") | Left of bar, right-aligned, vertically centered on bar. Fixed column width = width of longest name + 8px. |
| Segment value | Centered horizontally and vertically within its segment. If segment too narrow (text width + 8px > segment width), place above with leader line. |
| Unknown "?" | Same as segment value but use bold weight. |
| Bracket label | Centered below (or above) the bracket. Bracket spans exactly from left edge of first spanned element to right edge of last. |
| Difference label | Centered on the difference segment (the overhang of the longer bar beyond the shorter). |
| Bracket itself | Curly brace or line with ticks. Endpoints computed from: left = bar_start_x of leftmost spanned segment, right = bar_start_x + bar_length of rightmost spanned segment. |

**When variables change:**
- All bar lengths recompute from new values.
- Segment widths within bars recompute.
- Labels that fit inside segments may need to move outside if segment shrinks.
- Bracket endpoints shift with bar lengths.
- Difference segment length changes.

**Scale rule (critical):**
All bars in a comparison model use the same `px_per_unit`. A bar of value 8 must be exactly half the length of a bar of value 16. Compute, don't eyeball.

**Common errors to prevent:**
- Bars not left-aligned (comparison bars must start at the same x).
- Bracket endpoints not landing on segment boundaries.
- Segments within a bar not summing to the bar's total length.
- "?" placed on a known value instead of the unknown.
- Unit blocks of unequal width when they should be identical.

---

### Line Graphs

**Parametric inputs:**
```yaml
data:
  - series: "Temperature"
    points: [{x: 0, y: 24}, {x: 1, y: 26}, ...]
    style: {stroke: solid, marker: circle}
  - series: "Rainfall"
    points: [...]
    style: {stroke: dashed, marker: square}
x_axis: {label: "Month", ticks: ["Jan", "Feb", ...]}
y_axis: {label: "°C", min: 0, max: 40, step: 5}
```

**Point positioning (computed):**
```python
plot_x(value) = margin_left + (value - x_min) / (x_max - x_min) × plot_width
plot_y(value) = margin_top + plot_height - (value - y_min) / (y_max - y_min) × plot_height
```

**Label placement:**

| Label type | Position rule |
|-----------|--------------|
| Data point labels | Above the point with 6px gap. If above would collide with another point or label, try below, then right, then left. If all four positions collide, skip (rely on axis reading). |
| Axis tick labels | X-axis: centered below tick, 4px gap. Y-axis: right-aligned, 4px left of tick. |
| Series legend | Outside plot area. Prefer top-right or below the chart. Each entry: colour swatch + line style sample + series name. |
| Axis titles | Centered along axis, outside tick labels. |

**When variables change:**
- Points reposition.
- Data labels re-run collision detection.
- Axis scale may need to recompute (new max/min).
- Lines redraw between new point positions.

**Common errors to prevent:**
- Lines connecting wrong data points after reordering.
- Y-axis scale not accommodating new max value.
- Data labels overlapping each other at close-valued points.
- Dashed/solid line styles applied to wrong series.

---

### Timelines

**Parametric inputs:**
```yaml
events:
  - time: "8:00 AM"
    label: "School starts"
    duration: 30           # minutes (optional, for duration bars)
  - time: "8:30 AM"
    label: "Assembly"
    duration: 15
orientation: horizontal    # horizontal | vertical
scale: proportional        # proportional | equal_spacing
```

**Positioning (computed for proportional scale):**
```python
time_to_x(t) = margin_left + (t - start_time) / (end_time - start_time) × timeline_length
```

**Label placement:**

| Label type | Position rule |
|-----------|--------------|
| Event labels | Alternate above and below the timeline to avoid collision. First event above, second below, etc. If an event is too close to its neighbour (< label_width + 8px), stack on the same side with increased offset. |
| Time labels | Below the tick mark on the timeline, centered. |
| Duration bars | Thin rectangles sitting on the timeline, from time_to_x(start) to time_to_x(start + duration). Label centered inside if it fits, above otherwise. |
| Connector lines | Vertical lines from the timeline tick to the event label. Keep thin (0.5px), dashed. |

**When variables change:**
- Event positions shift on the timeline.
- Labels re-alternate and re-check collision.
- Duration bars resize.
- Timeline scale (start/end) may need to expand or contract.

**Common errors to prevent:**
- Events not in chronological order on the visual.
- Proportional spacing distorted (an event at 9:30 not halfway between 9:00 and 10:00).
- Labels piling up when many events are close together.
- Duration bars overlapping when they shouldn't.

---

### Geometry Diagrams (Composite/Overlapping)

**Parametric inputs:**
```yaml
shapes:
  - id: triangle_1
    type: triangle
    # vertices computed from given values
    base: $base_length
    height: $tri_height
    base_angle_left: $angle_A
  - id: circle_1
    type: circle
    center: computed        # e.g., centroid of triangle
    radius: $radius

styles:
  - shape: triangle_1
    edges:
      - [A, B]: {stroke: solid, width: 1.5}
      - [B, C]: {stroke: dashed, width: 1}
  - region: intersection(triangle_1, circle_1)
    fill: {type: hatching, angle: 45, spacing: 4, stroke_width: 0.5}

labels: [...]              # see below
annotations: [...]         # see below
scale_intent: not_to_scale # or to_scale
```

**Label placement for geometry:**

| Label type | Position rule |
|-----------|--------------|
| Side length ("12 cm") | Midpoint of the edge, offset perpendicular to the edge toward the outside of the shape. Offset = 8px. Text parallel to the edge (not rotated for readability — use horizontal text with a leader line if the edge is near-vertical). |
| Angle label ("35°") | Inside the angle, at a distance of 20% of the shorter arm's length from the vertex. The arc or angle marker sits between the two arms. |
| Vertex label ("A") | Outside the shape, 8px from the vertex, in the direction away from the shape's interior (computed: opposite to the centroid direction from that vertex). |
| Right-angle marker | Small square (5×5px) at the vertex, aligned to both arms. The square's sides are parallel to the two arms forming the right angle. |
| Height/construction line label | Midpoint of the construction line, offset to the side with more space. |
| "Not to scale" | Bottom-right corner, italic, small (10px). Always present when `scale_intent: not_to_scale`. |

**Shading and fill patterns (the tricky part):**

For overlap regions:
1. Compute the intersection region as a clipped path.
2. Apply the fill pattern (hatching, dots, solid) only to the clipped region.
3. Draw the fill BEFORE drawing the shape outlines (so outlines sit on top).
4. Draw labels LAST (so they sit on top of everything).

Z-order (bottom to top):
```
1. Background fills (solid colour regions)
2. Pattern fills (hatching, dots) on shaded regions
3. Shape outlines (solid, dashed)
4. Construction lines (dashed, thinner)
5. Markers (right-angle squares, tick marks, arrows)
6. Labels and annotations (always on top)
```

**When variables change:**
- Vertices recompute from new base/height/angle values.
- All labels reposition (they're anchored to edges/vertices, not coordinates).
- Intersection regions recompute.
- Shading/hatching fills new region automatically.
- "Not to scale" flag stays unchanged unless scale_intent changes.

**Common errors to prevent:**
- Label placed inside a shaded region where it's unreadable (move to outside).
- Angle marker on wrong vertex.
- Dashed line style on wrong edge.
- Right-angle marker not aligned to the actual arms of the angle.
- Hatching lines extending beyond the intended region (clipping path error).
- Labels overlapping each other at crowded vertices.

---

### 3D Solids with Dimensions (Cuboids, Prisms, Cylinders)

**Parametric inputs:**
```yaml
type: cuboid
dimensions:
  length: $length          # depth, along receding axis
  width: $width            # across front face
  height: $height          # vertical
fill:
  type: water_level
  filled_height: $water_h  # from base
  fill_style: hatching     # hatching | stipple | solid_grey
labels:
  - text: "$width cm"
    edge: front_bottom
  - text: "$height cm"
    edge: front_right_vertical
    show_as: "?"           # unknown
  - text: "$length cm"
    edge: top_receding_right
scale_intent: not_to_scale
```

**Isometric projection (computed):**
```python
COS30 = 0.866
SIN30 = 0.5
iso_x(x, y) = origin_x + (x - y) × COS30 × scale
iso_y(x, y, z) = origin_y - z × scale + (x + y) × SIN30 × scale

# Front-bottom-left vertex at (0,0,0) → screen origin
# Width runs along x-axis (front face, right)
# Depth runs along y-axis (receding, left)
# Height runs along z-axis (vertical, up)
```

**Visible faces computed:**
- Front face: always visible (the rectangle at y=0).
- Right face: always visible (the rectangle at x=width).
- Top face: always visible (the rectangle at z=height).
- Back, left, bottom: hidden. Draw back edges as dashed lines if needed for clarity.

**Water level rendering:**
```python
water_top_z = $water_h
# Draw filled front face region: from z=0 to z=water_top_z, full width
# Draw filled right face region: from z=0 to z=water_top_z, full depth
# Draw water surface: top face at z=water_top_z (light fill, solid outline)
# Air gap: front/right face regions from z=water_top_z to z=height (no fill)
```

**When variables change:**
- Water level moves up/down with $water_h.
- Dimension arrows recompute lengths and label values.
- If $height changes, entire solid rescales; water level ratio preserved.

---

### Cube Nets

**Parametric inputs:**
```yaml
face_size: 40                     # px per face side
nets:
  - id: A
    faces: [[0,0], [0,1], [0,2], [0,3], [1,2], [-1,2]]   # [col, row] grid positions
    correct: true
  - id: B
    faces: [[0,0], [1,0], [1,1], [2,1], [2,2], [3,2]]
    correct: false
show_reference_cube: true
```

**Rendering (computed):**
```python
for each net:
  for each [col, row] in faces:
    draw_rect(
      x = net_origin_x + col × face_size,
      y = net_origin_y + row × face_size,
      width = face_size,
      height = face_size
    )
  # Outline: trace the outer boundary of the connected shape (1.5px)
  # Internal shared edges: thin lines (0.5px)
```

**Label placement:**
- Net ID (A, B, C, D) centred below each net, 10px below lowest face.
- If faces are shaded (for "which face is opposite" questions), shade labels go inside each face, centred.

**When variables change:**
- Swap face grid positions to show different nets.
- `correct` flag drives answer key, not rendering.
- Optional: shade specific faces by adding `shade: [0, 3]` (indices) to highlight opposite-face pairs.

---

### Isometric Stacked Cubes

**Parametric inputs:**
```yaml
unit_size: 30                # px per cube edge
cubes:                       # occupancy grid: list of [x, y, z] positions
  - [0,0,0]
  - [1,0,0]
  - [2,0,0]
  - [0,1,0]
  - [0,0,1]
  # ... total must match problem's stated cube count
views_to_label: [front, side, top]
shading:
  top: "#f0f0f0"
  front: "#d0d0d0"
  side: "#b0b0b0"
```

**Visible face computation (computed):**
```python
cube_set = set of all (x, y, z)

for each cube (x, y, z):
  top_visible    = (x, y, z+1) not in cube_set
  front_visible  = (x, y-1, z) not in cube_set   # toward viewer
  right_visible  = (x+1, y, z) not in cube_set

  # Draw only visible faces using isometric projection
  if top_visible:
    draw_iso_face(top, shade=shading.top)
  if front_visible:
    draw_iso_face(front, shade=shading.front)
  if right_visible:
    draw_iso_face(right, shade=shading.side)
```

**Edge classification:**
```python
for each edge in all visible faces:
  if edge is shared between two visible faces of the same shade:
    style = internal (0.5px, light)
  else:
    style = outline (1.5px, dark)
```

**Rendering order (painter's algorithm):**
Sort cubes by (y descending, x ascending, z ascending) — draw far cubes first, near cubes last. This ensures correct occlusion without z-buffering.

**View labels:**
- "Front view" below-left with a horizontal arrow pointing right toward the solid.
- "Side view" below-right with a horizontal arrow pointing left toward the solid.
- "Top view" above with a vertical arrow pointing down toward the solid.
- Labels placed outside the solid's bounding box with ≥12px clearance.

**2D orthographic views (for answer/workspace grids):**
```python
front_view[col][row] = any cube at (x=col, y=any, z=row) exists?
side_view[col][row]  = any cube at (x=any, y=col, z=row) exists?
top_view[col][row]   = any cube at (x=col, y=row, z=any) exists?

# Render as grid of squares: filled = cube present, empty = no cube
```

**When variables change:**
- Add/remove entries from the cubes list.
- All visible faces recompute.
- 2D views recompute.
- Cube count label updates.
- Rendering order re-sorts.

---

## Dimension Lines (Measurement Arrows)

Dimension lines are the most error-prone annotation in AI-generated diagrams. They must be pixel-precise.

### Anatomy of a dimension line

```
     extension line          extension line
          │                       │
          │    ←── 12 cm ──→      │
          │                       │
  ────────┤                       ├────────
  edge A  │       (shape)         │  edge B
```

**Components:**
1. **Arrow line** — horizontal or vertical, with arrowheads at both ends. Exactly parallel to the edge being measured.
2. **Arrowheads** — pointing inward, tips touching the extension lines.
3. **Extension lines** — thin perpendicular lines connecting the shape's edge to the arrow line. Exactly perpendicular. Start at the shape edge, extend 2–3px past the arrow line.
4. **Label** — centred on the arrow line, with a gap (line breaks around the text, not through it).

### Precision rules

1. **Endpoint precision.** Arrow tip x/y must equal the extension line x/y to the pixel. No 2px gaps, no overshoots.
2. **Length accuracy.** If the dimension line labels an edge that is 120px on screen, the arrow span must be exactly 120px.
3. **Parallelism.** The arrow line's slope must equal the measured edge's slope. For horizontal edges: arrow line y₁ = y₂. For isometric 30° edges: arrow line follows the same 30° angle.
4. **Offset stacking.** When multiple dimension lines annotate the same shape, each sits at a different offset:
   - First dimension: 12px from shape edge.
   - Second dimension: 28px from shape edge (12 + 16).
   - Third: 44px. Pattern: 12 + (n-1) × 16.
5. **No crossings.** Dimension lines must never cross each other or cross the shape outline.

### Dimension lines on 3D isometric solids

- Only dimension edges that lie along the **front-facing planes**. Never dimension a receding depth edge directly — the foreshortened length misleads.
- Height dimensions: vertical line to the right of the front face.
- Width dimensions: horizontal line below the front face.
- Depth dimensions: along the top face's receding edge, or use a leader line to clear space with the actual value labelled.

---

## Arrow and Annotation Rules

Arrows and annotations appear across all chart types. Handle them uniformly.

### Arrow types

| Arrow type | When to use | Style | Endpoint rule |
|-----------|-------------|-------|---------------|
| Leader line | Label is far from its anchor | Thin (0.5px), dashed, no arrowhead | Starts at nearest edge of label bounding box, ends touching the anchor element's boundary |
| Callout arrow | Annotation pointing to a specific element | Thin (1px), solid, single arrowhead at target | Arrowhead tip touches target boundary, tail starts at annotation box edge |
| Dimension arrow | Shows a measured distance | 1px, solid, double arrowheads + perpendicular ticks | Both tips touch extension lines exactly (see Dimension Lines above) |
| Flow arrow | Shows direction or sequence | Medium (1.5px), solid, single arrowhead | Tail at source boundary, head at target boundary |
| Viewpoint arrow | Indicates viewing direction (3D) | Medium (1.5px), solid, single arrowhead | Points toward the solid from the label position, tip stops 6px from shape edge |

### Arrow endpoint precision rules

1. **Arrow tip touches target boundary.** Not 3px away. Not 3px past. The geometric tip of the arrowhead sits on the element's edge. Compute the intersection of the arrow line with the target shape's boundary.
2. **Arrow tail starts at source boundary.** For leader lines: the line starts at the nearest edge of the label's bounding box. For flow arrows: the line starts at the source shape's edge. Never start from the centre of a shape (it obscures the shape's content).
3. **Arrowhead size is consistent.** All arrows in the same diagram use the same arrowhead dimensions (width and length). Standard: 6px long, 4px wide.
4. **Arrow line does not extend past the arrowhead.** The line terminates at the arrowhead's base, not at its tip (the arrowhead is the tip).

### Arrow routing rules

1. **Never cross text.** Route around any label or annotation.
2. **Never cross the element you're annotating** (unless it's a callout pointing into the element).
3. **Prefer orthogonal paths** (horizontal + vertical segments) over diagonal lines — they read cleaner.
4. **Arrowheads point AT the target**, not past it.
5. **Leader lines connect to the nearest edge of the label**, not the centre. A label to the right of its anchor connects from its left edge.
6. **No arrow passes through a filled/shaded region** unless it is explicitly annotating that region. Route around.
7. **Minimum clearance.** Arrows must maintain ≥4px clearance from any element they do not connect to.

### Annotation boxes

For callout annotations (e.g., "This region is 1/4 of the circle"):

```yaml
annotation:
  text: "This is 1/4 of the circle"
  target: region(circle_1, sector_1)
  position: auto             # computed: find nearest clear space
  style:
    background: light_grey
    border: 0.5px solid
    border_radius: 4px
    padding: 4px 8px
    font_size: 10px
  arrow:
    from: annotation_box.nearest_edge_to_target
    to: target.centroid
    style: callout
```

Position is computed by trying (in order): right of target, above, left, below — picking the first position with no collision.

---

## Caption Placement

### Chart captions ("Figure 1: Distribution of...")

- Position: **below the chart**, centered, with 12px gap from the bottom axis.
- Font: 11px, normal weight.
- Width: never wider than the chart's plot area.
- If caption wraps to two lines, that's fine. Three lines means the caption is too long — shorten it.

### In-chart annotations ("Highest month" with arrow)

- Position: computed to be in the **largest empty region** of the chart.
- Finding the largest empty region: subdivide the plot area into a grid. Score each cell by distance to nearest data element. Place annotation in the highest-scoring cell.
- Connect to the target with a callout arrow.

### Legend placement

Priority order:
1. **Inside the plot area** in the largest empty region (if the chart has clear empty space).
2. **Below the chart**, horizontal layout, centred.
3. **Right of the chart** (increases total width — use only if the other options fail).

Never place a legend on top of data.

---

## Validation Checklist (Run After Every Render)

For the rendering agent to self-check, or for an audit agent to verify:

```
□ Every label is readable (not overlapping, not clipped, not inside a dark fill)
□ Every label points to the correct element (trace each anchor)
□ Every label is at minimum achievable distance from its anchor (no unnecessary gaps)
□ No two labels' bounding boxes overlap (2px minimum clearance)
□ No label bounding box intersects a line, edge, or arrow it doesn't describe
□ Labels on shaded regions have ≥4.5:1 contrast ratio or opaque background
□ Every arrow starts and ends at the correct elements (tips touch boundaries exactly)
□ All arrowheads in the diagram are the same size
□ No arrow crosses unrelated text or data (4px minimum clearance)
□ Dimension line endpoints match the edge they measure (pixel-precise)
□ Dimension lines are exactly parallel to the edges they measure
□ Extension lines are exactly perpendicular to dimension lines
□ Dimension labels are centred on their lines (not shifted toward either end)
□ Multiple dimension lines are stacked at consistent offsets (12, 28, 44px...)
□ No dimension lines cross each other
□ Percentages sum to 100 (pie charts)
□ Axis starts at zero (bar charts, unless explicitly non-zero)
□ All bars / segments at the same scale within a comparison
□ Bracket endpoints land on correct boundaries (bar models)
□ Data labels match the actual rendered size (bar height matches value)
□ Shading/hatching stays within its intended region
□ Z-order is correct (labels on top of everything)
□ "Not to scale" label present when applicable
□ Collision detection has run — no label-on-label overlaps
□ Canvas bounds respected — nothing clipped
□ 3D: isometric edges at 30° (measure), parallel edges parallel
□ 3D: visible faces correct (no interior faces drawn, no exterior faces missing)
□ 3D: face shading consistent (all tops same, all fronts same, all sides same)
□ 3D: cube count matches problem statement
□ Nets: exactly 6 identical squares, full-edge adjacency, grid-aligned
□ Changing any input variable produces a correct re-render (test with ±1)
```
