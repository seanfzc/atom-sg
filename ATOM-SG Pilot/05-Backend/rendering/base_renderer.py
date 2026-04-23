"""
Base renderer class for all geometry renderers.
Provides common functionality for VRS YAML parsing, validation, and output generation.
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Rectangle, Circle, Arc, Wedge, FancyBboxPatch
import numpy as np
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List
from abc import ABC, abstractmethod
import warnings

# MOE Pastel Color Scheme
MOE_COLORS = {
    'primary': '#A8D8EA',      # Light blue
    'secondary': '#AA96DA',    # Light purple
    'accent': '#FCBAD3',       # Light pink
    'highlight': '#FFFFD2',    # Light yellow
    'border': '#95E1D3',       # Mint green
    'text': '#2C3E50',         # Dark gray
    'shape_fill': '#E8F4F8',   # Very light blue
    'shape_stroke': '#5F9EA0', # Cadet blue
    'grid_line': '#D0E0E3',    # Light grid lines
    'grid_major': '#A0C0C3',   # Darker grid lines
    'construction': '#FF6B6B', # Construction lines (red)
    'hidden': '#B0B0B0',       # Hidden/dashed lines
    'hatching': '#87CEEB',     # Diagonal hatching
    'white': '#FFFFFF',
    'black': '#000000',
}

# Standard DPI for exam-quality output
OUTPUT_DPI = 150

# Standard figure sizes (in inches)
FIGURE_SIZES = {
    'small': (4, 4),      # Simple diagrams
    'medium': (6, 6),     # Standard diagrams
    'large': (8, 6),      # Complex diagrams
    'wide': (10, 6),      # Line graphs, wide diagrams
}


class ValidationError(Exception):
    """Raised when VRS specification validation fails."""
    pass


class BaseRenderer(ABC):
    """
    Abstract base class for all geometry renderers.
    
    Subclasses must implement:
        - validate_spec(): Validate VRS YAML specification
        - render(): Generate the diagram
    """
    
    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize the renderer.
        
        Args:
            output_dir: Directory for output files. If None, uses current directory.
        """
        self.output_dir = Path(output_dir) if output_dir else Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.colors = MOE_COLORS
        self.fig = None
        self.ax = None
        
    def load_vrs_yaml(self, yaml_path: str) -> Dict[str, Any]:
        """
        Load and parse VRS YAML specification file.
        
        Args:
            yaml_path: Path to YAML file
            
        Returns:
            Parsed YAML content as dictionary
            
        Raises:
            FileNotFoundError: If YAML file doesn't exist
            yaml.YAMLError: If YAML parsing fails
        """
        path = Path(yaml_path)
        if not path.exists():
            raise FileNotFoundError(f"VRS YAML file not found: {yaml_path}")
            
        with open(path, 'r') as f:
            spec = yaml.safe_load(f)
            
        return spec
    
    def load_vrs_string(self, yaml_string: str) -> Dict[str, Any]:
        """
        Parse VRS YAML from string.
        
        Args:
            yaml_string: YAML content as string
            
        Returns:
            Parsed YAML content as dictionary
        """
        return yaml.safe_load(yaml_string)
    
    @abstractmethod
    def validate_spec(self, spec: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate VRS YAML specification.
        
        Args:
            spec: Parsed YAML specification
            
        Returns:
            Tuple of (is_valid, list_of_error_messages)
        """
        pass
    
    @abstractmethod
    def render(self, spec: Dict[str, Any], output_filename: Optional[str] = None) -> str:
        """
        Render the diagram based on specification.
        
        Args:
            spec: Parsed YAML specification
            output_filename: Optional output filename (without extension)
            
        Returns:
            Path to generated PNG file
        """
        pass
    
    def create_figure(self, size: str = 'medium', dpi: int = OUTPUT_DPI) -> Tuple[plt.Figure, plt.Axes]:
        """
        Create a new figure with standard settings.
        
        Args:
            size: Figure size key from FIGURE_SIZES
            dpi: Output DPI
            
        Returns:
            Tuple of (figure, axes)
        """
        figsize = FIGURE_SIZES.get(size, FIGURE_SIZES['medium'])
        self.fig, self.ax = plt.subplots(figsize=figsize, dpi=dpi)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        return self.fig, self.ax
    
    def save_figure(self, filename: str, dpi: int = OUTPUT_DPI) -> str:
        """
        Save the current figure to PNG.
        
        Args:
            filename: Output filename (without extension)
            dpi: Output DPI
            
        Returns:
            Full path to saved file
        """
        if self.fig is None:
            raise RuntimeError("No figure to save. Call create_figure() first.")
            
        output_path = self.output_dir / f"{filename}.png"
        self.fig.savefig(output_path, format='png', dpi=dpi, 
                        bbox_inches='tight', facecolor='white', edgecolor='none')
        plt.close(self.fig)
        self.fig = None
        self.ax = None
        return str(output_path)
    
    def draw_grid(self, ax: plt.Axes, xlim: Tuple[float, float], 
                  ylim: Tuple[float, float], 
                  spacing: float = 1.0,
                  major_spacing: Optional[float] = None,
                  show_labels: bool = False) -> None:
        """
        Draw a grid on the axes.
        
        Args:
            ax: Matplotlib axes
            xlim: (min, max) x limits
            ylim: (min, max) y limits
            spacing: Grid line spacing
            major_spacing: Major grid line spacing (optional)
            show_labels: Whether to show axis labels
        """
        # Set limits
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # Draw minor grid lines
        x_min, x_max = xlim
        y_min, y_max = ylim
        
        for x in np.arange(np.ceil(x_min / spacing) * spacing, x_max + spacing, spacing):
            ax.axvline(x, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
        
        for y in np.arange(np.ceil(y_min / spacing) * spacing, y_max + spacing, spacing):
            ax.axhline(y, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
        
        # Draw major grid lines
        if major_spacing:
            for x in np.arange(np.ceil(x_min / major_spacing) * major_spacing, x_max + major_spacing, major_spacing):
                ax.axvline(x, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
            
            for y in np.arange(np.ceil(y_min / major_spacing) * major_spacing, y_max + major_spacing, major_spacing):
                ax.axhline(y, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
        
        if show_labels:
            ax.set_xticks(np.arange(x_min, x_max + spacing, spacing))
            ax.set_yticks(np.arange(y_min, y_max + spacing, spacing))
            ax.tick_params(axis='both', which='major', labelsize=8)
    
    def draw_angle_arc(self, ax: plt.Axes, center: Tuple[float, float], 
                       radius: float, start_angle: float, end_angle: float,
                       color: Optional[str] = None, linewidth: float = 1.5,
                       label: Optional[str] = None, label_offset: float = 1.2) -> None:
        """
        Draw an angle arc.
        
        Args:
            ax: Matplotlib axes
            center: (x, y) center point
            radius: Arc radius
            start_angle: Starting angle in degrees
            end_angle: Ending angle in degrees
            color: Arc color
            linewidth: Line width
            label: Optional angle label
            label_offset: Multiplier for label position
        """
        color = color or self.colors['shape_stroke']
        
        arc = Arc(center, radius * 2, radius * 2, 
                 angle=0, theta1=start_angle, theta2=end_angle,
                 color=color, linewidth=linewidth, zorder=2)
        ax.add_patch(arc)
        
        if label:
            mid_angle = np.radians((start_angle + end_angle) / 2)
            label_x = center[0] + radius * label_offset * np.cos(mid_angle)
            label_y = center[1] + radius * label_offset * np.sin(mid_angle)
            ax.text(label_x, label_y, label, ha='center', va='center',
                   fontsize=10, color=self.colors['text'],
                   bbox=dict(boxstyle='round,pad=0.2', 
                            facecolor=self.colors['highlight'], 
                            edgecolor='none', alpha=0.9))
    
    def draw_dimension_line(self, ax: plt.Axes, p1: Tuple[float, float], 
                           p2: Tuple[float, float], 
                           label: Optional[str] = None,
                           offset: float = 0.3,
                           color: Optional[str] = None) -> None:
        """
        Draw a dimension line with optional label.
        
        Args:
            ax: Matplotlib axes
            p1: Start point (x, y)
            p2: End point (x, y)
            label: Dimension label
            offset: Perpendicular offset for dimension line
            color: Line color
        """
        color = color or self.colors['text']
        
        # Calculate perpendicular direction
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = np.sqrt(dx**2 + dy**2)
        
        if length > 0:
            perp_x = -dy / length * offset
            perp_y = dx / length * offset
            
            # Offset points
            p1_offset = (p1[0] + perp_x, p1[1] + perp_y)
            p2_offset = (p2[0] + perp_x, p2[1] + perp_y)
            
            # Draw dimension line
            ax.plot([p1_offset[0], p2_offset[0]], 
                   [p1_offset[1], p2_offset[1]], 
                   color=color, linewidth=1, zorder=3)
            
            # Draw tick marks
            tick_len = 0.15
            for p in [p1_offset, p2_offset]:
                ax.plot([p[0] - tick_len * dy/length, p[0] + tick_len * dy/length],
                       [p[1] + tick_len * dx/length, p[1] - tick_len * dx/length],
                       color=color, linewidth=1, zorder=3)
            
            # Add label
            if label:
                mid_x = (p1_offset[0] + p2_offset[0]) / 2
                mid_y = (p1_offset[1] + p2_offset[1]) / 2
                ax.text(mid_x, mid_y, label, ha='center', va='center',
                       fontsize=9, color=color,
                       bbox=dict(boxstyle='round,pad=0.15', 
                                facecolor='white', edgecolor='none', alpha=0.9))
    
    def draw_hatching(self, ax: plt.Axes, vertices: List[Tuple[float, float]],
                     spacing: float = 0.3, angle: float = 45,
                     color: Optional[str] = None) -> None:
        """
        Draw diagonal hatching pattern in a polygon.
        
        Args:
            ax: Matplotlib axes
            vertices: List of (x, y) vertices defining the region
            spacing: Distance between hatch lines
            angle: Hatching angle in degrees
            color: Hatching color
        """
        color = color or self.colors['hatching']
        
        # Convert to numpy array
        poly = np.array(vertices)
        
        # Get bounding box
        x_min, y_min = poly.min(axis=0)
        x_max, y_max = poly.max(axis=0)
        
        # Create diagonal lines
        angle_rad = np.radians(angle)
        cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)
        
        # Calculate range for line origins
        diag_min = x_min * cos_a + y_min * sin_a
        diag_max = x_max * cos_a + y_max * sin_a
        
        for d in np.arange(diag_min, diag_max, spacing):
            # Line: x*cos_a + y*sin_a = d
            # Intersect with bounding box
            points = []
            
            # Left edge (x = x_min)
            if abs(sin_a) > 1e-6:
                y = (d - x_min * cos_a) / sin_a
                if y_min <= y <= y_max:
                    points.append((x_min, y))
            
            # Right edge (x = x_max)
            if abs(sin_a) > 1e-6:
                y = (d - x_max * cos_a) / sin_a
                if y_min <= y <= y_max:
                    points.append((x_max, y))
            
            # Bottom edge (y = y_min)
            if abs(cos_a) > 1e-6:
                x = (d - y_min * sin_a) / cos_a
                if x_min <= x <= x_max:
                    points.append((x, y_min))
            
            # Top edge (y = y_max)
            if abs(cos_a) > 1e-6:
                x = (d - y_max * sin_a) / cos_a
                if x_min <= x <= x_max:
                    points.append((x, y_max))
            
            if len(points) >= 2:
                ax.plot([points[0][0], points[1][0]], 
                       [points[0][1], points[1][1]],
                       color=color, linewidth=0.8, alpha=0.6, zorder=1)
    
    def add_title(self, ax: plt.Axes, title: str, subtitle: Optional[str] = None) -> None:
        """
        Add title to the diagram.
        
        Args:
            ax: Matplotlib axes
            title: Main title
            subtitle: Optional subtitle
        """
        if subtitle:
            full_title = f"{title}\n{subtitle}"
            ax.set_title(full_title, fontsize=12, fontweight='bold',
                        color=self.colors['text'], pad=15)
        else:
            ax.set_title(title, fontsize=14, fontweight='bold',
                        color=self.colors['text'], pad=15)
    
    def add_label(self, ax: plt.Axes, x: float, y: float, text: str,
                 ha: str = 'center', va: str = 'center',
                 fontsize: int = 10, color: Optional[str] = None,
                 box: bool = True) -> None:
        """
        Add a text label to the diagram.
        
        Args:
            ax: Matplotlib axes
            x: X position
            y: Y position
            text: Label text
            ha: Horizontal alignment
            va: Vertical alignment
            fontsize: Font size
            color: Text color
            box: Whether to add background box
        """
        color = color or self.colors['text']
        
        if box:
            ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize, color=color,
                   bbox=dict(boxstyle='round,pad=0.2', 
                            facecolor=self.colors['highlight'],
                            edgecolor=self.colors['border'], alpha=0.9))
        else:
            ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize, color=color)
    
    def process(self, yaml_input: str, output_filename: Optional[str] = None,
               is_file: bool = True) -> str:
        """
        Complete processing pipeline: load, validate, render, save.
        
        Args:
            yaml_input: Path to YAML file or YAML string
            output_filename: Optional output filename
            is_file: Whether yaml_input is a file path
            
        Returns:
            Path to generated PNG file
        """
        # Load specification
        if is_file:
            spec = self.load_vrs_yaml(yaml_input)
            if output_filename is None:
                output_filename = Path(yaml_input).stem
        else:
            spec = self.load_vrs_string(yaml_input)
            if output_filename is None:
                output_filename = 'output'
        
        # Validate
        is_valid, errors = self.validate_spec(spec)
        if not is_valid:
            raise ValidationError(f"Validation failed: {'; '.join(errors)}")
        
        # Render
        return self.render(spec, output_filename)