---
dashboard: problem-bank
title: Problem Bank Dashboard
description: Overview of problem cards grouped by pathway, difficulty, and geometry vs non-geometry.
---

```dataview
TABLE pathwayType, difficulty, COUNT(*) AS count
FROM "ATOM-SG Pilot"
WHERE type = "problem"
GROUP BY pathwayType, difficulty
SORT pathwayType ASC
```

## Geometry vs Non-Geometry Breakdown
```dataviewjs
const problems = dv.pages('"ATOM-SG Pilot"').filter(p => p.type === "problem");
const geometry = problems.filter(p => p.pathwayType && p.pathwayType.startsWith("geometry_"));
const nonGeometry = problems.filter(p => p.pathwayType && !p.pathwayType.startsWith("geometry_"));

dv.header(3, "Geometry vs Non-Geometry");
dv.list([
	`Total problems: ${problems.length}`,
	`Geometry problems: ${geometry.length}`,
	`Non-geometry problems: ${nonGeometry.length}`
]);
```

## Difficulty Distribution
```dataviewjs
const problems = dv.pages('"ATOM-SG Pilot"').filter(p => p.type === "problem");
const byDifficulty = {};
problems.forEach(p => {
	const d = p.difficulty || "Unknown";
	byDifficulty[d] = (byDifficulty[d] || 0) + 1;
});

dv.header(3, "Difficulty Distribution");
dv.table(["Difficulty", "Count"], Object.entries(byDifficulty).map(([k, v]) => [k, v]));
```

## Pathway Type Summary
```dataviewjs
const problems = dv.pages('"ATOM-SG Pilot"').filter(p => p.type === "problem");
const byPathway = {};
problems.forEach(p => {
	const pt = p.pathwayType || "Unknown";
	byPathway[pt] = (byPathway[pt] || 0) + 1;
});

dv.header(3, "Pathway Type Counts");
dv.table(["Pathway Type", "Count"], Object.entries(byPathway).map(([k, v]) => [k, v]));
```

## How to Add Problems
1. Use the `Problem-Card.md` template in `00-Templates`.
2. Ensure the frontmatter includes:
```yaml
---
type: problem
problemID: P5-Problem-001
pathwayType: geometry_measurement
difficulty: Easy
source: "P5 Exam 2025"
equationShadow: "Angle measurement = reading from protractor"
traps: "Misreading protractor scale"
visualNotes: ""
expectedArtifacts: "PDF render, rubric"
notes: ""
---
```
3. The dashboard will automatically include the problem.

## Notes
- `pathwayType` determines geometry vs non-geometry (geometry_* prefix).
- `difficulty` should be one of: Easy, Medium, Hard (or custom levels).
- For accurate counts, ensure all problem cards have `type: problem` in frontmatter.