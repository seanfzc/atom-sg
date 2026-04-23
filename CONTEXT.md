# ATOM-SG Project Context (The Bible)
**Last Updated:** 2026-04-23 | **Current Stage:** Stage 0 (Smoke Test)

## 🎯 Current Scope
- **Target:** 4 Questions (ACS Q15 Overlap, Nanyang Q19 3D, ACS Q16 XT, ACS Q10 Line Graph).
- **Subject:** 1 real child (Zeth).
- **Goal:** Prove end-to-end pipeline (Scan → YAML → Reconstruct → Test → Teach → Transfer).

## ✅ Quality Standard: "The Solvability Test"
- **Definition:** A reconstruction is valid **ONLY** if a human or student can solve it correctly using ONLY the visual and text information provided.
- **Answer Leakage:** Diagrams must NEVER reveal answers, classifications, or computed values.
- **Linguistic Rule:** Language must match Singapore PSLE standards (unambiguous, technical).

## 🛠️ Operational Rules
1. **Context First:** Every sub-agent MUST read this `CONTEXT.md` before starting work.
2. **The Ledger:** Sub-agents write progress to `subagentcomms/{task-name}.md`.
3. **The Boundary:** No sub-agent touches files outside its branch `manifest.md`.
4. **The Audit:** Every reconstruction requires a structured Vision LLM Audit (per-type checklist).
5. **Merging:** No direct commits to `main`. Merge only after a "Solvability PASS".

## 📊 Current Stage: Stage 0 (Smoke Test)
**Objective:** Pick ONE question (Question #4: Line Graph). Run full pipeline: OCR → VLM → YAML → Render. Verify solvability.
