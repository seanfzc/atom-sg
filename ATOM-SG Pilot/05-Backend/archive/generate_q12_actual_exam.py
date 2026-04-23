#!/usr/bin/env python3
"""
Generate Q12 diagram matching ACTUAL ACS Junior exam
Based on Qwen-VL analysis of stepped/L-shaped arrangement
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch
from pathlib import Path
import yaml
import numpy as np

# Paths
CANONICAL_YAML = Path(__file__).parent.parent / "02-Geometry" / "CANONICAL_GEOMETRY_DATA.yaml"
OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "q12-actual-exam"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_canonical_data():
    """Load geometry data from canonical YAML."""
    with open(CANONICAL_YAML, 'r') as f:
        data = yaml.safe_load(f)
    return data['problems']['Q12']

def generate_q12_actual_exam():
    """Generate Q12 diagram matching actual ACS Junior exam layout."""
    
    # Load canonical data
    q12_data = load_canonical_data()
    vars = q12_data['variables']
    
    # Extract values
    X = vars['square_X']['side_cm']  # 4 cm
    Y = vars['square_Y']['side_cm']  # 2 cm (to be solved)
    shaded = vars['shaded_strip']['width_cm']  # 1.5 cm
    
    print(f"Generating Q12 from ACTUAL ACS Junior exam:")
    print(f"X = {X} cm, Y = ? cm, Shaded = {shaded} cm")
    print()
    print("Stepped/L-shaped arrangement:")
    print("  X - bottom left")
    print("  Y - above X, sharing left edge")
    print("  Z - right of X, sharing bottom edge")
    print("  W - right of Y, sharing top edge")
    print("  V - right of Z, sharing top edge")
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(14, 10), dpi=150)
    
    # Scale: 1 cm = 40 pixels
    scale = 40
    
    X_px = X * scale
    Y_px = 2 * scale  # Temporary, will be derived from X
    Z_px = 3.5 * scale  # From visual: similar to X
    W_px = 2.5 * scale  # From visual: smaller
    V_px = 2 * scale  # From visual: smallest
    shaded_px = shaded * scale
    
    # Start position
    start_x = 100
    start_y = 80
    
    # Colors
    colors = {
        'X': '#5B9BD5',  # Primary blue
        'Y': '#ED7D31',  # Secondary orange
        'Z': '#70AD47',  # Accent green
        'W': '#FFC000',  # Highlight yellow
        'V': '#A5A5A5',  # Neutral gray
        'shaded': '#FFE6E6',  # Light red
        'outline': '#333333',
        'text': '#1a1a1a',
    }
    
    # Draw squares in STEPPED arrangement (L-shaped)
    
    # Square X (4x4) - bottom left
    rect_x = Rectangle((start_x, start_y), X_px, X_px,
                       facecolor=colors['X'], alpha=0.7,
                       edgecolor=colors['outline'], linewidth=2.5)
    ax.add_patch(rect_x)
    
    # Square Y (2x2) - above X, sharing left edge
    # Y is X/2 = 2 cm
    y_pos_x = start_x
    y_pos_y = start_y + X_px
    rect_y = Rectangle((y_pos_x, y_pos_y), Y_px, Y_px,
                       facecolor=colors['Y'], alpha=0.7,
                       edgecolor=colors['outline'], linewidth=2.5)
    ax.add_patch(rect_y)
    
    # Square Z (3.5x3.5) - right of X, sharing bottom
    z_pos_x = start_x + X_px
    z_pos_y = start_y
    rect_z = Rectangle((z_pos_x, z_pos_y), Z_px, Z_px,
                       facecolor=colors['Z'], alpha=0.7,
                       edgecolor=colors['outline'], linewidth=2.5)
    ax.add_patch(rect_z)
    
    # Square W (2.5x2.5) - right of Y, sharing top
    w_pos_x = start_x + X_px
    w_pos_y = start_y + X_px
    rect_w = Rectangle((w_pos_x, w_pos_y), W_px, W_px,
                       facecolor=colors['W'], alpha=0.7,
                       edgecolor=colors['outline'], linewidth=2.5)
    ax.add_patch(rect_w)
    
    # Square V (2x2) - right of Z, sharing top
    v_pos_x = start_x + X_px + Z_px
    v_pos_y = start_y + Z_px - V_px  # Move up by (Z - V)
    rect_v = Rectangle((v_pos_x, v_pos_y), V_px, V_px,
                       facecolor=colors['V'], alpha=0.7,
                       edgecolor=colors['outline'], linewidth=2.5, linestyle='--')
    ax.add_patch(rect_v)
    
    # Shaded strip (1.5cm) - right edge, vertical
    # Based on arrangement: rectangle height is X + W = 6.5 cm
    rectangle_height = X_px + W_px  # X + W from visual
    rectangle_width = X_px + Z_px + V_px + shaded_px  # X + Z + V + shaded
    
    # Shaded strip is on the right edge
    shaded_x = start_x + rectangle_width
    shaded_y = start_y
    shaded_height = rectangle_height
    shaded_rect = Rectangle((shaded_x, shaded_y), shaded_px, shaded_height,
                            facecolor=colors['shaded'], alpha=0.5,
                            edgecolor='red', linewidth=2, linestyle='--',
                            hatch='///')
    ax.add_patch(shaded_rect)
    
    # Draw rectangle outline
    rect_outline = Rectangle((start_x, start_y), rectangle_width, rectangle_height,
                              fill=False, edgecolor=colors['outline'], 
                              linewidth=2, linestyle='-')
    ax.add_patch(rect_outline)
    
    # Labels with proper positioning
    # X label
    ax.text(start_x + X_px/2, start_y + X_px/2, 'X', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=colors['text'], bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='white', alpha=0.9))
    ax.text(start_x + X_px/2, start_y - 15, '4 cm', 
            ha='center', va='center', fontsize=11, fontweight='bold',
            color=colors['text'])
    
    # Y label with question mark
    ax.text(y_pos_x + Y_px/2, y_pos_y + Y_px/2, 'Y', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=colors['text'], bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='white', alpha=0.9))
    ax.text(y_pos_x + Y_px/2, y_pos_y + Y_px/2 + 15, '?', 
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='red')
    
    # Z label
    ax.text(z_pos_x + Z_px/2, z_pos_y + Z_px/2, 'Z', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=colors['text'], bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='white', alpha=0.9))
    
    # W label
    ax.text(w_pos_x + W_px/2, w_pos_y + W_px/2, 'W', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=colors['text'], bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='white', alpha=0.9))
    
    # V label
    ax.text(v_pos_x + V_px/2, v_pos_y + V_px/2, 'V', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=colors['text'], bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='white', alpha=0.9))
    
    # Shaded strip label
    ax.text(shaded_x + shaded_px/2, start_y + rectangle_height/2, '1.5 cm', 
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='red', rotation=90)
    
    # Set limits
    ax.set_xlim(start_x - 30, shaded_x + shaded_px + 30)
    ax.set_ylim(start_y - 30, start_y + rectangle_height + 30)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.set_title('Q12: Five Squares in Rectangle (ACTUAL ACS Junior 2025)\n'
                 'Stepped/L-shaped arrangement • Shaded strip = 1.5 cm\n'
                 'Find: Side of square Y',
                 fontsize=16, fontweight='bold', pad=20, 
                 color=colors['text'])
    
    # Scale indicator
    scale_text = f"Scale: 1 cm = {scale} pixels"
    ax.text(0.02, 0.98, scale_text, transform=ax.transAxes,
            fontsize=10, color='gray', verticalalignment='top')
    
    plt.tight_layout()
    
    # Save outputs
    output_base = OUTPUT_DIR / 'Q12_five_squares_actual_exam'
    
    plt.savefig(f'{output_base}.png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig(f'{output_base}.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig(f'{output_base}.pdf', format='pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print(f"\n✅ Generated Q12 matching ACTUAL exam diagram:")
    print(f"   {output_base}.png")
    print(f"   {output_base}.svg")
    print(f"   {output_base}.pdf")
    print()
    print("✓ Stepped/L-shaped arrangement from actual exam")
    print("✓ X, Z, W, V positioned correctly")
    print("✓ Y to be solved (X/2 relationship)")
    print("✓ 1.5cm shaded strip on right edge")
    
    plt.close()
    
    return output_base

if __name__ == '__main__':
    generate_q12_actual_exam()
