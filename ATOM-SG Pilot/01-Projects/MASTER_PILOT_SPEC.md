# ATOM-SG Pilot Master Specification (v1.0)

## 🎯 Core Objective
Prove the end-to-end ATOM-SG pipeline (Scan → YAML → Reconstruct → Test → Teach → Transfer) using **4 high-quality questions** to measure whether forced identification + articulation improves solving in a real child (Zeth).

## 📊 The 4 Questions (Pilot Scope)
| # | Type | Goal |
|---|------|------|
| 1 | **Complex Geometry (Overlap)** | Area/perimeter with overlapping shapes and shaded regions. |
| 2 | **Isometric 3D Geometry** | Cube structures and orthographic projection. |
| 3 | **Cross-Thread Collision (XT)** | Fusing ratio + fraction + before-after (most frequent pathway). |
| 4 | **Data Interpretation (DI)** | Graph reconstruction + data extraction + reverse percentage. |

## ⚙️ The Pipeline Process
1. **Stage 1: Deconstruction** → Convert PDF to structured YAML (Solvability > Pixel Precision).
2. **Stage 2: Baseline PDF** → Render a printable 4-question test from YAML.
3. **Stage 3: Baseline Test** → Establish initial performance with Zeth (observation-only).
4. **Stage 4: Intervention** → 10 days of identification-first teaching (Pathway → Articulation → Solve).
5. **Stage 5: Transfer Test** → Measure improvement and skill transfer with 4 new problems of the same type.

## ✅ Quality & Safety Standards
- **Solvability First:** A reconstruction is valid ONLY if a student can solve it using only the visual and text info provided.
- **Answer Leakage Prevention:** Diagrams must NOT contain answer classifications (e.g., "Rhombus") or calculated values.
- **Linguistic Integrity:** Language must match Singapore PSLE standards (precise, unambiguous).
- **Data Separation:** YAML files must strictly separate `diagram_data` from `question/solution` logic.

## 📁 Workspace Governance
- **Redundancy Control:** Legacy scripts are kept in `05-Backend/archive/`. Only use `generate_renders.py` and `generate_baseline_exam_quality.py` for production.
- **Documentation:** All frameworks and specs reside in `01-Projects/`.
- **Knowledge Base:** `01-Core-Brain/` is the primary source of truth for problem nodes and taxonomy.
- **Rendering Source:** `03-Rendering/` is the dedicated home for diagram logic and templates.

## 🚀 Current Status & Timeline
- **Current Stage:** Stage 0 (Smoke Test) — Verifying Vision LLM pipeline on first question.
- **Target Deadline:** 28 days from April 21 (Target: May 19, 2026).

---
*Created: 2026-04-23 | Author: Zcaethbot*
