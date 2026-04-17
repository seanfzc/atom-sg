#!/usr/bin/env python3
"""
Render Generator for Geometry Problems
Generates SVG and PDF renders for all 25 geometry problems.
"""

import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend for headless execution
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, Circle, Polygon, FancyBboxPatch
import numpy as np
import os
from pathlib import Path

# Pastel color palette (as per rendering-stack project)
COLORS = {
    'primary': '#A8D8EA',      # Light blue
    'secondary': '#AA96DA',    # Light purple
    'accent': '#FCBAD3',       # Light pink
    'highlight': '#FFFFD2',    # Light yellow
    'border': '#95E1D3',       # Mint green
    'text': '#2C3E50',         # Dark gray
    'shape': '#87CEEB',        # Sky blue
    'line': '#5F9EA0',         # Cadet blue
    'fill': '#F0F8FF',         # Alice blue
}

# Output directory
OUTPUT_DIR = Path(__file__).parent / "artifacts/renders"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Problem data with diagram types and specifications
PROBLEMS = {
    'G001': {
        'type': 'angle-diagram',
        'subpathway': 'Measure angles with protractor',
        'description': 'Measure angles ∠A, ∠B, and ∠C in the diagram',
        'angles': [(45, 'A'), (75, 'B'), (60, 'C')],
        'difficulty': 'A'
    },
    'G002': {
        'type': 'angle-diagram',
        'subpathway': 'Angles on straight line',
        'description': 'Two angles on a straight line',
        'angles': [(75, 'A'), (105, 'B')],
        'straight_line': True,
        'difficulty': 'B'
    },
    'G003': {
        'type': 'angle-diagram',
        'subpathway': 'Angles around a point',
        'description': 'Three angles meet at a point',
        'angles': [(120, 'A'), (85, 'B'), (155, 'C')],
        'point': True,
        'difficulty': 'B'
    },
    'G004': {
        'type': 'angle-diagram',
        'subpathway': 'Vertically opposite angles',
        'description': 'Two straight lines intersect',
        'angles': [(40, 'A'), (140, 'B')],
        'intersecting_lines': True,
        'difficulty': 'B'
    },
    'G005': {
        'type': 'triangle',
        'subpathway': 'Triangle angle sum',
        'description': 'Triangle ABC with two angles given',
        'triangle': [(50, 'A'), (70, 'B'), (60, 'C')],
        'difficulty': 'C'
    },
    'G006': {
        'type': 'line-types',
        'subpathway': 'Perpendicular and parallel lines',
        'description': 'Identify perpendicular and parallel lines',
        'difficulty': 'A'
    },
    'G007': {
        'type': 'angle-diagram',
        'subpathway': 'Combined angle properties',
        'description': 'Two-step angle reasoning',
        'angles': [(110, 'A'), (70, 'B'), (20, 'C')],
        'difficulty': 'D'
    },
    'G008': {
        'type': 'angle-diagram',
        'subpathway': 'Reflex angle measurement',
        'description': 'Measure reflex angle ∠R',
        'angles': [(240, 'R')],
        'reflex': True,
        'difficulty': 'C'
    },
    'G009': {
        'type': 'rectangle',
        'subpathway': 'Rectangle perimeter',
        'description': 'Rectangle with length 8 cm and breadth 5 cm',
        'dimensions': (8, 5),
        'difficulty': 'A'
    },
    'G010': {
        'type': 'composite-shape',
        'subpathway': 'Perimeter of rectilinear figures',
        'description': 'Rectilinear figure with two rectangles',
        'difficulty': 'B'
    },
    'G011': {
        'type': 'composite-shape',
        'subpathway': 'Area of L-shape',
        'description': 'L-shape formed by two rectangles',
        'difficulty': 'B'
    },
    'G012': {
        'type': 'composite-shape',
        'subpathway': 'Area with cut-out rectangle',
        'description': 'Rectangular sheet with cut-out',
        'difficulty': 'C'
    },
    'G013': {
        'type': 'conversion',
        'subpathway': 'Length unit conversion',
        'description': 'Convert between m and cm',
        'conversions': ['3.5 m → 350 cm', '250 cm → 2.5 m'],
        'difficulty': 'A'
    },
    'G014': {
        'type': 'conversion',
        'subpathway': 'Area unit conversion',
        'description': 'Convert m² to cm²',
        'conversions': ['2.5 m² = 25,000 cm²'],
        'difficulty': 'B'
    },
    'G015': {
        'type': 'symmetry',
        'subpathway': 'Lines of symmetry',
        'description': 'Regular hexagon symmetry lines',
        'shape': 'hexagon',
        'difficulty': 'A'
    },
    'G016': {
        'type': 'symmetry',
        'subpathway': 'Complete symmetrical figure',
        'description': 'Reflection across vertical line',
        'difficulty': 'C'
    },
    'G017': {
        'type': 'cuboid',
        'subpathway': 'Cuboid volume',
        'description': 'Cuboid with dimensions 6×4×3 cm',
        'dimensions': (6, 4, 3),
        'difficulty': 'A'
    },
    'G018': {
        'type': 'cuboid',
        'subpathway': 'Volume with unit conversion',
        'description': 'Mixed units (0.5 m × 30 cm × 200 mm)',
        'dimensions': (0.5, 30, 20),
        'mixed_units': True,
        'difficulty': 'B'
    },
    'G019': {
        'type': 'net',
        'subpathway': 'Identify cube net',
        'description': 'Which net forms a cube?',
        'shape': 'cube',
        'difficulty': 'C'
    },
    'G020': {
        'type': 'net',
        'subpathway': 'Draw cuboid net',
        'description': 'Net of cuboid 4×2×1 cm',
        'dimensions': (4, 2, 1),
        'difficulty': 'D'
    },
    'G021': {
        'type': 'triangle-classification',
        'subpathway': 'Classify by sides',
        'description': 'Triangle with sides 5, 5, 5 cm',
        'classification': 'equilateral',
        'sides': [5, 5, 5],
        'difficulty': 'A'
    },
    'G022': {
        'type': 'triangle-classification',
        'subpathway': 'Classify by angles',
        'description': 'Triangle with angles 45°, 45°, 90°',
        'classification': 'right-isosceles',
        'angles': [45, 45, 90],
        'difficulty': 'A'
    },
    'G023': {
        'type': 'quadrilateral',
        'subpathway': 'Classify quadrilaterals',
        'description': 'Identify rhombus properties',
        'shape': 'rhombus',
        'difficulty': 'B'
    },
    'G024': {
        'type': 'circle',
        'subpathway': 'Circle circumference',
        'description': 'Circle with radius 7 cm',
        'radius': 7,
        'difficulty': 'C'
    },
    'G025': {
        'type': 'pie-chart',
        'subpathway': 'Interpret pie chart',
        'description': 'Pie chart sector with 90°',
        'angle': 90,
        'difficulty': 'D'
    }
}


def draw_angle_diagram(ax, problem_id, problem):
    """Draw angle measurement diagrams."""
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    angles = problem.get('angles', [])
    is_reflex = problem.get('reflex', False)
    is_point = problem.get('point', False)
    is_straight = problem.get('straight_line', False)
    is_intersecting = problem.get('intersecting_lines', False)

    if is_point:
        # Angles around a point
        current_angle = 0
        for angle_val, label in angles:
            # Draw rays (lines) for the angle
            ax.plot([0, np.cos(np.radians(current_angle))], 
                    [0, np.sin(np.radians(current_angle))], 
                    color=COLORS['line'], linewidth=1.5)
            ax.plot([0, np.cos(np.radians(current_angle + angle_val))],
                    [0, np.sin(np.radians(current_angle + angle_val))],
                    color=COLORS['line'], linewidth=1.5)
            
            # Draw angle arc
            arc = patches.Arc((0, 0), 1.2, 1.2, angle=current_angle, theta1=0, theta2=angle_val,
                            linewidth=2, edgecolor=COLORS['primary'])
            ax.add_patch(arc)

            # Label
            mid_angle = np.radians(current_angle + angle_val/2)
            ax.text(0.7*np.cos(mid_angle), 0.7*np.sin(mid_angle), f"∠{label}",
                   ha='center', va='center', fontsize=12, color=COLORS['text'],
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['highlight'], edgecolor=COLORS['border']))

            current_angle += angle_val

        # Center point
        ax.plot(0, 0, 'o', color=COLORS['text'], markersize=8)

    elif is_intersecting:
        # Intersecting lines
        ax.plot([-1, 1], [-1, 1], color=COLORS['line'], linewidth=2)
        ax.plot([-1, 1], [1, -1], color=COLORS['line'], linewidth=2)

        # Draw angle arcs
        arc1 = patches.Arc((0, 0), 0.8, 0.8, angle=-45, theta1=0, theta2=40,
                          linewidth=2, edgecolor=COLORS['primary'])
        ax.add_patch(arc1)
        ax.text(0.5, 0.1, "∠A=40°", ha='center', fontsize=10, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['highlight']))

        arc2 = patches.Arc((0, 0), 0.6, 0.6, angle=135, theta1=0, theta2=140,
                          linewidth=2, edgecolor=COLORS['secondary'])
        ax.add_patch(arc2)

    elif is_straight:
        # Angles on straight line
        ax.plot([-1.2, 1.2], [0, 0], color=COLORS['line'], linewidth=3)

        # Draw rays for angles
        ax.plot([0, np.cos(np.radians(75))], [0, np.sin(np.radians(75))], 
                color=COLORS['line'], linewidth=1.5)  # ray for ∠A
        ax.plot([0, np.cos(np.radians(180))], [0, np.sin(np.radians(180))], 
                color=COLORS['line'], linewidth=1.5)  # ray for ∠B

        # Draw angle arcs
        arc1 = patches.Arc((0, 0), 0.8, 0.8, angle=0, theta1=0, theta2=75,
                          linewidth=2, edgecolor=COLORS['primary'])
        ax.add_patch(arc1)
        ax.text(0.4, 0.25, f"∠A=75°", ha='center', fontsize=10, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['highlight']))

        arc2 = patches.Arc((0, 0), 0.8, 0.8, angle=0, theta1=75, theta2=180,
                          linewidth=2, edgecolor=COLORS['secondary'])
        ax.add_patch(arc2)
        ax.text(-0.5, 0.25, f"∠B=105°", ha='center', fontsize=10, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['accent']))

    elif is_reflex:
        # Reflex angle
        outer_arc = patches.Arc((0, 0), 1.4, 1.4, angle=0, theta1=0, theta2=240,
                              linewidth=2, edgecolor=COLORS['primary'])
        ax.add_patch(outer_arc)

        inner_arc = patches.Arc((0, 0), 0.6, 0.6, angle=0, theta1=240, theta2=360,
                              linewidth=2, edgecolor=COLORS['secondary'])
        ax.add_patch(inner_arc)

        ax.plot([-1.2, 1.2], [0, 0], color=COLORS['line'], linewidth=2)
        # Second ray for reflex angle
        ax.plot([0, np.cos(np.radians(240))], [0, np.sin(np.radians(240))], 
                color=COLORS['line'], linewidth=1.5)

        ax.text(0.7, 0.5, f"∠R=240°", ha='center', fontsize=12, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['highlight'], edgecolor=COLORS['border']))

    else:
        # Standard angles
        current_angle = 0
        for angle_val, label in angles:
            # Draw rays (lines) for the angle
            ax.plot([0, np.cos(np.radians(current_angle))], 
                    [0, np.sin(np.radians(current_angle))], 
                    color=COLORS['line'], linewidth=1.5)
            ax.plot([0, np.cos(np.radians(current_angle + angle_val))],
                    [0, np.sin(np.radians(current_angle + angle_val))],
                    color=COLORS['line'], linewidth=1.5)
            
            # Draw angle arc
            arc = patches.Arc((0, 0), 1.2, 1.2, angle=current_angle, theta1=0, theta2=angle_val,
                            linewidth=2, edgecolor=COLORS['primary'])
            ax.add_patch(arc)

            # Label
            mid_angle = np.radians(current_angle + angle_val/2)
            ax.text(0.7*np.cos(mid_angle), 0.7*np.sin(mid_angle), f"∠{label}",
                   ha='center', va='center', fontsize=12, color=COLORS['text'],
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['highlight'], edgecolor=COLORS['border']))

            current_angle += angle_val

    # Add problem description
    ax.text(0, -1.4, problem['description'], ha='center', fontsize=10,
           style='italic', color=COLORS['text'])


def draw_triangle(ax, problem_id, problem):
    """Draw triangle diagrams."""
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    triangle_angles = problem.get('triangle', [])

    # Draw triangle (approximate for visualization)
    triangle = Polygon([(0, 0), (4, 0), (1, 3.5)],
                      closed=True, facecolor=COLORS['fill'],
                      edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(triangle)

    # Add angle markers
    if problem_id == 'G005':
        # Angle A (at origin)
        arc1 = patches.Arc((0, 0), 0.6, 0.6, angle=0, theta1=0, theta2=74,
                          linewidth=2, edgecolor=COLORS['primary'])
        ax.add_patch(arc1)
        ax.text(0.4, 0.15, "∠A=50°", ha='center', fontsize=9, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['highlight']))

        # Angle B (at (4,0))
        arc2 = patches.Arc((4, 0), 0.6, 0.6, angle=180-74, theta1=0, theta2=61,
                          linewidth=2, edgecolor=COLORS['secondary'])
        ax.add_patch(arc2)
        ax.text(3.5, 0.15, "∠B=70°", ha='center', fontsize=9, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['accent']))

        # Angle C (at (1, 3.5))
        arc3 = patches.Arc((1, 3.5), 0.6, 0.6, angle=180+74, theta1=0, theta2=45,
                          linewidth=2, edgecolor=COLORS['primary'])
        ax.add_patch(arc3)
        ax.text(1, 2.8, "∠C=60°", ha='center', fontsize=9, color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['highlight']))

    # Add problem description
    ax.text(2, -0.8, problem['description'], ha='center', fontsize=10,
           style='italic', color=COLORS['text'])


def draw_line_types(ax, problem_id, problem):
    """Draw perpendicular and parallel lines."""
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Parallel lines
    ax.plot([0, 6], [3, 3], color=COLORS['line'], linewidth=2)
    ax.plot([0, 6], [1, 1], color=COLORS['line'], linewidth=2)

    # Mark parallel arrows
    ax.arrow(5, 3, 0.3, 0, head_width=0.1, color=COLORS['primary'])
    ax.arrow(5, 1, 0.3, 0, head_width=0.1, color=COLORS['primary'])

    # Perpendicular lines
    ax.plot([1, 1], [0.5, 2.5], color=COLORS['secondary'], linewidth=2)
    ax.plot([0, 2], [1.5, 1.5], color=COLORS['secondary'], linewidth=2)

    # Right angle marker
    square = patches.Rectangle((1, 1.5), 0.3, 0.3, fill=False,
                             edgecolor=COLORS['text'], linewidth=1)
    ax.add_patch(square)

    ax.text(3, 2, "Parallel Lines", ha='center', fontsize=11, color=COLORS['text'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['highlight']))
    ax.text(1, 0, "Perpendicular Lines", ha='center', fontsize=11, color=COLORS['text'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['accent']))


def draw_rectangle(ax, problem_id, problem):
    """Draw rectangle diagrams."""
    dimensions = problem.get('dimensions', (8, 5))

    ax.set_xlim(-1, dimensions[0] + 1)
    ax.set_ylim(-1, dimensions[1] + 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw rectangle
    rect = Rectangle((0, 0), dimensions[0], dimensions[1],
                    facecolor=COLORS['fill'],
                    edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(rect)

    # Add dimension labels
    ax.text(dimensions[0]/2, -0.5, f"length = {dimensions[0]} cm", ha='center',
           fontsize=11, color=COLORS['text'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['highlight']))
    ax.text(-0.5, dimensions[1]/2, f"breadth =\n{dimensions[1]} cm", ha='center',
           fontsize=11, color=COLORS['text'],
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['accent']))


def draw_composite_shape(ax, problem_id, problem):
    """Draw composite shapes (L-shape, etc.)."""
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    if problem_id == 'G011':
        # L-shape
        rect1 = Rectangle((0, 0), 6, 2, facecolor=COLORS['fill'],
                         edgecolor=COLORS['line'], linewidth=2)
        rect2 = Rectangle((0, 2), 2, 2, facecolor=COLORS['secondary'],
                         edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect1)
        ax.add_patch(rect2)

        ax.text(3, 1, "6×2", ha='center', va='center', fontsize=11, color=COLORS['text'])
        ax.text(1, 3, "2×2", ha='center', va='center', fontsize=11, color=COLORS['text'])

    elif problem_id == 'G012':
        # Rectangle with cut-out
        outer_rect = Rectangle((0, 0), 5, 3, facecolor=COLORS['fill'],
                              edgecolor=COLORS['line'], linewidth=2)
        inner_rect = Rectangle((1, 1), 2, 1, facecolor='white',
                              edgecolor=COLORS['text'], linewidth=2, linestyle='--')
        ax.add_patch(outer_rect)
        ax.add_patch(inner_rect)

        ax.text(2.5, 1.5, "cut-out", ha='center', va='center', fontsize=10, color=COLORS['text'])
        ax.text(2.5, -0.5, "5×3 cm", ha='center', fontsize=10, color=COLORS['text'])

    elif problem_id == 'G010':
        # Quarter-circle attached to rectangle corner (fix for P0-6 shape mismatch)
        # Rectangle 6×4 with quarter-circle radius 2 at top-right corner
        rect = Rectangle((0, 0), 6, 4, facecolor=COLORS['fill'],
                        edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect)
        
        # Quarter-circle (90° wedge) at top-right corner
        quarter_circle = patches.Wedge((6, 4), 2, 0, 90,
                                      facecolor=COLORS['secondary'],
                                      edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(quarter_circle)
        
        # Dimension labels
        ax.text(3, -0.5, "6 cm", ha='center', fontsize=10, color=COLORS['text'])
        ax.text(-0.5, 2, "4 cm", ha='center', fontsize=10, color=COLORS['text'])
        ax.text(6.5, 4.5, "r = 2 cm", ha='left', fontsize=10, color=COLORS['text'])
        
        # Indicate quarter-circle angle
        ax.plot([6, 8], [4, 4], color=COLORS['line'], linewidth=1, linestyle='--')
        ax.plot([6, 6], [4, 6], color=COLORS['line'], linewidth=1, linestyle='--')
        arc = patches.Arc((6, 4), 1.5, 1.5, angle=0, theta1=0, theta2=90,
                         linewidth=1.5, edgecolor=COLORS['primary'])
        ax.add_patch(arc)
        ax.text(6.8, 4.8, "90°", ha='center', fontsize=9, color=COLORS['text'])


def draw_conversion(ax, problem_id, problem):
    """Draw unit conversion diagrams."""
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    conversions = problem.get('conversions', [])

    y_pos = 4
    for i, conv in enumerate(conversions):
        ax.text(4, y_pos - i*1.2, conv, ha='center', fontsize=14,
               color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['highlight'],
                        edgecolor=COLORS['primary'], linewidth=2))

    ax.text(4, 0.5, problem['subpathway'], ha='center', fontsize=11,
           style='italic', color=COLORS['text'])


def draw_symmetry(ax, problem_id, problem):
    """Draw symmetry diagrams."""
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    if problem_id == 'G015':
        # Regular hexagon
        # Create hexagon vertices manually
        angles = np.linspace(0, 2*np.pi, 7)[:-1] + np.pi/6  # Start at 30 degrees
        radius = 2
        vertices = [(radius*np.cos(a), radius*np.sin(a)) for a in angles]
        hexagon = Polygon(vertices, closed=True, facecolor=COLORS['fill'],
                         edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(hexagon)

        # Draw symmetry lines
        for i in range(6):
            angle = i * np.pi / 3
            ax.plot([2*np.cos(angle), 2*np.cos(angle)],
                   [2*np.sin(angle), 2*np.sin(angle)],
                   color=COLORS['secondary'], linewidth=1.5, linestyle='--')

        ax.plot([0, 0], [-2, 2], color=COLORS['primary'], linewidth=2, linestyle='-')

    elif problem_id == 'G016':
        # Symmetry completion
        # Draw half shape
        triangle = Polygon([(0, 0), (1, 2), (0, 2)],
                         closed=True, facecolor=COLORS['fill'],
                         edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(triangle)

        # Mirror line
        ax.plot([0, 0], [-0.5, 2.5], color=COLORS['primary'],
               linewidth=3, label='Mirror line')

        # Dotted half (to be completed)
        triangle_mirror = Polygon([(0, 0), (-1, 2), (0, 2)],
                                 closed=True, facecolor=COLORS['secondary'],
                                 edgecolor=COLORS['line'], linewidth=2,
                                 linestyle='--', alpha=0.5)
        ax.add_patch(triangle_mirror)

        ax.text(0.1, 2.3, "Mirror line", ha='left', fontsize=10, color=COLORS['primary'])


def draw_cuboid(ax, problem_id, problem):
    """Draw 3D cuboid diagrams."""
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')
    ax.axis('off')

    dimensions = problem.get('dimensions', (6, 4, 3))

    if problem_id == 'G018':
        # Show mixed units
        ax.text(4, 5, "0.5 m", ha='center', fontsize=12, color=COLORS['text'])
        ax.text(4, 4, "× 30 cm", ha='center', fontsize=12, color=COLORS['text'])
        ax.text(4, 3, "× 200 mm", ha='center', fontsize=12, color=COLORS['text'])
        ax.text(4, 1.5, "= 300,000 cm³", ha='center', fontsize=13,
               color=COLORS['primary'], weight='bold',
               bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['highlight']))
    else:
        # Draw 3D cuboid representation
        # Front face
        rect_front = Rectangle((1, 1), dimensions[0], dimensions[1],
                              facecolor=COLORS['fill'],
                              edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_front)

        # Back face (offset for 3D effect)
        offset = 1
        rect_back = Rectangle((1 + offset, 1 + offset), dimensions[0], dimensions[1],
                             facecolor=COLORS['secondary'], alpha=0.5,
                             edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_back)

        # Connecting lines
        ax.plot([1, 1 + offset], [1, 1 + offset], color=COLORS['line'], linewidth=1.5)
        ax.plot([1 + dimensions[0], 1 + dimensions[0] + offset],
               [1, 1 + offset], color=COLORS['line'], linewidth=1.5)
        ax.plot([1, 1 + offset], [1 + dimensions[1], 1 + dimensions[1] + offset],
               color=COLORS['line'], linewidth=1.5)
        ax.plot([1 + dimensions[0], 1 + dimensions[0] + offset],
               [1 + dimensions[1], 1 + dimensions[1] + offset],
               color=COLORS['line'], linewidth=1.5)

        # Dimension labels with units (cm) for clarity
        ax.text(1 + dimensions[0]/2, 0.5, f"l={dimensions[0]} cm",
               ha='center', fontsize=10, color=COLORS['text'])
        ax.text(0.3, 1 + dimensions[1]/2, f"b={dimensions[1]} cm",
               ha='center', fontsize=10, color=COLORS['text'])
        # Height label with arrow to depth dimension (fix for G017 visual association)
        x_mid = 1 + dimensions[0] + offset/2
        y_mid = 1 + dimensions[1] + offset/2
        ax.annotate(f"h={dimensions[2]} cm", 
                   xy=(x_mid, y_mid),
                   xytext=(x_mid + 0.5, y_mid + 0.5),
                   arrowprops=dict(arrowstyle='->', color=COLORS['text'], lw=1),
                   ha='center', fontsize=10, color=COLORS['text'])


def draw_net(ax, problem_id, problem):
    """Draw net diagrams."""
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    if problem_id == 'G019':
        # Cube net (cross shape)
        # Center square
        rect_center = Rectangle((3, 1.5), 2, 2, facecolor=COLORS['fill'],
                               edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_center)

        # Top square
        rect_top = Rectangle((3, 3.5), 2, 2, facecolor=COLORS['secondary'],
                           edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_top)

        # Bottom square
        rect_bottom = Rectangle((3, -0.5), 2, 2, facecolor=COLORS['secondary'],
                              edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_bottom)

        # Left square
        rect_left = Rectangle((1, 1.5), 2, 2, facecolor=COLORS['secondary'],
                            edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_left)

        # Right square
        rect_right = Rectangle((5, 1.5), 2, 2, facecolor=COLORS['secondary'],
                             edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_right)

        ax.text(4, 2.5, "center", ha='center', va='center', fontsize=9, color=COLORS['text'])

    elif problem_id == 'G020':
        # Cuboid net
        dimensions = problem.get('dimensions', (4, 2, 1))

        # Main rectangle (length × height)
        rect_main = Rectangle((0, 1), dimensions[0], dimensions[2],
                            facecolor=COLORS['fill'],
                            edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_main)

        # Top (length × breadth)
        rect_top = Rectangle((0, 1 + dimensions[2]), dimensions[0], dimensions[1],
                           facecolor=COLORS['secondary'],
                           edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_top)

        # Bottom (length × breadth)
        rect_bottom = Rectangle((0, 1 - dimensions[1]), dimensions[0], dimensions[1],
                              facecolor=COLORS['secondary'],
                              edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_bottom)

        # Side (breadth × height)
        rect_side = Rectangle((dimensions[0], 1), dimensions[1], dimensions[2],
                             facecolor=COLORS['accent'],
                             edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(rect_side)

        # Dimension labels
        ax.text(dimensions[0]/2, 1 + dimensions[2]/2, f"{dimensions[0]}×{dimensions[2]}",
               ha='center', va='center', fontsize=9, color=COLORS['text'])
        ax.text(dimensions[0]/2, 1 + dimensions[2] + dimensions[1]/2, f"{dimensions[0]}×{dimensions[1]}",
               ha='center', va='center', fontsize=9, color=COLORS['text'])


def draw_triangle_classification(ax, problem_id, problem):
    """Draw triangle classification diagrams."""
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    if problem_id == 'G021':
        # Equilateral triangle
        triangle = Polygon([(2, 0), (5, 0), (3.5, 4.33)],
                          closed=True, facecolor=COLORS['fill'],
                          edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(triangle)

        # Add side labels
        ax.text(3.5, -0.4, "5 cm", ha='center', fontsize=10, color=COLORS['text'])
        ax.text(5.2, 2, "5 cm", ha='left', fontsize=10, color=COLORS['text'])
        ax.text(1.8, 2, "5 cm", ha='right', fontsize=10, color=COLORS['text'])

        ax.text(3.5, 5, "Equilateral", ha='center', fontsize=12, weight='bold',
               color=COLORS['primary'])

    elif problem_id == 'G022':
        # Right-isosceles triangle
        triangle = Polygon([(1, 1), (5, 1), (1, 5)],
                          closed=True, facecolor=COLORS['fill'],
                          edgecolor=COLORS['line'], linewidth=2)
        ax.add_patch(triangle)

        # Right angle marker
        square = patches.Rectangle((1, 1), 1, 1, fill=False,
                                 edgecolor=COLORS['text'], linewidth=1)
        ax.add_patch(square)

        # Angle labels
        ax.text(1.5, 1.5, "45°", ha='center', fontsize=9, color=COLORS['text'])
        ax.text(1.5, 4, "45°", ha='center', fontsize=9, color=COLORS['text'])
        ax.text(3.5, 1.3, "90°", ha='center', fontsize=9, color=COLORS['text'])

        ax.text(3, 5.5, "Right-Isosceles", ha='center', fontsize=12, weight='bold',
               color=COLORS['secondary'])


def draw_quadrilateral(ax, problem_id, problem):
    """Draw quadrilateral classification diagrams."""
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Rhombus
    rhombus = Polygon([(3, 0), (6, 2.5), (3, 5), (0, 2.5)],
                      closed=True, facecolor=COLORS['fill'],
                      edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(rhombus)

    ax.text(3, -0.4, "All sides equal", ha='center', fontsize=10, color=COLORS['text'])
    ax.text(3, 5.4, "Two pairs of parallel sides", ha='center', fontsize=10, color=COLORS['text'])
    ax.text(3, 2.5, "Rhombus", ha='center', va='center', fontsize=13, weight='bold',
           color=COLORS['primary'])


def draw_circle(ax, problem_id, problem):
    """Draw circle diagrams."""
    radius = problem.get('radius', 7)

    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw circle
    circle = patches.Circle((0, 0), radius, facecolor=COLORS['fill'],
                          edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(circle)

    # Draw radius
    ax.plot([0, radius], [0, 0], color=COLORS['primary'], linewidth=2)
    ax.text(radius/2, 0.2, f"r={radius} cm", ha='center', fontsize=11, color=COLORS['text'])

    # Draw diameter
    ax.plot([-radius, radius], [0, 0], color=COLORS['secondary'], linewidth=1.5, linestyle='--')
    ax.text(0, -0.5, f"d={2*radius} cm", ha='center', fontsize=11, color=COLORS['text'])

    # Center point
    ax.plot(0, 0, 'o', color=COLORS['text'], markersize=6)


def draw_pie_chart(ax, problem_id, problem):
    """Draw pie chart diagrams."""
    angle = problem.get('angle', 90)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw pie chart
    wedge = patches.Wedge((0, 0), 1, 0, angle,
                         facecolor=COLORS['secondary'],
                         edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(wedge)

    # Remaining wedge
    wedge_remaining = patches.Wedge((0, 0), 1, angle, 360,
                                   facecolor=COLORS['fill'],
                                   edgecolor=COLORS['line'], linewidth=2)
    ax.add_patch(wedge_remaining)

    # Add angle label
    mid_angle = np.radians(angle / 2)
    ax.text(0.6*np.cos(mid_angle), 0.6*np.sin(mid_angle), f"{angle}°",
           ha='center', va='center', fontsize=14, weight='bold', color=COLORS['text'])

    # Add fraction
    fraction = angle / 360
    ax.text(0, -1.3, f"Fraction = {fraction:.2f}", ha='center', fontsize=12,
           color=COLORS['primary'],
           bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['highlight']))


def generate_render(problem_id, problem):
    """Generate SVG and PDF renders for a single problem."""
    diagram_type = problem['type']

    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    # Draw based on diagram type
    if diagram_type == 'angle-diagram':
        draw_angle_diagram(ax, problem_id, problem)
    elif diagram_type == 'triangle':
        draw_triangle(ax, problem_id, problem)
    elif diagram_type == 'line-types':
        draw_line_types(ax, problem_id, problem)
    elif diagram_type == 'rectangle':
        draw_rectangle(ax, problem_id, problem)
    elif diagram_type == 'composite-shape':
        draw_composite_shape(ax, problem_id, problem)
    elif diagram_type == 'conversion':
        draw_conversion(ax, problem_id, problem)
    elif diagram_type == 'symmetry':
        draw_symmetry(ax, problem_id, problem)
    elif diagram_type == 'cuboid':
        draw_cuboid(ax, problem_id, problem)
    elif diagram_type == 'net':
        draw_net(ax, problem_id, problem)
    elif diagram_type == 'triangle-classification':
        draw_triangle_classification(ax, problem_id, problem)
    elif diagram_type == 'quadrilateral':
        draw_quadrilateral(ax, problem_id, problem)
    elif diagram_type == 'circle':
        draw_circle(ax, problem_id, problem)
    elif diagram_type == 'pie-chart':
        draw_pie_chart(ax, problem_id, problem)

    # Add problem ID and title
    ax.set_title(f"{problem_id}: {problem['subpathway']}",
                fontsize=14, weight='bold', color=COLORS['text'], pad=20)

    plt.tight_layout()

    # Generate filenames
    base_name = f"{problem_id}-{diagram_type}-v1"
    svg_path = OUTPUT_DIR / f"{base_name}.svg"
    pdf_path = OUTPUT_DIR / f"{base_name}.pdf"

    # Save SVG
    plt.savefig(svg_path, format='svg', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    # Save PDF
    plt.savefig(pdf_path, format='pdf', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    plt.close()

    return svg_path, pdf_path


def main():
    """Generate all renders."""
    print("Generating geometry problem renders...")
    print(f"Output directory: {OUTPUT_DIR}")

    renders_generated = []

    for problem_id, problem in PROBLEMS.items():
        try:
            svg_path, pdf_path = generate_render(problem_id, problem)
            renders_generated.append({
                'problem_id': problem_id,
                'type': problem['type'],
                'svg': str(svg_path.name),
                'pdf': str(pdf_path.name),
                'status': 'success'
            })
            print(f"✓ {problem_id}: {problem['type']}")
        except Exception as e:
            print(f"✗ {problem_id}: Error - {e}")
            renders_generated.append({
                'problem_id': problem_id,
                'type': problem.get('type', 'unknown'),
                'status': 'failed',
                'error': str(e)
            })

    print(f"\nGenerated {len([r for r in renders_generated if r['status'] == 'success'])} / {len(PROBLEMS)} renders")

    return renders_generated


if __name__ == "__main__":
    main()
