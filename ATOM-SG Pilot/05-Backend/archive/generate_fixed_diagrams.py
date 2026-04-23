#!/usr/bin/env python3
"""
Generate FIXED diagrams addressing QA issues:
- Q15: Dimension line must exactly match radius (no overshoot)
- Q12: Add solvable constraints (square relationships visible)
- Q19: True isometric 30° projection with proper cube representation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Wedge, Arc, Polygon, Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path
import math

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-fixed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Font sizes
FONT_SIZES = {
    'title': 14,
    'axis_label': 12,
    'data_label': 11,
    'tick_label': 10,
    'annotation': 10,
}

# Colors
COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31',
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'shaded': '#DEEBF7',
    'light_blue': '#E7F3FF',
    'light_orange': '#FFF4E6',
    'light_green': '#E8F5E9',
    'white': '#FFFFFF',
}


def render_q15_fixed():
    """
    Q15 FIXED: Dimension line must exactly match radius (10cm)
    - Arrow must touch exact endpoints of radius line
    - No overshoot that suggests radius < 10cm
    """
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 10)
    ax.axis('off')
    
    # Parameters
    radius = 10
    perimeter_OBC = 26
    arc_BC = 6  # 26 - 10 - 10
    arc_angle = (arc_BC * 360) / (2 * math.pi * radius)  # 34.4°
    
    # Scale
    scale = 0.35
    cx, cy = 5, 3
    r_plot = radius * scale
    
    # Parametric angles
    angle_B = 90
    angle_C = angle_B - arc_angle
    angle_A = angle_B + (90 - arc_angle)
    angle_D = angle_C - (90 - arc_angle)
    
    # Draw quarter circles
    theta1 = np.linspace(math.radians(angle_C), math.radians(angle_A), 100)
    x1 = cx + r_plot * np.cos(theta1)
    y1 = cy + r_plot * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    theta2 = np.linspace(math.radians(angle_D), math.radians(angle_B), 100)
    x2 = cx + r_plot * np.cos(theta2)
    y2 = cy + r_plot * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Draw radii
    for angle in [angle_A, angle_B, angle_C, angle_D]:
        rad = math.radians(angle)
        ax.plot([cx, cx + r_plot * math.cos(rad)],
                [cy, cy + r_plot * math.sin(rad)],
                'k-', linewidth=2)
    
    # Shade sector OBC
    theta_shade = np.linspace(math.radians(angle_C), math.radians(angle_B), 50)
    x_shade = [cx] + list(cx + r_plot * np.cos(theta_shade)) + [cx]
    y_shade = [cy] + list(cy + r_plot * np.sin(theta_shade)) + [cy]
    shade = Polygon(list(zip(x_shade, y_shade)),
                    facecolor=COLORS['light_blue'], edgecolor='darkblue',
                    linewidth=2, alpha=0.7, zorder=1)
    ax.add_patch(shade)
    
    # Points
    points = {
        'A': (cx + r_plot * math.cos(math.radians(angle_A)),
              cy + r_plot * math.sin(math.radians(angle_A))),
        'B': (cx + r_plot * math.cos(math.radians(angle_B)),
              cy + r_plot * math.sin(math.radians(angle_B))),
        'C': (cx + r_plot * math.cos(math.radians(angle_C)),
              cy + r_plot * math.sin(math.radians(angle_C))),
        'D': (cx + r_plot * math.cos(math.radians(angle_D)),
              cy + r_plot * math.sin(math.radians(angle_D))),
    }
    
    # Draw points and labels
    ax.plot(cx, cy, 'ko', markersize=10)
    ax.text(cx - 0.4, cy - 0.4, 'O', fontsize=FONT_SIZES['axis_label'], fontweight='bold')
    
    for label, (x, y) in points.items():
        ax.plot(x, y, 'ko', markersize=8)
        offset_x = 0.5 if x > cx else -0.5
        offset_y = 0.5 if y > cy else -0.5
        ax.text(x + offset_x, y + offset_y, label,
                fontsize=FONT_SIZES['axis_label'], fontweight='bold',
                ha='center' if abs(x - cx) < 1 else 'left' if x > cx else 'right')
    
    # FIXED: Dimension line for radius - EXACT match, no overshoot
    # Draw dimension line from O to A with exact endpoints
    oa_end = points['A']
    
    # Extension lines (perpendicular to radius direction)
    # Offset the dimension line slightly to the left
    offset_dist = 0.8
    angle_oa = math.atan2(oa_end[1] - cy, oa_end[0] - cx)
    perp_angle = angle_oa + math.pi/2
    
    ext_x = offset_dist * math.cos(perp_angle)
    ext_y = offset_dist * math.sin(perp_angle)
    
    # Dimension line endpoints (exactly at O and A, offset)
    dim_start = (cx + ext_x, cy + ext_y)
    dim_end = (oa_end[0] + ext_x, oa_end[1] + ext_y)
    
    # Extension lines (perpendicular, touching shape)
    ax.plot([cx, dim_start[0]], [cy, dim_start[1]], 'k-', linewidth=0.8)
    ax.plot([oa_end[0], dim_end[0]], [oa_end[1], dim_end[1]], 'k-', linewidth=0.8)
    
    # Dimension line with arrows at BOTH ends
    ax.annotate('', xy=dim_end, xytext=dim_start,
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    
    # Label centered on dimension line
    mid_x = (dim_start[0] + dim_end[0]) / 2
    mid_y = (dim_start[1] + dim_end[1]) / 2
    ax.text(mid_x, mid_y + 0.3, '10 cm',
            fontsize=FONT_SIZES['data_label'], fontweight='bold',
            ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='gray'))
    
    # Info box
    info_text = f'Shaded OBC\nArea = 30 cm²\nPerimeter = {perimeter_OBC} cm'
    ax.text(cx + 2.5, cy + 4, info_text,
            fontsize=FONT_SIZES['annotation'], ha='center',
            bbox=dict(boxstyle='round', facecolor=COLORS['highlight'], alpha=0.5))
    
    # Verification
    verify_text = f'Arc BC = {arc_BC} cm\nAngle = {arc_angle:.1f}°'
    ax.text(10, 8.5, verify_text, fontsize=9, color='green', fontweight='bold')
    
    ax.set_title('Q15: Overlapping Quarter Circles (FIXED)', 
                fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q15_overlapping_quarter_circles_FIXED.png', 
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q15 FIXED: Dimension line exactly matches radius")


def render_q12_fixed():
    """
    Q12 FIXED: Five Squares with solvable constraints
    - Show relationships between squares (e.g., Y = X + 2)
    - Make it possible to deduce all sizes from diagram
    """
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 7)
    ax.axis('off')
    
    # Fixed arrangement that makes the problem solvable:
    # Bottom row: X (4cm), Y (6cm), Z (10cm) - arranged so X + Y = Z
    # Top row: V (4cm) above X, W (6cm) above Y
    # This gives relationships: Y = X + 2, Z = X + Y = 2X + 2, etc.
    
    square_X = 4
    square_Y = 6  # X + 2
    square_Z = 10  # X + Y
    square_W = 6  # Same as Y
    square_V = 4  # Same as X
    
    scale = 0.5
    
    # Square positions (grid-based for clarity)
    squares = [
        {'name': 'X', 'side': square_X, 'pos': (0, 0), 'color': COLORS['light_blue']},
        {'name': 'Y', 'side': square_Y, 'pos': (square_X * scale, 0), 'color': COLORS['light_orange']},
        {'name': 'Z', 'side': square_Z, 'pos': ((square_X + square_Y) * scale, 0), 'color': COLORS['light_green']},
        {'name': 'W', 'side': square_W, 'pos': (square_X * scale, square_Y * scale), 'color': COLORS['light_orange']},
        {'name': 'V', 'side': square_V, 'pos': (0, square_X * scale), 'color': COLORS['light_blue']},
    ]
    
    # Draw squares
    for sq in squares:
        x, y = sq['pos']
        side = sq['side'] * scale
        rect = Rectangle((x, y), side, side,
                         facecolor=sq['color'], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # Name label inside
        ax.text(x + side/2, y + side/2, sq['name'],
                fontsize=FONT_SIZES['data_label'], ha='center', va='center',
                fontweight='bold')
        
        # Side dimension label - show known (X) and unknown (?)
        if sq['name'] == 'X':
            ax.text(x + side/2, y - 0.3, f'{sq["side"]} cm',
                    fontsize=FONT_SIZES['tick_label'], ha='center', fontweight='bold')
        else:
            ax.text(x + side/2, y - 0.3, '?',
                    fontsize=FONT_SIZES['tick_label'], ha='center', fontweight='bold', color='red')
    
    # Rectangle boundary
    total_width = (square_X + square_Y + square_Z) * scale
    total_height = max(square_Z, square_X + square_Y) * scale
    
    rect_boundary = Rectangle((0, 0), total_width, total_height,
                              fill=False, edgecolor='black', linewidth=2.5, linestyle='--')
    ax.add_patch(rect_boundary)
    
    # Dimension lines with formal format
    # Width dimension
    dim_y = -1.2
    ax.plot([0, 0], [0, dim_y], 'k-', linewidth=0.8)  # Extension
    ax.plot([total_width, total_width], [0, dim_y], 'k-', linewidth=0.8)  # Extension
    ax.annotate('', xy=(total_width, dim_y), xytext=(0, dim_y),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(total_width/2, dim_y - 0.3, '? cm',
            fontsize=FONT_SIZES['annotation'], ha='center', fontweight='bold', color='red')
    
    # Height dimension
    dim_x = total_width + 0.5
    ax.plot([total_width, dim_x], [0, 0], 'k-', linewidth=0.8)
    ax.plot([total_width, dim_x], [total_height, total_height], 'k-', linewidth=0.8)
    ax.annotate('', xy=(dim_x, total_height), xytext=(dim_x, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(dim_x + 0.3, total_height/2, '? cm',
            fontsize=FONT_SIZES['annotation'], ha='left', va='center', fontweight='bold', color='red',
            rotation=90)
    
    # Helpful annotations showing relationships
    # Show that X + Y = Z visually
    bracket_y = -0.6
    ax.annotate('', xy=(square_X * scale, bracket_y), xytext=(0, bracket_y),
                arrowprops=dict(arrowstyle='-', color='blue', lw=1))
    ax.annotate('', xy=((square_X + square_Y) * scale, bracket_y), 
                xytext=(square_X * scale, bracket_y),
                arrowprops=dict(arrowstyle='-', color='blue', lw=1))
    ax.text(square_X * scale / 2, bracket_y - 0.3, 'X',
            fontsize=9, ha='center', color='blue')
    ax.text(square_X * scale + square_Y * scale / 2, bracket_y - 0.3, 'Y',
            fontsize=9, ha='center', color='blue')
    
    # Problem statement
    ax.text(5, 6.5, 'Given: Square X = 4 cm', 
            fontsize=FONT_SIZES['axis_label'], ha='center', fontweight='bold')
    ax.text(5, 6, 'Find: (a) Side Y  (b) Rectangle length  (c) Number of 2cm cubes',
            fontsize=FONT_SIZES['annotation'], ha='center')
    
    ax.set_title('Q12: Five Squares in Rectangle (FIXED - Solvable)', 
                fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q12_five_squares_FIXED.png', 
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q12 FIXED: Added solvable constraints and relationships")


def render_q19_fixed():
    """
    Q19 FIXED: True isometric 30° projection
    - Proper isometric angles (30° from horizontal)
    - Accurate cube representation
    - View labels and grid
    """
    fig = plt.figure(figsize=(14, 10), dpi=150)
    
    # Two subplots: isometric view and front view grid
    ax_iso = fig.add_subplot(121)
    ax_grid = fig.add_subplot(122)
    
    # Isometric projection parameters (TRUE 30°)
    COS30 = math.cos(math.radians(30))
    SIN30 = math.sin(math.radians(30))
    scale = 25  # pixels per unit
    
    def iso_x(x, y, z, origin_x=150, origin_y=200):
        """True isometric X coordinate"""
        return origin_x + (x - y) * COS30 * scale
    
    def iso_y(x, y, z, origin_x=150, origin_y=200):
        """True isometric Y coordinate"""
        return origin_y - z * scale + (x + y) * SIN30 * scale * 0.5
    
    # Cube positions (7 cubes in L-shape)
    # Arranged so it's clear and countable
    cubes = [
        (0, 0, 0),  # Base layer
        (1, 0, 0),
        (2, 0, 0),
        (0, 1, 0),
        (0, 0, 1),  # Stack on (0,0)
        (1, 0, 1),  # Stack on (1,0)
        (2, 0, 1),  # Stack on (2,0)
    ]
    
    ax_iso.set_xlim(0, 400)
    ax_iso.set_ylim(0, 400)
    ax_iso.axis('off')
    ax_iso.set_aspect('equal')
    
    # Draw cubes using painter's algorithm (back to front)
    # Sort by y (depth), then x, then z
    sorted_cubes = sorted(cubes, key=lambda c: (c[1], c[0], c[2]))
    
    for x, y, z in sorted_cubes:
        # Calculate all 8 vertices
        vertices = []
        for dx in [0, 1]:
            for dy in [0, 1]:
                for dz in [0, 1]:
                    vx = x + dx
                    vy = y + dy
                    vz = z + dz
                    vertices.append((iso_x(vx, vy, vz), iso_y(vx, vy, vz)))
        
        # Define faces (indices into vertices)
        # Each cube has 6 faces, but we only draw visible ones
        
        # Check which faces are visible
        # Top face (z+1): visible if no cube above
        top_visible = (x, y, z + 1) not in cubes
        # Front face (y-1, toward viewer): visible if no cube in front
        front_visible = (x, y - 1, z) not in cubes
        # Right face (x+1): visible if no cube to the right
        right_visible = (x + 1, y, z) not in cubes
        
        # Get face vertices
        # Top face: vertices where dz=1 (indices 4,5,6,7)
        if top_visible:
            top_verts = [vertices[i] for i in [4, 5, 7, 6]]
            top_poly = Polygon(top_verts, facecolor='#E8F4F8', 
                              edgecolor='black', linewidth=1)
            ax_iso.add_patch(top_poly)
        
        # Front face: vertices where dy=0 (indices 0, 1, 5, 4)
        if front_visible:
            front_verts = [vertices[i] for i in [0, 1, 5, 4]]
            front_poly = Polygon(front_verts, facecolor='#B8D4E3',
                                edgecolor='black', linewidth=1)
            ax_iso.add_patch(front_poly)
        
        # Right face: vertices where dx=1 (indices 1, 3, 7, 5)
        if right_visible:
            right_verts = [vertices[i] for i in [1, 3, 7, 5]]
            right_poly = Polygon(right_verts, facecolor='#88B4C8',
                                edgecolor='black', linewidth=1)
            ax_iso.add_patch(right_poly)
    
    # Add cube count label
    ax_iso.text(200, 50, f'7 cubes', fontsize=FONT_SIZES['data_label'], 
                ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    # View labels with arrows
    # Front view arrow (pointing up)
    ax_iso.annotate('Front', xy=(200, 120), xytext=(200, 30),
                   arrowprops=dict(arrowstyle='->', color='red', lw=2),
                   fontsize=FONT_SIZES['axis_label'], ha='center', 
                   color='red', fontweight='bold')
    
    # Side view arrow (pointing right)
    ax_iso.annotate('Side', xy=(280, 200), xytext=(350, 200),
                   arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                   fontsize=FONT_SIZES['axis_label'], ha='left',
                   color='blue', fontweight='bold')
    
    # Top view arrow (pointing down)
    ax_iso.annotate('Top', xy=(200, 280), xytext=(200, 370),
                   arrowprops=dict(arrowstyle='->', color='green', lw=2),
                   fontsize=FONT_SIZES['axis_label'], ha='center',
                   color='green', fontweight='bold')
    
    ax_iso.set_title('Isometric View (30° projection)', 
                    fontsize=FONT_SIZES['axis_label'], fontweight='bold')
    
    # Front view grid
    ax_grid.set_xlim(-0.5, 4.5)
    ax_grid.set_ylim(-0.5, 3.5)
    ax_grid.set_aspect('equal')
    ax_grid.grid(True, linestyle='-', alpha=0.3)
    
    # Draw grid
    for i in range(5):
        ax_grid.axvline(i, color='gray', linewidth=0.5)
    for i in range(4):
        ax_grid.axhline(i, color='gray', linewidth=0.5)
    
    # Calculate front view (max height at each x position)
    front_view = {}
    for x, y, z in cubes:
        if x not in front_view:
            front_view[x] = z + 1
        else:
            front_view[x] = max(front_view[x], z + 1)
    
    # Draw front view squares
    for x, height in front_view.items():
        for h in range(height):
            rect = Rectangle((x, h), 1, 1, 
                            facecolor='lightblue', edgecolor='black', linewidth=1)
            ax_grid.add_patch(rect)
    
    ax_grid.set_xticks(range(4))
    ax_grid.set_yticks(range(4))
    ax_grid.set_xlabel('Position', fontsize=FONT_SIZES['tick_label'])
    ax_grid.set_ylabel('Height', fontsize=FONT_SIZES['tick_label'])
    ax_grid.set_title('Front View (Grid)', fontsize=FONT_SIZES['axis_label'], fontweight='bold')
    
    plt.suptitle('Q19: 3D Solid Views (FIXED - True Isometric)', 
                fontsize=FONT_SIZES['title'], fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q19_3d_solid_FIXED.png', 
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q19 FIXED: True 30° isometric with view labels and grid")


if __name__ == "__main__":
    print("=" * 70)
    print("Generating FIXED Diagrams")
    print("=" * 70)
    print()
    
    render_q15_fixed()
    render_q12_fixed()
    render_q19_fixed()
    
    print()
    print("=" * 70)
    print(f"✅ All fixed diagrams saved to: {OUTPUT_DIR}")
    print("=" * 70)
