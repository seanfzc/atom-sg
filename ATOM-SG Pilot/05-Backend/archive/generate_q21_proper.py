#!/usr/bin/env python3
"""
Generate CORRECT Q21 diagram - proper scale and orientation
Based on ACS Junior exam paper Q15
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def create_q21_proper():
    """
    Q21 from ACS Junior exam:
    - Center O at bottom
    - Two quarter circles: OAC and OBD (both centered at O)
    - They overlap forming shaded sector OBC
    - All radii = 10 cm
    """
    
    fig, ax = plt.subplots(figsize=(7, 6), dpi=150)
    ax.set_xlim(-12, 12)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    O = (0, 0)
    
    # From exam paper: O is at bottom, arc curves upward
    # Quarter circle OAC: from left (A) to somewhere (C)
    # Quarter circle OBD: from somewhere (B) to right (D)
    # They overlap in the middle (sector OBC)
    
    # Angles (in degrees, 0 = right, 90 = up, 180 = left)
    # A at ~135° (upper left)
    # D at ~45° (upper right)
    # B and C between them
    
    angle_A = 135  # Upper left
    angle_D = 45   # Upper right
    
    # Quarter circles are 90° each
    # Q1 (OAC): from A-45° to A+45° = 90° to 180°
    # Q2 (OBD): from D-45° to D+45° = 0° to 90°
    # Wait, that doesn't overlap...
    
    # Let me reconsider: both quarter circles must overlap
    # Q1 spans 90°, Q2 spans 90°, overlap is sector OBC
    
    # If Q1 goes from 120° to 210° (90° span)
    # And Q2 goes from 30° to 120° (90° span)
    # They overlap from 120° to... wait, 210° vs 30° doesn't overlap
    
    # The overlap must be within a 90° range
    # Let's say Q1: 90° to 180° (upper left quadrant)
    # Q2: 45° to 135° (spanning upper right to upper left)
    # Overlap: 90° to 135° = sector OBC
    
    angle_Q1_start = 90
    angle_Q1_end = 180
    angle_Q2_start = 45
    angle_Q2_end = 135
    
    # Points:
    # A = Q1 start = 90°
    # C = Q1 end = 180°
    # B = Q2 start = 45°
    # D = Q2 end = 135°
    
    # Wait, that makes C and D the same point (both at 135°?)
    # No: C is at 180°, D is at 135°
    # B is at 45°
    # A is at 90°
    
    # Overlap is from 90° to 135°
    angle_B = 90   # Start of overlap, on Q1
    angle_C = 135  # End of overlap, on Q2
    
    # Actually looking at exam diagram again:
    # A ---- B -shaded- C ---- D
    #  \         |          /
    #   \    sector OBC   /
    #    \      |        /
    #     \     |       /
    #      \    O      /
    
    # So going around: A -> B -> C -> D on the arc
    # Sector OBC is shaded (from O to B to C)
    
    # Q1 is OAC: from A to C (passing through B)
    # Q2 is OBD: from B to D (passing through C?)
    # Wait, if Q2 is from B to D and passes through C, then C is between B and D
    # So B -> C -> D on the arc
    # And A -> B -> C on the arc for Q1
    
    # So the order on arc is: A - B - C - D
    # Q1 covers A to C (includes B)
    # Q2 covers B to D (includes C)
    # Overlap is B to C
    
    # Angles (from vertical, clockwise):
    # Let's say A is at -60° from vertical (left side)
    # D is at +60° from vertical (right side)
    # B is at -30°
    # C is at +30°
    
    # In standard polar (0° = right, counter-clockwise):
    # Vertical up = 90°
    # A at 90° + 60° = 150°
    # D at 90° - 60° = 30°
    # B at 90° + 30° = 120°
    # C at 90° - 30° = 60°
    
    angle_A = 150  # Upper left
    angle_B = 120  # Between A and center
    angle_C = 60   # Between center and D
    angle_D = 30   # Upper right
    
    # Verify quarter circles:
    # Q1 (OAC): from A(150°) to C(60°)? That's 90°... but going clockwise
    # In matplotlib, angles go counter-clockwise
    # So Q1 from 60° to 150° = 90° ✓
    # Q2 (OBD): from B(120°) to D(30°)? That's 90° clockwise
    # Or from 30° to 120° = 90° counter-clockwise ✓
    
    # Draw Q1: arc from C (60°) to A (150°)
    theta1 = np.linspace(np.radians(60), np.radians(150), 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    # Draw Q2: arc from D (30°) to B (120°)
    theta2 = np.linspace(np.radians(30), np.radians(120), 100)
    x2 = r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Draw radii
    # OA
    ax.plot([0, r*np.cos(np.radians(angle_A))], 
            [0, r*np.sin(np.radians(angle_A))], 'k-', linewidth=2.5)
    # OB
    ax.plot([0, r*np.cos(np.radians(angle_B))], 
            [0, r*np.sin(np.radians(angle_B))], 'k-', linewidth=2.5)
    # OC
    ax.plot([0, r*np.cos(np.radians(angle_C))], 
            [0, r*np.sin(np.radians(angle_C))], 'k-', linewidth=2.5)
    # OD
    ax.plot([0, r*np.cos(np.radians(angle_D))], 
            [0, r*np.sin(np.radians(angle_D))], 'k-', linewidth=2.5)
    
    # Shade sector OBC (from B to C)
    theta_shade = np.linspace(np.radians(angle_B), np.radians(angle_C), 50)
    x_shade = [0] + list(r * np.cos(theta_shade)) + [0]
    y_shade = [0] + list(r * np.sin(theta_shade)) + [0]
    
    shade = patches.Polygon(list(zip(x_shade, y_shade)), 
                           facecolor='#5B9BD5', edgecolor='darkblue', 
                           linewidth=2, alpha=0.5)
    ax.add_patch(shade)
    
    # Mark points
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
    ax.text(points['A'][0]-0.8, points['A'][1]+0.3, 'A', fontsize=14, 
            ha='center', fontweight='bold')
    ax.text(points['B'][0]-0.6, points['B'][1]+0.6, 'B', fontsize=14, 
            ha='center', fontweight='bold', color='darkred')
    ax.text(points['C'][0]+0.6, points['C'][1]+0.6, 'C', fontsize=14, 
            ha='center', fontweight='bold', color='darkred')
    ax.text(points['D'][0]+0.8, points['D'][1]+0.3, 'D', fontsize=14, 
            ha='center', fontweight='bold')
    ax.text(points['O'][0], points['O'][1]-0.8, 'O', fontsize=14, 
            ha='center', fontweight='bold')
    
    # Label shaded region
    ax.text(2, 5, 'Shaded\nOBC', fontsize=11, ha='center', 
            fontweight='bold', color='darkblue')
    ax.text(2, 4.2, '30 cm²', fontsize=10, ha='center', color='darkblue')
    
    # Radius label
    ax.annotate('', xy=(points['A'][0]-0.3, points['A'][1]-0.3), 
                xytext=(0.3, 0.3),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(-3, 2, '10 cm', fontsize=11, ha='center', fontweight='bold')
    
    ax.set_title('Q21: Overlapping Quarter Circles OAC and OBD', 
                fontsize=13, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_proper.png', dpi=150, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Q21 proper diagram generated")
    print(f"   O at center (0,0)")
    print(f"   A at {angle_A}° (left)")
    print(f"   B at {angle_B}° (on arc)")
    print(f"   C at {angle_C}° (on arc)")
    print(f"   D at {angle_D}° (right)")
    print(f"   Q1: OAC spans {angle_C}° to {angle_A}° = 90°")
    print(f"   Q2: OBD spans {angle_D}° to {angle_B}° = 90°")
    print(f"   Overlap OBC: {angle_B}° to {angle_C}° = {angle_B-angle_C}° sector")

if __name__ == "__main__":
    create_q21_proper()
