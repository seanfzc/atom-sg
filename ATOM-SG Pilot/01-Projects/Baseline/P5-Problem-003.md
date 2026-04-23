---
type: problem
problemID: P5-Problem-003
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - Angle Chasing - Isosceles Triangle
difficulty: Easy
equationShadow: x = x (base angles of isosceles triangle are equal)
traps: Visual-Linguistic Mismatch (students may not recognize the triangle as isosceles without side markings)
visualNotes: |
  Diagram: Triangle with two equal sides marked.
  - Draw triangle ABC with AB = AC (two sides marked with tick marks)
  - Angle at vertex A (top) = 50°
  - Students need to find angle B and angle C

  TikZ code:
  \begin{tikzpicture}[scale=2]
    \coordinate (A) at (0,1.5);
    \coordinate (B) at (-1,-0.5);
    \coordinate (C) at (1,-0.5);

    \draw[thick] (A) -- (B);
    \draw[thick] (B) -- (C);
    \draw[thick] (C) -- (A);

    \node[above] at (A) {A};
    \node[below left] at (B) {B};
    \node[below right] at (C) {C};

    % Mark equal sides
    \draw (-0.5,0.5) -- (-0.4,0.45);
    \draw (0.5,0.5) -- (0.4,0.45);

    \draw (0.2,1.4) arc (60:120:0.2);
    \node at (0,1.6) {$50^\circ$};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation: (180° - 50°) ÷ 2 = 65°
  - Correct answer: angle B = angle C = 65°
  - Recognition of isosceles triangle property
notes: |
  Foundation-level problem testing isosceles triangle properties.
  The visual cue (tick marks on equal sides) teaches students to look for these markings.

  Solution reasoning:
  1. Observe that sides AB and AC have tick marks, meaning they are equal in length
  2. Therefore, triangle ABC is isosceles with AB = AC
  3. In an isosceles triangle, the base angles (opposite equal sides) are equal
  4. Angle B = angle C
  5. Sum of angles in a triangle = 180°
  6. 50° + angle B + angle C = 180°
  7. 50° + 2 × angle B = 180° (since angle B = angle C)
  8. 2 × angle B = 130°
  9. angle B = angle C = 65°

  Recognition skill taught: In an isosceles triangle, base angles are equal.
---