---
type: problem
problemID: P5-Problem-009
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Triangle + Straight Line
difficulty: Medium
equationShadow: x + y = 180, x + y + z = 180 (combining supplementary angles with triangle angle sum)
traps: Temporal Misdirection (students must decide whether to find interior angles first or use exterior angle theorem)
visualNotes: |
  Diagram: Triangle ABC with side BC extended to point D, forming an exterior angle.
  - Draw triangle ABC with base BC horizontal
  - Extend BC to the right to point D (so B-C-D is a straight line)
  - Angle at A (top) = 50°
  - Angle at B (bottom left) = 65°
  - Students need to find exterior angle ACD

  TikZ code:
  \begin{tikzpicture}[scale=2]
    \coordinate (A) at (0,1.5);
    \coordinate (B) at (-1,0);
    \coordinate (C) at (1,0);
    \coordinate (D) at (2.5,0);

    \draw[thick] (A) -- (B) -- (C) -- (A);
    \draw[thick] (C) -- (D);

    \node[above] at (A) {A};
    \node[below left] at (B) {B};
    \node[below] at (C) {C};
    \node[below right] at (D) {D};

    \draw (0.15,1.4) arc (100:140:0.2);
    \node at (0.4,1.6) {$50^\circ$};

    \draw (-0.7,0.15) arc (20:70:0.2);
    \node at (-0.5,0.4) {$65^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation showing either method:
    - Method 1: angle ACB = 180° - 50° - 65° = 65°, then angle ACD = 180° - 65° = 115°
    - Method 2: angle ACD = 50° + 65° = 115° (exterior angle theorem)
  - Correct answer: 115°
  - Recognition that exterior angle equals sum of opposite interior angles
notes: |
  Medium-level problem combining triangle angle sum with supplementary angles.
  Tests whether students recognize the exterior angle theorem shortcut.

  Solution reasoning (Method 1 - step by step):
  1. Find angle ACB using triangle angle sum: 180° - 50° - 65° = 65°
  2. Angles ACB and ACD are supplementary (straight line BCD)
  3. Angle ACD = 180° - 65° = 115°

  Solution reasoning (Method 2 - exterior angle theorem):
  1. Recognize that angle ACD is an exterior angle of triangle ABC
  2. Exterior angle = sum of opposite interior angles
  3. Angle ACD = angle A + angle B = 50° + 65° = 115°

  Recognition skill taught: An exterior angle of a triangle equals the sum of the two opposite interior angles.
---
