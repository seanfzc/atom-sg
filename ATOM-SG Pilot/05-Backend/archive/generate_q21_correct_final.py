#!/usr/bin/env python3
"""
Generate CORRECT Q21 diagram - FINAL VERSION
Verified against question text and given values.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"

def generate_q21_correct():
    """
    Q21 CORRECT geometry:
    - Two quarter circles OAC and OBD, both centered at O, radius 10
    - Shaded sector OBC has perimeter 26 cm
    - Therefore: arc BC = 26 - 10 - 10 = 6 cm
    - Arc BC angle = (6 / (2π×10)) × 360 = 34.4°
    - Each quarter circle = 90°
    - Arc AB = 90° - 34.4° = 55.6°
    - Arc CD = 90° - 34.4° = 55.6°
    """
    
    fig, ax = plt.subplots(figsize=(7, 6), dpi=150)
    ax.set_xlim(-3, 13)
    ax.set_ylim(-3, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    r = 10
    
    # Calculate angles based on given perimeter = 26 cm
    # Arc BC = 6 cm
    # Angle = (arc / circumference) × 360 = (6 / 62.83) × 360 = 34.4°
    arc_BC_deg = 34.4
    
    # Quarter circles = 90° each
    # Q1 (OAC) = arc AB + arc BC = 55.6° + 34.4° = 90°
    # Q2 (OBD) = arc BC + arc CD = 34.4° + 55.6° = 90°
    arc_AB_deg = 90 - arc_BC_deg  # 55.6°
    arc_CD_deg = 90 - arc_BC_deg  # 55.6°
    
    # Position angles (from vertical, clockwise)
    # Let's place B at 90° (vertical up)
    angle_B = 90
    angle_C = angle_B - arc_BC_deg  # 90 - 34.4 = 55.6°
    angle_A = angle_B + arc_AB_deg  # 90 + 55.6 = 145.6°
    angle_D = angle_C - arc_CD_deg  # 55.6 - 55.6 = 0°
    
    # Draw quarter circle OAC (from A to C, passing through B)
    theta1 = np.linspace(np.radians(angle_C), np.radians(angle_A), 100)
    x1 = r * np.cos(theta1)
    y1 = r * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5, label='Q1: OAC')
    
    # Draw quarter circle OBD (from B to D, passing through C)
    theta2 = np.linspace(np.radians(angle_D), np.radians(angle_B), 100)
    x2 = r * np.cos(theta2)
    y2 = r * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5, label='Q2: OBD')
    
    # Draw radii
    for angle in [angle_A, angle_B, angle_C, angle_D]:
        rad = np.radians(angle)
        ax.plot([0, r*np.cos(rad)], [0, r*np.sin(rad)], 'k-', linewidth=2.5)
    
    # Shade sector OBC (from B to C)
    theta_shade = np.linspace(np.radians(angle_C), np.radians(angle_B), 50)
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
    ax.text(points['A'][0]-0.8, points['A'][1]+0.3, 'A', fontsize=14, ha='center', fontweight='bold')
    ax.text(points['B'][0]-0.5, points['B'][1]+0.6, 'B', fontsize=14, ha='center', fontweight='bold', color='darkred')
    ax.text(points['C'][0]+0.6, points['C'][1]+0.4, 'C', fontsize=14, ha='center', fontweight='bold', color='darkred')
    ax.text(points['D'][0]+0.8, points['D'][1], 'D', fontsize=14, ha='center', fontweight='bold')
    ax.text(points['O'][0], points['O'][1]-0.8, 'O', fontsize=14, ha='center', fontweight='bold')
    
    # Radius label (outside)
    ax.annotate('', xy=(-2, 7), xytext=(0, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(-3.5, 5, '10 cm', fontsize=12, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Shaded region label
    ax.text(2, 6, 'Shaded OBC', fontsize=11, ha='center', fontweight='bold', color='darkblue')
    ax.text(2, 5.3, '30 cm²', fontsize=10, ha='center', color='darkblue')
    ax.text(2, 4.6, 'Perimeter = 26 cm', fontsize=9, ha='center', color='darkblue')
    
    # Verification annotation
    ax.text(8, 8, 'Verification:', fontsize=9, fontweight='bold', color='green')
    ax.text(8, 7.3, f'Arc BC = {arc_BC_deg:.1f}°', fontsize=8, color='green')
    ax.text(8, 6.8, f'Arc length = 6 cm', fontsize=8, color='green')
    ax.text(8, 6.3, f'Perimeter = 10+10+6 = 26 ✓', fontsize=8, color='green')
    
    ax.set_title('Q21: Overlapping Quarter Circles (CORRECT - Final)', fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_correct_final.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Q21 CORRECT diagram generated")
    print(f"   Arc BC = {arc_BC_deg:.1f}° (not 60°)")
    print(f"   Arc length = 6 cm")
    print(f"   Perimeter OBC = 10 + 10 + 6 = 26 cm ✓")
    print(f"   Quarter circles: 90° each ✓")
    
    # Verify solution
    print("\n" + "=" * 60)
    print("SOLUTION VERIFICATION:")
    print("=" * 60)
    
    # Area calculation
    area_Q1 = (90/360) * np.pi * r**2
    area_Q2 = area_Q1
    area_OBC = 30  # Given
    area_OABCD = area_Q1 + area_Q2 - area_OBC
    
    print(f"Area Q1 (quarter circle) = {area_Q1:.2f} cm²")
    print(f"Area Q2 (quarter circle) = {area_Q2:.2f} cm²")
    print(f"Area OBC (given) = {area_OBC} cm²")
    print(f"Area OABCD = {area_Q1:.2f} + {area_Q2:.2f} - {area_OBC} = {area_OABCD:.2f} cm²")
    print(f"Answer: {area_OABCD:.0f} cm²")
    
    # Perimeter calculation
    arc_AB = (arc_AB_deg/360) * 2 * np.pi * r
    arc_CD = (arc_CD_deg/360) * 2 * np.pi * r
    perimeter = arc_AB + arc_CD + r + r  # OA + OD
    
    print(f"\nArc AB = {arc_AB:.2f} cm")
    print(f"Arc CD = {arc_CD:.2f} cm")
    print(f"OA + OD = {r} + {r} = {2*r} cm")
    print(f"Perimeter OABCD = {arc_AB:.2f} + {arc_CD:.2f} + {2*r} = {perimeter:.2f} cm")

if __name__ == "__main__":
    generate_q21_correct()
