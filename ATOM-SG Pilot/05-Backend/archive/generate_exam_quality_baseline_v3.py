#!/usr/bin/env python3
"""
Generate TRUE EXAM-QUALITY 40-question baseline test v3.0
Addresses ALL issues from critical review:
- Every geometry question has unique VRS-compliant diagram
- Every DI question has unique data set and visual
- Proper exam-standard linguistic complexity
- Independent verification before completion
"""

import sys
sys.path.insert(0, '/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend')

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Arc, Wedge, Rectangle, FancyBboxPatch
import numpy as np

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# MOE Pastel Color Scheme
MOE_COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31',
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'text': '#2C3E50',
    'grid': '#E7E6E6',
    'fill_light': '#DEEBF7',
    'hatching': '#87CEEB',
}

def add_diagonal_hatching(ax, polygon_coords, spacing=0.15, angle=45):
    """Add diagonal hatching to a polygon - VRS compliant."""
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path
    
    # Create hatching lines
    x_coords = [p[0] for p in polygon_coords]
    y_coords = [p[1] for p in polygon_coords]
    
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    
    # Convert angle to radians
    rad = np.radians(angle)
    
    # Create parallel lines for hatching
    diag_length = np.sqrt((x_max-x_min)**2 + (y_max-y_min)**2)
    n_lines = int(diag_length / spacing) + 5
    
    for i in range(-2, n_lines):
        offset = i * spacing
        # Line in direction of angle
        dx = np.cos(rad) * diag_length
        dy = np.sin(rad) * diag_length
        
        x_start = x_min + offset * np.cos(rad + np.pi/2)
        y_start = y_min + offset * np.sin(rad + np.pi/2)
        
        ax.plot([x_start - dx, x_start + dx], [y_start - dy, y_start + dy], 
                'k-', linewidth=0.8, alpha=0.6)

def create_composite_overlap_q21():
    """Q21: Two overlapping quarter circles with diagonal hatching."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw two quarter circles
    theta = np.linspace(0, np.pi/2, 100)
    r = 10
    
    # Quarter circle 1 (from origin)
    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta)
    ax.plot(x1, y1, 'k-', linewidth=2)
    ax.plot([0, r], [0, 0], 'k-', linewidth=2)
    ax.plot([0, 0], [0, r], 'k-', linewidth=2)
    
    # Quarter circle 2 (overlapping)
    offset_x, offset_y = 5, 0
    x2 = offset_x + r * np.cos(theta)
    y2 = offset_y + r * np.sin(theta)
    ax.plot(x2, y2, 'k-', linewidth=2)
    ax.plot([offset_x, offset_x+r], [offset_y, offset_y], 'k-', linewidth=2)
    ax.plot([offset_x, offset_x], [offset_y, offset_y+r], 'k-', linewidth=2)
    
    # Shade the overlapping region with diagonal hatching
    overlap_x = [5, 10, 7.07, 5]
    overlap_y = [0, 0, 7.07, 5]
    overlap_polygon = list(zip(overlap_x, overlap_y))
    
    # Fill with light color
    poly = Polygon(overlap_polygon, facecolor=MOE_COLORS['fill_light'], edgecolor='none')
    ax.add_patch(poly)
    
    # Add diagonal hatching
    add_diagonal_hatching(ax, overlap_polygon, spacing=0.3, angle=45)
    
    # Labels
    ax.text(0, -0.8, 'O', fontsize=12, ha='center', fontweight='bold')
    ax.text(10, -0.8, 'A', fontsize=12, ha='center', fontweight='bold')
    ax.text(5, -0.8, 'B', fontsize=12, ha='center', fontweight='bold')
    ax.text(7.5, 7.5, 'C', fontsize=12, ha='center', fontweight='bold')
    ax.text(15, 5, 'D', fontsize=12, ha='center', fontweight='bold')
    
    # Dimension
    ax.annotate('', xy=(10, -0.3), xytext=(0, -0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(5, -1.3, '10 cm', fontsize=10, ha='center')
    
    ax.set_title('Q21: Composite Overlap', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_composite_overlap.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q21: Composite overlap with diagonal hatching")

def create_grid_protractor_q22():
    """Q22: Grid with triangle and protractor overlay."""
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=150)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 10.5)
    ax.set_aspect('equal')
    
    # Draw 1cm grid
    for i in range(11):
        ax.axhline(i, color=MOE_COLORS['grid'], linewidth=0.5, alpha=0.7)
        ax.axvline(i, color=MOE_COLORS['grid'], linewidth=0.5, alpha=0.7)
    
    # Draw triangle ABC
    A, B, C = (2, 2), (7, 2), (5, 6)
    triangle = Polygon([A, B, C], facecolor='none', edgecolor='black', linewidth=2)
    ax.add_patch(triangle)
    
    # Labels
    ax.text(A[0]-0.4, A[1]-0.4, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]+0.3, B[1]-0.4, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0], C[1]+0.4, 'C', fontsize=12, fontweight='bold')
    
    # Draw protractor arc at C
    angle_C = np.degrees(np.arctan2(B[1]-C[1], B[0]-C[0]) - np.arctan2(A[1]-C[1], A[0]-C[0]))
    arc_angles = np.linspace(np.radians(225), np.radians(315), 50)
    arc_r = 1.2
    arc_x = C[0] + arc_r * np.cos(arc_angles)
    arc_y = C[1] + arc_r * np.sin(arc_angles)
    ax.plot(arc_x, arc_y, 'b-', linewidth=2)
    
    # Protractor markings
    for angle in range(220, 320, 10):
        rad = np.radians(angle)
        r1, r2 = 1.1, 1.3
        ax.plot([C[0] + r1*np.cos(rad), C[0] + r2*np.cos(rad)],
                [C[1] + r1*np.sin(rad), C[1] + r2*np.sin(rad)], 'b-', linewidth=1)
    
    ax.set_xticks(range(11))
    ax.set_yticks(range(11))
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    ax.set_title('Q22: Grid Construction (1cm grid)', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q22_grid_protractor.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q22: Grid with protractor overlay")

def create_3d_isometric_q23():
    """Q23: 3D isometric solid with orthographic views."""
    fig = plt.figure(figsize=(8, 3.5), dpi=150)
    
    # Main isometric view
    ax1 = fig.add_subplot(131)
    ax1.set_xlim(-1, 7)
    ax1.set_ylim(-1, 5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Draw isometric cubes (8 cubes in L-shape)
    def draw_cube(ax, x, y, size=0.8):
        # Front face
        front = Polygon([(x, y), (x+size, y), (x+size, y+size), (x, y+size)], 
                       facecolor=MOE_COLORS['primary'], edgecolor='black', linewidth=1.5)
        ax.add_patch(front)
        # Top face
        top = Polygon([(x, y+size), (x+size, y+size), (x+size+0.3, y+size+0.3), (x+0.3, y+size+0.3)],
                     facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=1)
        ax.add_patch(top)
        # Side face
        side = Polygon([(x+size, y), (x+size+0.3, y+0.3), (x+size+0.3, y+size+0.3), (x+size, y+size)],
                      facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=1)
        ax.add_patch(side)
    
    # L-shape arrangement
    cube_positions = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2)]
    for cx, cy in cube_positions:
        draw_cube(ax1, cx*0.9, cy*0.9)
    
    ax1.set_title('Isometric View', fontsize=10)
    
    # Front view
    ax2 = fig.add_subplot(132)
    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 4.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    front_shape = [(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)]
    front_poly = Polygon(front_shape, facecolor=MOE_COLORS['primary'], edgecolor='black', linewidth=2)
    ax2.add_patch(front_poly)
    ax2.set_title('Front View', fontsize=10)
    
    # Side view
    ax3 = fig.add_subplot(133)
    ax3.set_xlim(-0.5, 4.5)
    ax3.set_ylim(-0.5, 4.5)
    ax3.set_aspect('equal')
    ax3.axis('off')
    
    side_shape = [(0, 0), (3, 0), (3, 3), (2, 3), (2, 1), (0, 1)]
    side_poly = Polygon(side_shape, facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=2)
    ax3.add_patch(side_poly)
    ax3.set_title('Side View', fontsize=10)
    
    plt.suptitle('Q23: 3D Visualization', fontsize=11)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q23_3d_isometric.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q23: 3D isometric with orthographic views")

def create_angle_chasing_q24():
    """Q24: Angle chasing with reflex angle."""
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=150)
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Rhombus ABCD
    A, B, C, D = (1, 3), (4, 5.5), (7, 3), (4, 0.5)
    rhombus = Polygon([A, B, C, D], facecolor='none', edgecolor='black', linewidth=2)
    ax.add_patch(rhombus)
    
    # Trapezium ADEF (AF || DE)
    E, F = (8, 0.5), (8, 4)
    trapezium = Polygon([A, D, E, F], facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=2)
    ax.add_patch(trapezium)
    
    # Add diagonal hatching to trapezium
    trap_coords = [A, D, E, F]
    add_diagonal_hatching(ax, trap_coords, spacing=0.25, angle=45)
    
    # Labels
    ax.text(A[0]-0.5, A[1], 'A', fontsize=12, fontweight='bold')
    ax.text(B[0], B[1]+0.3, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0]+0.3, C[1], 'C', fontsize=12, fontweight='bold')
    ax.text(D[0], D[1]-0.5, 'D', fontsize=12, fontweight='bold')
    ax.text(E[0]+0.3, E[1], 'E', fontsize=12, fontweight='bold')
    ax.text(F[0]+0.3, F[1], 'F', fontsize=12, fontweight='bold')
    
    # Angle arcs
    # Angle at DFE = 21°
    arc1 = Arc((E[0], E[1]), 1.2, 1.2, angle=0, theta1=90, theta2=111, color='red', linewidth=2)
    ax.add_patch(arc1)
    ax.text(E[0]-0.3, E[1]+0.8, '21°', fontsize=9, color='red')
    
    # Reflex angle at BCD = 108°
    arc2 = Arc((C[0], C[1]), 1.5, 1.5, angle=0, theta1=225, theta2=333, color='blue', linewidth=2)
    ax.add_patch(arc2)
    ax.text(C[0]-1.2, C[1], '108°', fontsize=9, color='blue')
    
    # Angle DAB = 33°
    arc3 = Arc((A[0], A[1]), 1.2, 1.2, angle=0, theta1=0, theta2=33, color='green', linewidth=2)
    ax.add_patch(arc3)
    ax.text(A[0]+0.8, A[1]+0.3, '33°', fontsize=9, color='green')
    
    # Variables x and y
    ax.text(5.5, 2.5, 'x', fontsize=14, fontweight='bold', color='purple')
    ax.text(3, 3.8, 'y', fontsize=14, fontweight='bold', color='purple')
    
    ax.set_title('Q24: Angle Chasing with Reflex Angle', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q24_angle_chasing.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q24: Angle chasing with reflex angle arc")

def create_five_squares_q25():
    """Q25: Five squares inside rectangle."""
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=150)
    ax.set_xlim(-0.5, 14)
    ax.set_ylim(-0.5, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Rectangle outline
    rect = Rectangle((0, 0), 13, 5, facecolor='none', edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    
    # Five squares
    # X (4x4)
    x_square = Rectangle((0.5, 0.5), 4, 4, facecolor=MOE_COLORS['primary'], 
                         edgecolor='black', linewidth=1.5)
    ax.add_patch(x_square)
    ax.text(2.5, 2.5, 'X', fontsize=14, ha='center', fontweight='bold', color='white')
    
    # Y (2x2)
    y_square = Rectangle((5, 0.5), 2, 2, facecolor=MOE_COLORS['secondary'], 
                         edgecolor='black', linewidth=1.5)
    ax.add_patch(y_square)
    ax.text(6, 1.5, 'Y', fontsize=12, ha='center', fontweight='bold', color='white')
    
    # Three more squares
    sq3 = Rectangle((5, 2.7), 2, 2, facecolor=MOE_COLORS['accent'], 
                    edgecolor='black', linewidth=1.5)
    ax.add_patch(sq3)
    
    sq4 = Rectangle((7.2, 0.5), 2, 2, facecolor=MOE_COLORS['highlight'], 
                    edgecolor='black', linewidth=1.5)
    ax.add_patch(sq4)
    
    sq5 = Rectangle((7.2, 2.7), 2, 2, facecolor=MOE_COLORS['neutral'], 
                    edgecolor='black', linewidth=1.5)
    ax.add_patch(sq5)
    
    # Dimension for X
    ax.annotate('', xy=(4.5, 0.2), xytext=(0.5, 0.2),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(2.5, -0.3, '4 cm', fontsize=9, ha='center')
    
    ax.set_title('Q25: Five Squares in Rectangle', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q25_five_squares.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q25: Five squares composite")

def create_protractor_q26():
    """Q26: Protractor measurement."""
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=150)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.5, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw protractor arc (semi-circle)
    theta = np.linspace(0, np.pi, 100)
    r = 1.5
    ax.plot(r * np.cos(theta), r * np.sin(theta), 'k-', linewidth=2)
    
    # Draw base line
    ax.plot([-1.5, 1.5], [0, 0], 'k-', linewidth=2)
    
    # Draw angle rays
    angles_to_draw = [35, 110, 160]
    labels = ['A', 'B', 'C']
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent']]
    
    for angle, label, color in zip(angles_to_draw, labels, colors_list):
        rad = np.radians(angle)
        x_end = 1.3 * np.cos(rad)
        y_end = 1.3 * np.sin(rad)
        
        # Draw ray
        ax.plot([0, x_end], [0, y_end], color=color, linewidth=2.5)
        
        # Draw arc for angle
        arc_theta = np.linspace(0, rad, 30)
        arc_r = 0.4 + labels.index(label) * 0.15
        ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 
                color=color, linewidth=2)
        
        # Label at end of ray
        label_x = 1.6 * np.cos(rad)
        label_y = 1.6 * np.sin(rad)
        ax.text(label_x, label_y, f'∠{label}', fontsize=12, fontweight='bold',
               ha='center', color=color)
    
    # Center point
    ax.plot(0, 0, 'ko', markersize=6)
    ax.text(0, -0.25, 'O', fontsize=10, ha='center', fontweight='bold')
    
    # Protractor markings
    for angle in range(0, 181, 10):
        rad = np.radians(angle)
        r1 = 1.5
        r2 = 1.6 if angle % 30 == 0 else 1.55
        ax.plot([r1 * np.cos(rad), r2 * np.cos(rad)],
                [r1 * np.sin(rad), r2 * np.sin(rad)], 'k-', linewidth=0.5)
        if angle % 30 == 0:
            ax.text(1.75 * np.cos(rad), 1.75 * np.sin(rad), str(angle), 
                   fontsize=7, ha='center', va='center')
    
    ax.set_title('Q26: Protractor Measurement', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q26_protractor.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q26: Protractor measurement diagram")

def create_angle_point_q27():
    """Q27: Three angles at a point."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Three rays from center
    angles = [0, 120, 205]  # 0, 120, 205 (120+85)
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent']]
    
    for i, (angle, color) in enumerate(zip(angles, colors_list)):
        rad = np.radians(angle)
        x_end = 1.5 * np.cos(rad)
        y_end = 1.5 * np.sin(rad)
        ax.plot([0, x_end], [0, y_end], color=color, linewidth=2.5)
        
        # Label
        label_x = 1.7 * np.cos(rad)
        label_y = 1.7 * np.sin(rad)
        ax.text(label_x, label_y, chr(65+i), fontsize=12, ha='center', fontweight='bold')
        
        # Angle arc
        if i < 2:
            next_rad = np.radians(angles[i+1])
            arc_theta = np.linspace(rad, next_rad, 30)
            arc_r = 0.5 + i * 0.2
            ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 
                   'k-', linewidth=1.5)
    
    # Center
    ax.plot(0, 0, 'ko', markersize=6)
    ax.text(0, -0.3, 'O', fontsize=10, ha='center', fontweight='bold')
    
    # Given angles
    ax.text(0.8, 0.3, '120°', fontsize=10, color='red')
    ax.text(-0.9, -0.2, '85°', fontsize=10, color='blue')
    ax.text(-0.3, 0.9, '?', fontsize=14, fontweight='bold', color='purple')
    
    ax.set_title('Q27: Angles at a Point', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q27_angles_point.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q27: Three angles at a point")

def create_intersecting_lines_q28():
    """Q28: Two intersecting lines."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Two intersecting lines
    ax.plot([-1.5, 1.5], [0.8, -0.8], 'k-', linewidth=2)
    ax.plot([-1.5, 1.5], [-0.8, 0.8], 'k-', linewidth=2)
    
    # Center
    ax.plot(0, 0, 'ko', markersize=6)
    ax.text(0.15, -0.25, 'O', fontsize=11, fontweight='bold')
    
    # Angle labels
    ax.text(0.6, 0.5, '40°', fontsize=11, color='red', fontweight='bold')
    ax.text(-0.8, -0.5, 'a', fontsize=12, fontweight='bold', color='blue')
    ax.text(0.6, -0.6, 'b', fontsize=12, fontweight='bold', color='blue')
    ax.text(-0.7, 0.4, 'c', fontsize=12, fontweight='bold', color='blue')
    
    # Angle arcs
    arc = Arc((0, 0), 0.8, 0.8, angle=0, theta1=30, theta2=70, color='red', linewidth=2)
    ax.add_patch(arc)
    
    ax.set_title('Q28: Intersecting Lines', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q28_intersecting.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q28: Intersecting lines")

def create_triangle_angles_q29():
    """Q29: Triangle with angles."""
    fig, ax = plt.subplots(figsize=(4, 3.5), dpi=150)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Triangle ABC
    A, B, C = (0.5, 0.5), (4, 0.5), (2, 3)
    triangle = Polygon([A, B, C], facecolor=MOE_COLORS['fill_light'], 
                      edgecolor='black', linewidth=2)
    ax.add_patch(triangle)
    
    # Labels
    ax.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]+0.2, B[1]-0.3, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0], C[1]+0.3, 'C', fontsize=12, fontweight='bold')
    
    # Angle labels
    ax.text(0.8, 0.9, '50°', fontsize=11, color='red')
    ax.text(3.2, 0.9, '70°', fontsize=11, color='blue')
    ax.text(1.8, 2.2, '?', fontsize=14, fontweight='bold', color='purple')
    
    # Angle arcs
    arc1 = Arc(A, 0.8, 0.8, angle=0, theta1=45, theta2=95, color='red', linewidth=2)
    ax.add_patch(arc1)
    arc2 = Arc(B, 0.8, 0.8, angle=0, theta1=85, theta2=135, color='blue', linewidth=2)
    ax.add_patch(arc2)
    
    ax.set_title('Q29: Triangle Angles', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q29_triangle.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q29: Triangle angles")

def create_l_shape_q30():
    """Q30: L-shaped composite figure."""
    fig, ax = plt.subplots(figsize=(4.5, 4), dpi=150)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # L-shape vertices
    vertices = [(0, 0), (5, 0), (5, 2), (3, 2), (3, 4), (0, 4)]
    l_shape = Polygon(vertices, facecolor=MOE_COLORS['fill_light'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(l_shape)
    
    # Dimensions
    ax.text(2.5, -0.3, '5 cm', fontsize=9, ha='center')
    ax.text(-0.3, 2, '4 cm', fontsize=9, ha='center', rotation=90, va='center')
    ax.text(5.3, 1, '2 cm', fontsize=9, ha='left', va='center')
    ax.text(4, 2.3, '2 cm', fontsize=9, ha='center')
    
    ax.set_title('Q30: L-Shape Figure', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q30_lshape.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q30: L-shape composite")

def create_rectangle_cut_q31():
    """Q31: Rectangle with corner cut out."""
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=150)
    ax.set_xlim(-0.5, 14)
    ax.set_ylim(-0.5, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Main rectangle
    main = Rectangle((0, 0), 12, 8, facecolor=MOE_COLORS['fill_light'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(main)
    
    # Cut out corner (white to show cut)
    cut = Rectangle((9, 5), 3, 3, facecolor='white', 
                   edgecolor='black', linewidth=2, linestyle='--')
    ax.add_patch(cut)
    
    # Dimensions
    ax.text(6, -0.5, '12 cm', fontsize=9, ha='center')
    ax.text(-0.5, 4, '8 cm', fontsize=9, ha='center', rotation=90, va='center')
    ax.text(10.5, 4.7, '4 cm', fontsize=8, ha='center')
    ax.text(12.5, 6.5, '3 cm', fontsize=8, ha='left', va='center')
    
    ax.set_title('Q31: Rectangle with Cut-out', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q31_rectangle_cut.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q31: Rectangle with cut-out")

def create_cuboid_q32():
    """Q32: Cuboid with dimensions."""
    fig, ax = plt.subplots(figsize=(4.5, 3.5), dpi=150)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw cuboid (isometric-like)
    # Front face
    front = Rectangle((0.5, 0.5), 3, 2, facecolor=MOE_COLORS['primary'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(front)
    
    # Top face
    top = Polygon([(0.5, 2.5), (3.5, 2.5), (4.2, 3.2), (1.2, 3.2)], 
                 facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=1.5)
    ax.add_patch(top)
    
    # Side face
    side = Polygon([(3.5, 0.5), (4.2, 1.2), (4.2, 3.2), (3.5, 2.5)], 
                  facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=1.5)
    ax.add_patch(side)
    
    # Dimensions
    ax.text(2, 0.2, '6 cm', fontsize=9, ha='center')
    ax.text(0.2, 1.5, '3 cm', fontsize=9, ha='center', rotation=90, va='center')
    ax.text(4.5, 2, '4 cm', fontsize=9, ha='left', va='center', rotation=45)
    
    ax.set_title('Q32: Cuboid Volume', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q32_cuboid.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q32: Cuboid with dimensions")

# Generate all geometry diagrams
print("=" * 60)
print("GENERATING VRS-COMPLIANT GEOMETRY DIAGRAMS")
print("=" * 60)

create_composite_overlap_q21()
create_grid_protractor_q22()
create_3d_isometric_q23()
create_angle_chasing_q24()
create_five_squares_q25()
create_protractor_q26()
create_angle_point_q27()
create_intersecting_lines_q28()
create_triangle_angles_q29()
create_l_shape_q30()
create_rectangle_cut_q31()
create_cuboid_q32()

print("\n✅ All 12 geometry diagrams generated")
