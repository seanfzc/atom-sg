---
type: problem
problemID: P5-Problem-017
source: ATOM-SG Baseline Test Pack - Week 1
pathwayType: Geometry - 3D Visualization - Surface Area of Cuboid
difficulty: Medium
equationShadow: SA = 2(lw + lh + wh) (surface area formula)
traps: Temporal Misdirection (students might calculate volume instead, or miss some faces)
visualNotes: |
  Diagram: Cuboid (rectangular prism) with dimensions labeled.
  - Draw an isometric view of a cuboid
  - Length = 8 cm, Width = 5 cm, Height = 4 cm
  - Students need to find the total surface area

  TikZ code:
  \begin{tikzpicture}[scale=0.8]
    % Front face
    \draw[thick] (0,0) -- (4,0) -- (4,2) -- (0,2) -- cycle;
    % Top face
    \draw[thick] (0,2) -- (1,3) -- (5,3) -- (4,2);
    % Right face
    \draw[thick] (4,0) -- (5,1) -- (5,3) -- (4,2);
    % Hidden edges (dashed)
    \draw[thick,dashed] (0,0) -- (1,1) -- (5,1);
    \draw[thick,dashed] (1,1) -- (1,3);

    % Dimension labels
    \node[below] at (2,0) {8 cm};
    \node[right] at (4.5,1) {4 cm};
    \node[above] at (2.5,2.5) {5 cm};
  \end{tikzpicture}
expectedArtifacts:
  - Student's calculation showing all 6 faces:
    - Front and back: 2 × (8 × 4) = 64 cm²
    - Top and bottom: 2 × (8 × 5) = 80 cm²
    - Left and right: 2 × (5 × 4) = 40 cm²
    - Total: 64 + 80 + 40 = 184 cm²
  - Correct answer: 184 cm²
  - OR using formula: 2(8×5 + 8×4 + 5×4) = 2(40 + 32 + 20) = 2(92) = 184 cm²
notes: |
  Medium-level problem testing surface area of a cuboid.
  Students must account for all 6 faces (3 pairs of identical rectangles).

  Solution reasoning:
  Method 1 - Counting faces:
  1. Front face: 8 cm × 4 cm = 32 cm²
  2. Back face (same as front): 32 cm²
  3. Top face: 8 cm × 5 cm = 40 cm²
  4. Bottom face (same as top): 40 cm²
  5. Left face: 5 cm × 4 cm = 20 cm²
  6. Right face (same as left): 20 cm²
  7. Total surface area = 32 + 32 + 40 + 40 + 20 + 20 = 184 cm²

  Method 2 - Formula:
  1. SA = 2(lw + lh + wh)
  2. SA = 2(8×5 + 8×4 + 5×4)
  3. SA = 2(40 + 32 + 20)
  4. SA = 2(92) = 184 cm²

  Common errors:
  - Calculating only 3 faces (forgetting opposite faces)
  - Calculating volume instead (8 × 5 × 4 = 160)
  - Mixing up dimensions

  Recognition skill taught: A cuboid has 6 faces in 3 identical pairs; surface area is the sum of all face areas.
---
