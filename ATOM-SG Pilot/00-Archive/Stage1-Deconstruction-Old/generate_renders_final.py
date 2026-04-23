import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import yaml
import os
from pathlib import Path

# Paths
YAML_DIR = Path("ATOM-SG Pilot/Stage1-Deconstruction/yaml")
OUTPUT_DIR = Path("ATOM-SG Pilot/Stage1-Deconstruction/outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Styles
COLORS = {
    'tank': '#2C3E50',
    'water': '#3498DB',
    'text': '#2C3E50',
    'rhombus': '#E5E7EB',
    'trapezium': '#DBEAFE',
    'line': '#2C3E50',
    'grid': '#BDC3C7'
}

def render_q7(ax, data):
    """Q7: Tank Filling - Isometric 3/4 View"""
    ax.set_axis_off()
    ax.set_aspect('equal')
    
    # Simple isometric projection for 80x60x50
    # Transformation matrix for isometric
    def project(x, y, z):
        return (x - y) * np.cos(np.radians(30)), (x + y) * np.sin(np.radians(30)) + z

    l, w, h = 8, 6, 5
    
    # Vertices
    v = [project(0,0,0), project(l,0,0), project(l,w,0), project(0,w,0),
         project(0,0,h), project(l,0,h), project(l,w,h), project(0,w,h)]
    
    # Draw water (bottom 2/3)
    wh = h * 2/3
    vw = [project(0,0,0), project(l,0,0), project(l,w,0), project(0,w,0),
          project(0,0,wh), project(l,0,wh), project(l,w,wh), project(0,w,wh)]
    
    # Draw bottom faces
    water_poly = [vw[0], vw[1], vw[5], vw[4]] # Front
    ax.add_patch(patches.Polygon(water_poly, color=COLORS['water'], alpha=0.3, hatch='..'))
    water_poly_side = [vw[1], vw[2], vw[6], vw[5]] # Right
    ax.add_patch(patches.Polygon(water_poly_side, color=COLORS['water'], alpha=0.3, hatch='..'))
    water_top = [vw[4], vw[5], vw[6], vw[7]] # Top surface
    ax.add_patch(patches.Polygon(water_top, color=COLORS['water'], alpha=0.5))

    # Draw tank edges
    edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
    for e in edges:
        p1, p2 = v[e[0]], v[e[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=COLORS['tank'], linewidth=2)

    # Labels
    # 80 cm (length)
    ax.annotate("80 cm", xy=project(l/2, 0, 0), xytext=(0, -20), textcoords='offset points', ha='center')
    # 60 cm (width)
    ax.annotate("60 cm", xy=project(l, w/2, 0), xytext=(15, -10), textcoords='offset points', ha='left')
    # 50 cm (total height)
    ax.annotate("", xy=project(l+0.5, 0, 0), xytext=project(l+0.5, 0, h), arrowprops=dict(arrowstyle='<->'))
    ax.text(project(l+1, 0, h/2)[0], project(l+1, 0, h/2)[1], "50 cm", va='center')
    # Unknown height ?
    ax.text(project(-0.5, 0, h/2)[0], project(-0.5, 0, h/2)[1], "?", fontsize=14, ha='right')
    
    # Tap A
    ax.text(project(l/2, w/2, h+1)[0], project(l/2, w/2, h+1)[1], "Tap A", ha='center', weight='bold')
    ax.annotate("", xy=project(l/2, w/2, h), xytext=project(l/2, w/2, h+0.8), arrowprops=dict(arrowstyle='->', lw=2))

    # Water label
    ax.text(project(l/2, 0, wh/2)[0], project(l/2, 0, wh/2)[1], "2/3 full", ha='center', weight='bold', color='white')

def render_q10(ax, data):
    """Q10: Line Graph - Clean with gridlines"""
    pts = data['data']
    x_labels = [p['x'] for p in pts]
    y_values = [p['y'] for p in pts]
    
    ax.plot(range(len(pts)), y_values, marker='o', color=COLORS['tank'], linewidth=2)
    ax.set_xticks(range(len(pts)))
    ax.set_xticklabels(x_labels)
    ax.set_ylabel(data['axes']['y']['label'])
    ax.set_xlabel(data['axes']['x']['label'])
    ax.set_ylim(0, 130)
    
    # Major gridlines at 20
    ax.set_yticks(np.arange(0, 130, 20))
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Minor ticks (4 units per tick)
    ax.set_yticks(np.arange(0, 130, 4), minor=True)
    ax.grid(True, which='minor', axis='y', linestyle=':', alpha=0.3)
    
    ax.text(0.5, 1.05, "120 T-shirts offered at 20% discount", transform=ax.transAxes, ha='center', weight='bold')

def render_q11(ax, data):
    """Q11: Circular Track"""
    ax.set_axis_off()
    ax.set_aspect('equal')
    
    circle = patches.Circle((0, 0), 2, fill=False, color=COLORS['line'], linewidth=3)
    ax.add_patch(circle)
    
    # Starting line
    ax.plot([0, 0], [1.8, 2.2], color='black', linewidth=3)
    
    # Runners
    ax.scatter([0.2], [2.1], color=COLORS['water'], s=100, label="Ray")
    ax.text(0.2, 2.3, "Ray", ha='center')
    ax.scatter([-0.2], [2.1], color='red', s=100, label="Wayne")
    ax.text(-0.2, 2.3, "Wayne", ha='center')
    
    # Labels
    ax.text(0, 0, "400 m Track", ha='center', va='center', weight='bold')
    
    # Arrow for direction
    ax.annotate("Running", xy=(1.5, 1.5), xytext=(0.5, 0.5), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

def render_q13(ax, data):
    """Q13: Rhombus + Trapezium - RECONSTRUCTED"""
    ax.set_axis_off()
    ax.set_aspect('equal')
    
    # Coordinates for Rhombus ABCD and Trapezium ADEF
    A = (2, 0)
    B = (0.5, 2.5)
    C = (2, 5)
    D = (3.5, 2.5)
    F = (0, 4) 
    E = (4, 4) 
    
    # Patches
    rhombus = patches.Polygon([A, B, C, D], closed=True, facecolor=COLORS['rhombus'], edgecolor='black', linewidth=2, alpha=0.5)
    trapezium = patches.Polygon([A, D, E, F], closed=True, facecolor=COLORS['trapezium'], edgecolor='black', linewidth=2, alpha=0.5)
    ax.add_patch(rhombus)
    ax.add_patch(trapezium)
    
    # Segments
    for shape in [[A,B,C,D,A], [A,D,E,F,A]]:
        x, y = zip(*shape)
        ax.plot(x, y, color='black', linewidth=2)
    
    # Vertices
    offsets = {'A': (0, -0.4), 'B': (-0.4, 0), 'C': (0, 0.4), 'D': (0.4, -0.2), 'E': (0.4, 0.4), 'F': (-0.4, 0.4)}
    for name, pos in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F)]:
        off = offsets[name]
        ax.text(pos[0]+off[0], pos[1]+off[1], name, fontsize=14, fontweight='bold', ha='center', va='center')
        
    # Angles
    ax.text(F[0]+0.4, F[1]-0.4, "21°", color='darkgreen', weight='bold', fontsize=12)
    ax.text(C[0], C[1]-0.6, "108°", ha='center', color='darkgreen', weight='bold', fontsize=12)
    ax.text(A[0]-0.6, A[1]+0.3, "33°", color='red', weight='bold', fontsize=12)
    
    # Unknowns
    ax.text(D[0]-0.6, D[1]+0.4, "x", fontsize=16, weight='bold', color='blue')
    ax.text(B[0]+0.6, B[1]-0.4, "y", fontsize=16, weight='bold', color='blue')
    
    # Arrows
    ax.annotate("", xy=(A[0]+(F[0]-A[0])*0.5, A[1]+(F[1]-A[1])*0.5), xytext=(A[0]+(F[0]-A[0])*0.45, A[1]+(F[1]-A[1])*0.45), arrowprops=dict(arrowstyle="->", color='black', lw=2))
    ax.annotate("", xy=(D[0]+(E[0]-D[0])*0.5, D[1]+(E[1]-D[1])*0.5), xytext=(D[0]+(E[0]-D[0])*0.45, D[1]+(E[1]-D[1])*0.45), arrowprops=dict(arrowstyle="->", color='black', lw=2))

    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 6)

def main():
    for qid in ["Q7", "Q10", "Q11", "Q13"]:
        with open(YAML_DIR / f"{qid}.yaml", 'r') as f:
            data = yaml.safe_load(f)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        if qid == "Q7": render_q7(ax, data['diagram_data'])
        elif qid == "Q10": render_q10(ax, data['diagram_data'])
        elif qid == "Q11": render_q11(ax, data['diagram_data'])
        elif qid == "Q13": render_q13(ax, data['diagram_data'])
        
        plt.title(f"Question {qid} Reconstruction", pad=20)
        plt.savefig(OUTPUT_DIR / f"{qid}_diagram.png", dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Generated {qid}_diagram.png")

if __name__ == "__main__":
    main()
