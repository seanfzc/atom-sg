"""
Grid Renderer Module

Generates exam-quality grid construction diagrams including:
- Square grids with 1cm precision
- Triangle and trapezium construction tasks
- Protractor measurement overlays
- Constraint visualization (parallel lines, equal length markers)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Rectangle, Arc, FancyArrowPatch
import numpy as np
from typing import Dict, Any, Optional, Tuple, List
try:
    from .base_renderer import BaseRenderer, MOE_COLORS, ValidationError
except ImportError:
    from base_renderer import BaseRenderer, MOE_COLORS, ValidationError


class GridRenderer(BaseRenderer):
    """
    Renderer for grid-based construction diagrams.
    
    Supports VRS YAML specifications with the following structure:
    
    ```yaml
    type: grid_construction
    title: "Triangle Construction"
    grid:
      type: square  # or dot
      size: 10      # grid units
      unit: 1cm     # real-world unit per grid unit
    shapes:
      - type: triangle
        vertices: [[0,0], [4,0], [2,3]]
        labels: ["A", "B", "C"]
        show_dimensions: true
      - type: trapezium
        vertices: [[0,0], [5,0], [4,3], [1,3]]
    constraints:
      - type: parallel
        lines: [[[0,0], [4,0]], [[1,3], [4,3]]]
      - type: equal_length
        segments: [[[0,0], [2,3]], [[4,0], [2,3]]]
    protractor:
      enabled: true
      position: [2, 0]
      angle_range: [0, 180]
    ```
    """
    
    def __init__(self, output_dir: Optional[str] = None):
        super().__init__(output_dir)
        self.grid_size = 10
        self.grid_unit = 1.0
        self.grid_type = 'square'
        
    def validate_spec(self, spec: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate grid construction VRS specification.
        
        Args:
            spec: Parsed YAML specification
            
        Returns:
            Tuple of (is_valid, list_of_error_messages)
        """
        errors = []
        
        # Check required fields
        if 'type' not in spec:
            errors.append("Missing required field: 'type'")
        elif spec['type'] != 'grid_construction':
            errors.append(f"Invalid type: {spec['type']}, expected 'grid_construction'")
        
        # Validate grid configuration
        if 'grid' not in spec:
            errors.append("Missing required field: 'grid'")
        else:
            grid = spec['grid']
            if 'size' not in grid:
                errors.append("Missing grid.size")
            if 'type' not in grid:
                errors.append("Missing grid.type")
            elif grid['type'] not in ['square', 'dot']:
                errors.append(f"Invalid grid.type: {grid['type']}")
        
        # Validate shapes if present
        if 'shapes' in spec:
            for i, shape in enumerate(spec['shapes']):
                if 'type' not in shape:
                    errors.append(f"Shape {i}: missing 'type'")
                if 'vertices' not in shape:
                    errors.append(f"Shape {i}: missing 'vertices'")
                elif not isinstance(shape['vertices'], list):
                    errors.append(f"Shape {i}: 'vertices' must be a list")
        
        # Validate protractor if present
        if 'protractor' in spec:
            pro = spec['protractor']
            if pro.get('enabled', False):
                if 'position' not in pro:
                    errors.append("Protractor enabled but missing 'position'")
        
        return len(errors) == 0, errors
    
    def render(self, spec: Dict[str, Any], output_filename: Optional[str] = None) -> str:
        """
        Render grid construction diagram.
        
        Args:
            spec: Validated VRS specification
            output_filename: Optional output filename
            
        Returns:
            Path to generated PNG file
        """
        # Extract configuration
        grid_config = spec.get('grid', {})
        self.grid_size = grid_config.get('size', 10)
        self.grid_unit = grid_config.get('unit', 1.0)
        self.grid_type = grid_config.get('type', 'square')
        
        # Create figure with appropriate size
        margin = 2
        fig_size = (self.grid_size + margin, self.grid_size + margin)
        self.fig, self.ax = plt.subplots(figsize=fig_size, dpi=150)
        
        # Set limits with padding
        padding = 1
        self.ax.set_xlim(-padding, self.grid_size + padding)
        self.ax.set_ylim(-padding, self.grid_size + padding)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Draw grid
        if self.grid_type == 'square':
            self._draw_square_grid()
        elif self.grid_type == 'dot':
            self._draw_dot_grid()
        
        # Draw shapes
        shapes = spec.get('shapes', [])
        for shape in shapes:
            self._draw_shape(shape)
        
        # Draw constraints
        constraints = spec.get('constraints', [])
        for constraint in constraints:
            self._draw_constraint(constraint)
        
        # Draw protractor if enabled
        protractor = spec.get('protractor', {})
        if protractor.get('enabled', False):
            self._draw_protractor(protractor)
        
        # Add title
        title = spec.get('title', 'Grid Construction')
        self.ax.set_title(title, fontsize=14, fontweight='bold',
                         color=self.colors['text'], pad=20)
        
        # Add grid scale label
        self.ax.text(self.grid_size / 2, -0.7, 
                    f"Grid: 1 unit = {self.grid_unit} cm",
                    ha='center', fontsize=9, color=self.colors['text'],
                    style='italic')
        
        # Save
        if output_filename is None:
            output_filename = spec.get('id', 'grid_construction')
        
        return self.save_figure(output_filename)
    
    def _draw_square_grid(self) -> None:
        """Draw square grid lines."""
        # Minor grid lines (every unit)
        for i in range(self.grid_size + 1):
            self.ax.axvline(i, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
            self.ax.axhline(i, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
        
        # Major grid lines (every 5 units)
        for i in range(0, self.grid_size + 1, 5):
            self.ax.axvline(i, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
            self.ax.axhline(i, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
        
        # Add axis labels
        for i in range(0, self.grid_size + 1, 5):
            self.ax.text(i, -0.3, str(i), ha='center', fontsize=8, color=self.colors['text'])
            self.ax.text(-0.3, i, str(i), ha='right', va='center', fontsize=8, color=self.colors['text'])
    
    def _draw_dot_grid(self) -> None:
        """Draw dot grid (for isometric-style construction)."""
        for x in range(self.grid_size + 1):
            for y in range(self.grid_size + 1):
                self.ax.plot(x, y, 'o', color=self.colors['grid_major'], 
                           markersize=3, zorder=0)
    
    def _draw_shape(self, shape: Dict[str, Any]) -> None:
        """Draw a geometric shape on the grid."""
        shape_type = shape.get('type', 'polygon')
        vertices = shape.get('vertices', [])
        labels = shape.get('labels', [])
        show_dimensions = shape.get('show_dimensions', False)
        fill_color = shape.get('fill_color', self.colors['shape_fill'])
        stroke_color = shape.get('stroke_color', self.colors['shape_stroke'])
        
        if not vertices:
            return
        
        # Draw polygon
        polygon = Polygon(vertices, closed=True, 
                         facecolor=fill_color, 
                         edgecolor=stroke_color, 
                         linewidth=2, zorder=2)
        self.ax.add_patch(polygon)
        
        # Add vertex labels
        for i, (vx, vy) in enumerate(vertices):
            if i < len(labels):
                label = labels[i]
                # Offset label slightly from vertex
                offset = 0.3
                angle = np.arctan2(vy - self.grid_size/2, vx - self.grid_size/2)
                label_x = vx + offset * np.cos(angle)
                label_y = vy + offset * np.sin(angle)
                self.ax.text(label_x, label_y, label, ha='center', va='center',
                           fontsize=11, fontweight='bold', color=self.colors['text'],
                           bbox=dict(boxstyle='circle,pad=0.1', 
                                    facecolor='white', edgecolor=stroke_color, linewidth=1.5))
        
        # Draw dimensions if requested
        if show_dimensions:
            self._draw_shape_dimensions(vertices, labels)
    
    def _draw_shape_dimensions(self, vertices: List[List[float]], labels: List[str]) -> None:
        """Draw dimension labels for shape sides."""
        n = len(vertices)
        for i in range(n):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % n]
            
            # Calculate length
            length = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
            length_cm = length * self.grid_unit
            
            # Midpoint
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            
            # Offset perpendicular to edge
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            length_norm = np.sqrt(dx**2 + dy**2)
            if length_norm > 0:
                offset_x = -dy / length_norm * 0.5
                offset_y = dx / length_norm * 0.5
                
                label_x = mid_x + offset_x
                label_y = mid_y + offset_y
                
                self.ax.text(label_x, label_y, f"{length_cm:.1f} cm",
                           ha='center', va='center', fontsize=9,
                           color=self.colors['text'],
                           bbox=dict(boxstyle='round,pad=0.15', 
                                    facecolor=self.colors['highlight'],
                                    edgecolor='none', alpha=0.9))
    
    def _draw_constraint(self, constraint: Dict[str, Any]) -> None:
        """Draw constraint visualization (parallel, equal length, etc.)."""
        constraint_type = constraint.get('type', '')
        
        if constraint_type == 'parallel':
            self._draw_parallel_constraint(constraint)
        elif constraint_type == 'equal_length':
            self._draw_equal_length_constraint(constraint)
        elif constraint_type == 'right_angle':
            self._draw_right_angle_constraint(constraint)
    
    def _draw_parallel_constraint(self, constraint: Dict[str, Any]) -> None:
        """Draw parallel line markers (arrows)."""
        lines = constraint.get('lines', [])
        
        for line in lines:
            if len(line) != 2:
                continue
            p1, p2 = line
            
            # Calculate midpoint
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            
            # Direction vector
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            length = np.sqrt(dx**2 + dy**2)
            
            if length > 0:
                # Draw parallel arrows
                arrow_len = 0.25
                angle = np.arctan2(dy, dx)
                
                # Two small arrows
                for offset in [-0.15, 0.15]:
                    ax_offset = -dy / length * offset
                    ay_offset = dx / length * offset
                    
                    self.ax.annotate('', 
                                   xy=(mid_x + arrow_len * np.cos(angle) + ax_offset,
                                       mid_y + arrow_len * np.sin(angle) + ay_offset),
                                   xytext=(mid_x - arrow_len * np.cos(angle) + ax_offset,
                                          mid_y - arrow_len * np.sin(angle) + ay_offset),
                                   arrowprops=dict(arrowstyle='->', color=self.colors['construction'],
                                                  lw=1.5))
    
    def _draw_equal_length_constraint(self, constraint: Dict[str, Any]) -> None:
        """Draw equal length markers (tick marks)."""
        segments = constraint.get('segments', [])
        
        for segment in segments:
            if len(segment) != 2:
                continue
            p1, p2 = segment
            
            # Calculate midpoint
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            
            # Direction vector
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            length = np.sqrt(dx**2 + dy**2)
            
            if length > 0:
                # Draw tick mark perpendicular to segment
                tick_len = 0.2
                perp_x = -dy / length * tick_len
                perp_y = dx / length * tick_len
                
                self.ax.plot([mid_x + perp_x, mid_x - perp_x],
                           [mid_y + perp_y, mid_y - perp_y],
                           color=self.colors['construction'], linewidth=2, zorder=3)
    
    def _draw_right_angle_constraint(self, constraint: Dict[str, Any]) -> None:
        """Draw right angle marker (square corner)."""
        vertex = constraint.get('vertex', [0, 0])
        arm1 = constraint.get('arm1', [1, 0])
        arm2 = constraint.get('arm2', [0, 1])
        
        # Draw small square at vertex
        square_size = 0.3
        
        # Calculate direction vectors
        v1_x = arm1[0] - vertex[0]
        v1_y = arm1[1] - vertex[1]
        v1_len = np.sqrt(v1_x**2 + v1_y**2)
        
        v2_x = arm2[0] - vertex[0]
        v2_y = arm2[1] - vertex[1]
        v2_len = np.sqrt(v2_x**2 + v2_y**2)
        
        if v1_len > 0 and v2_len > 0:
            # Normalize
            v1_x /= v1_len
            v1_y /= v1_len
            v2_x /= v2_len
            v2_y /= v2_len
            
            # Draw square
            square_x = vertex[0] + square_size * v1_x
            square_y = vertex[1] + square_size * v1_y
            
            rect = Rectangle((square_x - square_size * v1_x - square_size * v2_x,
                             square_y - square_size * v1_y - square_size * v2_y),
                            square_size, square_size, 
                            angle=np.degrees(np.arctan2(v1_y, v1_x)),
                            fill=False, edgecolor=self.colors['construction'],
                            linewidth=1.5, zorder=3)
            self.ax.add_patch(rect)
    
    def _draw_protractor(self, protractor: Dict[str, Any]) -> None:
        """Draw protractor overlay for angle measurement."""
        position = protractor.get('position', [0, 0])
        radius = protractor.get('radius', 3)
        angle_range = protractor.get('angle_range', [0, 180])
        
        px, py = position
        
        # Draw protractor semicircle
        arc = Arc((px, py), radius * 2, radius * 2,
                 angle=0, theta1=angle_range[0], theta2=angle_range[1],
                 color=self.colors['construction'], linewidth=1.5, linestyle='--', zorder=1)
        self.ax.add_patch(arc)
        
        # Draw angle markings
        for angle in range(angle_range[0], angle_range[1] + 1, 10):
            rad = np.radians(angle)
            x_outer = px + radius * np.cos(rad)
            y_outer = py + radius * np.sin(rad)
            x_inner = px + (radius - 0.3) * np.cos(rad)
            y_inner = py + (radius - 0.3) * np.sin(rad)
            
            self.ax.plot([x_inner, x_outer], [y_inner, y_outer],
                       color=self.colors['construction'], linewidth=1, zorder=1)
            
            # Label every 30 degrees
            if angle % 30 == 0:
                x_label = px + (radius + 0.4) * np.cos(rad)
                y_label = py + (radius + 0.4) * np.sin(rad)
                self.ax.text(x_label, y_label, str(angle), ha='center', va='center',
                           fontsize=8, color=self.colors['construction'])
        
        # Draw baseline
        self.ax.plot([px, px + radius], [py, py], 
                   color=self.colors['construction'], linewidth=1, linestyle='--', zorder=1)


# Convenience function for direct usage
def render_grid(yaml_spec: str, output_path: Optional[str] = None, is_file: bool = True) -> str:
    """
    Render a grid construction diagram from VRS YAML specification.
    
    Args:
        yaml_spec: Path to YAML file or YAML string
        output_path: Output directory path
        is_file: Whether yaml_spec is a file path
        
    Returns:
        Path to generated PNG file
    """
    renderer = GridRenderer(output_path)
    return renderer.process(yaml_spec, is_file=is_file)