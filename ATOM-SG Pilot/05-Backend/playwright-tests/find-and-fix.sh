#!/bin/bash
# Find and Fix Script
# Automatically finds common interaction issues and fixes them

echo "╔════════════════════════════════════════════════════════╗"
echo "║     Find & Fix: Automated Issue Detection             ║"
echo "╚════════════════════════════════════════════════════════╝"

FRONTEND_DIR="../frontend/static/js"
HTML_DIR="../frontend"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo "🔍 Scanning for common issues..."
echo ""

# Issue 1: e.preventDefault() blocking anchor tags
echo "1️⃣  Checking for e.preventDefault() blocking links..."
PREVENT_DEFAULT_COUNT=$(grep -r "preventDefault" $FRONTEND_DIR --include="*.js" | wc -l)
if [ $PREVENT_DEFAULT_COUNT -gt 0 ]; then
    echo "   ${YELLOW}Found $PREVENT_DEFAULT_COUNT preventDefault calls${NC}"
    grep -rn "preventDefault" $FRONTEND_DIR --include="*.js" | head -5
    
    # Check if any are on print-baseline
    if grep -q "print-baseline" $FRONTEND_DIR/baseline.js; then
        echo "   ${YELLOW}⚠️  baseline.js has preventDefault on print button${NC}"
        
        # Auto-fix: Comment out the preventDefault
        if grep -q "e.preventDefault()" $FRONTEND_DIR/baseline.js; then
            echo "   🔧 Auto-fixing..."
            sed -i.backup 's/e\.preventDefault();/\/\/ e.preventDefault(); \/\/ REMOVED: was blocking anchor tag/' $FRONTEND_DIR/baseline.js
            echo "   ${GREEN}✅ Fixed baseline.js${NC}"
        fi
    fi
else
    echo "   ${GREEN}✅ No preventDefault issues found${NC}"
fi

# Issue 2: Missing target="_blank" on PDF links
echo ""
echo "2️⃣  Checking PDF links for target=\"_blank\"..."
PDF_LINKS=$(grep -rn "api/v1/problems/pdf" $HTML_DIR --include="*.html" | grep -v "target=" | wc -l)
if [ $PDF_LINKS -gt 0 ]; then
    echo "   ${YELLOW}Found $PDF_LINKS PDF links without target=\"_blank\"${NC}"
    grep -rn "api/v1/problems/pdf" $HTML_DIR --include="*.html" | grep -v "target="
else
    echo "   ${GREEN}✅ All PDF links have target=\"_blank\"${NC}"
fi

# Issue 3: Check for null element references
echo ""
echo "3️⃣  Checking for potential null element references..."
NULL_CHECKS=$(grep -rn "getElementById.*addEventListener" $FRONTEND_DIR --include="*.js" | wc -l)
NULL_SAFE=$(grep -rn "getElementById.*if.*null" $FRONTEND_DIR --include="*.js" | wc -l)
echo "   Found $NULL_CHECKS addEventListener calls"
echo "   Found $NULL_SAFE null checks"
if [ $NULL_CHECKS -gt $NULL_SAFE ]; then
    echo "   ${YELLOW}⚠️  Some elements may not have null checks${NC}"
fi

# Issue 4: Check console for errors
echo ""
echo "4️⃣  Running quick smoke test..."
cd "$(dirname "$0")"
npx playwright test action-verification.spec.ts --grep "START HERE" --reporter=line 2>&1 | tail -20

echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║                      SUMMARY                           ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  1. Review changes in $FRONTEND_DIR"
echo "  2. Run full test suite: npm run test:action"
echo "  3. Do hands-on validation"
echo ""
