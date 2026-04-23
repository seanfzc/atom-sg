#!/usr/bin/env python3
"""
Documentation Consistency Verification Script
Ensures all ATOM-SG documentation is synchronized and consistent.

Usage: python verify_documentation_consistency.py
"""

import re
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent

def check_version_consistency():
    """Verify VERSION.md matches other documents."""
    errors = []
    
    # Read VERSION.md
    version_file = PROJECT_ROOT / "00-Templates" / "VERSION.md"
    if not version_file.exists():
        errors.append("VERSION.md not found")
        return errors
    
    version_content = version_file.read_text()
    
    # Extract version
    version_match = re.search(r'\*\*Current Version:\*\*\s*([\d.]+)', version_content)
    if not version_match:
        errors.append("VERSION.md: No version number found")
        return errors
    
    version = version_match.group(1)
    
    # Check README.md
    readme = PROJECT_ROOT / "README.md"
    if readme.exists():
        readme_content = readme.read_text()
        if f"**Version:** {version}" not in readme_content:
            errors.append(f"README.md: Version mismatch (expected {version})")
    
    # Check INDEX.md
    index = PROJECT_ROOT / "INDEX.md"
    if index.exists():
        index_content = index.read_text()
        if f"**Version:** {version}" not in index_content:
            errors.append(f"INDEX.md: Version mismatch (expected {version})")
    
    # Check CHANGELOG.md
    changelog = PROJECT_ROOT / "00-Templates" / "CHANGELOG.md"
    if changelog.exists():
        changelog_content = changelog.read_text()
        if f"## [{version}]" not in changelog_content:
            errors.append(f"CHANGELOG.md: Version {version} not documented")
    
    return errors

def check_required_documents():
    """Verify all required documents exist."""
    required = [
        "README.md",
        "INDEX.md",
        "MODEL_USAGE_POLICY.md",
        "00-Templates/VERSION.md",
        "00-Templates/CHANGELOG.md",
        "00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md",
        "00-Templates/Visual-Reconstruction-Spec.md",
        "00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md",
        "01-Projects/KANBAN.md",
        "01-Projects/SubAgentComms.md",
    ]
    
    errors = []
    for doc in required:
        path = PROJECT_ROOT / doc
        if not path.exists():
            errors.append(f"Missing required document: {doc}")
    
    return errors

def check_cross_references():
    """Verify cross-references between documents."""
    errors = []
    
    # Check that INDEX.md references all major docs
    index = PROJECT_ROOT / "INDEX.md"
    if index.exists():
        index_content = index.read_text()
        
        required_refs = [
            "ATOM-SG_FRAMEWORK_REVISION_v2.md",
            "COMPREHENSIVE_GAP_ANALYSIS.md",
            "Visual-Reconstruction-Spec.md",
            "MODEL_USAGE_POLICY.md",
        ]
        
        for ref in required_refs:
            if ref not in index_content:
                errors.append(f"INDEX.md: Missing reference to {ref}")
    
    return errors

def check_date_consistency():
    """Verify dates are current across documents."""
    errors = []
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Check VERSION.md
    version_file = PROJECT_ROOT / "00-Templates" / "VERSION.md"
    if version_file.exists():
        content = version_file.read_text()
        if f"Last Updated:** {today}" not in content:
            errors.append("VERSION.md: Date may be outdated")
    
    return errors

def main():
    """Run all consistency checks."""
    print("=" * 60)
    print("ATOM-SG Documentation Consistency Check")
    print("=" * 60)
    
    all_errors = []
    
    print("\n1. Checking version consistency...")
    errors = check_version_consistency()
    all_errors.extend(errors)
    if errors:
        for e in errors:
            print(f"   ❌ {e}")
    else:
        print("   ✅ Version consistent across documents")
    
    print("\n2. Checking required documents...")
    errors = check_required_documents()
    all_errors.extend(errors)
    if errors:
        for e in errors:
            print(f"   ❌ {e}")
    else:
        print("   ✅ All required documents present")
    
    print("\n3. Checking cross-references...")
    errors = check_cross_references()
    all_errors.extend(errors)
    if errors:
        for e in errors:
            print(f"   ❌ {e}")
    else:
        print("   ✅ Cross-references valid")
    
    print("\n4. Checking date consistency...")
    errors = check_date_consistency()
    all_errors.extend(errors)
    if errors:
        for e in errors:
            print(f"   ⚠️  {e}")
    else:
        print("   ✅ Dates current")
    
    print("\n" + "=" * 60)
    if all_errors:
        print(f"Found {len(all_errors)} issue(s). Please fix before committing.")
        return 1
    else:
        print("All consistency checks passed! ✅")
        return 0

if __name__ == "__main__":
    exit(main())
