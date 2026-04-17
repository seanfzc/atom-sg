#!/usr/bin/env python3
"""
OCR Pipeline for Geometry Problem PDFs.
Processes PDFs from renders directory, extracts text via OCR, saves to ocr directory.
Optionally registers results via Backend API.
"""

import os
import sys
import json
import logging
from pathlib import Path
import tempfile

# Add parent directory to path for imports if needed
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import fitz  # PyMuPDF
    import pytesseract
    from PIL import Image
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Directories (relative to this script's parent directory)
ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts"
RENDERS_DIR = ARTIFACTS_DIR / "renders"
OCR_DIR = ARTIFACTS_DIR / "ocr"

# Ensure directories exist
OCR_DIR.mkdir(exist_ok=True)

# Backend API configuration (optional)
API_BASE_URL = os.environ.get("BACKEND_API_URL", "http://localhost:3000/api")
ENABLE_API = os.environ.get("ENABLE_BACKEND_API", "false").lower() == "true"

def extract_text_from_pdf(pdf_path: Path, dpi=200):
    """
    Extract text from PDF using OCR.
    Returns a dict: {page_num: {"text": str, "confidence": float}}
    """
    doc = fitz.open(pdf_path)
    results = {}
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        # Render page as image
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))
        img_path = tempfile.mktemp(suffix='.png')
        pix.save(img_path)
        
        # Open image with PIL
        img = Image.open(img_path)
        
        # Run OCR with Tesseract
        # Use --psm 6 (assuming uniform block of text) or adjust based on content
        config = '--psm 6'
        text = pytesseract.image_to_string(img, config=config)
        
        # Get confidence data
        data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)
        confidences = [c for c in data['conf'] if c != -1]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
        
        results[page_num + 1] = {
            "text": text,
            "confidence": avg_confidence
        }
        
        # Clean up temporary image
        os.remove(img_path)
        
        logger.info(f"Page {page_num + 1}: extracted {len(text)} chars, confidence {avg_confidence:.2f}")
    
    doc.close()
    return results

def save_ocr_results(pdf_path: Path, ocr_results: dict):
    """
    Save OCR results to a text file in OCR_DIR.
    Also save metadata as JSON.
    """
    base_name = pdf_path.stem  # e.g., G001_G1_20260413_143401
    text_file = OCR_DIR / f"{base_name}.txt"
    meta_file = OCR_DIR / f"{base_name}_meta.json"
    
    # Combine text from all pages
    full_text = ""
    for page_num, data in sorted(ocr_results.items()):
        full_text += f"--- Page {page_num} ---\n"
        full_text += data["text"]
        if not data["text"].endswith("\n"):
            full_text += "\n"
    
    with open(text_file, 'w') as f:
        f.write(full_text)
    logger.info(f"Saved OCR text to {text_file}")
    
    # Save metadata
    metadata = {
        "pdf_path": str(pdf_path),
        "pages": len(ocr_results),
        "total_confidence": sum(d["confidence"] for d in ocr_results.values()) / len(ocr_results) if ocr_results else 0,
        "per_page": {pg: {"confidence": d["confidence"], "text_length": len(d["text"])} for pg, d in ocr_results.items()}
    }
    with open(meta_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    logger.info(f"Saved metadata to {meta_file}")
    
    return text_file, meta_file

def register_with_backend(pdf_path: Path, ocr_results: dict, text_file: Path, meta_file: Path):
    """
    Register OCR results with Backend API (if enabled).
    This is a placeholder; actual implementation depends on API spec.
    """
    if not ENABLE_API:
        logger.info("Backend API registration disabled.")
        return False
    
    # Extract problem ID from filename (e.g., G001_G1_20260413_143401 -> G001)
    problem_id = pdf_path.stem.split('_')[0]
    
    # TODO: Determine render_id (maybe from database or mapping)
    # For now, we'll skip.
    logger.warning("Backend API registration not yet implemented.")
    return False

def process_pdf(pdf_path: Path):
    """Process a single PDF."""
    logger.info(f"Processing {pdf_path.name}")
    
    # Check if already processed
    base_name = pdf_path.stem
    text_file = OCR_DIR / f"{base_name}.txt"
    if text_file.exists():
        logger.info(f"OCR output already exists: {text_file}. Skipping.")
        return True
    
    try:
        ocr_results = extract_text_from_pdf(pdf_path)
        if not ocr_results:
            logger.warning(f"No OCR results for {pdf_path.name}")
            return False
        
        text_file, meta_file = save_ocr_results(pdf_path, ocr_results)
        register_with_backend(pdf_path, ocr_results, text_file, meta_file)
        return True
    except Exception as e:
        logger.error(f"Error processing {pdf_path.name}: {e}")
        return False

def main():
    """Main entry point."""
    import argparse
    parser = argparse.ArgumentParser(description='OCR Pipeline for Geometry Problem PDFs')
    parser.add_argument('--pdf', '-p', type=str, help='Process a specific PDF file')
    parser.add_argument('--all', '-a', action='store_true', help='Process all PDFs in renders directory')
    args = parser.parse_args()
    
    if args.pdf:
        pdf_path = Path(args.pdf).resolve()
        if not pdf_path.exists():
            logger.error(f"PDF file not found: {pdf_path}")
            return 1
        pdf_files = [pdf_path]
    elif args.all:
        if not RENDERS_DIR.exists():
            logger.error(f"Renders directory not found: {RENDERS_DIR}")
            return 1
        pdf_files = list(RENDERS_DIR.glob("*.pdf"))
        if not pdf_files:
            logger.info("No PDF files found in renders directory.")
            return 0
    else:
        logger.error("Please specify either --pdf <file> or --all")
        return 1
    
    logger.info(f"Found {len(pdf_files)} PDFs to process.")
    
    success_count = 0
    for pdf_path in pdf_files:
        if process_pdf(pdf_path):
            success_count += 1
    
    logger.info(f"Processing complete. Success: {success_count}/{len(pdf_files)}")
    return 0 if success_count == len(pdf_files) else 1

if __name__ == "__main__":
    sys.exit(main())