#!/bin/bash

# ATOM-SG Pilot MVP - Backup Script
# Backs up artifacts and configuration

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
BACKUP_ROOT="${BACKUP_ROOT:-./backups}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$BACKUP_ROOT/$TIMESTAMP"
BACKUP_NAME="atom-sg-backup-$TIMESTAMP.tar.gz"

# Source directory (relative to script location)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SOURCE_DIR="$SCRIPT_DIR/../05-Backend"

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}ATOM-SG Pilot MVP Backup${NC}"
echo -e "${GREEN}==========================================${NC}"
echo ""

# Check if source directory exists
if [[ ! -d "$SOURCE_DIR" ]]; then
    echo -e "${RED}Error: Source directory not found: $SOURCE_DIR${NC}"
    exit 1
fi

# Create backup directory
mkdir -p "$BACKUP_DIR"

echo "Backup source: $SOURCE_DIR"
echo "Backup destination: $BACKUP_DIR"
echo ""

# Backup artifacts
echo "1. Backing up artifacts..."
if [[ -d "$SOURCE_DIR/artifacts" ]]; then
    mkdir -p "$BACKUP_DIR/artifacts"
    cp -r "$SOURCE_DIR/artifacts"/* "$BACKUP_DIR/artifacts/" 2>/dev/null || true
    echo "   - Artifacts: $(find "$SOURCE_DIR/artifacts" -type f | wc -l) files"
else
    echo "   - No artifacts directory found"
fi

# Backup configuration
echo "2. Backing up configuration..."
if [[ -f "$SOURCE_DIR/.env" ]]; then
    cp "$SOURCE_DIR/.env" "$BACKUP_DIR/"
    echo "   - Environment file (.env)"
fi

if [[ -f "$SOURCE_DIR/requirements.txt" ]]; then
    cp "$SOURCE_DIR/requirements.txt" "$BACKUP_DIR/"
    echo "   - Requirements file"
fi

# Backup database (if SQLite exists)
echo "3. Backing up database..."
if [[ -f "$SOURCE_DIR/data/atom-sg.db" ]]; then
    mkdir -p "$BACKUP_DIR/data"
    cp "$SOURCE_DIR/data/atom-sg.db" "$BACKUP_DIR/data/"
    echo "   - SQLite database"
elif [[ -f "$SOURCE_DIR/atom-sg.db" ]]; then
    mkdir -p "$BACKUP_DIR/data"
    cp "$SOURCE_DIR/atom-sg.db" "$BACKUP_DIR/data/"
    echo "   - SQLite database (root)"
else
    echo "   - No SQLite database found"
fi

# Backup logs
echo "4. Backing up logs..."
if [[ -d "$SOURCE_DIR/logs" ]]; then
    mkdir -p "$BACKUP_DIR/logs"
    cp -r "$SOURCE_DIR/logs"/* "$BACKUP_DIR/logs/" 2>/dev/null || true
    echo "   - Logs: $(find "$SOURCE_DIR/logs" -type f | wc -l) files"
else
    echo "   - No logs directory found"
fi

# Create archive
echo "5. Creating archive..."
cd "$BACKUP_ROOT"
tar -czf "$BACKUP_NAME" "$TIMESTAMP"
cd - > /dev/null

# Calculate size
BACKUP_SIZE=$(du -h "$BACKUP_ROOT/$BACKUP_NAME" | cut -f1)

echo ""
echo -e "${GREEN}Backup Complete!${NC}"
echo "Archive: $BACKUP_ROOT/$BACKUP_NAME"
echo "Size: $BACKUP_SIZE"
echo "Contents:"
echo "  - artifacts/ (student sessions, renders, OCR results)"
echo "  - configuration files"
echo "  - database (if exists)"
echo "  - logs (if exists)"
echo ""

# Cleanup temporary directory
rm -rf "$BACKUP_DIR"

# Retention policy (keep last 30 backups)
echo "6. Applying retention policy (keep last 30 backups)..."
cd "$BACKUP_ROOT"
ls -t | grep -E '^atom-sg-backup-[0-9]{8}_[0-9]{6}\.tar\.gz$' | tail -n +31 | xargs rm -f 2>/dev/null || true
cd - > /dev/null

BACKUP_COUNT=$(ls "$BACKUP_ROOT"/*.tar.gz 2>/dev/null | wc -l | tr -d ' ')
echo "   Total backups retained: $BACKUP_COUNT"

echo ""
echo -e "${GREEN}==========================================${NC}"
echo "To restore a backup:"
echo "  tar -xzf $BACKUP_ROOT/$BACKUP_NAME"
echo "  cp -r $TIMESTAMP/* /path/to/05-Backend/"
echo ""
echo "For automated backups, add to crontab:"
echo "  0 2 * * * $(pwd)/deployment/backup.sh"
echo -e "${GREEN}==========================================${NC}"