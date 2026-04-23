"""
Test Suite for Geometry Renderers

Tests each renderer with 2-3 example problems to verify functionality.
Generates PNG outputs for visual verification.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from grid_renderer import GridRenderer
from isometric_renderer import IsometricRenderer
from composite_renderer import CompositeRenderer
from linegraph_renderer import LineGraphRenderer

# Output directory for test renders
OUTPUT_DIR = Path(__file__).parent / "test_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def test_grid_renderer():
    """Test GridRenderer with 3 example problems."""
    print("\n" + "="*60)
    print("TESTING GRID RENDERER")
    print("="*60)
    
    renderer = GridRenderer(str(OUTPUT_DIR))
    
    # Test 1: Triangle Construction on Grid
    print("\n1. Triangle Construction on Grid...")
    spec1 = """
type: grid_construction
title: "Construct Triangle ABC"
id: grid_triangle_001
grid:
  type: square
  size: 8
  unit: 1cm
shapes:
  - type: triangle
    vertices: [[1, 1], [5, 1], [3, 4]]
    labels: ["A", "B", "C"]
    show_dimensions: true
    fill_color: "#E8F4F8"
constraints:
  - type: equal_length
    segments: [[[1, 1], [3, 4]], [[5, 1], [3, 4]]]
protractor:
  enabled: false
"""
    try:
        path = renderer.process(spec1, output_filename="grid_triangle", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: Trapezium with Parallel Lines
    print("\n2. Trapezium Construction with Parallel Markers...")
    spec2 = """
type: grid_construction
title: "Trapezium PQRS"
id: grid_trapezium_001
grid:
  type: square
  size: 10
  unit: 1cm
shapes:
  - type: trapezium
    vertices: [[2, 1], [7, 1], [6, 4], [3, 4]]
    labels: ["P", "Q", "R", "S"]
    show_dimensions: true
    fill_color: "#F0F8FF"
constraints:
  - type: parallel
    lines: [[[2, 1], [7, 1]], [[3, 4], [6, 4]]]
  - type: right_angle
    vertex: [3, 4]
    arm1: [6, 4]
    arm2: [3, 1]
protractor:
  enabled: false
"""
    try:
        path = renderer.process(spec2, output_filename="grid_trapezium", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: Protractor Measurement Task
    print("\n3. Protractor Angle Measurement...")
    spec3 = """
type: grid_construction
title: "Measure Angle XYZ"
id: grid_protractor_001
grid:
  type: square
  size: 8
  unit: 1cm
shapes:
  - type: triangle
    vertices: [[2, 2], [6, 2], [2, 5]]
    labels: ["X", "Y", "Z"]
    show_dimensions: false
    fill_color: "#FFFFD2"
protractor:
  enabled: true
  position: [2, 2]
  radius: 3
  angle_range: [0, 90]
"""
    try:
        path = renderer.process(spec3, output_filename="grid_protractor", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")


def test_isometric_renderer():
    """Test IsometricRenderer with 3 example problems."""
    print("\n" + "="*60)
    print("TESTING ISOMETRIC RENDERER")
    print("="*60)
    
    renderer = IsometricRenderer(str(OUTPUT_DIR))
    
    # Test 1: Simple Cube Stack
    print("\n1. Isometric Cube Arrangement...")
    spec1 = """
type: isometric_3d
title: "Cube Stack (3 Cubes)"
id: iso_cubes_001
view: isometric
grid:
  type: isometric_dot
  size: [6, 6]
  spacing: 1cm
cubes:
  - position: [0, 0, 0]
    color: primary
  - position: [1, 0, 0]
    color: secondary
  - position: [0, 0, 1]
    color: accent
hidden_edges: true
cube_size: 1.0
"""
    try:
        path = renderer.process(spec1, output_filename="iso_cubes", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: L-Shape Cube Arrangement
    print("\n2. L-Shape Cube Arrangement...")
    spec2 = """
type: isometric_3d
title: "L-Shape Solid"
id: iso_lshape_001
view: isometric
grid:
  type: isometric_dot
  size: [8, 8]
  spacing: 1cm
cubes:
  - position: [0, 0, 0]
    color: primary
  - position: [1, 0, 0]
    color: primary
  - position: [2, 0, 0]
    color: primary
  - position: [0, 1, 0]
    color: primary
  - position: [0, 2, 0]
    color: primary
  - position: [0, 0, 1]
    color: secondary
hidden_edges: true
cube_size: 1.0
"""
    try:
        path = renderer.process(spec2, output_filename="iso_lshape", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: Orthographic Projections
    print("\n3. Orthographic Projection Views...")
    spec3 = """
type: orthographic
title: "Orthographic Views of Cube Stack"
id: ortho_views_001
view: orthographic
orthographic_views:
  - view: top
    show: true
  - view: front
    show: true
  - view: side
    show: true
cubes:
  - position: [0, 0, 0]
    color: primary
  - position: [1, 0, 0]
    color: primary
  - position: [0, 1, 0]
    color: secondary
  - position: [1, 1, 0]
    color: secondary
  - position: [0, 0, 1]
    color: accent
"""
    try:
        path = renderer.process(spec3, output_filename="ortho_views", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")


def test_composite_renderer():
    """Test CompositeRenderer with 3 example problems."""
    print("\n" + "="*60)
    print("TESTING COMPOSITE RENDERER")
    print("="*60)
    
    renderer = CompositeRenderer(str(OUTPUT_DIR))
    
    # Test 1: Overlapping Quarter Circles
    print("\n1. Overlapping Quarter Circles...")
    spec1 = """
type: composite_shapes
title: "Overlapping Quarter Circles"
id: composite_qc_001
shapes:
  - type: quarter_circle
    center: [0, 0]
    radius: 4
    quadrant: 1
    fill_color: "#A8D8EA"
  - type: quarter_circle
    center: [4, 0]
    radius: 4
    quadrant: 2
    fill_color: "#AA96DA"
intersections:
  - shapes: [0, 1]
    hatching: true
    label: "shaded"
labels:
  - x: 2
    y: 2.5
    text: "A"
  - x: 0
    y: -0.5
    text: "O"
  - x: 4
    y: -0.5
    text: "P"
"""
    try:
        path = renderer.process(spec1, output_filename="composite_quarter_circles", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: Reflex Angle
    print("\n2. Reflex Angle Diagram...")
    spec2 = """
type: composite_shapes
title: "Reflex Angle at Point O"
id: composite_reflex_001
reflex_angles:
  - vertex: [3, 3]
    angle: 270
    radius: 2
    label: "reflex ∠AOB = 270°"
shapes:
  - type: sector
    center: [3, 3]
    radius: 1.5
    start_angle: 0
    end_angle: 90
    fill_color: "#FFFFD2"
labels:
  - x: 3
    y: 3
    text: "O"
  - x: 5.5
    y: 3
    text: "A"
  - x: 3
    y: 0.5
    text: "B"
"""
    try:
        path = renderer.process(spec2, output_filename="composite_reflex_angle", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: Rhombus and Trapezium Composite
    print("\n3. Rhombus + Trapezium Composite...")
    spec3 = """
type: composite_shapes
title: "Composite Shape: Rhombus and Trapezium"
id: composite_multi_001
multi_shapes:
  - type: rhombus_trapezium
    rhombus:
      center: [3, 2]
      diagonal1: 6
      diagonal2: 4
    trapezium:
      vertices: [[0, 0], [6, 0], [5, 3], [1, 3]]
labels:
  - x: 3
    y: -0.5
    text: "AB = 6 cm"
  - x: 6.5
    y: 1.5
    text: "height = 3 cm"
"""
    try:
        path = renderer.process(spec3, output_filename="composite_multi_shape", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")


def test_linegraph_renderer():
    """Test LineGraphRenderer with 3 example problems."""
    print("\n" + "="*60)
    print("TESTING LINE GRAPH RENDERER")
    print("="*60)
    
    renderer = LineGraphRenderer(str(OUTPUT_DIR))
    
    # Test 1: Water Tank Volume (Rate of Change)
    print("\n1. Water Tank Volume with Rate Highlight...")
    spec1 = """
type: line_graph
title: "Water Tank Volume Over Time"
id: linegraph_tank_001
grid:
  x_range: [0, 10]
  y_range: [0, 100]
  x_unit: "hours"
  y_unit: "litres"
  x_major: 2
  y_major: 20
axes:
  x_label: "Time (hours)"
  y_label: "Volume (L)"
data_series:
  - name: "Tank A"
    type: line
    points: [[0, 0], [2, 20], [4, 50], [6, 80], [8, 90], [10, 100]]
    color: primary
    show_points: true
highlights:
  - type: rate_of_change
    interval: [2, 4]
    series: 0
    label: "Fastest fill rate"
annotations:
  - x: 4
    y: 50
    text: "50L"
    arrow: true
    offset_x: 0.5
    offset_y: 10
"""
    try:
        path = renderer.process(spec1, output_filename="linegraph_rate", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 2: Cumulative Data (Step Graph)
    print("\n2. Cumulative Sales Data...")
    spec2 = """
type: line_graph
title: "Cumulative Sales Over 6 Months"
id: linegraph_cumulative_001
grid:
  x_range: [0, 6]
  y_range: [0, 150]
  x_unit: "months"
  y_unit: "sales"
  x_major: 1
  y_major: 30
axes:
  x_label: "Month"
  y_label: "Cumulative Sales"
data_series:
  - name: "2024 Sales"
    type: cumulative
    points: [[0, 0], [1, 20], [2, 45], [3, 75], [4, 100], [5, 130], [6, 150]]
    color: secondary
    show_points: true
  - name: "2023 Sales"
    type: cumulative
    points: [[0, 0], [1, 15], [2, 35], [3, 60], [4, 85], [5, 110], [6, 140]]
    color: accent
    show_points: true
highlights:
  - type: region
    x_range: [3, 5]
    y_range: [60, 130]
    label: "Q2 Growth"
"""
    try:
        path = renderer.process(spec2, output_filename="linegraph_cumulative", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Test 3: Reverse Calculation Prompt
    print("\n3. Reverse Calculation Problem...")
    spec3 = """
type: line_graph
title: "Distance vs Time Graph"
id: linegraph_reverse_001
grid:
  x_range: [0, 8]
  y_range: [0, 80]
  x_unit: "hours"
  y_unit: "km"
  x_major: 1
  y_major: 20
axes:
  x_label: "Time (hours)"
  y_label: "Distance (km)"
data_series:
  - name: "Journey"
    type: line
    points: [[0, 0], [2, 20], [4, 40], [6, 60], [8, 80]]
    color: primary
    show_points: true
highlights:
  - type: reverse_calculation
    question: "When did the journey reach 40 km?"
    answer_x: 4
    answer_y: 40
annotations:
  - x: 4
    y: 40
    text: "40 km"
    arrow: false
    offset_x: 0.3
    offset_y: 5
"""
    try:
        path = renderer.process(spec3, output_filename="linegraph_reverse", is_file=False)
        print(f"   ✓ Generated: {path}")
    except Exception as e:
        print(f"   ✗ Error: {e}")


def run_all_tests():
    """Run all renderer tests."""
    print("\n" + "="*60)
    print("GEOMETRY RENDERER TEST SUITE")
    print("="*60)
    print(f"Output directory: {OUTPUT_DIR}")
    
    test_grid_renderer()
    test_isometric_renderer()
    test_composite_renderer()
    test_linegraph_renderer()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
    print(f"\nTest outputs saved to: {OUTPUT_DIR}")
    print("\nGenerated files:")
    for f in sorted(OUTPUT_DIR.glob("*.png")):
        print(f"  - {f.name}")


if __name__ == "__main__":
    run_all_tests()