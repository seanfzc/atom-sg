# Issue: subagents list showing stale/cached data

## Problem
When checking sub-agent status via `subagents list`, the system returns outdated information:

**Example:**
- Sub-agent actually completed at: Wed 2026-04-15 14:32
- User asked for update at: Wed 2026-04-15 15:25
- `subagents list` showed: "running 14m24s" (incorrect - showed only 14m elapsed instead of 53m)

## Impact
- Misleading status reports to users
- Incorrect decision-making based on stale data
- User confusion about task completion status

## Root Cause
The `subagents list` command appears to cache sub-agent status information and does not refresh in real-time for completed tasks.

## Recommended Fix (for OpenClaw Team)
1. Make `subagents list` always return real-time data
2. Add a `lastUpdated` timestamp to each sub-agent entry
3. Consider removing completed sub-agents from the "active" list after a short grace period
4. Add an explicit `subagents status --session-id <id>` command for checking individual sub-agent status

## Workaround for Now (for Agent Behavior)
Before reporting sub-agent status to users:
1. **Check for expected output files** (existence + file timestamp)
2. **If file exists and was created recently**, consider task complete
3. **Do not rely solely on `subagents list`** for completion status

## Example Workaround Implementation
```javascript
// Instead of:
const status = await subagents.list();
if (status.active.some(s => s.sessionId === expectedId)) {
  reply("Still running...");
}

// Use:
const expectedFile = workspacePath + "/EXPECTED_OUTPUT.md";
if (fs.existsSync(expectedFile)) {
  const stats = fs.statSync(expectedFile);
  const ageMinutes = (Date.now() - stats.mtimeMs) / 60000;
  if (ageMinutes < 60) {
    reply(`Completed ${ageMinutes.toFixed(0)} minutes ago`);
  }
}
```

## Agent Behavior Update Required
- When user asks for updates on sub-agent tasks:
  1. First check if expected output file exists
  2. Check file modification time
  3. Only use `subagents list` as secondary confirmation
  4. If discrepancy exists, trust file timestamps over subagents list

## Filed By
- Who: Zcaethbot (main agent)
- When: Wed 2026-04-15 15:30 GMT+8
- Context: UX test deep dive sub-agent completion status check
- User feedback: "you did not tell me you were done previously"

---

*This issue should be addressed by OpenClaw development team. In the meantime, agents will use file-based verification for sub-agent completion status.*
