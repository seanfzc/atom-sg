#!/bin/bash

# ATOM-SG Pilot MVP - Backup Restore Script
# Restores from a backup archive

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
BACKUP_ROOT="${BACKUP_ROOT:-./backups}"
TARGET_DIR="${TARGET_DIR:-../05-Backend}"

# Display usage
usage() {
    echo -e "${GREEN}ATOM-SG Pilot MVP - Backup Restore${NC}"
    echo ""
    echo "Usage: $0 <backup_file>"
    echo ""
    echo "Arguments:"
    echo "  <backup_file>  Path to backup archive (e.g., backups/atom-sg-backup-20250101_020000.tar.gz)"
    echo ""
    echo "Environment variables:"
    echo "  BACKUP_ROOT    Backup directory (default: ./backups)"
    echo "  TARGET_DIR     Target restore directory (default: ../05-Backend)"
    echo ""
    echo "Examples:"
    echo "  $0 backups/atom-sg-backup-20250101_020000.tar.gz"
    echo "  TARGET_DIR=/opt/atom-sg $0 latest"
    echo ""
    exit 1
}

# Check if backup file exists
check_backup_file() {
    local backup_file="$1"
    
    if [ ! -f "$backup_file" ]; then
        echo -e "${RED}Error: Backup file not found: $backup_file${NC}"
        echo ""
        echo "Available backups in $BACKUP_ROOT:"
        ls -lh "$BACKUP_ROOT"/atom-sg-backup-*.tar.gz 2>/dev/null || echo "  (none)"
        exit 1
    fi
}

# Extract backup
extract_backup() {
    local backup_file="$1"
    local temp_dir=$(mktemp -d)
    
    echo -e "${GREEN}Extracting backup: $(basename "$backup_file")${NC}"
    
    # Extract to temp directory
    tar -xzf "$backup_file" -C "$temp_dir"
    
    # Get the extracted directory name (should be timestamp)
    local extracted_dir=$(find "$temp_dir" -maxdepth 1 -type d -name "20*" | head -1)
    
    if [ -z "$extracted_dir" ]; then
        echo -e "${RED}Error: Could not find extracted backup directory${NC}"
        rm -rf "$temp_dir"
        exit 1
    fi
    
    echo "Backup contents:"
    find "$extracted_dir" -type f | sed 's|^|  |'
    
    echo "$extracted_dir"
}

# Restore artifacts
restore_artifacts() {
    local source_dir="$1"
    
    echo ""
    echo -e "${GREEN}1. Restoring artifacts...${NC}"
    
    if [ -d "$source_dir/artifacts" ]; then
        mkdir -p "$TARGET_DIR/artifacts"
        echo "   Copying artifacts..."
        cp -r "$source_dir/artifacts"/* "$TARGET_DIR/artifacts/" 2>/dev/null || true
        echo "   - Restored $(find "$source_dir/artifacts" -type f | wc -l) files"
    else
        echo "   - No artifacts directory in backup"
    fi
}

# Restore configuration
restore_configuration() {
    local source_dir="$1"
    
    echo -e "${GREEN}2. Restoring configuration...${NC}"
    
    # .env file
    if [ -f "$source_dir/.env" ]; then
        if [ -f "$TARGET_DIR/.env" ]; then
            echo "   - .env exists in target, creating .env.backup-restored instead"
            cp "$source_dir/.env" "$TARGET_DIR/.env.backup-restored"
        else
            cp "$source_dir/.env" "$TARGET_DIR/"
            echo "   - Restored .env file"
        fi
    fi
    
    # requirements.txt
    if [ -f "$source_dir/requirements.txt" ]; then
        cp "$source_dir/requirements.txt" "$TARGET_DIR/"
        echo "   - Restored requirements.txt"
    fi
}

# Restore database
restore_database() {
    local source_dir="$1"
    
    echo -e "${GREEN}3. Restoring database...${NC}"
    
    # Check for database in data/ or root
    local db_source=""
    
    if [ -f "$source_dir/data/atom-sg.db" ]; then
        db_source="$source_dir/data/atom-sg.db"
    elif [ -f "$source_dir/atom-sg.db" ]; then
        db_source="$source_dir/atom-sg.db"
    fi
    
    if [ -n "$db_source" ]; then
        mkdir -p "$TARGET_DIR/data"
        cp "$db_source" "$TARGET_DIR/data/atom-sg.db"
        echo "   - Restored SQLite database"
    else
        echo "   - No database found in backup"
    fi
}

# Restore logs
restore_logs() {
    local source_dir="$1"
    
    echo -e "${GREEN}4. Restoring logs...${NC}"
    
    if [ -d "$source_dir/logs" ]; then
        mkdir -p "$TARGET_DIR/logs"
        cp -r "$source_dir/logs"/* "$TARGET_DIR/logs/" 2>/dev/null || true
        echo "   - Restored $(find "$source_dir/logs" -type f | wc -l) log files"
    else
        echo "   - No logs directory in backup"
    fi
}

# Verify target directory
verify_target() {
    echo -e "${GREEN}5. Verifying target directory...${NC}"
    
    if [ ! -d "$TARGET_DIR" ]; then
        echo -e "${YELLOW}Warning: Target directory does not exist: $TARGET_DIR${NC}"
        read -p "Create directory? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            mkdir -p "$TARGET_DIR"
            echo "   Created target directory"
        else
            echo -e "${RED}Aborting restore${NC}"
            exit 1
        fi
    fi
    
    echo "   Target: $TARGET_DIR"
    echo "   Size: $(du -sh "$TARGET_DIR" 2>/dev/null | cut -f1) (before restore)"
}

# Main restore function
main_restore() {
    local backup_file="$1"
    
    echo -e "${GREEN}==========================================${NC}"
    echo -e "${GREEN}ATOM-SG Pilot MVP - Backup Restore${NC}"
    echo -e "${GREEN}==========================================${NC}"
    echo ""
    
    # If "latest" is specified, find the most recent backup
    if [ "$backup_file" = "latest" ]; then
        backup_file=$(ls -t "$BACKUP_ROOT"/atom-sg-backup-*.tar.gz 2>/dev/null | head -1)
        if [ -z "$backup_file" ]; then
            echo -e "${RED}Error: No backups found in $BACKUP_ROOT${NC}"
            exit 1
        fi
        echo "Using latest backup: $(basename "$backup_file")"
    fi
    
    check_backup_file "$backup_file"
    verify_target
    
    # Confirm restore
    echo ""
    echo -e "${YELLOW}WARNING: This will overwrite existing files in:${NC}"
    echo "  $TARGET_DIR"
    echo ""
    read -p "Are you sure you want to continue? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}Restore cancelled${NC}"
        exit 0
    fi
    
    # Extract and restore
    local extracted_dir=$(extract_backup "$backup_file")
    
    restore_artifacts "$extracted_dir"
    restore_configuration "$extracted_dir"
    restore_database "$extracted_dir"
    restore_logs "$extracted_dir"
    
    # Cleanup
    rm -rf "$(dirname "$extracted_dir")"
    
    echo ""
    echo -e "${GREEN}✅ Restore complete!${NC}"
    echo ""
    echo "Restored to: $TARGET_DIR"
    echo "Size after restore: $(du -sh "$TARGET_DIR" 2>/dev/null | cut -f1)"
    echo ""
    echo "Next steps:"
    echo "  1. Review restored configuration files"
    echo "  2. Restart the application if it's running"
    echo "  3. Verify data integrity"
    echo ""
    echo -e "${GREEN}==========================================${NC}"
}

# Check arguments
if [ $# -lt 1 ]; then
    usage
fi

main_restore "$1"