# Geometry‑Specific Recognition‑First Loop
*Aligned with Geometry Taxonomy, Baseline Test Framework, and GeoBot outputs*

## Overview
This is a geometry‑specific adaptation of the Recognition‑First Loop, designed to work seamlessly with the Geometry Taxonomy (18 nano‑nodes), Baseline Test Framework (4 sub‑pathways, 25 items), and GeoBot’s Problem‑Pack Plan. The loop trains students to rapidly recognize geometry problem patterns, articulate the underlying equation shadows, and build fluency for PSLE Paper 2 structured questions.

## Integration Points
- **Nano‑Nodes:** Uses the 18 granular geometry skills defined in `Geometry_Taxonomy_NanoNodes.md`
- **Sub‑Pathways:** Maps to G1–G4 (Angle Reasoning, Area & Perimeter, Volume & 3D, Properties & Classification)
- **Equation Shadows:** Each nano‑node has a symbolic representation (e.g., `∠A + ∠B = 180°` for angles on a straight line)
- **Problem Bank:** Draws from the 25‑item Problem‑Pack Plan (G001–G025) or can be extended with new problems

## The Loop Steps (Geometry Variant)

### Step 1: Read
**Objective:** Parse the geometry problem statement and diagram.
**Focus:** Identify key geometric elements, measurements, relationships, and what is being asked.
**Time:** ~15–30 seconds (varies by complexity).

**What to look for:**
- Shape types (triangles, quadrilaterals, circles, composite figures)
- Given measurements (angles, lengths, radii)
- Geometric relationships (parallel/perpendicular lines, symmetry, angles on straight line)
- What needs to be found (missing angle, area, perimeter, volume, classification)

### Step 2: Identify Pathway
**Objective:** Classify the problem into:
1. **Sub‑Pathway (G1–G4)** – broad category
2. **Specific Nano‑Node** – granular skill from the 18‑item taxonomy

**Decision tree:**
- **G1 Angle Reasoning:** Problems about angles, angle properties, angle sums
- **G2 Area & Perimeter:** Problems about perimeter/area of rectilinear or composite figures, unit conversion, symmetry
- **G3 Volume & 3D:** Problems about volume of cubes/cuboids, nets, spatial visualization  
- **G4 Properties & Classification:** Problems about classifying shapes, circle properties, pie charts

**Example identification:**
> *Problem:* "In triangle ABC, ∠A = 65° and ∠B = 45°. Find ∠C."  
> **Sub‑pathway:** G1 Angle Reasoning  
> **Nano‑node:** "Apply angle sum of triangle (180°) to find missing angles"

**Time:** ~30 seconds for pathway identification.

### Step 3: Articulate
**Objective:** Verbally explain:
1. **Why** this problem belongs to the identified sub‑pathway and nano‑node
2. **What equation shadow** applies
3. **Which cues** in the problem trigger that shadow

**Articulation structure:**
1. "This is a **G1 Angle Reasoning** problem because it involves finding an unknown angle."
2. "The specific nano‑node is **'Apply angle sum of triangle (180°) to find missing angles'**."
3. "The equation shadow is: `∠A + ∠B + ∠C = 180°`."
4. "The cues are: 'triangle ABC' (triangle context), '∠A = 65° and ∠B = 45°' (two angles given), 'find ∠C' (missing third angle)."

**Time:** ~45–60 seconds for articulation.

### Step 4: Shadow
**Objective:** Set up the equation shadow—write the algebraic/arithmetic representation of the problem.

**Actions:**
- Write the equation shadow (e.g., `65 + 45 + C = 180`)
- Label variables with what they represent
- Include units if applicable

**Example shadow setup:**
```
Let ∠C = C
Equation shadow: 65° + 45° + C = 180°
```

**Time:** ~30 seconds for shadow setup.

### Step 5: Solve
**Objective:** Execute the arithmetic/algebra to find the answer.

**Actions:**
- Perform calculations step‑by‑step
- Include units in final answer
- Check reasonableness (e.g., angle between 0–180°, positive area/volume)

**Example solution:**
```
65 + 45 + C = 180
110 + C = 180
C = 180 - 110
C = 70°
```

**Time:** Variable based on complexity (30–90 seconds).

## Pathway Radar Warm‑up (Geometry Variant)

**Objective:** Rapid recognition training for geometry problems only.
**Structure:** 3‑question mix covering different sub‑pathways.
**Total time:** 5 minutes.

### Question Mix (example)
1. **G1 item** (Angle Reasoning) – 2 minutes
2. **G2 item** (Area & Perimeter) – 2 minutes  
3. **G4 item** (Properties & Classification) – 1 minute

### Warm‑up Flow
1. Question appears with **allocated time**.
2. Student must:
   - Identify sub‑pathway (G1–G4)
   - Identify specific nano‑node
   - Articulate equation shadow and cues
3. Timer stops after articulation; no solving required.
4. Immediate rubric feedback.

### Timing Basis
Aligned with PSLE Paper 2 structured‑question timing:
- G1/G2 items: 2 minutes (standard 4‑mark question recognition phase)
- G3/G4 items: 1–2 minutes based on complexity

## Rubric Alignment

The geometry‑specific loop uses a **unified rubric** that merges:
1. **Recognition‑First Loop's 3‑level quality scale** (Vague/Partial/Clear)
2. **Baseline Test's 4‑dimension assessment** (Pathway ID, Equation‑Shadow Setup, Algebraic Execution, Explanation)

| Dimension | 🔴 Vague (Level 1) | 🟡 Partial (Level 2) | 🟢 Clear (Level 3) |
|-----------|-------------------|---------------------|-------------------|
| **Pathway Identification** | Names only broad topic ("it's about angles") | Identifies correct sub‑pathway (G1–G4) but not nano‑node | Identifies both sub‑pathway **and** specific nano‑node |
| **Equation‑Shadow Setup** | Cannot state any equation shadow | States correct equation shadow but cannot link to problem cues | States equation shadow **and** explains how each cue maps to it |
| **Algebraic Execution** | (Not assessed in warm‑up; for full loop only) | (Not assessed in warm‑up) | (Not assessed in warm‑up) |
| **Explanation & Justification** | Generic explanation ("use the formula") | Explains which formula to use but not why it fits | Clearly justifies choice of equation shadow using geometric principles |

## Implementation with GeoBot Outputs

### Using the Problem‑Pack Plan
The 25 items (G001–G025) are pre‑mapped to:
- Sub‑pathway (G1–G4)
- Nano‑node
- Equation shadow
- Difficulty zone (A–D)

**For Pathway Radar warm‑up:**
- Select 1 item from each sub‑pathway
- Use difficulty zones B/C for balanced challenge
- Ensure equation shadows are clearly mappable to problem cues

### Integration with Geometry‑Rubrics.md
Each nano‑node has a rubric template in `Geometry‑Rubrics.md`. The articulation step should reference:
- `subpathway` field (nano‑node description)
- `equationShadow` field
- `articulationRubric.level1/2/3` for quality benchmarks

### Automated Feedback Potential
GeoBot could generate immediate feedback by:
1. Matching student's articulation to expected nano‑node
2. Checking if mentioned cues align with problem elements  
3. Comparing stated equation shadow to pre‑defined shadow

## Example: Full Loop Execution

**Problem G005 (from Problem‑Pack Plan):**
> In triangle PQR, ∠P = 55° and ∠Q = 70°. Find ∠R.

**Step 1 – Read:** Triangle with two angles given, find third angle.

**Step 2 – Identify Pathway:**
- Sub‑pathway: **G1 Angle Reasoning**
- Nano‑node: **"Apply angle sum of triangle (180°) to find missing angles"**

**Step 3 – Articulate:**
"This is a G1 Angle Reasoning problem because it involves finding an unknown angle in a triangle. The specific nano‑node is 'Apply angle sum of triangle (180°) to find missing angles'. The equation shadow is `∠P + ∠Q + ∠R = 180°`. The cues are: 'triangle PQR' (triangle context), '∠P = 55° and ∠Q = 70°' (two angles given), 'find ∠R' (missing third angle)."

**Step 4 – Shadow:**
```
Let ∠R = R
Equation: 55° + 70° + R = 180°
```

**Step 5 – Solve:**
```
55 + 70 + R = 180
125 + R = 180
R = 180 - 125
R = 55°
```

## Adapting for Different Difficulty Zones

| Zone | Recognition Focus | Articulation Expectation | Time Allocation |
|------|-------------------|-------------------------|-----------------|
| **A (Basic)** | Identify sub‑pathway only | State equation shadow | 1–1.5 minutes |
| **B (Standard)** | Identify sub‑pathway + nano‑node | Explain cues → shadow mapping | 1.5–2 minutes |
| **C (Multi‑step)** | Identify multiple nano‑nodes | Explain sequence of shadows | 2–2.5 minutes |
| **D (Complex)** | Decompose into multiple sub‑pathways | Articulate integrated solution strategy | 2.5–3 minutes |

## Next Steps

1. **Select warm‑up items** from Problem‑Pack Plan (G001–G025) for each sub‑pathway.
2. **Create articulation prompts** for each item (expected sub‑pathway, nano‑node, equation shadow).
3. **Develop feedback templates** using the unified rubric.
4. **Pilot test** with sample geometry problems.
5. **Integrate with rendering pipeline** for diagram display.

## Related Files
- `Geometry_Taxonomy_NanoNodes.md` – 18 nano‑nodes
- `Geometry-Subpathway-Mapping.md` – G1–G4 mapping
- `Problem-Pack-Plan.md` – 25‑item bank
- `Geometry-Rubrics.md` – rubric templates
- `subagentcomms.md` – project coordination

---
*Created: 2026‑04‑13 | Owner: Zcaethbot | Status: Draft | Aligns with GeoBot v1.0*