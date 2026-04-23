#!/usr/bin/env python3
"""
Generate all geometry diagrams from YAML specifications
Uses matplotlib to render exam-quality diagrams
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Arc, Wedge, Rectangle, FancyBboxPatch
import numpy as np
from pathlib import Path
import yaml

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
}

def draw_grid(ax, size=10, spacing=1):
    """Draw square grid with 1cm precision."""
    for i in range(size + 1):
        ax.axhline(i * spacing, color=MOE_COLORS['grid'], linewidth=0.5, alpha=0.7)
        ax.axvline(i * spacing, color=MOE_COLORS['grid'], linewidth=0.5, alpha=0.7)

def draw_protractor(ax, center, radius=1.5):
    """Draw protractor arc with markings."""
    theta = np.linspace(0, np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, 'k-', linewidth=2)
    
    # Markings every 10 degrees
    for angle in range(0, 181, 10):
        rad = np.radians(angle)
        r1 = radius
        r2 = radius + 0.1 if angle % 30 == 0 else radius + 0.05
        ax.plot([center[0] + r1*np.cos(rad), center[0] + r2*np.cos(rad)],
                [center[1] + r1*np.sin(rad), center[1] + r2*np.sin(rad)], 
                'k-', linewidth=0.5)

def generate_G001():
    """G001: Protractor measurement."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.set_xlim(-2, 6)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    center = (2, 0.5)
    
    # Draw protractor
    draw_protractor(ax, center, radius=2)
    
    # Draw angle rays
    angles = [45, 120, 90]
    labels = ['A', 'B', 'C']
    colors = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent']]
    
    for angle, label, color in zip(angles, labels, colors):
        rad = np.radians(angle)
        x_end = center[0] + 1.8 * np.cos(rad)
        y_end = center[1] + 1.8 * np.sin(rad)
        ax.plot([center[0], x_end], [center[1], y_end], 
                color=color, linewidth=2.5)
        
        # Arc for angle
        arc_theta = np.linspace(0, rad, 30)
        arc_r = 0.5 + labels.index(label) * 0.2
        ax.plot(center[0] + arc_r * np.cos(arc_theta),
                center[1] + arc_r * np.sin(arc_theta),
                color=color, linewidth=2)
        
        # Label
        label_x = center[0] + 2.2 * np.cos(rad)
        label_y = center[1] + 2.2 * np.sin(rad)
        ax.text(label_x, label_y, f'∠{label}', fontsize=12, 
               ha='center', fontweight='bold', color=color)
    
    # Center point
    ax.plot(center[0], center[1], 'ko', markersize=8)
    ax.text(center[0], center[1]-0.3, 'O', fontsize=11, ha='center', fontweight='bold')
    
    ax.set_title('G001: Measure angles ∠A, ∠B, ∠C', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G001.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G001: Protractor measurement")

def generate_G002():
    """G002: Angles on straight line."""
    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Straight line ABC
    ax.plot([-5, 5], [0, 0], 'k-', linewidth=2.5)
    
    # Point D above
    D = (2, 3)
    
    # Draw lines from B to D
    ax.plot([0, D[0]], [0, D[1]], 'k-', linewidth=2)
    
    # Points
    ax.plot(-5, 0, 'ko', markersize=8)
    ax.plot(0, 0, 'ko', markersize=8)
    ax.plot(5, 0, 'ko', markersize=8)
    ax.plot(D[0], D[1], 'ko', markersize=8)
    
    # Labels
    ax.text(-5, -0.5, 'A', fontsize=12, ha='center', fontweight='bold')
    ax.text(0, -0.5, 'B', fontsize=12, ha='center', fontweight='bold')
    ax.text(5, -0.5, 'C', fontsize=12, ha='center', fontweight='bold')
    ax.text(D[0]+0.3, D[1], 'D', fontsize=12, ha='left', fontweight='bold')
    
    # Angle labels
    ax.text(-1.5, 0.8, '35°', fontsize=11, color='red', fontweight='bold')
    ax.text(2.5, 0.8, '85°', fontsize=11, color='blue', fontweight='bold')
    ax.text(0.5, 2, '?', fontsize=14, fontweight='bold', color='purple')
    
    # Angle arcs
    arc1 = Arc((0, 0), 1.5, 1.5, angle=0, theta1=0, theta2=35, 
               color='red', linewidth=2)
    ax.add_patch(arc1)
    
    arc2 = Arc((0, 0), 2, 2, angle=0, theta1=35, theta2=120, 
               color='blue', linewidth=2)
    ax.add_patch(arc2)
    
    ax.set_title('G002: Angles on Straight Line', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G002.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G002: Angles on straight line")

def generate_G010():
    """G010: Composite rectangles."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.set_xlim(-0.5, 13)
    ax.set_ylim(-0.5, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Rectangle A: 8 x 5
    rect_A = Rectangle((0, 0), 8, 5, facecolor=MOE_COLORS['fill_light'], 
                       edgecolor='black', linewidth=2)
    ax.add_patch(rect_A)
    ax.text(4, 2.5, 'A', fontsize=14, ha='center', fontweight='bold')
    
    # Rectangle B: 4 x 6 (joined along 5cm side, so height extends)
    rect_B = Rectangle((8, 0), 4, 6, facecolor=MOE_COLORS['accent'], 
                       edgecolor='black', linewidth=2, alpha=0.3)
    ax.add_patch(rect_B)
    ax.text(10, 3, 'B', fontsize=14, ha='center', fontweight='bold')
    
    # Dimensions
    ax.text(4, -0.4, '8 cm', fontsize=10, ha='center')
    ax.text(-0.4, 2.5, '5 cm', fontsize=10, ha='center', rotation=90, va='center')
    ax.text(10, -0.4, '4 cm', fontsize=10, ha='center')
    ax.text(12.4, 3, '6 cm', fontsize=10, ha='left', va='center', rotation=90)
    
    ax.set_title('G010: Composite Rectangles', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G010.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G010: Composite rectangles")

def generate_G017():
    """G017: Cuboid volume."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw cuboid (isometric-like)
    # Front face
    front = Rectangle((1, 0.5), 3, 2, facecolor=MOE_COLORS['primary'], 
                     edgecolor='black', linewidth=2)
    ax.add_patch(front)
    
    # Top face
    top = Polygon([(1, 2.5), (4, 2.5), (5, 3.5), (2, 3.5)], 
                 facecolor=MOE_COLORS['fill_light'], edgecolor='black', linewidth=1.5)
    ax.add_patch(top)
    
    # Side face
    side = Polygon([(4, 0.5), (5, 1.5), (5, 3.5), (4, 2.5)], 
                  facecolor=MOE_COLORS['secondary'], edgecolor='black', linewidth=1.5)
    ax.add_patch(side)
    
    # Dimensions
    ax.text(2.5, 0.2, '6 cm', fontsize=10, ha='center')
    ax.text(0.7, 1.5, '3 cm', fontsize=10, ha='center', rotation=90, va='center')
    ax.text(5.2, 2, '4 cm', fontsize=10, ha='left', va='center', rotation=45)
    
    ax.set_title('G017: Cuboid Volume', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G017.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G017: Cuboid volume")

def generate_G021():
    """G021: Triangle classification."""
    fig, ax = plt.subplots(figsize=(4, 3.5), dpi=150)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Equilateral triangle
    A = (0.5, 0.5)
    B = (4.5, 0.5)
    C = (2.5, 4)
    
    triangle = Polygon([A, B, C], facecolor=MOE_COLORS['fill_light'], 
                      edgecolor='black', linewidth=2)
    ax.add_patch(triangle)
    
    # Labels
    ax.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=12, ha='center', fontweight='bold')
    ax.text(B[0]+0.3, B[1]-0.3, 'B', fontsize=12, ha='center', fontweight='bold')
    ax.text(C[0], C[1]+0.3, 'C', fontsize=12, ha='center', fontweight='bold')
    
    # Side lengths
    ax.text(2.5, -0.2, '5 cm', fontsize=10, ha='center')
    ax.text(0.5, 2.3, '5 cm', fontsize=10, ha='center', rotation=60, va='center')
    ax.text(4.5, 2.3, '5 cm', fontsize=10, ha='center', rotation=-60, va='center')
    
    ax.set_title('G021: Triangle Classification', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G021.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G021: Triangle classification")

def generate_G024():
    """G024: Circle circumference."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Circle
    circle = plt.Circle((0, 0), 2, facecolor='none', edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    
    # Center
    ax.plot(0, 0, 'ko', markersize=6)
    ax.text(0, -0.3, 'O', fontsize=11, ha='center', fontweight='bold')
    
    # Radius line
    ax.plot([0, 2], [0, 0], 'k-', linewidth=1.5)
    ax.text(1, -0.3, '7 cm', fontsize=10, ha='center')
    
    # Pi value
    ax.text(0, 2.5, 'π = 22/7', fontsize=11, ha='center', 
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    ax.set_title('G024: Circle Circumference', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G024.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G024: Circle circumference")

# Generate all diagrams
if __name__ == "__main__":
    print("=" * 60)
    print("Generating Geometry Diagrams from Specifications")
    print("=" * 60)
    
    generate_G001()
    generate_G002()
    generate_G010()
    generate_G017()
    generate_G021()
    generate_G024()
    
    print("\n" + "=" * 60)
    print("✅ Basic geometry diagrams complete")
    print("=" * 60)
