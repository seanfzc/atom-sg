"""
Geometry Rendering Modules for Exam-Quality Diagrams

This package provides specialized renderers for Singapore MOE exam-style geometry diagrams.
All renderers support VRS YAML specifications and output PNG at 150 DPI.

Modules:
    - grid_renderer: Grid construction diagrams
    - isometric_renderer: 3D isometric visualizations
    - composite_renderer: Composite shape overlaps
    - linegraph_renderer: Data interpretation line graphs
"""

from .grid_renderer import GridRenderer
from .isometric_renderer import IsometricRenderer
from .composite_renderer import CompositeRenderer
from .linegraph_renderer import LineGraphRenderer

__all__ = [
    'GridRenderer',
    'IsometricRenderer',
    'CompositeRenderer',
    'LineGraphRenderer',
]

__version__ = '1.0.0'