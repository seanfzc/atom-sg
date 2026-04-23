# BATCH 02 RISK BRIEF — Rule 6 Audit Pass

## Source: Rosyth 2026 P6 Math CA1 Algebra Q5–Q10
## Auditor: v2.1 (with Rule 6: Inter-Thread Check)
## Status: PRE-EXTRACTION ANALYSIS

---

## 1. THE COLLISION MAP (Integrity)

Based on typical Rosyth CA1 P6 Algebra exam structure (Q5–Q10 = increasing difficulty, concept blending begins at Q7+), here is the projected thread classification:

| Q# | Node ID | Projected Topic | Classification | Threads Involved | Dual-Parentage Required? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q5 | ROSYTH-P6-ALG-05 | Simplify expression: $3x + 5x - 2$ | **PURE** | Thread A (Expressions) | No |
| Q6 | ROSYTH-P6-ALG-06 | Solve equation: $4x - 7 = 13$ | **PURE** | Thread C (Equations) | No |
| Q7 | ROSYTH-P6-ALG-07 | Ratio word problem with equation setup: "Ali has $x$ stickers, Baba has $3x$, total is 48" | **HYBRID** | Thread A + Thread C | ⚠️ YES — Ratio (A) + Equation Solving (C) |
| Q8 | ROSYTH-P6-ALG-08 | Fraction of remainder: "Spent $\frac{1}{3}$ of money, then $\frac{2}{5}$ of remainder" | **PURE** | Thread D (Remainder Pivot) | No |
| Q9 | ROSYTH-P6-ALG-09 | Ratio + Remainder: "Divided marbles in ratio $2:3$, gave away $\frac{1}{4}$ of his share" | **HYBRID** | Thread A + Thread D | ⚠️ YES — Ratio (A) + Remainder Pivot (D) |
| Q10 | ROSYTH-P6-ALG-10 | Multi-concept: "Solve for $x$ where $\frac{3x+5}{4} = 8$, then find ratio of parts" | **HYBRID** | Thread A + Thread C + Thread D | 🔴 YES — Triple-thread collision |

### Collision Summary

| Type | Count | Nodes |
| :--- | :--- | :--- |
| PURE (single thread) | 3 | Q5, Q6, Q8 |
| HYBRID (dual thread) | 2 | Q7, Q9 |
| HYBRID (triple thread) | 1 | Q10 |

**Rule 6 Enforcement:** Q7, Q9, and Q10 require explicit dual/triple-parentage links or they will be REJECTED for Structural Blindness.

---

## 2. THE CLS GRADIENT PRE-FLIGHT

### Estimated Complexity Scores ($C_t$)

| Node | Projected $C_t$ | Nearest Bridge Parent | Parent $C_t$ | CLS Jump | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ALG-05 | 2.8 | P4-A1-UnitScaling | 2.2 | 0.6 | ✅ Safe |
| ALG-06 | 3.2 | P4-A2-BalancingEquations | 2.4 | 0.8 | ✅ Safe |
| ALG-07 | 3.8 | P4-A1 (2.2) + P4-A2 (2.4) | Dual: 2.2/2.4 | 1.6 / 1.4 | ⚠️ Thread A jump = 1.6 EXCEEDS 1.5 |
| ALG-08 | 3.4 | P4-F3-RemainderChaining | 2.8 | 0.6 | ✅ Safe |
| ALG-09 | 4.0 | P4-A1 (2.2) + P4-F2 (2.3) | Dual: 2.2/2.3 | 1.8 / 1.7 | 🔴 BOTH jumps EXCEED 1.5 |
| ALG-10 | 4.5 | P4-A1 (2.2) + P4-A2 (2.4) + P4-F3 (2.8) | Triple: 2.2/2.4/2.8 | 2.3 / 2.1 / 1.7 | 🔴 ALL jumps EXCEED 1.5 |

### Flagged Nodes

| Node | Issue | Required Action |
| :--- | :--- | :--- |
| **ALG-07** | CLS 1.6 from Thread A parent | Forge P5 transition node OR accept with "Boss Fight: Odyssey Level" tag |
| **ALG-09** | CLS 1.8 and 1.7 from both parents | 🔴 Mandatory bridge insertion — cannot proceed without P5 transition |
| **ALG-10** | CLS 2.3 / 2.1 / 1.7 — all exceed threshold | 🔴 Mandatory bridge insertion — "Boss Fight: Odyssey Level" + P5 bridges |

---

## 3. BRIDGE DEFICIT REPORT

### Do we need P5 Transition Nodes? YES.

The current bridge infrastructure tops out at P4 ($C_t$ ~2.2–2.8). The Hybrid Zone Q7–Q10 demands nodes at $C_t$ ~3.0–3.5 to create a smooth gradient. We need **P5-level transition nodes** that combine concepts from two threads.

### Proposed P5 Transition Nodes

| Node ID | Purpose | Threads Bridged | Target $C_t$ | Verb Test |
| :--- | :--- | :--- | :--- | :--- |
| **P5-H1-RatioEquation** | Combine ratio setup with equation solving: "Ali has $x$, Baba has $3x$, total = 48. Solve." | A + C | 3.2 | "Set up a ratio AS an equation and solve for the unknown." |
| **P5-H2-RatioRemainder** | Combine ratio with fractional take-away: "Shared in ratio 2:3. Ali gave away $\frac{1}{4}$ of his share." | A + D | 3.3 | "Apply a fraction to ONE part of a ratio, then recalculate the total." |
| **P5-H3-EquationFraction** | Solve fractional equations: "$\frac{3x+5}{4} = 8$" | C + D | 3.4 | "Clear a fraction from an equation using inverse operations, then solve." |

### Updated CLS Gradients (With P5 Bridges)

| Path | Before P5 Bridge | After P5 Bridge |
| :--- | :--- | :--- |
| P4-A1 (2.2) → ALG-07 (3.8) | CLS = 1.6 ⚠️ | P4-A1 (2.2) → **P5-H1 (3.2)** → ALG-07 (3.8): CLS = 1.0 + 0.6 ✅ |
| P4-A1 (2.2) → ALG-09 (4.0) | CLS = 1.8 🔴 | P4-A1 (2.2) → **P5-H2 (3.3)** → ALG-09 (4.0): CLS = 1.1 + 0.7 ✅ |
| P4-A2 (2.4) → ALG-10 (4.5) | CLS = 2.1 🔴 | P4-A2 (2.4) → **P5-H3 (3.4)** → ALG-10 (4.5): CLS = 1.0 + 1.1 ✅ |

### Verdict: THREE P5 Transition Nodes required before Batch 02 extraction of Hybrid nodes.

---

## 4. GAME SMITH CALIBRATION

### Can Age 6 Seeds handle Hybrid mechanics?

| Hybrid Node | Threads | Game Mechanic Fusion | Feasibility |
| :--- | :--- | :--- | :--- |
| **ALG-07** (Ratio + Equation) | A + C | "The Box Packer" (units) + "The Scale Master" (balance) → **"The Box Scale"**: Pack boxes of unknown gems onto a balanced scale. If 4 boxes = 48 gems, how many per box? | ✅ Natural fusion — units on a scale |
| **ALG-09** (Ratio + Remainder) | A + D | "The Box Packer" (units) + "The Shrinking Treasure" (remainder) → **"The Shared Treasure"**: Split gems in ratio 2:3 between pirates. Pirate 1 gives away 1/4 of his share. How many left? | ✅ Feasible — split first, then shrink one pile |
| **ALG-10** (Equation + Fraction + Ratio) | A + C + D | "The Scale Master" + "The Undo Machine" + "The Pizza Thief" → **"The Grand Heist"**: A locked vault with $\frac{3x+5}{4}$ gems showing through a window. Player must: (1) clear the fraction (multiply by 4), (2) undo the +5, (3) divide by 3, (4) split result in a ratio. | ⚠️ Complex but viable — requires 3-stage level with sequential unlocks |

### Game Smith Recommendation

| Node | Recommended Approach |
| :--- | :--- |
| ALG-07 | Single combined game ("The Box Scale") — two mechanics feel like one |
| ALG-09 | Two-phase game ("The Shared Treasure") — Phase 1: split, Phase 2: shrink |
| ALG-10 | **Multi-stage Boss Battle** ("The Grand Heist") — three sequential mini-games. Flag as "Odyssey Level: Boss Fight" in Level_Config_JSON. Reserve Claude-Sonnet for heuristic mapping per Economist Override. |

---

## 5. EXECUTIVE SUMMARY & RECOMMENDATION

### Risk Matrix

| Risk | Severity | Mitigation |
| :--- | :--- | :--- |
| CLS jumps > 1.5 on Hybrid nodes | 🔴 HIGH | Forge 3 P5 Transition Nodes |
| Structural Blindness (Rule 6) on Q7/Q9/Q10 | 🔴 HIGH | Enforce dual/triple-parentage links |
| Age 6 Seed complexity on triple-hybrid Q10 | ⚠️ MEDIUM | Multi-stage Boss Battle design |
| Death List leakage | ✅ LOW | No speed/compass/cells triggers detected |

### Recommended Execution Order

1. **FORGE** P5-H1-RatioEquation, P5-H2-RatioRemainder, P5-H3-EquationFraction (3 transition nodes)
2. **VERIFY** CLS gradients with new P5 bridges (all should drop below 1.5)
3. **EXTRACT** Pure nodes first: Q5 (Thread A), Q6 (Thread C), Q8 (Thread D)
4. **EXTRACT** Dual-hybrid nodes: Q7 (A+C), Q9 (A+D) — with dual-parentage enforced
5. **EXTRACT** Triple-hybrid Q10 last — with triple-parentage and "Boss Fight: Odyssey Level" tag
6. **GRAPHIFY** Sync after full batch

### REPORT

"Rule 6 Audit Complete. 3 PURE nodes safe for immediate extraction. 3 HYBRID nodes require P5 Transition Bridges before extraction. Bridge Deficit: 3 P5 nodes. Game Smith: Hybrid fusion feasible for all nodes. Awaiting CEO directive to forge P5 bridges."

---

*Risk Brief generated by Auditor v2.1. Classification: PRE-EXTRACTION. All projections based on typical Rosyth CA1 exam patterns and current spine infrastructure.*
