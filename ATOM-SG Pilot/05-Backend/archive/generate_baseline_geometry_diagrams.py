#!/usr/bin/env python3
"""
Generate ONLY the geometry diagrams needed for:
1. Baseline Test (40 questions)
2. Training/Intervention (25 geometry problems)
3. Transfer Testing (variations)

Based on Problem-Pack-Plan: 25 geometry items (G001-G025)
~20 need diagrams, 5 are text-only
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Arc, Wedge, Rectangle, FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MOE_COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31', 
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'fill_light': '#DEEBF7',
}

# ============================================================
# G1: ANGLE REASONING (8 diagrams)
# ============================================================

def generate_G001():
    """Protractor measurement."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.set_xlim(-2, 6)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    center = (2, 0.5)
    
    # Protractor arc
    theta = np.linspace(0, np.pi, 100)
    x = center[0] + 2 * np.cos(theta)
    y = center[1] + 2 * np.sin(theta)
    ax.plot(x, y, 'k-', linewidth=2)
    
    # Markings
    for angle in range(0, 181, 10):
        rad = np.radians(angle)
        r1, r2 = 2, 2.15 if angle % 30 == 0 else 2.08
        ax.plot([center[0] + r1*np.cos(rad), center[0] + r2*np.cos(rad)],
                [center[1] + r1*np.sin(rad), center[1] + r2*np.sin(rad)], 'k-', linewidth=0.5)
    
    # Angle rays
    angles = [45, 120, 90]
    labels = ['A', 'B', 'C']
    colors = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent']]
    
    for angle, label, color in zip(angles, labels, colors):
        rad = np.radians(angle)
        x_end = center[0] + 1.8 * np.cos(rad)
        y_end = center[1] + 1.8 * np.sin(rad)
        ax.plot([center[0], x_end], [center[1], y_end], color=color, linewidth=2.5)
        
        arc_theta = np.linspace(0, rad, 30)
        arc_r = 0.4 + labels.index(label) * 0.15
        ax.plot(center[0] + arc_r * np.cos(arc_theta),
                center[1] + arc_r * np.sin(arc_theta), color=color, linewidth=2)
        
        label_x = center[0] + 2.3 * np.cos(rad)
        label_y = center[1] + 2.3 * np.sin(rad)
        ax.text(label_x, label_y, f'∠{label}', fontsize=12, ha='center', fontweight='bold', color=color)
    
    ax.plot(center[0], center[1], 'ko', markersize=8)
    ax.text(center[0], center[1]-0.3, 'O', fontsize=11, ha='center', fontweight='bold')
    ax.set_title('G001: Measure angles ∠A, ∠B, ∠C', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G001.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G001")

def generate_G003():
    """Angles at a point."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Three rays from center
    angles = [0, 110, 200]  # Three angles that sum to 310, leaving 50° for fourth
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent']]
    
    for i, (angle, color) in enumerate(zip(angles, colors_list)):
        rad = np.radians(angle)
        x_end = 1.5 * np.cos(rad)
        y_end = 1.5 * np.sin(rad)
        ax.plot([0, x_end], [0, y_end], color=color, linewidth=2.5)
        
        label_x = 1.7 * np.cos(rad)
        label_y = 1.7 * np.sin(rad)
        ax.text(label_x, label_y, chr(65+i), fontsize=12, ha='center', fontweight='bold')
        
        if i < 2:
            next_rad = np.radians(angles[i+1])
            arc_theta = np.linspace(rad, next_rad, 30)
            arc_r = 0.5 + i * 0.2
            ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), 'k-', linewidth=1.5)
    
    # Fourth ray for unknown angle
    ax.plot([0, 1.5], [0, 0], color=MOE_COLORS['neutral'], linewidth=2.5)
    ax.text(1.7, 0, 'D', fontsize=12, ha='center', fontweight='bold')
    
    # Given angles
    ax.text(0.8, 0.6, '110°', fontsize=10, color='red')
    ax.text(-0.9, -0.3, '90°', fontsize=10, color='blue')
    ax.text(0.3, -0.8, '?', fontsize=14, fontweight='bold', color='purple')
    
    ax.plot(0, 0, 'ko', markersize=8)
    ax.text(0, -0.25, 'O', fontsize=10, ha='center', fontweight='bold')
    ax.set_title('G003: Angles at a Point', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G003.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G003")

def generate_G004():
    """Vertically opposite angles."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Two intersecting lines
    ax.plot([-1.5, 1.5], [1, -1], 'k-', linewidth=2.5)
    ax.plot([-1.5, 1.5], [-1, 1], 'k-', linewidth=2.5)
    
    ax.plot(0, 0, 'ko', markersize=8)
    ax.text(0.15, -0.2, 'O', fontsize=11, fontweight='bold')
    
    # Angle labels
    ax.text(0.5, 0.5, '50°', fontsize=11, color='red', fontweight='bold')
    ax.text(-0.7, -0.5, 'a', fontsize=12, fontweight='bold', color='blue')
    ax.text(0.5, -0.6, 'b', fontsize=12, fontweight='bold', color='blue')
    ax.text(-0.6, 0.4, 'c', fontsize=12, fontweight='bold', color='blue')
    
    # Arc
    arc = Arc((0, 0), 0.8, 0.8, angle=0, theta1=30, theta2=70, color='red', linewidth=2)
    ax.add_patch(arc)
    
    ax.set_title('G004: Vertically Opposite Angles', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G004.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G004")

def generate_G005():
    """Triangle angle sum."""
    fig, ax = plt.subplots(figsize=(4, 3.5), dpi=150)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    A, B, C = (0.5, 0.5), (4.5, 0.5), (2.5, 3.5)
    triangle = Polygon([A, B, C], facecolor=MOE_COLORS['fill_light'], 
                      edgecolor='black', linewidth=2)
    ax.add_patch(triangle)
    
    ax.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=12, fontweight='bold')
    ax.text(B[0]+0.2, B[1]-0.3, 'B', fontsize=12, fontweight='bold')
    ax.text(C[0], C[1]+0.3, 'C', fontsize=12, fontweight='bold')
    
    ax.text(0.8, 0.9, '55°', fontsize=11, color='red')
    ax.text(3.8, 0.9, '65°', fontsize=11, color='blue')
    ax.text(2.3, 2.5, '?', fontsize=14, fontweight='bold', color='purple')
    
    arc1 = Arc(A, 0.8, 0.8, angle=0, theta1=45, theta2=100, color='red', linewidth=2)
    ax.add_patch(arc1)
    arc2 = Arc(B, 0.8, 0.8, angle=0, theta1=80, theta2=135, color='blue', linewidth=2)
    ax.add_patch(arc2)
    
    ax.set_title('G005: Triangle Angle Sum', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G005.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G005")

# ============================================================
# G2: AREA & PERIMETER (6 diagrams - excluding G013, G014 text-only)
# ============================================================

def generate_G009():
    """Rectangle perimeter."""
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)
    ax.set_xlim(-0.5, 9)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    rect = Rectangle((0, 0), 8, 4, facecolor=MOE_COLORS['fill_light'], 
                    edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    
    ax.text(4, -0.4, '8 cm', fontsize=11, ha='center', fontweight='bold')
    ax.text(-0.4, 2, '4 cm', fontsize=11, ha='center', rotation=90, va='center', fontweight='bold')
    
    ax.set_title('G009: Rectangle Perimeter', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G009.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G009")

def generate_G011():
    """L-shape composite area."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.5, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # L-shape vertices
    vertices = [(0, 0), (5, 0), (5, 2), (3, 2), (3, 4), (0, 4)]
    l_shape = Polygon(vertices, facecolor=MOE_COLORS['fill_light'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(l_shape)
    
    # Dimensions
    ax.text(2.5, -0.4, '5 cm', fontsize=10, ha='center')
    ax.text(-0.4, 2, '4 cm', fontsize=10, ha='center', rotation=90, va='center')
    ax.text(5.4, 1, '2 cm', fontsize=10, ha='left', va='center')
    ax.text(4, 2.4, '2 cm', fontsize=10, ha='center')
    
    ax.set_title('G011: L-Shape Composite Area', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G011.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G011")

def generate_G012():
    """Rectangle with cut-out."""
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=150)
    ax.set_xlim(-0.5, 9)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Main rectangle
    main = Rectangle((0, 0), 8, 4, facecolor=MOE_COLORS['fill_light'], 
                    edgecolor='black', linewidth=2)
    ax.add_patch(main)
    
    # Cut-out
    cut = Rectangle((6, 2), 2, 2, facecolor='white', 
                   edgecolor='black', linewidth=2, linestyle='--')
    ax.add_patch(cut)
    
    ax.text(4, -0.4, '8 cm', fontsize=10, ha='center')
    ax.text(-0.4, 2, '4 cm', fontsize=10, ha='center', rotation=90, va='center')
    ax.text(7, 1.7, '2 cm', fontsize=9, ha='center')
    ax.text(8.4, 3, '2 cm', fontsize=9, ha='left', va='center')
    
    ax.set_title('G012: Rectangle with Cut-out', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G012.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G012")

def generate_G015():
    """Lines of symmetry."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-2, 4)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Square
    square = Rectangle((0, 0), 3, 3, facecolor=MOE_COLORS['fill_light'], 
                      edgecolor='black', linewidth=2)
    ax.add_patch(square)
    
    # Symmetry lines (dashed)
    ax.plot([1.5, 1.5], [0, 3], 'b--', linewidth=1.5, alpha=0.7)
    ax.plot([0, 3], [1.5, 1.5], 'b--', linewidth=1.5, alpha=0.7)
    ax.plot([0, 3], [0, 3], 'b--', linewidth=1.5, alpha=0.7)
    ax.plot([0, 3], [3, 0], 'b--', linewidth=1.5, alpha=0.7)
    
    ax.text(1.5, -0.5, 'How many lines\nof symmetry?', fontsize=10, ha='center')
    
    ax.set_title('G015: Lines of Symmetry', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G015.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G015")

# ============================================================
# G3: VOLUME & 3D (4 diagrams)
# ============================================================

def generate_G018():
    """Cuboid with unit conversion."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cuboid (larger than G017)
    front = Rectangle((1, 0.5), 4, 2.5, facecolor=MOE_COLORS['primary'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(front)
    
    top = Polygon([(1, 3), (5, 3), (6, 4), (2, 4)], 
                 facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=1.5)
    ax.add_patch(top)
    
    side = Polygon([(5, 0.5), (6, 1.5), (6, 4), (5, 3)], 
                  facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=1.5)
    ax.add_patch(side)
    
    ax.text(3, 0.2, '50 cm', fontsize=10, ha='center')
    ax.text(0.7, 1.75, '30 cm', fontsize=10, ha='center', rotation=90, va='center')
    ax.text(6.2, 2.5, '20 cm', fontsize=10, ha='left', va='center', rotation=45)
    
    ax.set_title('G018: Cuboid Volume (Unit Conversion)', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G018.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G018")

def generate_G019():
    """Net of cube."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cross-shaped net
    positions = [(2, 2), (2, 0), (0, 2), (2, 4), (4, 2), (6, 2)]
    labels = ['Base', 'Front', 'Left', 'Back', 'Right', 'Top']
    
    for i, (pos, label) in enumerate(zip(positions, labels)):
        square = Rectangle(pos, 2, 2, facecolor=MOE_COLORS['fill_light'], 
                          edgecolor='black', linewidth=1.5)
        ax.add_patch(square)
        ax.text(pos[0]+1, pos[1]+1, label, fontsize=8, ha='center', va='center')
    
    ax.set_title('G019: Net of a Cube', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G019.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G019")

def generate_G020():
    """Draw net from 3D shape."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cuboid 3D view
    front = Rectangle((0.5, 0.5), 3, 2, facecolor=MOE_COLORS['primary'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(front)
    
    top = Polygon([(0.5, 2.5), (3.5, 2.5), (4.5, 3.5), (1.5, 3.5)], 
                 facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=1.5)
    ax.add_patch(top)
    
    side = Polygon([(3.5, 0.5), (4.5, 1.5), (4.5, 3.5), (3.5, 2.5)], 
                  facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=1.5)
    ax.add_patch(side)
    
    ax.text(2, -0.3, 'Draw the net', fontsize=11, ha='center', fontweight='bold')
    
    ax.set_title('G020: Draw Net from 3D Shape', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G020.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G020")

# ============================================================
# G4: PROPERTIES & CLASSIFICATION (5 diagrams)
# ============================================================

def generate_G022():
    """Triangle by angles."""
    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Three triangles
    triangles = [
        ([0.5, 0.5], [3.5, 0.5], [2, 2.5]),  # Acute
        ([4, 0.5], [7, 0.5], [4, 2.5]),       # Right
        ([7.5, 0.5], [9.5, 0.5], [8.5, 2])    # Obtuse
    ]
    labels = ['A', 'B', 'C']
    
    for i, (tri, label) in enumerate(zip(triangles, labels)):
        A, B, C = tri
        triangle = Polygon([A, B, C], facecolor=MOE_COLORS['fill_light'], 
                          edgecolor='black', linewidth=2)
        ax.add_patch(triangle)
        ax.text((A[0]+B[0]+C[0])/3, 2.8, label, fontsize=12, ha='center', fontweight='bold')
    
    ax.set_title('G022: Classify Triangles by Angles', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G022.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G022")

def generate_G023():
    """Quadrilateral classification."""
    fig, ax = plt.subplots(figsize=(8, 2.5), dpi=150)
    ax.set_xlim(-0.5, 12)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Square
    square = Rectangle((0, 0), 2, 2, facecolor=MOE_COLORS['fill_light'], 
                      edgecolor='black', linewidth=2)
    ax.add_patch(square)
    ax.text(1, -0.4, 'A', fontsize=11, ha='center', fontweight='bold')
    
    # Rectangle
    rect = Rectangle((3, 0), 2.5, 1.5, facecolor=MOE_COLORS['fill_light'], 
                    edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(4.25, -0.4, 'B', fontsize=11, ha='center', fontweight='bold')
    
    # Parallelogram
    para = Polygon([(6.5, 0), (8.5, 0), (9, 2), (7, 2)], 
                  facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=2)
    ax.add_patch(para)
    ax.text(7.75, -0.4, 'C', fontsize=11, ha='center', fontweight='bold')
    
    # Rhombus
    rhombus = Polygon([(10, 1), (11, 2.5), (12, 1), (11, -0.5)], 
                     facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=2)
    ax.add_patch(rhombus)
    ax.text(11, -0.9, 'D', fontsize=11, ha='center', fontweight='bold')
    
    ax.set_title('G023: Classify Quadrilaterals', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G023.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G023")

def generate_G025():
    """Pie chart fractions."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Pie chart with 90° sector
    sizes = [25, 35, 20, 20]
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], 
                   MOE_COLORS['accent'], MOE_COLORS['highlight']]
    explode = (0.05, 0, 0, 0)
    
    wedges, texts = ax.pie(sizes, explode=explode, colors=colors_list,
                          startangle=90, wedgeprops=dict(edgecolor='black', linewidth=1.5))
    
    # Highlight 90° sector
    ax.text(0.5, 0.5, '90°', fontsize=12, ha='center', fontweight='bold', color='white')
    
    ax.set_title('G025: Pie Chart Fractions', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G025.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G025")

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Generating Baseline Geometry Diagrams")
    print("=" * 60)
    
    # G1: Angle Reasoning
    generate_G001()
    generate_G003()
    generate_G004()
    generate_G005()
    
    # G2: Area & Perimeter
    generate_G009()
    generate_G011()
    generate_G012()
    generate_G015()
    
    # G3: Volume & 3D
    generate_G018()
    generate_G019()
    generate_G020()
    
    # G4: Properties
    generate_G022()
    generate_G023()
    generate_G025()
    
    print("\n" + "=" * 60)
    print("✅ Generated 14 new geometry diagrams")
    print("=" * 60)
    print("\nTotal diagrams now available:")
    print("  - G001-G025: 20 diagrams")
    print("  - Q21-Q25: 5 diagrams")
    print("  - Total: 25 geometry diagrams")
