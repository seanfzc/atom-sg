---
title: Topic #51 — Deconstruction Pipeline
description: Vision LLM 3-layer pipeline (OCR + VLM + OpenCV) → YAML
status: active
owner: Vision LLM Bot
last_updated: 2026-04-22 10:30 SGT
---

# Topic #51 — Deconstruction Pipeline

## Purpose

Coordinate the Vision LLM 3-layer extraction pipeline for converting 4 exam questions from PDF to structured YAML with confidence scores.

**Critical Requirement (Stage 0 Finding 1):** Separate diagram data from question/solution data to prevent answer leakage to renderer.

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Scope

- **Layer 1: OCR (RapidOCR)** — Extract text, labels, numeric values
- **Layer 2: Vision LLM (Qwen/Ollama/Moondream)** — Extract structure, relationships, pathway classification
- **Layer 3: OpenCV** — Pixel-precise measurements, angles, dimensions, line styles
- **Merge:** Combine all three layers into tagged YAML with confidence scores
- **Separation:** Enforce `diagram_data:` vs `question:`/`solution:`/`answer_key:` structure

## Tasks (Assigned from SOR v4.5)

| ID | Task | Owner | Target | Success Criteria |
|----|------|-------|-----------------|
| D1 | Install and configure Vision LLM model | Vision LLM Bot | 2026-04-23 | Model selected and operational |
| D2 | Install and configure OpenCV | OpenCV Bot | 2026-04-23 | OpenCV functions working |
| D3 | Implement 3-layer merge logic | Vision LLM Bot | 2026-04-24 | Source priority, confidence tagging, conflict detection |
| D4 | Create YAML schemas for problem types | Vision LLM Bot | 2026-04-23 | Schema defined for all 4 question types with diagram/question separation |
| D5 | Deconstruct 4 exam questions to YAML | Vision LLM Bot | 2026-04-26 | All 4 questions output as tagged YAML with `diagram_data:` separated from `question:`/`solution:`/`answer_key:` |

## Diagram vs Question Data Separation (Fix 1)

**Critical Requirement from Stage 0:** YAML must have TWO CLEARLY SEPARATED sections:

### 1. `diagram_data:` Section — VISIBLE ONLY

- What to DRAW: shapes, labels, dimensions, annotations that appear visually on original diagram
- NO solutions
- NO derived values
- NO answers
- NO calculations

### 2. `question:` / `solution:` / `answer_key:` Sections — NEVER RENDERED

- Question text, solution steps, answer key
- These sections are NEVER passed to the renderer
- Renderer only reads `diagram_data:` section

**Validation:** Before committing YAML, verify that NO values from `solution:` or `answer_key:` appear in `diagram_data:`

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Reporting

- **Progress Updates:** Report daily to this topic only (not directly to Sean)
- **Task Completion:** Report when each D-task completes
- **Blocking Issues:** Report immediately if any task blocks

## Success Criteria

- All 4 exam questions converted to YAML with `diagram_data:` separated from `question:`/`solution:`/`answer_key:`
- All YAML files validated for structural integrity
- Vision LLM model selected and operational
- NO answer leakage to renderer

---

*Updated: 2026-04-22 based on Stage 0 Finding 1*
