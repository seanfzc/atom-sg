"""
Isometric Renderer Module

Generates exam-quality 3D isometric diagrams including:
- Isometric cube arrangements
- Orthographic projection views (top/front/side)
- Dot grids for student construction
- Hidden edge rendering (dashed lines)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch
import numpy as np
from typing import Dict, Any, Optional, Tuple, List
try:
    from .base_renderer import BaseRenderer, MOE_COLORS, ValidationError
except ImportError:
    from base_renderer import BaseRenderer, MOE_COLORS, ValidationError


class IsometricRenderer(BaseRenderer):
    """
    Renderer for 3D isometric and orthographic diagrams.
    
    Supports VRS YAML specifications with the following structure:
    
    ```yaml
    type: isometric_3d
    title: "Cube Arrangement"
    view: isometric  # or orthographic
    grid:
      type: isometric_dot
      size: [10, 10]
      spacing: 1cm
    cubes:
      - position: [0, 0, 0]
        color: primary
      - position: [1, 0, 0]
        color: secondary
      - position: [0, 1, 0]
    orthographic_views:
      - view: top
        show: true
      - view: front
        show: true
      - view: side
        show: true
    hidden_edges: true
    ```
    """
    
    # Isometric projection constants
    ISO_ANGLE = np.radians(30)  # 30 degrees
    ISO_COS = np.cos(ISO_ANGLE)
    ISO_SIN = np.sin(ISO_ANGLE)
    
    def __init__(self, output_dir: Optional[str] = None):
        super().__init__(output_dir)
        self.cube_size = 1.0
        self.show_hidden = True
        
    def validate_spec(self, spec: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate isometric/orthographic VRS specification.
        
        Args:
            spec: Parsed YAML specification
            
        Returns:
            Tuple of (is_valid, list_of_error_messages)
        """
        errors = []
        
        # Check required fields
        if 'type' not in spec:
            errors.append("Missing required field: 'type'")
        elif spec['type'] not in ['isometric_3d', 'orthographic']:
            errors.append(f"Invalid type: {spec['type']}")
        
        # Validate view type
        view = spec.get('view', 'isometric')
        if view not in ['isometric', 'orthographic']:
            errors.append(f"Invalid view: {view}")
        
        # Validate cubes if present
        if 'cubes' in spec:
            for i, cube in enumerate(spec['cubes']):
                if 'position' not in cube:
                    errors.append(f"Cube {i}: missing 'position'")
                elif len(cube['position']) != 3:
                    errors.append(f"Cube {i}: position must be [x, y, z]")
        
        # Validate orthographic views if present
        if 'orthographic_views' in spec:
            valid_views = ['top', 'front', 'side', 'left', 'right']
            for i, view_spec in enumerate(spec['orthographic_views']):
                if 'view' not in view_spec:
                    errors.append(f"Orthographic view {i}: missing 'view'")
                elif view_spec['view'] not in valid_views:
                    errors.append(f"Orthographic view {i}: invalid view '{view_spec['view']}'")
        
        return len(errors) == 0, errors
    
    def render(self, spec: Dict[str, Any], output_filename: Optional[str] = None) -> str:
        """
        Render isometric or orthographic diagram.
        
        Args:
            spec: Validated VRS specification
            output_filename: Optional output filename
            
        Returns:
            Path to generated PNG file
        """
        view_type = spec.get('view', 'isometric')
        self.show_hidden = spec.get('hidden_edges', True)
        self.cube_size = spec.get('cube_size', 1.0)
        
        # Create figure
        if view_type == 'orthographic':
            self.fig, self.ax = plt.subplots(figsize=(12, 6), dpi=150)
        else:
            self.fig, self.ax = plt.subplots(figsize=(8, 8), dpi=150)
        
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Render based on view type
        if view_type == 'orthographic':
            self._render_orthographic(spec)
        else:
            self._render_isometric(spec)
        
        # Add title
        title = spec.get('title', '3D Visualization')
        self.ax.set_title(title, fontsize=14, fontweight='bold',
                         color=self.colors['text'], pad=20)
        
        # Save
        if output_filename is None:
            output_filename = spec.get('id', 'isometric_3d')
        
        return self.save_figure(output_filename)
    
    def _render_isometric(self, spec: Dict[str, Any]) -> None:
        """Render isometric view of cubes."""
        grid_config = spec.get('grid', {})
        grid_type = grid_config.get('type', 'isometric_dot')
        grid_size = grid_config.get('size', [10, 10])
        
        # Draw isometric grid
        if grid_type == 'isometric_dot':
            self._draw_isometric_dot_grid(grid_size)
        elif grid_type == 'isometric_line':
            self._draw_isometric_line_grid(grid_size)
        
        # Get cubes and sort by depth (back to front)
        cubes = spec.get('cubes', [])
        cubes_sorted = sorted(cubes, key=lambda c: c['position'][0] + c['position'][1] + c['position'][2])
        
        # Draw cubes
        for cube in cubes_sorted:
            self._draw_isometric_cube(cube)
    
    def _render_orthographic(self, spec: Dict[str, Any]) -> None:
        """Render orthographic projection views."""
        views = spec.get('orthographic_views', [
            {'view': 'top', 'show': True},
            {'view': 'front', 'show': True},
            {'view': 'side', 'show': True}
        ])
        
        cubes = spec.get('cubes', [])
        
        # Calculate positions for three views
        view_spacing = 5
        view_positions = {
            'top': (-view_spacing, 0),
            'front': (0, 0),
            'side': (view_spacing, 0)
        }
        
        for view_spec in views:
            if not view_spec.get('show', True):
                continue
                
            view_name = view_spec['view']
            offset = view_positions.get(view_name, (0, 0))
            
            # Draw view label
            self.ax.text(offset[0] + 2, offset[1] + 4.5, view_name.upper(),
                       ha='center', fontsize=12, fontweight='bold',
                       color=self.colors['text'])
            
            # Draw view border
            border = Rectangle((offset[0], offset[1]), 4, 4,
                             fill=False, edgecolor=self.colors['grid_major'],
                             linewidth=2, linestyle='--')
            self.ax.add_patch(border)
            
            # Draw cubes in this view
            self._draw_orthographic_view(view_name, cubes, offset)
    
    def _draw_isometric_dot_grid(self, size: List[int]) -> None:
        """Draw isometric dot grid."""
        max_x, max_y = size
        
        # Isometric grid spacing
        dx = 1.0
        dy = np.sin(np.radians(60))
        
        for row in range(max_y + 1):
            for col in range(max_x + 1):
                # Isometric projection
                x = (col - row) * dx * self.ISO_COS
                y = (col + row) * dy
                
                self.ax.plot(x, y, 'o', color=self.colors['grid_major'],
                           markersize=3, zorder=0)
    
    def _draw_isometric_line_grid(self, size: List[int]) -> None:
        """Draw isometric line grid."""
        max_x, max_y = size
        
        # Draw isometric grid lines
        for i in range(max_x + max_y + 1):
            # Lines in one direction
            x1 = (i) * self.ISO_COS
            y1 = (0) * self.ISO_SIN
            x2 = (i - max_y) * self.ISO_COS
            y2 = (max_y) * self.ISO_SIN
            
            self.ax.plot([x1, x2], [y1, y2], color=self.colors['grid_line'],
                       linewidth=0.5, zorder=0)
    
    def _draw_isometric_cube(self, cube: Dict[str, Any]) -> None:
        """Draw a single cube in isometric projection."""
        pos = cube.get('position', [0, 0, 0])
        color_key = cube.get('color', 'primary')
        
        # Get color
        if color_key in self.colors:
            fill_color = self.colors[color_key]
        else:
            fill_color = self.colors['primary']
        
        # Calculate isometric vertices
        vertices = self._calculate_isometric_cube_vertices(pos, self.cube_size)
        
        # Define faces (back to front order for proper rendering)
        faces = [
            ('back', [vertices[4], vertices[5], vertices[6], vertices[7]], True),
            ('left', [vertices[0], vertices[4], vertices[7], vertices[3]], True),
            ('bottom', [vertices[0], vertices[1], vertices[5], vertices[4]], True),
            ('right', [vertices[1], vertices[2], vertices[6], vertices[5]], False),
            ('top', [vertices[3], vertices[7], vertices[6], vertices[2]], False),
            ('front', [vertices[0], vertices[3], vertices[2], vertices[1]], False),
        ]
        
        # Draw hidden faces first (dashed)
        if self.show_hidden:
            for face_name, face_vertices, hidden in faces:
                if hidden:
                    face = Polygon(face_vertices, closed=True,
                                 facecolor=self.colors['shape_fill'],
                                 edgecolor=self.colors['hidden'],
                                 linewidth=1, linestyle='--',
                                 alpha=0.5, zorder=1)
                    self.ax.add_patch(face)
        
        # Draw visible faces
        for face_name, face_vertices, hidden in faces:
            if not hidden:
                # Vary color slightly for different faces
                if face_name == 'top':
                    face_color = fill_color
                elif face_name == 'front':
                    face_color = self._darken_color(fill_color, 0.9)
                else:  # right
                    face_color = self._darken_color(fill_color, 0.8)
                
                face = Polygon(face_vertices, closed=True,
                             facecolor=face_color,
                             edgecolor=self.colors['shape_stroke'],
                             linewidth=1.5, zorder=2)
                self.ax.add_patch(face)
    
    def _calculate_isometric_cube_vertices(self, pos: List[int], size: float) -> List[Tuple[float, float]]:
        """Calculate isometric projection vertices for a cube."""
        x, y, z = pos
        
        # Base vertices (before isometric projection)
        base_vertices = [
            (x, y, z),           # 0: front-left-bottom
            (x + size, y, z),    # 1: front-right-bottom
            (x + size, y + size, z),  # 2: back-right-bottom
            (x, y + size, z),    # 3: back-left-bottom
            (x, y, z + size),    # 4: front-left-top
            (x + size, y, z + size),  # 5: front-right-top
            (x + size, y + size, z + size),  # 6: back-right-top
            (x, y + size, z + size),  # 7: back-left-top
        ]
        
        # Apply isometric projection
        projected = []
        for vx, vy, vz in base_vertices:
            # Isometric projection formulas
            iso_x = (vx - vy) * self.ISO_COS
            iso_y = (vx + vy) * self.ISO_SIN + vz * 0.5
            projected.append((iso_x, iso_y))
        
        return projected
    
    def _draw_orthographic_view(self, view_name: str, cubes: List[Dict], 
                                offset: Tuple[float, float]) -> None:
        """Draw orthographic projection of cubes."""
        ox, oy = offset
        
        # Determine projection based on view
        if view_name == 'top':
            # Project onto XY plane (looking down Z)
            projected_cubes = []
            for cube in cubes:
                pos = cube['position']
                projected_cubes.append({
                    'x': pos[0],
                    'y': pos[1],
                    'color': cube.get('color', 'primary')
                })
        elif view_name == 'front':
            # Project onto XZ plane (looking down Y)
            projected_cubes = []
            for cube in cubes:
                pos = cube['position']
                projected_cubes.append({
                    'x': pos[0],
                    'y': pos[2],
                    'color': cube.get('color', 'primary')
                })
        else:  # side (right side, looking down X)
            # Project onto YZ plane
            projected_cubes = []
            for cube in cubes:
                pos = cube['position']
                projected_cubes.append({
                    'x': pos[1],
                    'y': pos[2],
                    'color': cube.get('color', 'primary')
                })
        
        # Draw projected cubes
        for cube in projected_cubes:
            color_key = cube['color']
            fill_color = self.colors.get(color_key, self.colors['primary'])
            
            rect = Rectangle((ox + cube['x'], oy + cube['y']), 
                           1, 1,
                           facecolor=fill_color,
                           edgecolor=self.colors['shape_stroke'],
                           linewidth=1.5)
            self.ax.add_patch(rect)
    
    def _darken_color(self, hex_color: str, factor: float) -> str:
        """Darken a hex color by a factor."""
        # Convert hex to RGB
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        # Darken
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        
        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"


# Convenience function for direct usage
def render_isometric(yaml_spec: str, output_path: Optional[str] = None, is_file: bool = True) -> str:
    """
    Render an isometric/orthographic diagram from VRS YAML specification.
    
    Args:
        yaml_spec: Path to YAML file or YAML string
        output_path: Output directory path
        is_file: Whether yaml_spec is a file path
        
    Returns:
        Path to generated PNG file
    """
    renderer = IsometricRenderer(output_path)
    return renderer.process(yaml_spec, is_file=is_file)