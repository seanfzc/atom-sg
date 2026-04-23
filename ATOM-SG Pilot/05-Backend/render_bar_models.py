#!/usr/bin/env python3
"""
Render bar model diagrams following 4-gates approach
Focus: Reasoning chain visibility, not technical accuracy
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "bar-models-v1"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Colors for bar models
COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31',
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'shaded': '#DEEBF7',
}

def create_panel(fig, position, title):
    """Create a panel with title."""
    ax = fig.add_axes(position)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')
    ax.text(5, 2.7, title, fontsize=11, ha='center', fontweight='bold')
    return ax

def draw_bar(ax, x, y, width, height, color, label=None, value=None):
    """Draw a bar with optional label."""
    bar = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.02",
                         facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(bar)
    
    if label:
        ax.text(x + width/2, y + height/2, label, 
               fontsize=10, ha='center', va='center', fontweight='bold')
    
    if value:
        ax.text(x + width/2, y - 0.3, value,
               fontsize=9, ha='center')
    
    return bar

def draw_bracket(ax, x1, x2, y, label):
    """Draw a bracket with label."""
    # Draw bracket line
    ax.plot([x1, x1], [y, y+0.2], 'k-', linewidth=1)
    ax.plot([x2, x2], [y, y+0.2], 'k-', linewidth=1)
    ax.plot([x1, x2], [y+0.2, y+0.2], 'k-', linewidth=1)
    
    # Label
    ax.text((x1+x2)/2, y+0.4, label, fontsize=9, ha='center', fontweight='bold')

def render_q21_bar_model():
    """
    Q21: Overlapping quarter circles
    Use bar model to show area calculation
    """
    fig = plt.figure(figsize=(10, 12), dpi=150)
    
    # Panel 1: Establish facts
    ax1 = create_panel(fig, [0.05, 0.75, 0.9, 0.2], "Panel 1: What We Know")
    
    draw_bar(ax1, 0.5, 0.5, 3, 0.8, COLORS['primary'], "Q1", "78.5 cm²")
    draw_bar(ax1, 4, 0.5, 3, 0.8, COLORS['secondary'], "Q2", "78.5 cm²")
    draw_bar(ax1, 2.5, 1.5, 1.5, 0.6, COLORS['highlight'], "OBC", "30 cm²")
    
    ax1.text(5, 0.2, "Two quarter circles overlap. Shaded part = 30 cm²", 
            fontsize=9, ha='center', style='italic')
    
    # Panel 2: Area calculation
    ax2 = create_panel(fig, [0.05, 0.52, 0.9, 0.2], "Panel 2: Find Total Area")
    
    # Show: Q1 + Q2 - overlap
    draw_bar(ax2, 0.5, 0.5, 3, 0.8, COLORS['primary'], "", "78.5")
    ax2.text(2, 1.5, "+", fontsize=14, ha='center')
    draw_bar(ax2, 2.5, 0.5, 3, 0.8, COLORS['secondary'], "", "78.5")
    ax2.text(4, 1.5, "-", fontsize=14, ha='center')
    draw_bar(ax2, 4.5, 0.5, 1.5, 0.8, COLORS['highlight'], "", "30")
    ax2.text(6, 1.5, "=", fontsize=14, ha='center')
    draw_bar(ax2, 6.5, 0.5, 3, 0.8, COLORS['accent'], "Answer", "127 cm²")
    
    # Panel 3: Perimeter - find arc BC
    ax3 = create_panel(fig, [0.05, 0.29, 0.9, 0.2], "Panel 3: Find Arc BC")
    
    ax3.text(5, 2, "Perimeter OBC = OB + OC + arc BC = 26 cm", fontsize=10, ha='center')
    ax3.text(5, 1.5, "26 = 10 + 10 + arc BC", fontsize=10, ha='center')
    ax3.text(5, 1, "arc BC = 6 cm", fontsize=12, ha='center', 
            fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    # Panel 4: Perimeter OABCD
    ax4 = create_panel(fig, [0.05, 0.06, 0.9, 0.2], "Panel 4: Find Perimeter OABCD")
    
    ax4.text(5, 2, "Outer boundary = arc AD + OA + OD", fontsize=10, ha='center')
    ax4.text(5, 1.5, "= (arc AB + arc BC + arc CD) + 10 + 10", fontsize=9, ha='center')
    ax4.text(5, 1, "= 25.4 + 20 = 45.4 cm", fontsize=11, ha='center',
            fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.suptitle('Q21: Overlapping Quarter Circles (Bar Model Approach)', 
                fontsize=13, fontweight='bold', y=0.98)
    
    plt.savefig(OUTPUT_DIR / 'Q21_bar_model.png', dpi=150, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q21 bar model rendered")

def render_sample_bar_models():
    """Render sample bar models for common problem types."""
    
    # Part-whole model
    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    # Whole bar split into parts
    draw_bar(ax, 1, 1, 3, 0.8, COLORS['primary'], "Part A", "30")
    draw_bar(ax, 4, 1, 2, 0.8, COLORS['secondary'], "Part B", "20")
    draw_bracket(ax, 1, 6, 2.2, "Total = 50")
    
    ax.set_title('Part-Whole Model', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'part_whole_model.png', dpi=150, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Comparison model
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.5)
    ax.axis('off')
    
    # Two bars for comparison
    draw_bar(ax, 1, 2, 4, 0.6, COLORS['primary'], "John", "40")
    draw_bar(ax, 1, 1, 2.5, 0.6, COLORS['secondary'], "Mary", "25")
    
    # Difference
    ax.plot([3.5, 3.5], [1.3, 1.9], 'r-', linewidth=2)
    ax.text(3.7, 1.6, "Diff = 15", fontsize=9, color='red', fontweight='bold')
    
    ax.set_title('Comparison Model', fontsize=12, pad=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'comparison_model.png', dpi=150, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Sample bar models rendered")

if __name__ == "__main__":
    print("=" * 60)
    print("Rendering Bar Models (New 4-Gates Approach)")
    print("=" * 60)
    
    render_q21_bar_model()
    render_sample_bar_models()
    
    print("\n" + "=" * 60)
    print("✅ Bar models rendered")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)
