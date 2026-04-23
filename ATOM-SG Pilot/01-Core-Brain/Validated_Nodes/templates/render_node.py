#!/usr/bin/env python3
"""
ATOM-SG Node Renderer (v1.0)
Renders a new Atomic Unit node from the combined template.

Usage:
  python3 render_node.py --config node_config.json --output ../ROSYTH-P6-ALG-03.md

The config JSON should contain key-value pairs matching the {{PLACEHOLDER}} 
fields in atomic_node_template.md.
"""

import argparse
import json
import os
import re
import sys

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(TEMPLATE_DIR, "atomic_node_template.md")


def load_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def render(template: str, config: dict) -> str:
    """Replace all {{KEY}} placeholders with values from config."""
    rendered = template
    for key, value in config.items():
        placeholder = "{{" + key + "}}"
        # Convert lists to comma-separated quoted strings for YAML arrays
        if isinstance(value, list):
            value = ", ".join(f'"{v}"' for v in value)
        # Convert numbers to string for replacement
        rendered = rendered.replace(placeholder, str(value))

    # Warn about any remaining placeholders
    remaining = re.findall(r"\{\{(\w+)\}\}", rendered)
    if remaining:
        print(f"Warning: Unfilled placeholders: {remaining}", file=sys.stderr)

    return rendered


def main():
    parser = argparse.ArgumentParser(
        description="Render an ATOM-SG Atomic Unit node from template + config."
    )
    parser.add_argument(
        "--config", required=True, help="Path to JSON config file with node fields."
    )
    parser.add_argument(
        "--output", required=True, help="Output path for the rendered .md file."
    )
    parser.add_argument(
        "--template",
        default=TEMPLATE_FILE,
        help="Path to template file (default: atomic_node_template.md in same dir).",
    )

    args = parser.parse_args()

    template = load_template(args.template)
    config = load_config(args.config)
    rendered = render(template, config)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"✅ Node rendered: {args.output}")
    print(f"   Node ID: {config.get('NODE_ID', 'UNKNOWN')}")
    print(f"   Bimodal: {config.get('BIMODAL_MODE', 'UNKNOWN')}")
    print(f"   MOE Code: {config.get('MOE_CODE', 'UNKNOWN')}")
    print(f"   Seed: {config.get('SEED_NODE', 'UNKNOWN')}")


if __name__ == "__main__":
    main()
