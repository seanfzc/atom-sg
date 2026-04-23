---
type: problem
problemID: P5-Problem-016
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Properties - Parallelogram Properties
difficulty: Medium
equationShadow: Opposite angles equal, consecutive angles supplementary (angle properties)
traps: Visual-Linguistic Mismatch (students might treat it as a rectangle and assume 90° angles)
visualNotes: |
  Diagram: Parallelogram ABCD with one angle given.
  - Draw a parallelogram (not a rectangle - slanted sides)
  - Label vertices A, B, C, D going around
  - Angle A (bottom left, acute) = 55°
  - Students need to find angles B, C, and D

  TikZ code:
  \begin{tikzpicture}[scale=1.8]
    \coordinate (A) at (0,0);
    \coordinate (B) at (3,0);
    \coordinate (C) at (3.8,1.5);
    \coordinate (D) at (0.8,1.5);

    \draw[thick] (A) -- (B) -- (C) -- (D) -- (A);

    \node[below left] at (A) {A};
    \node[below right] at (B) {B};
    \node[upper right] at (C) {C};
    \node[upper left] at (D) {D};

    % Mark parallel sides with arrows
    \draw[->,thick] (0.2,0) -- (0.9,0);
    \draw[->,thick] (2.1,0) -- (2.8,0);
    \draw[->,thick] (0.85,1.5) -- (1.55,1.5);
    \draw[->,thick] (2.05,1.5) -- (2.75,1.5);

    % Angle A
    \draw (0.3,0) arc (0:55:0.3);
    \node at (0.5,0.25) {$55^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculations:
    - Angle C = 55° (opposite angles equal)
    - Angle B = 180° - 55° = 125° (consecutive angles supplementary)
    - Angle D = 125° (opposite angles equal)
  - Correct answers: Angle B = 125°, Angle C = 55°, Angle D = 125°
  - Verification that sum = 360°
notes: |
  Medium-level problem testing parallelogram angle properties.
  Students must know opposite angles are equal and consecutive angles are supplementary.

  Solution reasoning:
  1. Identify the shape as a parallelogram (opposite sides parallel, marked with arrows)
  2. Property 1: Opposite angles in a parallelogram are equal
     - Angle A = Angle C = 55°
     - Angle B = Angle D
  3. Property 2: Consecutive angles in a parallelogram are supplementary (sum to 180°)
     - Angle A + Angle B = 180°
     - 55° + Angle B = 180°
     - Angle B = 125°
  4. Therefore Angle D = 125° (opposite to B)
  5. Check: 55° + 125° + 55° + 125° = 360° ✓

  Common errors:
  - Assuming all angles are 90° (treating it as a rectangle)
  - Thinking opposite angles are supplementary instead of equal

  Recognition skill taught: In a parallelogram, opposite angles are equal and consecutive angles are supplementary (sum to 180°).
---
