---
type: problem
problemID: P5-Problem-004
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Basic Angle Sum
difficulty: Easy
equationShadow: x + y + z = 180 (sum of angles in triangle)
traps: Temporal Misdirection (students might jump to calculating without planning which angles to find first)
visualNotes: |
  Diagram: Right-angled triangle with one acute angle given.
  - Draw right-angled triangle ABC with right angle at C
  - Mark the right angle with a small square
  - Angle A = 35°
  - Students need to find angle B

  TikZ code:
  \begin{tikzpicture}[scale=2]
    \coordinate (C) at (0,0);
    \coordinate (A) at (0,1.3);
    \coordinate (B) at (1.5,0);

    \draw[thick] (A) -- (C) -- (B) -- (A);

    \node[above] at (A) {A};
    \node[below] at (C) {C};
    \node[right] at (B) {B};

    % Right angle marker
    \draw (0,0.2) -- (0.2,0.2) -- (0.2,0);

    \draw (0.15,1.1) arc (90:130:0.2);
    \node at (0.4,1.2) {$35^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation: 180° - 90° - 35° = 55°
  - Correct answer: 55°
  - Recognition of right angle symbol
notes: |
  Foundation-level problem testing triangle angle sum theorem with a right angle.
  The right angle is visually marked, not given in text.

  Solution reasoning:
  1. Identify that the small square at C indicates a right angle (90°)
  2. Triangle ABC has angles at A, B, and C
  3. Sum of angles in any triangle = 180°
  4. angle A + angle B + angle C = 180°
  5. 35° + angle B + 90° = 180°
  6. angle B = 180° - 35° - 90° = 55°

  Recognition skill taught: Look for the right angle symbol (small square) to identify 90° angles.
---