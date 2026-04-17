---
dashboard: risks
title: Risks Dashboard
description: Track project risks with severity, impact, and mitigation status.
---

```dataview
TABLE severity, impact, status, assigned, mitigation
FROM "ATOM-SG Pilot"
WHERE type = "risk"
SORT severity DESC, status ASC
```

## Columns Description
- **severity**: High / Medium / Low
- **impact**: Description of potential impact on project
- **status**: Open / Mitigated / Closed
- **assigned**: Owner responsible for mitigation
- **mitigation**: Planned or applied mitigation actions

## How to Add Risks
1. Create a new note in the appropriate folder (e.g., `01-Projects/Risk-001.md`)
2. Include the following frontmatter:

```yaml
---
type: risk
id: Risk-001
severity: High
impact: "Description of impact"
status: Open
assigned: "@owner"
mitigation: "Planned actions"
dateIdentified: 2026-04-12
---
```

3. The dashboard will automatically include the risk.

## Current Summary
```dataviewjs
const risks = dv.pages('"ATOM-SG Pilot"').filter(p => p.type === "risk");
const total = risks.length;
const open = risks.filter(r => r.status === "Open").length;
const high = risks.filter(r => r.severity === "High").length;
const mitigated = risks.filter(r => r.status === "Mitigated").length;

dv.header(3, "Risk Summary");
dv.list([
	`Total risks: ${total}`,
	`Open risks: ${open}`,
	`High severity: ${high}`,
	`Mitigated: ${mitigated}`
]);
```