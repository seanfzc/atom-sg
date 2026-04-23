#!/usr/bin/env python3
"""
Convert existing professional PDF renders to PNG for embedding in baseline test.
Uses pdf2image or falls back to matplotlib recreation.
"""

from pathlib import Path
import subprocess
import sys

RENDERS_DIR = Path(__file__).parent / "artifacts" / "renders"

def convert_pdf_to_png(pdf_path, png_path):
    """Convert PDF to PNG using pdftoppm or similar."""
    try:
        # Try using pdftoppm (comes with poppler)
        result = subprocess.run([
            "pdftoppm", "-png", "-r", "150", 
            str(pdf_path), str(png_path).replace(".png", "")
        ], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    
    try:
        # Try using ImageMagick convert
        result = subprocess.run([
            "convert", "-density", "150", str(pdf_path), 
            "-quality", "90", str(png_path)
        ], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    
    return False

def main():
    """Convert all G-series renders to PNG."""
    pdf_files = list(RENDERS_DIR.glob("G*-v1.pdf"))
    
    print(f"Found {len(pdf_files)} PDF renders to convert")
    
    converted = 0
    for pdf_file in pdf_files:
        png_file = pdf_file.with_suffix(".png")
        if png_file.exists():
            print(f"✓ {png_file.name} already exists")
            converted += 1
            continue
            
        print(f"Converting {pdf_file.name}...", end=" ")
        if convert_pdf_to_png(pdf_file, png_file):
            print("✓")
            converted += 1
        else:
            print("✗ (conversion tools not available)")
    
    print(f"\n✓ {converted}/{len(pdf_files)} renders ready for embedding")
    
    if converted < len(pdf_files):
        print("\nNote: Install poppler (pdftoppm) or ImageMagick for PDF conversion:")
        print("  brew install poppler  # macOS")
        print("  brew install imagemagick  # macOS")

if __name__ == "__main__":
    main()
