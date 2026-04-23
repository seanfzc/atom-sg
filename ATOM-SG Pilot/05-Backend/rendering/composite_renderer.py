"""
Composite Renderer Module

Generates exam-quality composite shape diagrams including:
- Overlapping quarter circles and sectors
- Shaded intersection regions with diagonal hatching
- Reflex angle arcs (>180°)
- Multi-shape composites (rhombus + trapezium)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Arc, Wedge, Circle, PathPatch, Path
import numpy as np
from typing import Dict, Any, Optional, Tuple, List
try:
    from .base_renderer import BaseRenderer, MOE_COLORS, ValidationError
except ImportError:
    from base_renderer import BaseRenderer, MOE_COLORS, ValidationError


class CompositeRenderer(BaseRenderer):
    """
    Renderer for composite shape diagrams.
    
    Supports VRS YAML specifications with the following structure:
    
    ```yaml
    type: composite_shapes
    title: "Overlapping Quarter Circles"
    shapes:
      - type: quarter_circle
        center: [0, 0]
        radius: 4
        quadrant: 1  # 1, 2, 3, or 4
        fill_color: primary
      - type: sector
        center: [4, 0]
        radius: 4
        start_angle: 90
        end_angle: 180
        fill_color: secondary
    intersections:
      - shapes: [0, 1]
        hatching: true
        label: "shaded region"
    reflex_angles:
      - vertex: [0, 0]
        angle: 270
        label: "reflex ∠A"
    multi_shapes:
      - type: rhombus_trapezium
        rhombus:
          center: [2, 2]
          diagonal1: 6
          diagonal2: 4
        trapezium:
          vertices: [[0,0], [6,0], [5,3], [1,3]]
    ```
    """
    
    def __init__(self, output_dir: Optional[str] = None):
        super().__init__(output_dir)
        
    def validate_spec(self, spec: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate composite shapes VRS specification.
        
        Args:
            spec: Parsed YAML specification
            
        Returns:
            Tuple of (is_valid, list_of_error_messages)
        """
        errors = []
        
        # Check required fields
        if 'type' not in spec:
            errors.append("Missing required field: 'type'")
        elif spec['type'] != 'composite_shapes':
            errors.append(f"Invalid type: {spec['type']}, expected 'composite_shapes'")
        
        # Validate shapes if present
        if 'shapes' in spec:
            valid_types = ['quarter_circle', 'semicircle', 'sector', 'circle', 
                          'triangle', 'rectangle', 'rhombus', 'trapezium']
            for i, shape in enumerate(spec['shapes']):
                if 'type' not in shape:
                    errors.append(f"Shape {i}: missing 'type'")
                elif shape['type'] not in valid_types:
                    errors.append(f"Shape {i}: invalid type '{shape['type']}'")
                
                if shape.get('type') in ['quarter_circle', 'sector', 'circle']:
                    if 'center' not in shape:
                        errors.append(f"Shape {i}: missing 'center'")
                    if 'radius' not in shape:
                        errors.append(f"Shape {i}: missing 'radius'")
        
        # Validate reflex angles if present
        if 'reflex_angles' in spec:
            for i, angle in enumerate(spec['reflex_angles']):
                if 'vertex' not in angle:
                    errors.append(f"Reflex angle {i}: missing 'vertex'")
                if 'angle' not in angle:
                    errors.append(f"Reflex angle {i}: missing 'angle'")
                elif angle['angle'] <= 180:
                    errors.append(f"Reflex angle {i}: angle must be > 180°")
        
        return len(errors) == 0, errors
    
    def render(self, spec: Dict[str, Any], output_filename: Optional[str] = None) -> str:
        """
        Render composite shape diagram.
        
        Args:
            spec: Validated VRS specification
            output_filename: Optional output filename
            
        Returns:
            Path to generated PNG file
        """
        # Create figure
        self.fig, self.ax = plt.subplots(figsize=(8, 8), dpi=150)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Set default limits (will be adjusted based on shapes)
        self.ax.set_xlim(-1, 10)
        self.ax.set_ylim(-1, 10)
        
        # Draw shapes
        shapes = spec.get('shapes', [])
        shape_objects = []
        for shape in shapes:
            shape_obj = self._draw_shape(shape)
            shape_objects.append(shape_obj)
        
        # Draw intersections with hatching
        intersections = spec.get('intersections', [])
        for intersection in intersections:
            self._draw_intersection(intersection, shape_objects)
        
        # Draw reflex angles
        reflex_angles = spec.get('reflex_angles', [])
        for angle in reflex_angles:
            self._draw_reflex_angle(angle)
        
        # Draw multi-shape composites
        multi_shapes = spec.get('multi_shapes', [])
        for multi in multi_shapes:
            self._draw_multi_shape(multi)
        
        # Add title
        title = spec.get('title', 'Composite Shapes')
        self.ax.set_title(title, fontsize=14, fontweight='bold',
                         color=self.colors['text'], pad=20)
        
        # Add dimensions/labels if specified
        labels = spec.get('labels', [])
        for label in labels:
            self._draw_label(label)
        
        # Auto-adjust limits with padding
        self.ax.autoscale_view()
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        padding = 0.5
        self.ax.set_xlim(xlim[0] - padding, xlim[1] + padding)
        self.ax.set_ylim(ylim[0] - padding, ylim[1] + padding)
        
        # Save
        if output_filename is None:
            output_filename = spec.get('id', 'composite_shapes')
        
        return self.save_figure(output_filename)
    
    def _draw_shape(self, shape: Dict[str, Any]) -> Dict[str, Any]:
        """Draw a single shape and return its geometric info."""
        shape_type = shape.get('type', '')
        fill_color = shape.get('fill_color', 'primary')
        stroke_color = shape.get('stroke_color', 'shape_stroke')
        
        # Get actual colors
        fill = self.colors.get(fill_color, self.colors['primary'])
        stroke = self.colors.get(stroke_color, self.colors['shape_stroke'])
        
        shape_obj = {'type': shape_type, 'params': shape}
        
        if shape_type == 'quarter_circle':
            center = shape.get('center', [0, 0])
            radius = shape.get('radius', 1)
            quadrant = shape.get('quadrant', 1)
            
            # Determine angles based on quadrant
            angle_map = {1: (0, 90), 2: (90, 180), 3: (180, 270), 4: (270, 360)}
            start, end = angle_map.get(quadrant, (0, 90))
            
            wedge = Wedge(center, radius, start, end,
                         facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(wedge)
            
            # Draw radii
            rad1 = (center[0] + radius * np.cos(np.radians(start)),
                   center[1] + radius * np.sin(np.radians(start)))
            rad2 = (center[0] + radius * np.cos(np.radians(end)),
                   center[1] + radius * np.sin(np.radians(end)))
            
            self.ax.plot([center[0], rad1[0]], [center[1], rad1[1]], 
                       color=stroke, linewidth=2, zorder=2)
            self.ax.plot([center[0], rad2[0]], [center[1], rad2[1]], 
                       color=stroke, linewidth=2, zorder=2)
            
            shape_obj['geometry'] = {'center': center, 'radius': radius, 
                                    'start': start, 'end': end}
            
        elif shape_type == 'semicircle':
            center = shape.get('center', [0, 0])
            radius = shape.get('radius', 1)
            orientation = shape.get('orientation', 'up')  # up, down, left, right
            
            angle_map = {'up': (0, 180), 'down': (180, 360), 
                        'left': (90, 270), 'right': (-90, 90)}
            start, end = angle_map.get(orientation, (0, 180))
            
            wedge = Wedge(center, radius, start, end,
                         facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(wedge)
            
            # Draw diameter
            rad1 = (center[0] + radius * np.cos(np.radians(start)),
                   center[1] + radius * np.sin(np.radians(start)))
            rad2 = (center[0] + radius * np.cos(np.radians(end)),
                   center[1] + radius * np.sin(np.radians(end)))
            
            self.ax.plot([rad1[0], rad2[0]], [rad1[1], rad2[1]], 
                       color=stroke, linewidth=2, zorder=2)
            
            shape_obj['geometry'] = {'center': center, 'radius': radius,
                                    'start': start, 'end': end}
            
        elif shape_type == 'sector':
            center = shape.get('center', [0, 0])
            radius = shape.get('radius', 1)
            start_angle = shape.get('start_angle', 0)
            end_angle = shape.get('end_angle', 90)
            
            wedge = Wedge(center, radius, start_angle, end_angle,
                         facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(wedge)
            
            # Draw radii
            rad1 = (center[0] + radius * np.cos(np.radians(start_angle)),
                   center[1] + radius * np.sin(np.radians(start_angle)))
            rad2 = (center[0] + radius * np.cos(np.radians(end_angle)),
                   center[1] + radius * np.sin(np.radians(end_angle)))
            
            self.ax.plot([center[0], rad1[0]], [center[1], rad1[1]], 
                       color=stroke, linewidth=2, zorder=2)
            self.ax.plot([center[0], rad2[0]], [center[1], rad2[1]], 
                       color=stroke, linewidth=2, zorder=2)
            
            shape_obj['geometry'] = {'center': center, 'radius': radius,
                                    'start': start_angle, 'end': end_angle}
            
        elif shape_type == 'circle':
            center = shape.get('center', [0, 0])
            radius = shape.get('radius', 1)
            
            circle = Circle(center, radius,
                          facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(circle)
            
            shape_obj['geometry'] = {'center': center, 'radius': radius}
            
        elif shape_type == 'triangle':
            vertices = shape.get('vertices', [[0, 0], [1, 0], [0.5, 1]])
            
            triangle = Polygon(vertices, closed=True,
                             facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(triangle)
            
            shape_obj['geometry'] = {'vertices': vertices}
            
        elif shape_type == 'rectangle':
            xy = shape.get('xy', [0, 0])
            width = shape.get('width', 1)
            height = shape.get('height', 1)
            
            rect = patches.Rectangle(xy, width, height,
                                    facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(rect)
            
            shape_obj['geometry'] = {'xy': xy, 'width': width, 'height': height}
            
        elif shape_type == 'rhombus':
            center = shape.get('center', [0, 0])
            diagonal1 = shape.get('diagonal1', 2)
            diagonal2 = shape.get('diagonal2', 2)
            
            # Rhombus vertices
            vertices = [
                [center[0], center[1] + diagonal2/2],
                [center[0] + diagonal1/2, center[1]],
                [center[0], center[1] - diagonal2/2],
                [center[0] - diagonal1/2, center[1]]
            ]
            
            rhombus = Polygon(vertices, closed=True,
                            facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(rhombus)
            
            shape_obj['geometry'] = {'vertices': vertices}
            
        elif shape_type == 'trapezium':
            vertices = shape.get('vertices', [[0, 0], [2, 0], [1.5, 1], [0.5, 1]])
            
            trapezium = Polygon(vertices, closed=True,
                              facecolor=fill, edgecolor=stroke, linewidth=2, zorder=1)
            self.ax.add_patch(trapezium)
            
            shape_obj['geometry'] = {'vertices': vertices}
        
        return shape_obj
    
    def _draw_intersection(self, intersection: Dict[str, Any], 
                          shape_objects: List[Dict]) -> None:
        """Draw hatching in intersection region of shapes."""
        shape_indices = intersection.get('shapes', [])
        label = intersection.get('label', '')
        
        if len(shape_indices) < 2:
            return
        
        # Get the intersecting shapes
        shape1 = shape_objects[shape_indices[0]]
        shape2 = shape_objects[shape_indices[1]]
        
        # For now, approximate intersection as bounding box overlap
        # In a full implementation, this would use proper polygon intersection
        
        # Calculate approximate intersection region
        geom1 = shape1.get('geometry', {})
        geom2 = shape2.get('geometry', {})
        
        if 'center' in geom1 and 'center' in geom2 and 'radius' in geom1:
            # Circle/circle or circle/sector intersection
            c1 = geom1['center']
            c2 = geom2['center']
            r = geom1['radius']
            
            # Approximate intersection as polygon
            # For quarter circles meeting at a point
            if shape1['type'] == 'quarter_circle' and shape2['type'] == 'quarter_circle':
                # Intersection is a lens shape - approximate with polygon
                angles = np.linspace(0, 90, 20)
                vertices1 = [(c1[0] + r * np.cos(np.radians(a)),
                            c1[1] + r * np.sin(np.radians(a))) for a in angles]
                
                angles2 = np.linspace(90, 180, 20)
                vertices2 = [(c2[0] + r * np.cos(np.radians(a)),
                            c2[1] + r * np.sin(np.radians(a))) for a in angles2]
                
                vertices = vertices1 + vertices2
                
                # Draw hatching
                self._draw_hatching_in_region(vertices, label)
    
    def _draw_hatching_in_region(self, vertices: List[Tuple[float, float]], 
                                 label: str = '') -> None:
        """Draw diagonal hatching pattern in a region."""
        if not vertices:
            return
        
        # Convert to numpy array
        poly = np.array(vertices)
        
        # Get bounding box
        x_min, y_min = poly.min(axis=0)
        x_max, y_max = poly.max(axis=0)
        
        # Draw diagonal hatching lines
        spacing = 0.25
        angle = 45
        angle_rad = np.radians(angle)
        cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)
        
        # Calculate range for line origins
        diag_min = x_min * cos_a + y_min * sin_a
        diag_max = x_max * cos_a + y_max * sin_a
        
        for d in np.arange(diag_min, diag_max, spacing):
            # Find intersection with bounding box
            points = []
            
            # Left edge
            if abs(sin_a) > 1e-6:
                y = (d - x_min * cos_a) / sin_a
                if y_min <= y <= y_max:
                    points.append((x_min, y))
            
            # Right edge
            if abs(sin_a) > 1e-6:
                y = (d - x_max * cos_a) / sin_a
                if y_min <= y <= y_max:
                    points.append((x_max, y))
            
            # Bottom edge
            if abs(cos_a) > 1e-6:
                x = (d - y_min * sin_a) / cos_a
                if x_min <= x <= x_max:
                    points.append((x, y_min))
            
            # Top edge
            if abs(cos_a) > 1e-6:
                x = (d - y_max * sin_a) / cos_a
                if x_min <= x <= x_max:
                    points.append((x, y_max))
            
            if len(points) >= 2:
                self.ax.plot([points[0][0], points[1][0]], 
                           [points[0][1], points[1][1]],
                           color=self.colors['hatching'], linewidth=1.5, alpha=0.7, zorder=3)
        
        # Add label if provided
        if label:
            center_x = (x_min + x_max) / 2
            center_y = (y_min + y_max) / 2
            self.ax.text(center_x, center_y, label, ha='center', va='center',
                       fontsize=10, color=self.colors['text'],
                       bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor=self.colors['highlight'],
                                edgecolor=self.colors['border']))
    
    def _draw_reflex_angle(self, angle_spec: Dict[str, Any]) -> None:
        """Draw a reflex angle (>180°)."""
        vertex = angle_spec.get('vertex', [0, 0])
        angle = angle_spec.get('angle', 270)
        label = angle_spec.get('label', f'{angle}°')
        radius = angle_spec.get('radius', 1.5)
        
        # Draw the reflex arc (outer arc)
        # Reflex angle goes the "long way" around
        start_angle = 0
        end_angle = angle
        
        # Draw outer arc
        arc = Arc(vertex, radius * 2, radius * 2,
                 angle=0, theta1=start_angle, theta2=end_angle,
                 color=self.colors['construction'], linewidth=2, zorder=3)
        self.ax.add_patch(arc)
        
        # Draw inner arc (the acute/obtuse angle)
        inner_arc = Arc(vertex, radius * 0.6, radius * 0.6,
                       angle=end_angle, theta1=0, theta2=360-angle,
                       color=self.colors['shape_stroke'], linewidth=1.5, linestyle='--', zorder=3)
        self.ax.add_patch(inner_arc)
        
        # Draw angle arms
        arm1_end = (vertex[0] + radius * 1.5, vertex[1])
        arm2_end = (vertex[0] + radius * 1.5 * np.cos(np.radians(angle)),
                   vertex[1] + radius * 1.5 * np.sin(np.radians(angle)))
        
        self.ax.plot([vertex[0], arm1_end[0]], [vertex[1], arm1_end[1]],
                   color=self.colors['shape_stroke'], linewidth=2, zorder=2)
        self.ax.plot([vertex[0], arm2_end[0]], [vertex[1], arm2_end[1]],
                   color=self.colors['shape_stroke'], linewidth=2, zorder=2)
        
        # Add label
        mid_angle = np.radians(angle / 2)
        label_x = vertex[0] + (radius + 0.5) * np.cos(mid_angle)
        label_y = vertex[1] + (radius + 0.5) * np.sin(mid_angle)
        self.ax.text(label_x, label_y, label, ha='center', va='center',
                   fontsize=11, fontweight='bold', color=self.colors['text'],
                   bbox=dict(boxstyle='round,pad=0.3', 
                            facecolor=self.colors['highlight'],
                            edgecolor=self.colors['construction']))
    
    def _draw_multi_shape(self, multi: Dict[str, Any]) -> None:
        """Draw multi-shape composite (e.g., rhombus + trapezium)."""
        multi_type = multi.get('type', '')
        
        if multi_type == 'rhombus_trapezium':
            rhombus = multi.get('rhombus', {})
            trapezium = multi.get('trapezium', {})
            
            # Draw rhombus
            center = rhombus.get('center', [2, 2])
            d1 = rhombus.get('diagonal1', 6)
            d2 = rhombus.get('diagonal2', 4)
            
            rhombus_vertices = [
                [center[0], center[1] + d2/2],
                [center[0] + d1/2, center[1]],
                [center[0], center[1] - d2/2],
                [center[0] - d1/2, center[1]]
            ]
            
            rhombus_poly = Polygon(rhombus_vertices, closed=True,
                                  facecolor=self.colors['primary'],
                                  edgecolor=self.colors['shape_stroke'],
                                  linewidth=2, alpha=0.6, zorder=1)
            self.ax.add_patch(rhombus_poly)
            
            # Draw trapezium
            vertices = trapezium.get('vertices', [[0, 0], [6, 0], [5, 3], [1, 3]])
            
            trapezium_poly = Polygon(vertices, closed=True,
                                   facecolor=self.colors['secondary'],
                                   edgecolor=self.colors['shape_stroke'],
                                   linewidth=2, alpha=0.6, zorder=2)
            self.ax.add_patch(trapezium_poly)
            
            # Label vertices
            labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            for i, (vx, vy) in enumerate(vertices):
                offset = 0.3
                self.ax.text(vx + offset, vy + offset, labels[i % len(labels)],
                           ha='center', va='center', fontsize=10, fontweight='bold',
                           color=self.colors['text'],
                           bbox=dict(boxstyle='circle,pad=0.1', facecolor='white',
                                    edgecolor=self.colors['shape_stroke']))
    
    def _draw_label(self, label: Dict[str, Any]) -> None:
        """Draw a label at specified position."""
        x = label.get('x', 0)
        y = label.get('y', 0)
        text = label.get('text', '')
        
        self.ax.text(x, y, text, ha='center', va='center',
                   fontsize=10, color=self.colors['text'],
                   bbox=dict(boxstyle='round,pad=0.2',
                            facecolor=self.colors['highlight'],
                            edgecolor=self.colors['border']))


# Convenience function for direct usage
def render_composite(yaml_spec: str, output_path: Optional[str] = None, is_file: bool = True) -> str:
    """
    Render a composite shape diagram from VRS YAML specification.
    
    Args:
        yaml_spec: Path to YAML file or YAML string
        output_path: Output directory directory path
        is_file: Whether yaml_spec is a file path
        
    Returns:
        Path to generated PNG file
    """
    renderer = CompositeRenderer(output_path)
    return renderer.process(yaml_spec, is_file=is_file)