#!/bin/bash

# ATOM-SG Playwright Test Setup Script
# Usage: ./setup.sh

set -e

echo "🎭 Setting up Playwright for ATOM-SG MVP..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js 18+ required. Current version: $(node --version)"
    exit 1
fi

echo "✅ Node.js $(node --version) found"

# Install npm dependencies
echo "📦 Installing npm dependencies..."
npm install

# Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
npx playwright install

# Create test results directory
mkdir -p test-results

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Ensure MVP is running at http://192.168.2.6 (or set BASE_URL)"
echo "  2. Run tests: npm test"
echo "  3. Run with UI: npm run test:ui"
echo "  4. View report: npm run report"
echo ""
echo "Environment variables:"
echo "  BASE_URL=http://192.168.2.6  # Target MVP URL"
echo "  CI=true                      # Run in CI mode"
