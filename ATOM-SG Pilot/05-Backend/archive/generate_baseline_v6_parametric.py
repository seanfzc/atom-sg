#!/usr/bin/env python3
"""
Generate Baseline Test v6.0 using Parametric + 4-Gates Approach
Combines: 4-gates reasoning + parametric variable-driven rendering
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Wedge, Arc
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-parametric"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Font sizes (Rule 5)
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
}

class ParametricDiagram:
    """Base class for parametric diagrams."""
    
    def __init__(self, width=8, height=6, dpi=150):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.axis('off')
        self.labels = []  # For collision detection
        
    def add_label(self, text, anchor_x, anchor_y, offset_dir='above', 
                  offset_dist=0.3, fontsize=10, fontweight='normal'):
        """Add label with anchor point and offset (Rule 1)."""
        
        # Compute position from anchor and offset
        dx, dy = 0, 0
        if offset_dir == 'above':
            dy = offset_dist
        elif offset_dir == 'below':
            dy = -offset_dist
        elif offset_dir == 'left':
            dx = -offset_dist
        elif offset_dir == 'right':
            dx = offset_dist
            
        x = anchor_x + dx
        y = anchor_y + dy
        
        # Rule 3: Stay within canvas
        x = max(0.5, min(9.5, x))
        y = max(0.5, min(9.5, y))
        
        text_obj = self.ax.text(x, y, text, fontsize=fontsize, 
                               fontweight=fontweight, ha='center')
        
        self.labels.append({
            'text': text,
            'x': x,
            'y': y,
            'obj': text_obj
        })
        
        return text_obj
    
    def draw_bar(self, x, y, width, height, color, label=None, value=None):
        """Draw bar with parametric dimensions."""
        bar = FancyBboxPatch((x, y), width, height,
                            boxstyle="round,pad=0.02",
                            facecolor=color, edgecolor='black', linewidth=1.5)
        self.ax.add_patch(bar)
        
        if label:
            # Label inside bar (Rule: inside if tall enough)
            if height > 0.8:
                self.ax.text(x + width/2, y + height/2, label,
                           fontsize=FONT_SIZES['data_label'], 
                           ha='center', va='center', fontweight='bold',
                           color='white' if color in [COLORS['primary'], COLORS['secondary']] else 'black')
            else:
                # Label above
                self.add_label(label, x + width/2, y + height, 'above', 0.2)
        
        if value:
            self.add_label(str(value), x + width/2, y, 'below', 0.3)
        
        return bar
    
    def save(self, filename):
        """Save diagram."""
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / filename, dpi=150, 
                   bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"✅ Saved: {filename}")


def render_q21_parametric():
    """
    Q21: Overlapping quarter circles
    Parametric: radius, arc_angle, shaded_area
    """
    # Gate 0: Solve
    radius = 10
    perimeter_OBC = 26
    arc_BC = perimeter_OBC - 20  # 6 cm
    
    # Calculate angle from arc length
    # arc = (θ/360) × 2πr
    # θ = arc × 360 / (2πr)
    arc_angle = (arc_BC * 360) / (2 * np.pi * radius)  # ~34.4°
    
    # Gate 3: Scale
    scale = 0.3  # cm to plot units
    
    # Create diagram
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    ax.set_xlim(-5, 15)
    ax.set_ylim(-3, 12)
    ax.axis('off')
    
    # Center O
    center = (5, 2)
    
    # Angles (parametric from arc_BC)
    angle_B = 90  # degrees
    angle_C = angle_B - arc_angle
    angle_A = angle_B + (90 - arc_angle)  # Quarter circle = 90°
    angle_D = angle_C - (90 - arc_angle)
    
    # Draw quarter circles
    r_plot = radius * scale
    
    # Q1: OAC
    theta1 = np.linspace(np.radians(angle_C), np.radians(angle_A), 100)
    x1 = center[0] + r_plot * np.cos(theta1)
    y1 = center[1] + r_plot * np.sin(theta1)
    ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    # Q2: OBD
    theta2 = np.linspace(np.radians(angle_D), np.radians(angle_B), 100)
    x2 = center[0] + r_plot * np.cos(theta2)
    y2 = center[1] + r_plot * np.sin(theta2)
    ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Radii
    for angle in [angle_A, angle_B, angle_C, angle_D]:
        rad = np.radians(angle)
        ax.plot([center[0], center[0] + r_plot * np.cos(rad)],
                [center[1], center[1] + r_plot * np.sin(rad)],
                'k-', linewidth=2)
    
    # Shade sector OBC
    theta_shade = np.linspace(np.radians(angle_C), np.radians(angle_B), 50)
    x_shade = [center[0]] + list(center[0] + r_plot * np.cos(theta_shade)) + [center[0]]
    y_shade = [center[1]] + list(center[1] + r_plot * np.sin(theta_shade)) + [center[1]]
    
    shade = patches.Polygon(list(zip(x_shade, y_shade)),
                           facecolor=COLORS['shaded'], edgecolor='darkblue',
                           linewidth=2, alpha=0.6)
    ax.add_patch(shade)
    
    # Labels (parametric - anchored to elements)
    points = {
        'A': (center[0] + r_plot * np.cos(np.radians(angle_A)),
              center[1] + r_plot * np.sin(np.radians(angle_A))),
        'B': (center[0] + r_plot * np.cos(np.radians(angle_B)),
              center[1] + r_plot * np.sin(np.radians(angle_B))),
        'C': (center[0] + r_plot * np.cos(np.radians(angle_C)),
              center[1] + r_plot * np.sin(np.radians(angle_C))),
        'D': (center[0] + r_plot * np.cos(np.radians(angle_D)),
              center[1] + r_plot * np.sin(np.radians(angle_D))),
        'O': center
    }
    
    # Draw points and labels
    for label, (x, y) in points.items():
        ax.plot(x, y, 'ko', markersize=10)
        
        # Offset based on position
        offset_x = 0.5 if x > center[0] else -0.5
        offset_y = 0.5 if y > center[1] else -0.5
        
        ax.text(x + offset_x, y + offset_y, label,
               fontsize=FONT_SIZES['axis_label'], fontweight='bold',
               ha='center' if abs(x - center[0]) < 1 else 'left' if x > center[0] else 'right')
    
    # Dimension label (parametric)
    ax.annotate('', xy=(center[0] - 3, center[1] + 4), xytext=center,
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(center[0] - 2, center[1] + 2.5, f'{radius} cm',
           fontsize=FONT_SIZES['data_label'], fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Shaded region info
    ax.text(center[0] + 1, center[1] + 3, f'Shaded OBC\nArea = 30 cm²\nPerimeter = {perimeter_OBC} cm',
           fontsize=FONT_SIZES['annotation'], ha='center',
           bbox=dict(boxstyle='round', facecolor=COLORS['highlight'], alpha=0.5))
    
    # Verification
    computed_arc = (arc_angle / 360) * 2 * np.pi * radius
    ax.text(12, 10, f'Verification:\nArc BC = {arc_BC} cm\nAngle = {arc_angle:.1f}°',
           fontsize=9, ha='left', color='green', fontweight='bold')
    
    ax.set_title('Q21: Overlapping Quarter Circles (Parametric)', 
                fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q21_parametric.png', dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Q21 parametric: arc_BC={arc_BC}cm, angle={arc_angle:.1f}°")


def render_bar_chart_parametric(data, title, filename):
    """
    Parametric bar chart
    data: list of {label, value}
    """
    # Gate 0: Variables from data
    values = [d['value'] for d in data]
    max_val = max(values)
    
    # Gate 3: Scale
    axis_max = np.ceil(max_val / 10) * 10  # Round up to nearest 10
    
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    
    # Parametric bar sizing
    n_bars = len(data)
    gap_ratio = 0.3
    plot_width = 8
    bar_width = plot_width / (n_bars + (n_bars + 1) * gap_ratio)
    gap = bar_width * gap_ratio
    
    # Draw bars
    for i, item in enumerate(data):
        x = gap + i * (bar_width + gap)
        bar_height = (item['value'] / axis_max) * 6  # Scale to plot height
        
        color = COLORS['primary'] if i % 2 == 0 else COLORS['secondary']
        
        # Draw bar
        bar = FancyBboxPatch((x, 0), bar_width, bar_height,
                            boxstyle="round,pad=0.02",
                            facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(bar)
        
        # Label (parametric: inside if tall enough)
        if bar_height > 0.8:
            ax.text(x + bar_width/2, bar_height/2, str(item['value']),
                   fontsize=FONT_SIZES['data_label'], ha='center', va='center',
                   fontweight='bold', color='white')
        else:
            ax.text(x + bar_width/2, bar_height + 0.2, str(item['value']),
                   fontsize=FONT_SIZES['data_label'], ha='center', fontweight='bold')
        
        # X-axis label
        ax.text(x + bar_width/2, -0.5, item['label'],
               fontsize=FONT_SIZES['tick_label'], ha='center')
    
    # Y-axis
    ax.set_ylim(0, axis_max * 1.1 / (axis_max / 6))  # Normalize
    ax.set_xlim(0, 10)
    
    # Gridlines (parametric)
    for y in np.linspace(0, axis_max, 5):
        plot_y = (y / axis_max) * 6
        ax.axhline(plot_y, color='gray', linestyle='--', alpha=0.3, linewidth=0.5)
        ax.text(-0.3, plot_y, str(int(y)), fontsize=FONT_SIZES['tick_label'],
               ha='right', va='center')
    
    ax.set_title(title, fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ {filename}: {n_bars} bars, max={max_val}")


def render_pie_chart_parametric(data, title, filename):
    """
    Parametric pie chart
    data: list of {label, value}
    """
    # Gate 0: Calculate from data
    total = sum(d['value'] for d in data)
    
    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Parametric angles
    start_angle = 0
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['highlight']]
    
    for i, item in enumerate(data):
        fraction = item['value'] / total
        sweep_angle = fraction * 360
        
        # Draw slice
        wedge = Wedge((0, 0), 1, start_angle, start_angle + sweep_angle,
                     facecolor=colors[i % len(colors)], 
                     edgecolor='black', linewidth=1.5)
        ax.add_patch(wedge)
        
        # Label position (parametric from angle)
        mid_angle = np.radians(start_angle + sweep_angle/2)
        label_x = 1.2 * np.cos(mid_angle)
        label_y = 1.2 * np.sin(mid_angle)
        
        pct = fraction * 100
        ax.text(label_x, label_y, f"{item['label']}\n{pct:.0f}%",
               fontsize=FONT_SIZES['data_label'], ha='center', va='center',
               fontweight='bold')
        
        start_angle += sweep_angle
    
    ax.set_title(title, fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150,
               bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ {filename}: total={total}")


if __name__ == "__main__":
    print("=" * 60)
    print("Generating Parametric Diagrams v6.0")
    print("=" * 60)
    
    # Q21
    render_q21_parametric()
    
    # Bar chart example (Q35)
    books_data = [
        {'label': 'Ali', 'value': 12},
        {'label': 'Ben', 'value': 8},
        {'label': 'Cal', 'value': 15},
        {'label': 'Dan', 'value': 6},
        {'label': 'Eve', 'value': 10},
    ]
    render_bar_chart_parametric(books_data, 'Q35: Books Read by Students', 'Q35_books_parametric.png')
    
    # Pie chart example (Q37)
    spending_data = [
        {'label': 'Transport', 'value': 24},
        {'label': 'Food', 'value': 60},
        {'label': 'Savings', 'value': 6},
        {'label': 'Clothes', 'value': 10},
    ]
    render_pie_chart_parametric(spending_data, "Q37: Isabelle's Spending", 'Q37_spending_parametric.png')
    
    print("\n" + "=" * 60)
    print("✅ Parametric diagrams generated")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)
