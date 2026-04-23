#!/usr/bin/env python3
"""
Generate ALL parametric diagrams for baseline test v6.0
Comprehensive rendering using 4-gates + parametric approach
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Wedge, Arc, Polygon, Rectangle
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path
import math

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "baseline-v6-all"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Font sizes (Rule 5 from Parametric Guide)
FONT_SIZES = {
    'title': 14,
    'axis_label': 12,
    'data_label': 11,
    'tick_label': 10,
    'annotation': 10,
    'footnote': 9,
}

# Colors
COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31',
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'shaded': '#DEEBF7',
    'light_blue': '#E7F3FF',
    'light_orange': '#FFF4E6',
    'light_green': '#E8F5E9',
}

class ParametricRenderer:
    """Base class for parametric diagram rendering."""
    
    def __init__(self, width=10, height=8, dpi=150):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        self.labels = []
        self.scale = 1.0
        
    def set_canvas(self, xlim, ylim):
        """Set canvas limits."""
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.axis('off')
        
    def add_label(self, text, anchor_x, anchor_y, offset_dir='above', 
                  offset_dist=0.4, fontsize=10, fontweight='normal', 
                  color='black', bbox=False):
        """Add label with anchor point and offset (Rule 1)."""
        dx, dy = 0, 0
        ha, va = 'center', 'center'
        
        if offset_dir == 'above':
            dy = offset_dist
            va = 'bottom'
        elif offset_dir == 'below':
            dy = -offset_dist
            va = 'top'
        elif offset_dir == 'left':
            dx = -offset_dist
            ha = 'right'
        elif offset_dir == 'right':
            dx = offset_dist
            ha = 'left'
        elif offset_dir == 'above_left':
            dx, dy = -offset_dist*0.7, offset_dist*0.7
            ha, va = 'right', 'bottom'
        elif offset_dir == 'above_right':
            dx, dy = offset_dist*0.7, offset_dist*0.7
            ha, va = 'left', 'bottom'
        elif offset_dir == 'below_left':
            dx, dy = -offset_dist*0.7, -offset_dist*0.7
            ha, va = 'right', 'top'
        elif offset_dir == 'below_right':
            dx, dy = offset_dist*0.7, -offset_dist*0.7
            ha, va = 'left', 'top'
            
        x = anchor_x + dx
        y = anchor_y + dy
        
        # Rule 3: Stay within canvas
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        padding = 0.3
        x = max(xlim[0] + padding, min(xlim[1] - padding, x))
        y = max(ylim[0] + padding, min(ylim[1] - padding, y))
        
        kwargs = {
            'fontsize': fontsize,
            'fontweight': fontweight,
            'ha': ha,
            'va': va,
            'color': color
        }
        
        if bbox:
            kwargs['bbox'] = dict(boxstyle='round,pad=0.2', 
                                 facecolor='white', alpha=0.9, edgecolor='gray')
        
        text_obj = self.ax.text(x, y, text, **kwargs)
        self.labels.append({'text': text, 'x': x, 'y': y, 'obj': text_obj})
        return text_obj
    
    def draw_point(self, x, y, label=None, label_dir='above', markersize=8):
        """Draw a point with optional label."""
        self.ax.plot(x, y, 'ko', markersize=markersize, zorder=5)
        if label:
            self.add_label(label, x, y, label_dir, fontsize=FONT_SIZES['axis_label'], 
                          fontweight='bold')
    
    def save(self, filename, title=None):
        """Save diagram."""
        if title:
            self.ax.set_title(title, fontsize=FONT_SIZES['title'], 
                            fontweight='bold', pad=15)
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / filename, dpi=150, 
                   bbox_inches='tight', facecolor='white', edgecolor='none')
        plt.close()
        print(f"  ✅ {filename}")


def render_q15_overlapping_quarter_circles():
    """
    Q15: Overlapping Quarter Circles (ACS Junior)
    Parametric: radius, arc_BC, arc_angle
    """
    r = ParametricRenderer(10, 8)
    r.set_canvas((-2, 12), (-2, 10))
    
    # Gate 0: Variables
    radius = 10
    perimeter_OBC = 26
    arc_BC = perimeter_OBC - 20  # 6 cm
    arc_angle = (arc_BC * 360) / (2 * math.pi * radius)  # 34.4°
    area_quarter = 0.25 * math.pi * radius**2
    
    # Scale
    scale = 0.35
    cx, cy = 5, 3
    
    # Parametric angles
    angle_B = 90
    angle_C = angle_B - arc_angle
    angle_A = angle_B + (90 - arc_angle)
    angle_D = angle_C - (90 - arc_angle)
    
    # Draw quarter circle 1 (OAC)
    theta1 = np.linspace(math.radians(angle_C), math.radians(angle_A), 100)
    x1 = cx + radius*scale * np.cos(theta1)
    y1 = cy + radius*scale * np.sin(theta1)
    r.ax.plot(x1, y1, 'k-', linewidth=2.5)
    
    # Draw quarter circle 2 (OBD)
    theta2 = np.linspace(math.radians(angle_D), math.radians(angle_B), 100)
    x2 = cx + radius*scale * np.cos(theta2)
    y2 = cy + radius*scale * np.sin(theta2)
    r.ax.plot(x2, y2, 'k-', linewidth=2.5)
    
    # Draw radii
    for angle in [angle_A, angle_B, angle_C, angle_D]:
        rad = math.radians(angle)
        r.ax.plot([cx, cx + radius*scale * math.cos(rad)],
                 [cy, cy + radius*scale * math.sin(rad)],
                 'k-', linewidth=2)
    
    # Shade sector OBC
    theta_shade = np.linspace(math.radians(angle_C), math.radians(angle_B), 50)
    x_shade = [cx] + list(cx + radius*scale * np.cos(theta_shade)) + [cx]
    y_shade = [cy] + list(cy + radius*scale * np.sin(theta_shade)) + [cy]
    shade = Polygon(list(zip(x_shade, y_shade)),
                   facecolor=COLORS['light_blue'], edgecolor='darkblue',
                   linewidth=2, alpha=0.7, zorder=1)
    r.ax.add_patch(shade)
    
    # Points with parametric positions
    points = {
        'A': (cx + radius*scale * math.cos(math.radians(angle_A)),
              cy + radius*scale * math.sin(math.radians(angle_A))),
        'B': (cx + radius*scale * math.cos(math.radians(angle_B)),
              cy + radius*scale * math.sin(math.radians(angle_B))),
        'C': (cx + radius*scale * math.cos(math.radians(angle_C)),
              cy + radius*scale * math.sin(math.radians(angle_C))),
        'D': (cx + radius*scale * math.cos(math.radians(angle_D)),
              cy + radius*scale * math.sin(math.radians(angle_D))),
    }
    
    # Draw points and labels
    r.draw_point(cx, cy, 'O', 'below_left', markersize=10)
    for label, (x, y) in points.items():
        r.draw_point(x, y, label, 'above' if y > cy else 'below', markersize=8)
    
    # Dimension label (parametric)
    r.ax.annotate('', xy=(cx - 2, cy + 3.5), xytext=(cx, cy),
                 arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    r.add_label(f'{radius} cm', cx - 1.5, cy + 2, fontsize=FONT_SIZES['data_label'],
               fontweight='bold', bbox=True)
    
    # Info box
    info_text = f'Shaded OBC\nArea = 30 cm²\nPerimeter = {perimeter_OBC} cm'
    r.add_label(info_text, cx + 2, cy + 4, fontsize=FONT_SIZES['annotation'],
               bbox=True)
    
    # Verification
    verify_text = f'Verification:\nArc BC = {arc_BC} cm\nAngle = {arc_angle:.1f}°'
    r.add_label(verify_text, 10, 8, fontsize=9, color='green', fontweight='bold')
    
    r.save('Q15_overlapping_quarter_circles.png', 
          'Q15: Overlapping Quarter Circles (Parametric)')


def render_q12_five_squares():
    """
    Q12: Five Squares in Rectangle
    Parametric: square sizes, arrangement
    """
    r = ParametricRenderer(12, 8)
    r.set_canvas((-1, 11), (-1, 7))
    
    # Typical arrangement: 3 squares bottom, 2 on top
    # Square X = 4cm (smallest)
    # Deduce: Y = 6cm, Z = 10cm (example based on typical exam patterns)
    
    square_X = 4
    square_Y = 6
    square_Z = 10
    
    # Scale
    scale = 0.5
    
    # Draw squares (parametric positions)
    squares = [
        {'name': 'X', 'side': square_X, 'pos': (0, 0), 'color': COLORS['light_blue']},
        {'name': 'Y', 'side': square_Y, 'pos': (square_X*scale, 0), 'color': COLORS['light_orange']},
        {'name': 'Z', 'side': square_Z, 'pos': ((square_X+square_Y)*scale, 0), 'color': COLORS['light_green']},
        {'name': 'W', 'side': square_Y, 'pos': (square_X*scale, square_Y*scale), 'color': COLORS['light_orange']},
        {'name': 'V', 'side': square_X, 'pos': (0, square_X*scale), 'color': COLORS['light_blue']},
    ]
    
    for sq in squares:
        x, y = sq['pos']
        side = sq['side'] * scale
        rect = Rectangle((x, y), side, side, 
                         facecolor=sq['color'], edgecolor='black', linewidth=2)
        r.ax.add_patch(rect)
        
        # Label inside
        r.ax.text(x + side/2, y + side/2, sq['name'],
                 fontsize=FONT_SIZES['data_label'], ha='center', va='center',
                 fontweight='bold')
        
        # Side dimension
        if sq['name'] == 'X':
            r.add_label(f'{sq["side"]} cm', x + side/2, y - 0.3, 'below',
                       fontsize=FONT_SIZES['tick_label'])
    
    # Rectangle boundary
    total_width = (square_X + square_Y + square_Z) * scale
    total_height = max(square_Z, square_X + square_Y) * scale
    
    r.ax.plot([0, total_width, total_width, 0, 0],
             [0, 0, total_height, total_height, 0],
             'k--', linewidth=2)
    
    # Dimensions
    r.add_label(f'Length = {square_X + square_Y + square_Z} cm', 
               total_width/2, -0.8, fontsize=FONT_SIZES['annotation'])
    
    r.save('Q12_five_squares.png', 'Q12: Five Squares in Rectangle')


def render_q19_3d_solid():
    """
    Q19: 3D Solid Views (Isometric)
    Parametric: cube positions, views
    """
    r = ParametricRenderer(14, 10)
    r.set_canvas((-1, 13), (-1, 9))
    
    # Isometric projection parameters
    iso_angle = math.radians(30)
    cos_iso = math.cos(iso_angle)
    sin_iso = math.sin(iso_angle)
    
    def iso_x(x, y, z):
        return 2 + (x - z) * cos_iso * 0.8
    
    def iso_y(x, y, z):
        return 2 + (x + z) * sin_iso * 0.8 + y * 0.8
    
    # Cube positions (7 cubes)
    cubes = [
        (0, 0, 0), (0, 1, 0),  # Stack of 2 at (0,0)
        (1, 0, 0), (1, 1, 0), (1, 2, 0),  # Stack of 3 at (1,0)
        (2, 0, 0), (2, 1, 0),  # Stack of 2 at (2,0)
    ]
    
    # Draw cubes (back to front)
    for x, y, z in sorted(cubes, key=lambda c: (c[2], c[0], c[1])):
        # Cube vertices in isometric
        base = [
            (iso_x(x, y, z), iso_y(x, y, z)),
            (iso_x(x+1, y, z), iso_y(x+1, y, z)),
            (iso_x(x+1, y, z+1), iso_y(x+1, y, z+1)),
            (iso_x(x, y, z+1), iso_y(x, y, z+1)),
        ]
        top = [
            (iso_x(x, y+1, z), iso_y(x, y+1, z)),
            (iso_x(x+1, y+1, z), iso_y(x+1, y+1, z)),
            (iso_x(x+1, y+1, z+1), iso_y(x+1, y+1, z+1)),
            (iso_x(x, y+1, z+1), iso_y(x, y+1, z+1)),
        ]
        
        # Draw faces
        # Top face
        top_poly = Polygon(top, facecolor=COLORS['light_blue'], 
                          edgecolor='black', linewidth=1.5)
        r.ax.add_patch(top_poly)
        
        # Front face
        front = [base[0], base[1], top[1], top[0]]
        front_poly = Polygon(front, facecolor=COLORS['primary'], 
                            edgecolor='black', linewidth=1.5, alpha=0.8)
        r.ax.add_patch(front_poly)
        
        # Right face
        right = [base[1], base[2], top[2], top[1]]
        right_poly = Polygon(right, facecolor=COLORS['secondary'], 
                            edgecolor='black', linewidth=1.5, alpha=0.8)
        r.ax.add_patch(right_poly)
    
    # Title
    r.ax.set_title('Q19: 3D Solid (7 cubes) - Isometric View', 
                  fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    r.save('Q19_3d_solid.png')


def render_bar_chart(data, title, filename, y_max=None):
    """
    Parametric bar chart
    data: list of {label, value}
    """
    values = [d['value'] for d in data]
    max_val = max(values)
    axis_max = y_max or (np.ceil(max_val / 10) * 10)
    
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    
    # Parametric bar sizing
    n_bars = len(data)
    gap_ratio = 0.3
    plot_width = 8
    bar_width = plot_width / (n_bars + (n_bars + 1) * gap_ratio)
    gap = bar_width * gap_ratio
    
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], 
              COLORS['highlight'], COLORS['neutral']]
    
    for i, item in enumerate(data):
        x = gap + i * (bar_width + gap)
        bar_height = (item['value'] / axis_max) * 5
        
        color = colors[i % len(colors)]
        
        # Draw bar
        bar = FancyBboxPatch((x, 0), bar_width, bar_height,
                            boxstyle="round,pad=0.02",
                            facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(bar)
        
        # Value label (inside if tall enough)
        if bar_height > 0.6:
            ax.text(x + bar_width/2, bar_height/2, str(item['value']),
                   fontsize=FONT_SIZES['data_label'], ha='center', va='center',
                   fontweight='bold', color='white')
        else:
            ax.text(x + bar_width/2, bar_height + 0.15, str(item['value']),
                   fontsize=FONT_SIZES['data_label'], ha='center', fontweight='bold')
        
        # X label
        ax.text(x + bar_width/2, -0.4, item['label'],
               fontsize=FONT_SIZES['tick_label'], ha='center')
    
    # Y-axis gridlines
    for y in np.linspace(0, axis_max, 5):
        plot_y = (y / axis_max) * 5
        ax.axhline(plot_y, color='gray', linestyle='--', alpha=0.3, linewidth=0.5)
        ax.text(-0.2, plot_y, str(int(y)), fontsize=FONT_SIZES['tick_label'],
               ha='right', va='center')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 6)
    ax.axis('off')
    ax.set_title(title, fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✅ {filename}")


def render_pie_chart(data, title, filename):
    """
    Parametric pie chart
    data: list of {label, value}
    """
    total = sum(d['value'] for d in data)
    
    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    start_angle = 0
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], 
              COLORS['highlight']]
    
    for i, item in enumerate(data):
        fraction = item['value'] / total
        sweep_angle = fraction * 360
        
        # Draw slice
        wedge = Wedge((0, 0), 1, start_angle, start_angle + sweep_angle,
                     facecolor=colors[i % len(colors)], 
                     edgecolor='black', linewidth=1.5)
        ax.add_patch(wedge)
        
        # Label position (parametric)
        mid_angle = math.radians(start_angle + sweep_angle/2)
        label_r = 1.25
        label_x = label_r * math.cos(mid_angle)
        label_y = label_r * math.sin(mid_angle)
        
        pct = fraction * 100
        ax.text(label_x, label_y, f"{item['label']}\n{pct:.0f}%",
               fontsize=FONT_SIZES['data_label'], ha='center', va='center',
               fontweight='bold')
        
        start_angle += sweep_angle
    
    ax.set_title(title, fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✅ {filename}")


def render_line_graph(data, title, filename):
    """
    Parametric line graph
    data: list of {x, y}
    """
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    
    x_vals = [d['x'] for d in data]
    y_vals = [d['y'] for d in data]
    
    x_max, y_max = max(x_vals), max(y_vals)
    
    # Plot line
    ax.plot(x_vals, y_vals, 'o-', color=COLORS['primary'], 
           linewidth=2.5, markersize=8, markeredgecolor='black',
           markerfacecolor=COLORS['primary'])
    
    # Grid
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # Points with values
    for d in data:
        ax.text(d['x'], d['y'] + y_max*0.05, str(d['y']),
               fontsize=FONT_SIZES['data_label'], ha='center', fontweight='bold')
    
    ax.set_xlim(min(x_vals) - 0.5, max(x_vals) + 0.5)
    ax.set_ylim(0, y_max * 1.2)
    ax.set_title(title, fontsize=FONT_SIZES['title'], fontweight='bold', pad=15)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✅ {filename}")


if __name__ == "__main__":
    print("=" * 70)
    print("Generating ALL Parametric Diagrams for Baseline Test v6.0")
    print("=" * 70)
    print()
    
    # Geometry Questions
    print("📐 Geometry Diagrams:")
    render_q15_overlapping_quarter_circles()
    render_q12_five_squares()
    render_q19_3d_solid()
    
    # Data Interpretation
    print("\n📊 Data Interpretation:")
    
    # Q35: Bar chart
    books_data = [
        {'label': 'Ali', 'value': 12},
        {'label': 'Ben', 'value': 8},
        {'label': 'Cal', 'value': 15},
        {'label': 'Dan', 'value': 6},
        {'label': 'Eve', 'value': 10},
    ]
    render_bar_chart(books_data, "Q35: Books Read by Students", 
                    'Q35_books_bar_chart.png')
    
    # Q37: Pie chart
    spending_data = [
        {'label': 'Transport', 'value': 24},
        {'label': 'Food', 'value': 60},
        {'label': 'Savings', 'value': 6},
        {'label': 'Clothes', 'value': 10},
    ]
    render_pie_chart(spending_data, "Q37: Isabelle's Spending",
                    'Q37_spending_pie_chart.png')
    
    # Q33: Line graph
    sales_data = [
        {'x': 1, 'y': 45},
        {'x': 2, 'y': 52},
        {'x': 3, 'y': 48},
        {'x': 4, 'y': 60},
        {'x': 5, 'y': 55},
        {'x': 6, 'y': 68},
    ]
    render_line_graph(sales_data, "Q33: T-Shirt Sales Over 6 Months",
                     'Q33_tshirt_sales_line_graph.png')
    
    print()
    print("=" * 70)
    print(f"✅ All diagrams generated in: {OUTPUT_DIR}")
    print("=" * 70)
