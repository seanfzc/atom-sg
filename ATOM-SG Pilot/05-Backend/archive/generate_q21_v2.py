#!/usr/bin/env python3
"""
Generate CORRECTED Q21 diagram v2
O, B, C are 3 distinct vertices forming triangle OBC with area 30 cm²
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, FancyArrowPatch
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def create_q21_v2():
    """
    Q21 configuration:
    - O = (0, 0) - center of Q1
    - B = (10, 0) - on x-axis (also point A)
    - C = (8, 6) - on Q1 arc
    - Triangle OBC has area = 30 cm²
    - Q2 center at A(10,0), arc from (10,10) to (0,0)
    
    Area calculation:
    O(0,0), B(10,0), C(8,6)
    Area = 0.5 * base * height = 0.5 * 10 * 6 = 30 ✓
    """
    
    fig, ax = plt.subplots(figsize=(6.5, 5.5), dpi=150)
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    
    # Define points
    O = (0, 0)
    B = (10, 0)  # Same as A
    C = (8, 6)
    A = (10, 0)  # Same as B
    D = (10, 10)
    
    # Draw Q1: center O(0,0), arc from (0,10) to (10,0)
    theta1 = np.linspace(0, np.pi/2, 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    ax.plot([0, r], [0, 0], 'k-', linewidth=2.5)  # base
    ax.plot([0, 0], [0, r], 'k-', linewidth=2.5)  # side
    
    # Draw Q2: center A(10,0), arc from (10,10) to (0,0)
    theta2 = np.linspace(np.pi/2, np.pi, 100)
    x2 = 10 + r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    ax.plot([10, 0], [0, 0], 'k-', linewidth=2.5)  # base (shared)
    ax.plot([10, 10], [0, r], 'k-', linewidth=2.5)  # side
    
    # Shade triangle OBC
    triangle = plt.Polygon([O, B, C], facecolor='#DEEBF7', edgecolor='blue', 
                          linewidth=2, alpha=0.7)
    ax.add_patch(triangle)
    
    # Add light diagonal hatching ONLY inside triangle
    # Draw diagonal lines within triangle bounds
    for i in range(-2, 12):
        # Line: y = x - i (diagonal)
        # Find intersection with triangle edges
        x_line = np.array([i, i+6])
        y_line = x_line - i
        
        # Clip to triangle roughly
        mask = (y_line >= 0) & (y_line <= 6) & (x_line >= 0) & (x_line <= 10)
        if np.any(mask):
            valid_x = x_line[mask]
            valid_y = y_line[mask]
            if len(valid_x) >= 2:
                ax.plot(valid_x, valid_y, 'b--', linewidth=0.8, alpha=0.5)
    
    # Mark points with clear dots
    ax.plot(O[0], O[1], 'ko', markersize=10)
    ax.plot(B[0], B[1], 'ko', markersize=10)
    ax.plot(C[0], C[1], 'ko', markersize=10)
    ax.plot(D[0], D[1], 'ko', markersize=8)
    
    # Labels with leader lines for clarity
    # O at origin
    ax.text(O[0]-0.8, O[1]-0.6, 'O', fontsize=14, ha='center', fontweight='bold')
    
    # B at (10,0) - note it's same as A
    ax.text(B[0]+0.6, B[1]-0.6, 'B', fontsize=14, ha='center', fontweight='bold', color='red')
    ax.text(B[0]+0.6, B[1]-1.3, '(A)', fontsize=10, ha='center', color='gray')
    
    # C at (8,6)
    ax.text(C[0]+0.7, C[1]+0.3, 'C', fontsize=14, ha='center', fontweight='bold', color='red')
    
    # D at (10,10)
    ax.text(D[0]+0.6, D[1]+0.3, 'D', fontsize=14, ha='center', fontweight='bold')
    
    # Dimension
    ax.annotate('', xy=(10, -0.3), xytext=(0, -0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(5, -1.0, '10 cm', fontsize=11, ha='center', fontweight='bold')
    
    # Label the shaded triangle
    ax.text(6, 2.5, 'OBC', fontsize=12, ha='center', fontweight='bold', color='blue',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='blue'))
    ax.text(6, 1.8, '30 cm²', fontsize=10, ha='center', color='blue')
    
    # Show coordinates for clarity (optional, can remove)
    ax.text(0.5, 9.5, 'Q1 center: O(0,0)', fontsize=8, color='gray')
    ax.text(0.5, 9.0, 'Q2 center: A(10,0)', fontsize=8, color='gray')
    
    ax.set_title('Q21: Two Overlapping Quarter Circles (Corrected)', fontsize=12, pad=15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_v2_corrected.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q21 v2 generated - O, B, C are distinct vertices")
    print("   O = (0, 0)")
    print("   B = (10, 0) [same as A]")
    print("   C = (8, 6)")
    print("   Area OBC = 30 cm² ✓")

if __name__ == "__main__":
    create_q21_v2()
