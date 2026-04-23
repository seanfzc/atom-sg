#!/usr/bin/env python3
"""
Matplotlib template for pastel-colored bar models.
"""

import matplotlib.pyplot as plt
import matplotlib
from typing import List, Dict, Any
import yaml
import sys
import os

# Set pastel color palette
PASTEL_COLORS = [
    "#FFB6C1",  # Light Pink
    "#98FB98",  # Pale Green
    "#87CEEB",  # Sky Blue
    "#FFD700",  # Gold
    "#DDA0DD",  # Plum
    "#F0E68C",  # Khaki
    "#E0FFFF",  # Light Cyan
    "#FFE4E1",  # Misty Rose
]

def create_bar_model(labels: List[str], values: List[float], colors: List[str] = None,
                     title: str = "Bar Model", output_path: str = "bar_model.svg") -> None:
    """
    Create a pastel-colored bar chart and save as SVG.
    """
    if colors is None:
        colors = PASTEL_COLORS[:len(labels)]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                 f'{height}', ha='center', va='bottom', fontsize=12)
    
    plt.title(title, fontsize=16, pad=20)
    plt.ylabel('Value', fontsize=14)
    plt.ylim(0, max(values) * 1.2)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Remove top and right spines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(output_path, format='svg')
    plt.close()
    print(f"Saved bar model to {output_path}")

def load_problem_card(yaml_path: str) -> Dict[str, Any]:
    """Load a problem card YAML file."""
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    # Example standalone usage
    if len(sys.argv) > 1:
        card = load_problem_card(sys.argv[1])
        data = card.get('data', {})
        create_bar_model(
            labels=data.get('labels', ['A', 'B']),
            values=data.get('values', [30, 20]),
            colors=data.get('colors'),
            title=card.get('title', 'Bar Model'),
            output_path='output.svg'
        )
    else:
        # Demo with sample data
        create_bar_model(
            labels=['Part A', 'Part B', 'Part C'],
            values=[45, 30, 25],
            title='Sample Bar Model'
        )