---
type: problem
problemID: P5-Problem-002
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Parallel Lines
difficulty: Easy
equationShadow: x = y (corresponding angles on parallel lines are equal)
traps: Visual-Linguistic Mismatch (parallel lines aren't explicitly marked, requiring visual inference)
visualNotes: |
  Diagram: Two parallel lines cut by a transversal.
  - Draw two horizontal parallel lines: l1 (top) and l2 (bottom)
  - Draw a diagonal transversal line cutting through both from bottom-left to top-right
  - Label the angle where the transversal meets l1 (top-left) as 72°
  - Students need to find the corresponding angle where the transversal meets l2 (bottom-left)

  TikZ code:
  \begin{tikzpicture}[scale=2]
    \draw[thick] (-1,1) -- (3,1) node[right] {$l_1$};
    \draw[thick] (-1,-0.5) -- (3,-0.5) node[right] {$l_2$};
    \draw[thick] (0,-0.8) -- (2.5,1.3);

    \draw (0.2,0.7) arc (70:120:0.25);
    \node at (0.1,1) {$72^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's identification of corresponding angles
  - Correct answer: 72°
  - Recognition that corresponding angles are equal when lines are parallel
notes: |
  Foundation-level problem testing corresponding angles on parallel lines.
  The trap is that students need to recognize which angles correspond to each other.

  Solution reasoning:
  1. Identify that l1 and l2 are parallel lines (they look horizontal and never meet)
  2. The diagonal line is a transversal cutting both parallel lines
  3. When parallel lines are cut by a transversal, corresponding angles are equal
  4. The marked angle (72°) corresponds to the angle at the bottom-left intersection
  5. Therefore, the unknown angle = 72°

  Recognition skill taught: Parallel lines cut by a transversal create corresponding angles that are equal.
---