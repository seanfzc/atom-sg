# Word Problems Track - ATOM-SG Pilot

## Overview
This directory contains 20 word problems for the Week 1 Baseline Test, covering the key pathways identified from analysis of 94 questions across 5 elite-school prelim papers.

## Problem Distribution

### Pathway Breakdown

| Pathway | Count | Problem IDs |
|---------|-------|-------------|
| **Before-After Change** | 6 | WP001, WP002, WP007, WP009, WP012, WP019 |
| **Part-Whole with Comparison** | 7 | WP003, WP004, WP008, WP013, WP015, WP017, WP020 |
| **Cross-Thread Collision** | 5 | WP005, WP006, WP010, WP011, WP014, WP018 |
| **Data Interpretation** | 0 | (Located in 01-Projects/Baseline/) |

### Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| Easy | 5 |
| Medium | 10 |
| Hard | 5 |

## File Structure

```
03-WordProblems/
├── README.md
├── problems/
│   ├── WP001.md (Before-After, Easy)
│   ├── WP002.md (Before-After, Medium)
│   ├── WP003.md (Part-Whole, Easy)
│   ├── WP004.md (Part-Whole, Medium)
│   ├── WP005.md (Cross-Thread, Medium)
│   ├── WP006.md (Cross-Thread, Hard)
│   ├── WP007.md (Before-After, Medium)
│   ├── WP008.md (Part-Whole, Medium)
│   ├── WP009.md (Before-After, Easy)
│   ├── WP010.md (Part-Whole, Hard)
│   ├── WP011.md (Cross-Thread, Hard)
│   ├── WP012.md (Before-After, Medium)
│   ├── WP013.md (Part-Whole, Easy)
│   ├── WP014.md (Cross-Thread, Medium)
│   ├── WP015.md (Part-Whole, Medium)
│   ├── WP016.md (Before-After, Hard)
│   ├── WP017.md (Part-Whole, Hard)
│   ├── WP018.md (Cross-Thread, Hard)
│   ├── WP019.md (Before-After, Medium)
│   └── WP020.md (Part-Whole, Medium)
```

## Problem Format

Each problem file includes:
- **problemID**: Unique identifier (WP001-WP020)
- **pathwayType**: Classification for recognition training
- **difficulty**: Easy, Medium, or Hard
- **equationShadow**: Expected student articulation
- **traps**: Common mistakes and misconceptions
- **question**: Problem statement
- **answer**: Correct answer
- **solutionSteps**: Step-by-step solution
- **articulationRubric**: 3-level rubric for assessing student articulation

## Integration with Baseline Test

These 20 Word Problems combine with:
- **12 Geometry problems** (from 02-Geometry/problems/)
- **8 Data Interpretation problems** (from 01-Projects/Baseline/)

To form the complete **40-question Week 1 Baseline Test**.

## Usage

1. **Baseline Test Generation**: Use these problems to generate the printable PDF
2. **Gap Map Analysis**: OCR scans identify which pathways are weakest
3. **Intervention Training**: Focus on the 3 weakest pathways from Weeks 2-4
4. **Transfer Test**: Week 5 uses new unseen problems from same pathways

## Source

Problems created based on:
- Analysis of 94 questions from 5 elite-school prelim papers (ACS Junior, Nanyang, Henry Park, Nan Hua, RGPS)
- Statement of Requirements v4.1 pathway distribution
- Common P6 exam question patterns and traps

## Created

2026-04-19 - Created as part of MVP baseline test pack completion.
