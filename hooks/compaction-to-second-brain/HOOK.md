---
name: compaction-to-second-brain
description: "Save compaction summaries to second brain raw folder"
metadata:
  openclaw:
    emoji: "🧠"
    events:
      - session:compact:after
    requires:
      config:
        - workspace.dir
---

# Compaction to Second Brain

When OpenClaw compacts a conversation to stay within token limits, this hook saves the compaction metadata and summary to the second brain raw folder for later reference and education-focused analysis.

## What it does

1. Listens for `session:compact:after` events
2. Creates a markdown file in `second-brain-simple/raw/conversations/` with:
   - Compaction timestamp
   - Token counts before/after
   - Number of messages compacted
   - Summary length
   - Session metadata
3. Tags the file for education transformation potential

## Configuration

No configuration needed. Assumes second brain is located at `<workspace>/second-brain-simple/`.

## Education Lens

The saved file includes prompts for education transformation:
- How could this conversation be turned into a learning game?
- What concepts were discussed that could be simplified for children?
- What critical thinking patterns emerged?

This ensures Sean's professional conversations contribute to his sons' educational development.