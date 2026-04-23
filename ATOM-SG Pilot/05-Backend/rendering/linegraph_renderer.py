"""
Line Graph Renderer Module

Generates exam-quality data interpretation diagrams including:
- Line graphs with grid backgrounds
- Cumulative data visualization
- Rate of change highlighting
- Reverse calculation prompts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
import numpy as np
from typing import Dict, Any, Optional, Tuple, List
try:
    from .base_renderer import BaseRenderer, MOE_COLORS, ValidationError
except ImportError:
    from base_renderer import BaseRenderer, MOE_COLORS, ValidationError


class LineGraphRenderer(BaseRenderer):
    """
    Renderer for line graph data interpretation diagrams.
    
    Supports VRS YAML specifications with the following structure:
    
    ```yaml
    type: line_graph
    title: "Water Tank Volume Over Time"
    grid:
      x_range: [0, 10]
      y_range: [0, 100]
      x_unit: "hours"
      y_unit: "litres"
      x_major: 2
      y_major: 20
    axes:
      x_label: "Time (hours)"
      y_label: "Volume (L)"
    data_series:
      - name: "Tank A"
        type: line
        points: [[0,0], [2,20], [4,50], [6,80], [8,90], [10,100]]
        color: primary
        show_points: true
      - name: "Tank B"
        type: cumulative
        points: [[0,0], [2,15], [4,35], [6,55], [8,70], [10,85]]
        color: secondary
    highlights:
      - type: rate_of_change
        interval: [2, 4]
        label: "Fastest fill rate"
      - type: reverse_calculation
        question: "When did Tank A reach 50L?"
        answer_x: 4
    annotations:
      - x: 4
        y: 50
        text: "50L"
        arrow: true
    ```
    """
    
    def __init__(self, output_dir: Optional[str] = None):
        super().__init__(output_dir)
        
    def validate_spec(self, spec: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate line graph VRS specification.
        
        Args:
            spec: Parsed YAML specification
            
        Returns:
            Tuple of (is_valid, list_of_error_messages)
        """
        errors = []
        
        # Check required fields
        if 'type' not in spec:
            errors.append("Missing required field: 'type'")
        elif spec['type'] != 'line_graph':
            errors.append(f"Invalid type: {spec['type']}, expected 'line_graph'")
        
        # Validate grid configuration
        if 'grid' not in spec:
            errors.append("Missing required field: 'grid'")
        else:
            grid = spec['grid']
            if 'x_range' not in grid:
                errors.append("Missing grid.x_range")
            if 'y_range' not in grid:
                errors.append("Missing grid.y_range")
        
        # Validate data series
        if 'data_series' not in spec:
            errors.append("Missing required field: 'data_series'")
        else:
            for i, series in enumerate(spec['data_series']):
                if 'points' not in series:
                    errors.append(f"Data series {i}: missing 'points'")
                elif not isinstance(series['points'], list):
                    errors.append(f"Data series {i}: 'points' must be a list")
                else:
                    for j, point in enumerate(series['points']):
                        if not isinstance(point, (list, tuple)) or len(point) != 2:
                            errors.append(f"Data series {i}, point {j}: must be [x, y]")
        
        return len(errors) == 0, errors
    
    def render(self, spec: Dict[str, Any], output_filename: Optional[str] = None) -> str:
        """
        Render line graph diagram.
        
        Args:
            spec: Validated VRS specification
            output_filename: Optional output filename
            
        Returns:
            Path to generated PNG file
        """
        # Extract configuration
        grid_config = spec.get('grid', {})
        x_range = grid_config.get('x_range', [0, 10])
        y_range = grid_config.get('y_range', [0, 100])
        x_unit = grid_config.get('x_unit', '')
        y_unit = grid_config.get('y_unit', '')
        x_major = grid_config.get('x_major', 1)
        y_major = grid_config.get('y_major', 10)
        
        axes_config = spec.get('axes', {})
        x_label = axes_config.get('x_label', f'X ({x_unit})' if x_unit else 'X')
        y_label = axes_config.get('y_label', f'Y ({y_unit})' if y_unit else 'Y')
        
        # Create figure
        self.fig, self.ax = plt.subplots(figsize=(10, 7), dpi=150)
        
        # Set limits
        x_padding = (x_range[1] - x_range[0]) * 0.1
        y_padding = (y_range[1] - y_range[0]) * 0.1
        self.ax.set_xlim(x_range[0] - x_padding, x_range[1] + x_padding)
        self.ax.set_ylim(y_range[0] - y_padding, y_range[1] + y_padding)
        
        # Draw grid
        self._draw_graph_grid(x_range, y_range, x_major, y_major)
        
        # Draw axes
        self._draw_axes(x_range, y_range, x_label, y_label)
        
        # Draw data series
        data_series = spec.get('data_series', [])
        for series in data_series:
            self._draw_data_series(series)
        
        # Draw highlights
        highlights = spec.get('highlights', [])
        for highlight in highlights:
            self._draw_highlight(highlight, data_series)
        
        # Draw annotations
        annotations = spec.get('annotations', [])
        for annotation in annotations:
            self._draw_annotation(annotation)
        
        # Add title
        title = spec.get('title', 'Line Graph')
        self.ax.set_title(title, fontsize=14, fontweight='bold',
                         color=self.colors['text'], pad=20)
        
        # Add legend if multiple series
        if len(data_series) > 1:
            self.ax.legend(loc='best', fontsize=10, framealpha=0.9)
        
        # Save
        if output_filename is None:
            output_filename = spec.get('id', 'line_graph')
        
        return self.save_figure(output_filename)
    
    def _draw_graph_grid(self, x_range: List[float], y_range: List[float],
                        x_major: float, y_major: float) -> None:
        """Draw graph paper style grid."""
        # Minor grid lines
        x_minor = x_major / 2
        y_minor = y_major / 2
        
        for x in np.arange(x_range[0], x_range[1] + x_minor, x_minor):
            self.ax.axvline(x, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
        
        for y in np.arange(y_range[0], y_range[1] + y_minor, y_minor):
            self.ax.axhline(y, color=self.colors['grid_line'], linewidth=0.5, zorder=0)
        
        # Major grid lines
        for x in np.arange(x_range[0], x_range[1] + x_major, x_major):
            self.ax.axvline(x, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
        
        for y in np.arange(y_range[0], y_range[1] + y_major, y_major):
            self.ax.axhline(y, color=self.colors['grid_major'], linewidth=1.0, zorder=0)
    
    def _draw_axes(self, x_range: List[float], y_range: List[float],
                  x_label: str, y_label: str) -> None:
        """Draw graph axes with labels."""
        # Draw axes lines
        self.ax.axhline(y_range[0], color=self.colors['text'], linewidth=2, zorder=2)
        self.ax.axvline(x_range[0], color=self.colors['text'], linewidth=2, zorder=2)
        
        # X-axis ticks and labels
        x_major = self._calculate_major_step(x_range)
        for x in np.arange(x_range[0], x_range[1] + x_major, x_major):
            self.ax.plot([x, x], [y_range[0], y_range[0] + 0.02 * (y_range[1] - y_range[0])],
                       color=self.colors['text'], linewidth=2, zorder=2)
            self.ax.text(x, y_range[0] - 0.08 * (y_range[1] - y_range[0]), 
                       str(int(x)), ha='center', fontsize=10, color=self.colors['text'])
        
        # Y-axis ticks and labels
        y_major = self._calculate_major_step(y_range)
        for y in np.arange(y_range[0], y_range[1] + y_major, y_major):
            self.ax.plot([x_range[0], x_range[0] + 0.02 * (x_range[1] - x_range[0])], [y, y],
                       color=self.colors['text'], linewidth=2, zorder=2)
            self.ax.text(x_range[0] - 0.05 * (x_range[1] - x_range[0]), y, 
                       str(int(y)), ha='right', va='center', fontsize=10, color=self.colors['text'])
        
        # Axis labels
        self.ax.text((x_range[0] + x_range[1]) / 2, 
                    y_range[0] - 0.15 * (y_range[1] - y_range[0]),
                    x_label, ha='center', fontsize=12, fontweight='bold', color=self.colors['text'])
        
        self.ax.text(x_range[0] - 0.12 * (x_range[1] - x_range[0]),
                    (y_range[0] + y_range[1]) / 2,
                    y_label, ha='center', va='center', fontsize=12, fontweight='bold',
                    color=self.colors['text'], rotation=90)
    
    def _calculate_major_step(self, range_vals: List[float]) -> float:
        """Calculate appropriate major step size."""
        span = range_vals[1] - range_vals[0]
        if span <= 10:
            return 1
        elif span <= 50:
            return 5
        elif span <= 100:
            return 10
        elif span <= 500:
            return 50
        else:
            return 100
    
    def _draw_data_series(self, series: Dict[str, Any]) -> None:
        """Draw a data series (line or cumulative)."""
        series_type = series.get('type', 'line')
        points = series.get('points', [])
        color_key = series.get('color', 'primary')
        show_points = series.get('show_points', True)
        name = series.get('name', 'Series')
        
        if not points:
            return
        
        color = self.colors.get(color_key, self.colors['primary'])
        
        # Extract x and y values
        x_vals = [p[0] for p in points]
        y_vals = [p[1] for p in points]
        
        if series_type == 'cumulative':
            # Draw cumulative/step style
            for i in range(len(points) - 1):
                # Horizontal line
                self.ax.plot([x_vals[i], x_vals[i+1]], [y_vals[i], y_vals[i]],
                           color=color, linewidth=2.5, zorder=3)
                # Vertical step
                self.ax.plot([x_vals[i+1], x_vals[i+1]], [y_vals[i], y_vals[i+1]],
                           color=color, linewidth=2.5, linestyle='--', zorder=3)
        else:
            # Standard line
            self.ax.plot(x_vals, y_vals, color=color, linewidth=2.5, 
                       marker='o' if show_points else None,
                       markersize=8 if show_points else 0,
                       markerfacecolor='white', markeredgecolor=color,
                       markeredgewidth=2, zorder=3, label=name)
        
        # Draw points if requested
        if show_points:
            for x, y in points:
                self.ax.plot(x, y, 'o', color=color, markersize=8,
                           markerfacecolor='white', markeredgewidth=2, zorder=4)
    
    def _draw_highlight(self, highlight: Dict[str, Any], 
                       data_series: List[Dict]) -> None:
        """Draw highlight for rate of change or reverse calculation."""
        highlight_type = highlight.get('type', '')
        
        if highlight_type == 'rate_of_change':
            self._draw_rate_highlight(highlight, data_series)
        elif highlight_type == 'reverse_calculation':
            self._draw_reverse_calculation(highlight)
        elif highlight_type == 'region':
            self._draw_region_highlight(highlight)
    
    def _draw_rate_highlight(self, highlight: Dict[str, Any],
                            data_series: List[Dict]) -> None:
        """Highlight a rate of change interval."""
        interval = highlight.get('interval', [0, 1])
        label = highlight.get('label', 'Rate of change')
        series_idx = highlight.get('series', 0)
        
        if series_idx >= len(data_series):
            return
        
        series = data_series[series_idx]
        points = series.get('points', [])
        
        # Find points within interval
        x_start, x_end = interval
        
        # Draw shaded region
        y_range = self.ax.get_ylim()
        rect = Rectangle((x_start, y_range[0]), x_end - x_start, 
                        y_range[1] - y_range[0],
                        facecolor=self.colors['highlight'], alpha=0.3,
                        edgecolor=self.colors['accent'], linewidth=2,
                        linestyle='--', zorder=1)
        self.ax.add_patch(rect)
        
        # Add label
        mid_x = (x_start + x_end) / 2
        y_pos = y_range[1] - 0.1 * (y_range[1] - y_range[0])
        self.ax.text(mid_x, y_pos, label, ha='center', va='top',
                   fontsize=10, color=self.colors['text'],
                   bbox=dict(boxstyle='round,pad=0.3',
                            facecolor=self.colors['accent'],
                            edgecolor=self.colors['text'], alpha=0.8))
        
        # Draw slope triangle
        # Find corresponding y values
        y_start = None
        y_end = None
        for i, (x, y) in enumerate(points):
            if abs(x - x_start) < 0.01:
                y_start = y
            if abs(x - x_end) < 0.01:
                y_end = y
        
        if y_start is not None and y_end is not None:
            # Draw slope triangle
            color = self.colors.get(series.get('color', 'primary'), self.colors['primary'])
            self.ax.plot([x_start, x_end], [y_start, y_start],
                       color=color, linewidth=1.5, linestyle=':', zorder=4)
            self.ax.plot([x_end, x_end], [y_start, y_end],
                       color=color, linewidth=1.5, linestyle=':', zorder=4)
            
            # Calculate and display rate
            rate = (y_end - y_start) / (x_end - x_start)
            self.ax.text(x_end + 0.2, (y_start + y_end) / 2,
                       f'{rate:.1f} L/hr', ha='left', va='center',
                       fontsize=9, color=color, fontweight='bold')
    
    def _draw_reverse_calculation(self, highlight: Dict[str, Any]) -> None:
        """Draw reverse calculation prompt."""
        question = highlight.get('question', '')
        answer_x = highlight.get('answer_x')
        answer_y = highlight.get('answer_y')
        
        # Draw question box
        x_range = self.ax.get_xlim()
        y_range = self.ax.get_ylim()
        
        # Position question box
        box_x = x_range[0] + 0.05 * (x_range[1] - x_range[0])
        box_y = y_range[1] - 0.15 * (y_range[1] - y_range[0])
        
        self.ax.text(box_x, box_y, f"❓ {question}",
                   ha='left', va='top', fontsize=11, fontweight='bold',
                   color=self.colors['text'],
                   bbox=dict(boxstyle='round,pad=0.5',
                            facecolor=self.colors['highlight'],
                            edgecolor=self.colors['construction'],
                            linewidth=2))
        
        # Draw answer indicator if provided
        if answer_x is not None:
            y_pos = answer_y if answer_y is not None else y_range[0]
            
            # Draw vertical dashed line to answer
            self.ax.axvline(answer_x, color=self.colors['construction'],
                          linewidth=2, linestyle='--', zorder=4)
            
            # Draw arrow pointing to answer
            self.ax.annotate('', xy=(answer_x, y_pos),
                           xytext=(answer_x, y_pos + 0.15 * (y_range[1] - y_range[0])),
                           arrowprops=dict(arrowstyle='->', color=self.colors['construction'],
                                          lw=2))
            
            # Answer label
            self.ax.text(answer_x, y_pos + 0.18 * (y_range[1] - y_range[0]),
                       f'x = {answer_x}', ha='center', fontsize=10,
                       color=self.colors['construction'], fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                                edgecolor=self.colors['construction']))
    
    def _draw_region_highlight(self, highlight: Dict[str, Any]) -> None:
        """Highlight a region of interest."""
        x_range = highlight.get('x_range', [0, 1])
        y_range = highlight.get('y_range', [0, 1])
        label = highlight.get('label', '')
        
        # Draw shaded rectangle
        rect = Rectangle((x_range[0], y_range[0]),
                        x_range[1] - x_range[0],
                        y_range[1] - y_range[0],
                        facecolor=self.colors['accent'], alpha=0.2,
                        edgecolor=self.colors['accent'], linewidth=2,
                        linestyle='--', zorder=1)
        self.ax.add_patch(rect)
        
        # Add label
        if label:
            mid_x = (x_range[0] + x_range[1]) / 2
            mid_y = (y_range[0] + y_range[1]) / 2
            self.ax.text(mid_x, mid_y, label, ha='center', va='center',
                       fontsize=10, color=self.colors['text'],
                       bbox=dict(boxstyle='round,pad=0.3',
                                facecolor='white',
                                edgecolor=self.colors['accent']))
    
    def _draw_annotation(self, annotation: Dict[str, Any]) -> None:
        """Draw an annotation with optional arrow."""
        x = annotation.get('x', 0)
        y = annotation.get('y', 0)
        text = annotation.get('text', '')
        show_arrow = annotation.get('arrow', False)
        offset_x = annotation.get('offset_x', 0.5)
        offset_y = annotation.get('offset_y', 0.5)
        
        text_x = x + offset_x
        text_y = y + offset_y
        
        if show_arrow:
            self.ax.annotate(text, xy=(x, y), xytext=(text_x, text_y),
                           arrowprops=dict(arrowstyle='->', color=self.colors['text'],
                                          lw=1.5),
                           fontsize=10, color=self.colors['text'],
                           bbox=dict(boxstyle='round,pad=0.2',
                                    facecolor=self.colors['highlight'],
                                    edgecolor=self.colors['border']))
        else:
            self.ax.text(text_x, text_y, text,
                       fontsize=10, color=self.colors['text'],
                       bbox=dict(boxstyle='round,pad=0.2',
                                facecolor=self.colors['highlight'],
                                edgecolor=self.colors['border']))


# Convenience function for direct usage
def render_linegraph(yaml_spec: str, output_path: Optional[str] = None, is_file: bool = True) -> str:
    """
    Render a line graph diagram from VRS YAML specification.
    
    Args:
        yaml_spec: Path to YAML file or YAML string
        output_path: Output directory path
        is_file: Whether yaml_spec is a file path
        
    Returns:
        Path to generated PNG file
    """
    renderer = LineGraphRenderer(output_path)
    return renderer.process(yaml_spec, is_file=is_file)