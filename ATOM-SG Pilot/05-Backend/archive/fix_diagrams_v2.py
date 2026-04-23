#!/usr/bin/env python3
"""
Fix identified diagram errors based on VISUAL_ERRORS_LEARNINGS.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, FancyArrowPatch
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def fix_Q21():
    """Fix Q21: Clear radius label placement."""
    fig, ax = plt.subplots(figsize=(7, 5.5), dpi=150)
    ax.set_xlim(-3, 13)
    ax.set_ylim(-3, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    
    # Points (same as before)
    angle_A, angle_B, angle_C, angle_D = 150, 120, 60, 30
    
    # Draw quarter circles
    theta1 = np.linspace(np.radians(60), np.radians(150), 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    theta2 = np.linspace(np.radians(30), np.radians(120), 100)
    x2 = r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Draw radii
    for angle in [angle_A, angle_B, angle_C, angle_D]:
        rad = np.radians(angle)
        ax.plot([0, r*np.cos(rad)], [0, r*np.sin(rad)], 'k-', linewidth=2.5)
    
    # Shade sector OBC
    theta_shade = np.linspace(np.radians(60), np.radians(120), 50)
    x_shade = [0] + list(r * np.cos(theta_shade)) + [0]
    y_shade = [0] + list(r * np.sin(theta_shade)) + [0]
    shade = patches.Polygon(list(zip(x_shade, y_shade)), 
                           facecolor='#5B9BD5', edgecolor='darkblue', 
                           linewidth=2, alpha=0.5)
    ax.add_patch(shade)
    
    # Points
    points = {
        'A': (r*np.cos(np.radians(angle_A)), r*np.sin(np.radians(angle_A))),
        'B': (r*np.cos(np.radians(angle_B)), r*np.sin(np.radians(angle_B))),
        'C': (r*np.cos(np.radians(angle_C)), r*np.sin(np.radians(angle_C))),
        'D': (r*np.cos(np.radians(angle_D)), r*np.sin(np.radians(angle_D))),
        'O': (0, 0)
    }
    
    for label, (x, y) in points.items():
        ax.plot(x, y, 'ko', markersize=10, zorder=5)
    
    # Labels
    ax.text(points['A'][0]-0.8, points['A'][1]+0.3, 'A', fontsize=14, ha='center', fontweight='bold')
    ax.text(points['B'][0]-0.6, points['B'][1]+0.6, 'B', fontsize=14, ha='center', fontweight='bold', color='darkred')
    ax.text(points['C'][0]+0.6, points['C'][1]+0.6, 'C', fontsize=14, ha='center', fontweight='bold', color='darkred')
    ax.text(points['D'][0]+0.8, points['D'][1]+0.3, 'D', fontsize=14, ha='center', fontweight='bold')
    ax.text(points['O'][0], points['O'][1]-0.8, 'O', fontsize=14, ha='center', fontweight='bold')
    
    # FIXED: Clear radius label outside the shape
    ax.annotate('', xy=(-8, 8), xytext=(0, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(-5.5, 5.5, '10 cm', fontsize=12, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    ax.text(-7.5, 7.5, 'radius', fontsize=9, ha='center', color='gray', style='italic')
    
    # Shaded region label
    ax.text(2, 5, 'Shaded\nOBC', fontsize=11, ha='center', fontweight='bold', color='darkblue')
    ax.text(2, 4.2, '30 cm²', fontsize=10, ha='center', color='darkblue')
    
    ax.set_title('Q21: Overlapping Quarter Circles OAC and OBD (FIXED)', fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_fixed.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q21 fixed - radius label moved outside")

def fix_G001():
    """Fix G001: Add degree labels, space arcs, mark 0°."""
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
    ax.set_xlim(-2.5, 7)
    ax.set_ylim(-0.8, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    center = (2, 0.5)
    
    # Protractor arc
    theta = np.linspace(0, np.pi, 100)
    x = center[0] + 2.2 * np.cos(theta)
    y = center[1] + 2.2 * np.sin(theta)
    ax.plot(x, y, 'k-', linewidth=2)
    
    # FIXED: Degree markings with labels
    for angle in range(0, 181, 10):
        rad = np.radians(angle)
        r1, r2 = 2.2, 2.35 if angle % 30 == 0 else 2.28
        ax.plot([center[0] + r1*np.cos(rad), center[0] + r2*np.cos(rad)],
                [center[1] + r1*np.sin(rad), center[1] + r2*np.sin(rad)], 'k-', linewidth=0.8)
        
        # Add labels at 30° intervals
        if angle % 30 == 0:
            label_r = 2.6
            ax.text(center[0] + label_r*np.cos(rad), center[1] + label_r*np.sin(rad),
                   f'{angle}°', fontsize=8, ha='center', va='center')
    
    # FIXED: Clear 0° baseline
    ax.plot([center[0], center[0] + 2.5], [center[1], center[1]], 'k--', linewidth=1, alpha=0.5)
    ax.text(center[0] + 2.7, center[1], '0°', fontsize=9, ha='left', va='center', color='gray')
    
    # Angle rays with FIXED spacing
    angles = [45, 120, 90]
    labels = ['A', 'B', 'C']
    colors = ['#5B9BD5', '#ED7D31', '#70AD47']
    
    for i, (angle, label, color) in enumerate(zip(angles, labels, colors)):
        rad = np.radians(angle)
        x_end = center[0] + 2.0 * np.cos(rad)
        y_end = center[1] + 2.0 * np.sin(rad)
        ax.plot([center[0], x_end], [center[1], y_end], color=color, linewidth=2.5)
        
        # FIXED: Arcs at different radii to prevent overlap
        arc_r = 0.5 + i * 0.4  # Increased spacing
        arc_theta = np.linspace(0, rad, 30)
        ax.plot(center[0] + arc_r * np.cos(arc_theta),
                center[1] + arc_r * np.sin(arc_theta), color=color, linewidth=2.5)
        
        label_x = center[0] + 2.5 * np.cos(rad)
        label_y = center[1] + 2.5 * np.sin(rad)
        ax.text(label_x, label_y, f'∠{label}', fontsize=13, ha='center', fontweight='bold', color=color)
    
    ax.plot(center[0], center[1], 'ko', markersize=10)
    ax.text(center[0], center[1]-0.4, 'O', fontsize=12, ha='center', fontweight='bold')
    
    ax.set_title('G001: Measure angles ∠A, ∠B, ∠C (FIXED)', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G001_fixed.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G001 fixed - degree labels, spaced arcs, 0° marked")

def fix_G011():
    """Fix G011: Add all dimensions including internal edge."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # L-shape vertices
    vertices = [(0, 0), (0, 4), (3, 4), (3, 2), (5, 2), (5, 0)]
    l_shape = patches.Polygon(vertices, facecolor='#DEEBF7', edgecolor='black', linewidth=2.5)
    ax.add_patch(l_shape)
    
    # FIXED: All dimensions with leader lines
    # Left side (full height)
    ax.annotate('', xy=(-0.3, 0), xytext=(-0.3, 4),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(-0.8, 2, '4 cm', fontsize=11, ha='center', rotation=90, va='center', fontweight='bold')
    
    # Bottom (full width)
    ax.annotate('', xy=(0, -0.3), xytext=(5, -0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(2.5, -0.7, '5 cm', fontsize=11, ha='center', fontweight='bold')
    
    # Right side (lower part)
    ax.annotate('', xy=(5.3, 0), xytext=(5.3, 2),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(5.8, 1, '2 cm', fontsize=11, ha='center', rotation=90, va='center', fontweight='bold')
    
    # FIXED: Internal step dimension
    ax.annotate('', xy=(3, 4.3), xytext=(5, 4.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(4, 4.7, '2 cm', fontsize=11, ha='center', fontweight='bold')
    
    # Step height
    ax.annotate('', xy=(3.3, 2), xytext=(3.3, 4),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(3.8, 3, '2 cm', fontsize=11, ha='center', rotation=90, va='center', fontweight='bold')
    
    # Optional: Show component rectangles with dashed lines
    ax.plot([3, 3], [0, 2], 'b--', linewidth=1, alpha=0.5)
    ax.text(1.5, 1, 'A', fontsize=12, ha='center', color='blue', alpha=0.7)
    ax.text(4, 1, 'B', fontsize=12, ha='center', color='blue', alpha=0.7)
    
    ax.set_title('G011: L-Shape Composite Area (FIXED)', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G011_fixed.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G011 fixed - all dimensions including internal edges")

def fix_G017():
    """Fix G017: Horizontal labels, dashed hidden edges."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=150)
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Front face
    front = patches.Rectangle((1, 0.5), 4, 2.5, facecolor='#5B9BD5', 
                             edgecolor='black', linewidth=2)
    ax.add_patch(front)
    
    # Top face
    top = patches.Polygon([(1, 3), (5, 3), (6, 4), (2, 4)], 
                         facecolor='#DEEBF7', edgecolor='black', linewidth=1.5)
    ax.add_patch(top)
    
    # Side face
    side = patches.Polygon([(5, 0.5), (6, 1.5), (6, 4), (5, 3)], 
                          facecolor='#5B9BD5', edgecolor='black', linewidth=1.5, alpha=0.7)
    ax.add_patch(side)
    
    # FIXED: Dashed hidden edges
    ax.plot([1, 2], [0.5, 1.5], 'k--', linewidth=1, alpha=0.5)
    ax.plot([2, 6], [1.5, 1.5], 'k--', linewidth=1, alpha=0.5)
    ax.plot([2, 2], [1.5, 4], 'k--', linewidth=1, alpha=0.5)
    
    # FIXED: Horizontal dimension labels
    ax.text(3, 0.2, '6 cm', fontsize=11, ha='center', fontweight='bold')
    ax.text(0.5, 1.75, '3 cm', fontsize=11, ha='center', fontweight='bold')
    ax.text(6.5, 2.5, '4 cm', fontsize=11, ha='center', fontweight='bold')  # Horizontal!
    
    ax.set_title('G017: Cuboid Volume (FIXED)', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'G017_fixed.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ G017 fixed - horizontal labels, dashed hidden edges")

if __name__ == "__main__":
    print("=" * 60)
    print("Fixing Diagram Errors")
    print("=" * 60)
    
    fix_Q21()
    fix_G001()
    fix_G011()
    fix_G017()
    
    print("\n" + "=" * 60)
    print("✅ All diagrams fixed")
    print("=" * 60)
