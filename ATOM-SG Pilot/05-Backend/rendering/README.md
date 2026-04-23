# Geometry Rendering Modules

Exam-quality diagram renderers for Singapore MOE math problems. All renderers support VRS YAML specifications and output PNG at 150 DPI with professional MOE pastel color schemes.

## Modules

### 1. Grid Renderer (`grid_renderer.py`)

Renders grid construction diagrams for:
- Square grids with 1cm precision
- Triangle/trapezium construction tasks
- Protractor measurement overlays
- Constraint visualization (parallel lines, equal length markers)

**Example Usage:**
```python
from rendering.grid_renderer import GridRenderer

renderer = GridRenderer(output_dir="./outputs")
path = renderer.process("spec.yaml", is_file=True)
```

**VRS Specification Example:**
```yaml
type: grid_construction
title: "Construct Triangle ABC"
grid:
  type: square
  size: 8
  unit: 1cm
shapes:
  - type: triangle
    vertices: [[1, 1], [5, 1], [3, 4]]
    labels: ["A", "B", "C"]
    show_dimensions: true
constraints:
  - type: parallel
    lines: [[[0,0], [4,0]], [[1,3], [4,3]]]
```

### 2. Isometric Renderer (`isometric_renderer.py`)

Renders 3D visualizations for:
- Isometric cube arrangements
- Orthographic projection views (top/front/side)
- Dot grids for student construction
- Hidden edge rendering (dashed lines)

**Example Usage:**
```python
from rendering.isometric_renderer import IsometricRenderer

renderer = IsometricRenderer(output_dir="./outputs")
path = renderer.process("spec.yaml", is_file=True)
```

**VRS Specification Example:**
```yaml
type: isometric_3d
title: "Cube Stack"
view: isometric
grid:
  type: isometric_dot
  size: [6, 6]
cubes:
  - position: [0, 0, 0]
    color: primary
  - position: [1, 0, 0]
    color: secondary
hidden_edges: true
```

### 3. Composite Renderer (`composite_renderer.py`)

Renders composite shape diagrams for:
- Overlapping quarter circles/sectors
- Shaded intersection regions (diagonal hatching)
- Reflex angle arcs (>180°)
- Multi-shape composites (rhombus+trapezium)

**Example Usage:**
```python
from rendering.composite_renderer import CompositeRenderer

renderer = CompositeRenderer(output_dir="./outputs")
path = renderer.process("spec.yaml", is_file=True)
```

**VRS Specification Example:**
```yaml
type: composite_shapes
title: "Overlapping Quarter Circles"
shapes:
  - type: quarter_circle
    center: [0, 0]
    radius: 4
    quadrant: 1
  - type: quarter_circle
    center: [4, 0]
    radius: 4
    quadrant: 2
intersections:
  - shapes: [0, 1]
    hatching: true
    label: "shaded"
reflex_angles:
  - vertex: [0, 0]
    angle: 270
    label: "reflex ∠A"
```

### 4. Line Graph Renderer (`linegraph_renderer.py`)

Renders data interpretation diagrams for:
- Line graphs with grid backgrounds
- Cumulative data visualization
- Rate of change highlighting
- Reverse calculation prompts

**Example Usage:**
```python
from rendering.linegraph_renderer import LineGraphRenderer

renderer = LineGraphRenderer(output_dir="./outputs")
path = renderer.process("spec.yaml", is_file=True)
```

**VRS Specification Example:**
```yaml
type: line_graph
title: "Water Tank Volume Over Time"
grid:
  x_range: [0, 10]
  y_range: [0, 100]
  x_unit: "hours"
  y_unit: "litres"
axes:
  x_label: "Time (hours)"
  y_label: "Volume (L)"
data_series:
  - name: "Tank A"
    type: line
    points: [[0, 0], [2, 20], [4, 50], [6, 80], [10, 100]]
    color: primary
highlights:
  - type: rate_of_change
    interval: [2, 4]
    label: "Fastest fill rate"
  - type: reverse_calculation
    question: "When did Tank A reach 50L?"
    answer_x: 4
```

## Color Scheme

All renderers use the MOE Pastel color palette:

| Color Key | Hex Code | Usage |
|-----------|----------|-------|
| primary | #A8D8EA | Main shapes, highlights |
| secondary | #AA96DA | Secondary elements |
| accent | #FCBAD3 | Accents, highlights |
| highlight | #FFFFD2 | Labels, callouts |
| border | #95E1D3 | Borders, outlines |
| text | #2C3E50 | Text, labels |
| shape_fill | #E8F4F8 | Shape fills |
| shape_stroke | #5F9EA0 | Shape outlines |
| grid_line | #D0E0E3 | Grid lines |
| construction | #FF6B6B | Construction lines |
| hidden | #B0B0B0 | Hidden/dashed lines |

## Testing

Run the test suite:
```bash
python3 test_renderers.py
```

This generates 12 test images (3 per renderer) in `test_outputs/`.

## Base Renderer

All renderers inherit from `BaseRenderer` which provides:
- VRS YAML loading and parsing
- Validation framework
- Figure creation and saving
- Common drawing utilities (grids, angle arcs, dimensions, hatching)
- MOE color palette

## API Reference

### BaseRenderer Methods

- `load_vrs_yaml(path)` - Load YAML from file
- `load_vrs_string(yaml_string)` - Parse YAML from string
- `validate_spec(spec)` - Validate specification (abstract)
- `render(spec, output_filename)` - Render diagram (abstract)
- `process(yaml_input, output_filename, is_file)` - Complete pipeline
- `create_figure(size, dpi)` - Create figure with standard settings
- `save_figure(filename, dpi)` - Save figure to PNG
- `draw_grid(ax, xlim, ylim, spacing, major_spacing)` - Draw grid
- `draw_angle_arc(ax, center, radius, start_angle, end_angle, ...)` - Draw angle arc
- `draw_dimension_line(ax, p1, p2, label, offset)` - Draw dimension line
- `draw_hatching(ax, vertices, spacing, angle)` - Draw diagonal hatching

## Output Specifications

- **Format**: PNG
- **DPI**: 150 (configurable)
- **Color Space**: RGB
- **Background**: White
- **Aspect Ratio**: Equal (1:1) for geometric diagrams

## Dependencies

- matplotlib
- numpy
- pyyaml

Install with:
```bash
pip install matplotlib numpy pyyaml
```