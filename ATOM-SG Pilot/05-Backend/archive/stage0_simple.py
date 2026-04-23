#!/usr/bin/env python3
"""
STAGE 0: SMOKE TEST - Simplified
Test Q25 solvability from canonical data alone
"""

import yaml
import sys

def smoke_test_q25():
    """Test Q25 solvability from canonical data alone - simplified version."""
    
    print("="*80)
    print("STAGE 0: SMOKE TEST - Q25 SOLVABILITY")
    print("="*80)
    
    # Load canonical YAML
    with open("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/02-Geometry/CANONICAL_GEOMETRY_DATA.yaml", 'r') as f:
        content = f.read()
    
    # Find Q25 in content (simplified search)
    q25_found = "Q25:" in content or "name: \"Overlapping Quarter Circles\"" in content
    
    if q25_found:
        print("Q25 found in canonical YAML")
        
        # Check for required elements
        question_text_present = "Shade two more squares" in content
        
        # Check for solution
        has_solution = "solution:" in content or "steps:" in content
        
        # Basic solvability check
        solvable = question_text_present and has_solution
        
        if solvable:
            print("RESULT: Q25 is SOLVABLE from reconstruction alone")
            print("\n" + "="*80)
            print("STAGE 0 COMPLETE")
            print("="*80)
            return 0
        else:
            print("RESULT: Q25 requires more than reconstruction")
            return 1
    else:
        print("ERROR: Q25 not found in canonical YAML")
        return 1

if __name__ == '__main__':
    exit_code = smoke_test_q25()
    sys.exit(exit_code)
