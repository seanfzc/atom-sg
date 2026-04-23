#!/usr/bin/env python3
"""
ATOM-SG Minimal Node Forge (v1.0)
Lightweight script to stamp out new Atomic Unit nodes in /Second_Brain/.

Usage:
  python3 forge_node.py

Edit the forge_node() call at the bottom to create new nodes.
"""

import os


def forge_node(node_id, topic, trigger, formula, seed, mode, output_dir="./Second_Brain/"):
    template = f"""---
node_id: {node_id}
source: "Rosyth 2026 P6 Math"
topic: "{topic}"
triad_axis:
  linguistic: "Trigger: {trigger}"
  visual: "Template: To be assigned by Architect"
  logic: "Formula: {formula}"
vertical_continuity:
  seed_node: "{seed}"
bimodal_calibration:
  mode: "{mode}"
---
# {node_id} Logic Breakdown
(Populate with Neo Pipeline output here...)
"""
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{node_id}.md")
    with open(file_path, "w") as f:
        f.write(template)
    print(f"✅ Node {node_id} forged at {file_path}")


# Example Usage:
# forge_node("ROSYTH-P6-ALG-03", "Simplifying Expressions", "Sum of", "3x + 5x = 8x", "P1-N1-PartWhole", "Mode A")
