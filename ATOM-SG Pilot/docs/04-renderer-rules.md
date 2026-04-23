# Renderer Rules — What to Draw, What to Hide

**Prerequisites:** `01-rendering-gates.md`, `02-label-arrow-rules.md`

---

## The Rule

**Render only what a student sees on the printed exam page. Nothing more.**

The renderer reads the `diagram:` section of the YAML only. It ignores `question:`, `solution:`, `answer:`, and all metadata. If the YAML is not separated into sections, apply this filter: if a field contains "derived", "calculated", "solution", "answer", "confidence", or "source" — skip it.

---

## Never Render (HIDE List)

These must never appear on a reconstructed exam diagram:

- **Calculated answers** — "x = 147°", "y = 84°", "2 2/3 minutes"
- **Working steps and equations** — "x + 33° = 180°", "80,000 ÷ 30,000 = 2.67"
- **Derived quantities** — "Total volume: 240,000 cm³", "Rate: 30,000 cm³/min"
- **Inter-point calculations on graphs** — "Day 1: 120 − 96 = 24 sold"
- **Summary/answer boxes** — "Most sold: Day 4 (28 T-shirts)"
- **Value badges on graph data points** — "96", "76", "60" next to dots. Students read values from gridlines — that is part of the test.
- **Solution legends or colour keys** — "Rhombus ABCD / Trapezium ADEF" unless on the original
- **Pipeline metadata** — confidence scores, source tags, timestamps, tool names

**If in doubt:** look at the original exam page. If the text does not appear there, do not render it.

---

## Pre-Render Checklist

```
□ No calculated answers visible anywhere on the diagram
□ No working steps, equations, or derivations visible
□ No derived values (volumes, rates, totals, percentages) visible
□ No data point value labels unless present on the original
□ No summary or answer boxes
□ No metadata (confidence, source, pipeline)
□ All elements from the original ARE present (no missing labels, arrows, icons, "?")
□ A student sees exactly the same information as on the printed page — no more, no less
```
