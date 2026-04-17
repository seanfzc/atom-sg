---
type: problem
problemID: P5-Problem-020
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Composite Figures - Trapezium with Semicircle
difficulty: Hard
equationShadow: Area = Area_trapezium - Area_semicircle or Area_trapezium + Area_semicircle (depending on configuration)
traps: Temporal Misdirection (students must correctly identify which areas to add/subtract; may confuse radius and diameter)
visualNotes: |
  Diagram: Trapezium with a semicircle removed from one side (or added).
  - Draw a right trapezium with parallel sides 10 cm (bottom) and 6 cm (top)
  - Height = 4 cm
  - A semicircle with diameter 4 cm is cut out from the right side (on the vertical side)
  - Students need to find the remaining area

  TikZ code:
  \begin{tikzpicture}[scale=0.5]
    % Right trapezium
    % Bottom: 10, Top: 6, Height: 4
    % Left side vertical, right side slanted
    \coordinate (A) at (0,0);
    \coordinate (B) at (10,0);
    \coordinate (C) at (7,4);
    \coordinate (D) at (0,4);

    % Draw trapezium
    \draw[thick] (A) -- (B) -- (C) -- (D) -- (A);

    % Semicircle cut out from right side
    % Actually, let's put semicircle on the bottom edge
    % Semicircle with diameter on bottom edge, center at (5,0), radius 2
    \begin{scope}
      \clip (0,0) rectangle (10,4);
      \fill[white] (5,0) circle (2);
    \end{scope}
    
    % Redraw outline
    \draw[thick] (A) -- (B);
    \draw[thick] (B) -- (C);
    \draw[thick] (C) -- (D);
    \draw[thick] (D) -- (A);
    
    % Semicircle (cut out - dashed)
    \draw[thick,dashed] (3,0) arc (180:0:2);

    % Labels
    \node[below] at (5,-0.3) {10 cm};
    \node[above] at (3.5,4) {6 cm};
    \node[left] at (-0.3,2) {4 cm};
    \node at (5,0.8) {4 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation:
    - Area of trapezium = ½ × (10 + 6) × 4 = 32 cm²
    - Radius of semicircle = 4 ÷ 2 = 2 cm
    - Area of semicircle = ½ × π × 2² = 2π ≈ 6.28 cm²
    - Shaded/remaining area = 32 - 6.28 = 25.72 cm²
  - Correct answer: 32 - 2π cm² or approximately 25.7 cm²
  - Clear identification of trapezium formula and semicircle area
notes: |
  Hard-level problem combining trapezium area with semicircle area subtraction.
  Requires multiple formulas and careful calculation.

  Solution reasoning:
  1. Identify the composite shape: trapezium with semicircular cutout
  2. Calculate area of trapezium:
     - Formula: A = ½ × (a + b) × h
     - A = ½ × (10 + 6) × 4 = ½ × 16 × 4 = 32 cm²
  3. Calculate area of semicircle:
     - Diameter = 4 cm (matches height of trapezium)
     - Radius = 4 ÷ 2 = 2 cm
     - Area = ½ × π × r² = ½ × π × 4 = 2π cm² ≈ 6.28 cm²
  4. Calculate remaining area:
     - Area = 32 - 2π ≈ 32 - 6.28 = 25.72 cm²

  Common errors:
  - Using diameter instead of radius for circle area
  - Forgetting the ½ in semicircle area
  - Adding instead of subtracting the semicircle
  - Wrong trapezium formula

  Recognition skill taught: Complex composite figures require identifying component shapes, applying correct formulas, and carefully determining whether to add or subtract areas.
---
