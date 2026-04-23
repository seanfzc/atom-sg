#!/usr/bin/env python3
"""
Geometry diagram templates for Matplotlib.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_angle_diagram(ax):
    """Draw a simple angle diagram (protractor)."""
    # Draw two rays from origin
    ax.plot([0, 3], [0, 0], 'k-', lw=2)
    ax.plot([0, 2], [0, 2], 'k-', lw=2)
    # Arc
    arc = patches.Arc((0,0), 2, 2, angle=0, theta1=0, theta2=45, color='blue', lw=2)
    ax.add_patch(arc)
    ax.text(1, 0.2, '45°', fontsize=12)
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_rectangle_diagram(ax):
    """Draw a rectangle."""
    rect = patches.Rectangle((1,1), 5, 3, linewidth=2, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_cuboid_diagram(ax):
    """Draw a simple 3D cuboid."""
    # front face
    rect = patches.Rectangle((1,1), 4, 3, linewidth=2, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(rect)
    # back face offset
    ax.plot([1,1.5], [1,0.5], 'k-', lw=2)
    ax.plot([5,5.5], [1,0.5], 'k-', lw=2)
    ax.plot([1,1.5], [4,3.5], 'k-', lw=2)
    ax.plot([5,5.5], [4,3.5], 'k-', lw=2)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_circle_diagram(ax):
    """Draw a circle with radius."""
    circle = patches.Circle((3,3), 2, linewidth=2, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(circle)
    # radius line
    ax.plot([3,5], [3,3], 'r-', lw=2)
    ax.text(4, 2.8, 'r', fontsize=12, color='red')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_pie_chart_diagram(ax):
    """Draw a simple pie chart sector."""
    wedge = patches.Wedge((3,3), 2, 0, 90, linewidth=2, edgecolor='black', facecolor='orange')
    ax.add_patch(wedge)
    ax.text(3, 5.5, '90° sector', fontsize=12, ha='center')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

def create_geometry_diagram(diagram_type, output_path=None):
    """
    Create a geometry diagram based on type.
    Supported types: 'angle', 'rectangle', 'cuboid', 'circle', 'pie'.
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    if diagram_type == 'angle':
        draw_angle_diagram(ax)
    elif diagram_type == 'rectangle':
        draw_rectangle_diagram(ax)
    elif diagram_type == 'cuboid':
        draw_cuboid_diagram(ax)
    elif diagram_type == 'circle':
        draw_circle_diagram(ax)
    elif diagram_type == 'pie':
        draw_pie_chart_diagram(ax)
    else:
        raise ValueError(f"Unsupported diagram type: {diagram_type}")
    
    ax.set_title(diagram_type.capitalize(), fontsize=10)
    plt.tight_layout()
    if output_path:
        fig.savefig(output_path, format='pdf', bbox_inches='tight')
    return fig

if __name__ == "__main__":
    # Demo: create all diagram types
    for dtype in ['angle', 'rectangle', 'cuboid', 'circle', 'pie']:
        fig = create_geometry_diagram(dtype, f"{dtype}_demo.pdf")
        plt.close(fig)
        print(f"Created {dtype}_demo.pdf")