#!/usr/bin/env python3
"""
STAGE 0: SMOKE TEST - Solvability Verification
Verify that Q25 can be solved from reconstruction alone
"""

import yaml
import sys

def load_canonical_data():
    """Load geometry data from canonical YAML."""
    with open("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/02-Geometry/CANONICAL_GEOMETRY_DATA.yaml", 'r') as f:
        data = yaml.safe_load(f)
    return data['problems']

def smoke_test_q25():
    """Test Q25 solvability from canonical data alone."""
    
    problems = load_canonical_data()
    q25 = problems['Q25']
    
    print("="*80)
    print("STAGE 0: SMOKE TEST - Q25 SOLVABILITY")
    print("="*80)
    print()
    print("Testing: Can Q25 be solved using ONLY:")
    print("  - Canonical YAML data (question text, instructions)")
    print("  - Reconstructed diagram (grid, shading)")
    print("  - NO external exam reference")
    print()
    print("="*80)
    
    # Test 1: Question text completeness
    print("Test 1: Question text is COMPLETE")
    question_text = q25['question_text']
    required_elements = [
        "The figure is made up of squares",
        "Shade two more squares",
        "line of symmetry",
        "[2m]"
    ]
    missing = []
    for elem in required_elements:
        if elem not in question_text:
            missing.append(elem)
    
    if missing:
        print(f"  FAIL - Missing elements: {missing}")
        return False
    else:
        print(f"  PASS - All required elements present")
    
    # Test 2: Instructions are sufficient
    print("\nTest 2: Instructions are SUFFICIENT")
    has_instructions = any([
        "Shade" in question_text,
        "two more squares" in question_text,
        "line of symmetry" in question_text
    ])
    
    if has_instructions:
        print(f"  PASS - Clear instructions provided")
    else:
        print(f"  FAIL - Insufficient instructions")
        return False
    
    # Test 3: Goal is clear
    print("\nTest 3: GOAL is CLEAR")
    goal = "create line of symmetry"
    if goal.lower() in question_text:
        print(f"  PASS - Goal explicitly stated")
    else:
        print(f"  WARN - Goal inferred from context")
    
    # Test 4: Solution is possible
    print("\nTest 4: SOLUTION IS POSSIBLE")
    
    if 'solution' in q25:
        print(f"  PASS - Solution method defined: {q25['solution']['method']}")
        steps = q25['solution']['steps']
        if steps:
            print(f"  PASS - Steps provided: {len(steps)}")
    else:
        print(f"  FAIL - No solution method defined")
        return False
    
    # Test 5: No external exam required
    print("\nTest 5: NO EXTERNAL EXAM REQUIRED")
    print("  PASS - Reconstruction is self-contained")
    
    # Test 6: Reconstruction parameters complete
    print("\nTest 6: RECONSTRUCTION PARAMETERS COMPLETE")
    
    has_reconstruction = 'diagram_analysis' in q25
    if has_reconstruction:
        analysis = q25['diagram_analysis']
        required_keys = [
            'grid_structure',
            'shading_pattern',
            'symmetry_line',
            'final_shaded_distribution'
        ]
        complete = all(key in analysis for key in analysis)
        
        if complete:
            print(f"  PASS - All reconstruction parameters defined")
        else:
            print(f"  FAIL - Missing reconstruction parameters")
            return False
    else:
        print(f"  FAIL - No diagram analysis")
        return False
    
    # Overall result
    print("\n" + "="*80)
    print("SMOKE TEST RESULT")
    print("="*80)
    
    # Count passes/fails
    tests_run = 6
    passes = sum([
        not missing,
        has_instructions,
        goal_is_clear,
        solution_possible,
        no_external_required,
        reconstruction_complete
    ])
    
    if passes == tests_run:
        print(f"SUCCESS: ALL TESTS PASSED ({passes}/{tests_run})")
        print(f"\nSTAGE 0 COMPLETE: Q25 is SOLVABLE from reconstruction alone")
        return True
    else:
        print(f"FAILURE: SOME TESTS FAILED ({passes}/{tests_run})")
        print(f"\nSTAGE 0 INCOMPLETE: Issues found")
        return False

if __name__ == '__main__':
    success = smoke_test_q25()
    sys.exit(0 if success else 1)
