---
type: problem
problemID: P5-Problem-001
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Supplementary Angles
difficulty: Easy
equationShadow: x + y = 180 (linear relationship between supplementary angles)
traps: Visual-Linguistic Mismatch (students see the diagram but miss that angles share a straight line)
visualNotes: |
  Diagram: Two rays OA and OB forming a straight line, with point C between them.
  - Draw horizontal line segment AB with A on the left, B on the right
  - Point O is in the middle of AB
  - Ray OC extends upward from O, forming angle AOC = 65°
  - Students need to find angle COB

  TikZ code:
  \begin{tikzpicture}[scale=2]
    \coordinate (O) at (0,0);
    \coordinate (A) at (-1.5,0);
    \coordinate (B) at (1.5,0);
    \coordinate (C) at (0,1.2);

    \draw[thick] (A) -- (B);
    \draw[thick] (O) -- (C);

    \node[below] at (A) {A};
    \node[below] at (B) {B};
    \node[below left] at (O) {O};
    \node[above] at (C) {C};

    \draw (0.4,0) arc (0:65:0.4);
    \node at (0.6,0.2) {$65^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's written calculation showing 180° - 65° = 115°
  - Correct answer: 115°
  - Recognition that points A, O, B lie on a straight line
notes: |
  This is a foundation-level problem testing the concept of supplementary angles.
  The visual trap is that students might incorrectly think OC is perpendicular to AB.

  Solution reasoning:
  1. Identify that points A, O, B lie on a straight line
  2. Therefore, angle AOB = 180° (straight angle)
  3. Angle AOB = angle AOC + angle COB
  4. 180° = 65° + angle COB
  5. angle COB = 180° - 65° = 115°

  Recognition skill taught: When two rays share a common endpoint and form a straight line with a third ray between them, the two resulting angles are supplementary (sum to 180°).
---