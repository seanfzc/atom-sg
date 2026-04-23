#!/usr/bin/env python3
"""
Generate 8 UNIQUE Data Interpretation visuals for v3.0
Each question gets its own unique data set and chart
"""

import sys
sys.path.insert(0, '/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend')

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).parent / "artifacts" / "renders" / "exam-quality-baseline-v3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# MOE Pastel Color Scheme
MOE_COLORS = {
    'primary': '#5B9BD5',
    'secondary': '#ED7D31',
    'accent': '#70AD47',
    'highlight': '#FFC000',
    'neutral': '#A5A5A5',
    'purple': '#9F6CD4',
    'teal': '#4ECDC4',
    'coral': '#FF6B6B',
}

def create_line_graph_q33():
    """Q33: T-shirt sales - unsold over 7 days."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    unsold = [120, 95, 70, 45, 30, 20, 15]
    
    ax.plot(days, unsold, marker='o', markersize=8, linewidth=2.5, 
            color=MOE_COLORS['primary'], markerfacecolor='white', 
            markeredgewidth=2, markeredgecolor=MOE_COLORS['primary'])
    
    # Add value labels
    for i, (day, val) in enumerate(zip(days, unsold)):
        ax.text(i, val + 5, str(val), ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Day', fontsize=11, fontweight='bold')
    ax.set_ylabel('T-shirts Unsold', fontsize=11, fontweight='bold')
    ax.set_title('Q33: T-shirt Inventory Over One Week', fontsize=12, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(0, 140)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q33_line_graph.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q33: Line graph - T-shirt sales")

def create_line_graph_q34():
    """Q34: Temperature over a week - DIFFERENT data."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temp = [28, 31, 33, 30, 27, 29, 32]
    
    ax.plot(days, temp, marker='s', markersize=8, linewidth=2.5, 
            color=MOE_COLORS['secondary'], markerfacecolor='white',
            markeredgewidth=2, markeredgecolor=MOE_COLORS['secondary'])
    
    for i, (day, val) in enumerate(zip(days, temp)):
        ax.text(i, val + 0.8, f'{val}°C', ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Day', fontsize=11, fontweight='bold')
    ax.set_ylabel('Temperature (°C)', fontsize=11, fontweight='bold')
    ax.set_title('Q34: Daily Temperature Record', fontsize=12, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(24, 36)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q34_line_graph.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q34: Line graph - Temperature (DIFFERENT from Q33)")

def create_bar_chart_q35():
    """Q35: Books read by students."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    students = ['Ali', 'Ben', 'Cal', 'Dan', 'Eve']
    books = [12, 8, 15, 6, 10]
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent'], 
                   MOE_COLORS['highlight'], MOE_COLORS['neutral']]
    
    bars = ax.bar(students, books, color=colors_list, edgecolor='black', linewidth=1.5, width=0.6)
    
    for bar, val in zip(bars, books):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylabel('Number of Books', fontsize=11, fontweight='bold')
    ax.set_xlabel('Student', fontsize=11, fontweight='bold')
    ax.set_title('Q35: Books Read During Holidays', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylim(0, 18)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q35_bar_chart.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q35: Bar chart - Books read")

def create_bar_chart_q36():
    """Q36: Test scores - DIFFERENT data."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    subjects = ['Math', 'Science', 'English', 'Chinese', 'Art']
    scores = [85, 72, 68, 78, 90]
    colors_list = [MOE_COLORS['purple'], MOE_COLORS['teal'], MOE_COLORS['coral'],
                   MOE_COLORS['accent'], MOE_COLORS['highlight']]
    
    bars = ax.bar(subjects, scores, color=colors_list, edgecolor='black', linewidth=1.5, width=0.6)
    
    for bar, val in zip(bars, scores):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylabel('Score', fontsize=11, fontweight='bold')
    ax.set_xlabel('Subject', fontsize=11, fontweight='bold')
    ax.set_title('Q36: Test Scores by Subject', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q36_bar_chart.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q36: Bar chart - Test scores (DIFFERENT from Q35)")

def create_pie_chart_q37():
    """Q37: Isabelle's spending."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    
    labels = ['Transport\n24%', 'Food\n60%', 'Savings\n6%', 'Clothes\n10%']
    sizes = [24, 60, 6, 10]
    colors_list = [MOE_COLORS['primary'], MOE_COLORS['secondary'], MOE_COLORS['accent'], MOE_COLORS['neutral']]
    explode = (0.03, 0.03, 0.03, 0.03)
    
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors_list,
                                       autopct='%1.0f%%', startangle=90,
                                       wedgeprops=dict(edgecolor='black', linewidth=1.5),
                                       textprops={'fontsize': 9})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax.set_title("Q37: Isabelle's Monthly Allowance", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q37_pie_chart.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q37: Pie chart - Spending")

def create_pie_chart_q38():
    """Q38: Fruit distribution - DIFFERENT data."""
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    
    labels = ['Apples\n20%', 'Oranges\n35%', 'Bananas\n25%', 'Grapes\n20%']
    sizes = [20, 35, 25, 20]
    colors_list = [MOE_COLORS['coral'], MOE_COLORS['secondary'], MOE_COLORS['highlight'], MOE_COLORS['purple']]
    explode = (0.03, 0.03, 0.03, 0.03)
    
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors_list,
                                       autopct='%1.0f%%', startangle=45,
                                       wedgeprops=dict(edgecolor='black', linewidth=1.5),
                                       textprops={'fontsize': 9})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax.set_title("Q38: Fruit Basket Distribution", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q38_pie_chart.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q38: Pie chart - Fruits (DIFFERENT from Q37)")

def create_line_graph_q39():
    """Q39: Website visitors - DIFFERENT data."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    hours = ['8am', '10am', '12pm', '2pm', '4pm', '6pm', '8pm']
    visitors = [45, 120, 180, 150, 95, 200, 80]
    
    ax.plot(hours, visitors, marker='D', markersize=7, linewidth=2.5, 
            color=MOE_COLORS['accent'], markerfacecolor='white',
            markeredgewidth=2, markeredgecolor=MOE_COLORS['accent'])
    
    for i, (hour, val) in enumerate(zip(hours, visitors)):
        ax.text(i, val + 8, str(val), ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Time of Day', fontsize=11, fontweight='bold')
    ax.set_ylabel('Number of Visitors', fontsize=11, fontweight='bold')
    ax.set_title('Q39: Website Traffic by Hour', fontsize=12, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(0, 230)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q39_line_graph.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q39: Line graph - Website traffic (DIFFERENT from Q33/Q34)")

def create_line_graph_q40():
    """Q40: Plant growth - DIFFERENT data."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    
    weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6']
    height = [5, 8, 12, 15, 22, 28]
    
    ax.plot(weeks, height, marker='*', markersize=12, linewidth=2.5, 
            color=MOE_COLORS['purple'], markerfacecolor=MOE_COLORS['highlight'],
            markeredgewidth=1.5, markeredgecolor='black')
    
    for i, (week, val) in enumerate(zip(weeks, height)):
        ax.text(i, val + 1, f'{val}cm', ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Time', fontsize=11, fontweight='bold')
    ax.set_ylabel('Height (cm)', fontsize=11, fontweight='bold')
    ax.set_title('Q40: Plant Growth Over 6 Weeks', fontsize=12, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(0, 32)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'Q40_line_graph.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Q40: Line graph - Plant growth (DIFFERENT from Q33/Q34/Q39)")

# Generate all DI charts
print("=" * 60)
print("GENERATING 8 UNIQUE DATA INTERPRETATION VISUALS")
print("=" * 60)

create_line_graph_q33()
create_line_graph_q34()
create_bar_chart_q35()
create_bar_chart_q36()
create_pie_chart_q37()
create_pie_chart_q38()
create_line_graph_q39()
create_line_graph_q40()

print("\n✅ All 8 DI charts generated - EACH QUESTION HAS UNIQUE DATA")
