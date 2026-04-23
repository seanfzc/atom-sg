#!/usr/bin/env python3
"""
OCR Pipeline for ATOM-SG Pilot.
Extract text from PDFs or images, with fallback to OCR when text not selectable.
"""

import tempfile
import os
import re
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_dependencies():
    """Check if required packages are available."""
    try:
        import pytesseract
        from PIL import Image
        import fitz  # PyMuPDF
        import pdfplumber  # for PDF text extraction
        logger.info("All Python dependencies installed.")
        return True
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        return False

def extract_text_from_pdf(pdf_path, use_ocr_fallback=True):
    """
    Extract text from PDF using pdfplumber (selectable text).
    If no text found and use_ocr_fallback is True, fallback to OCR.
    Returns dict of page_number -> text.
    """
    import pdfplumber
    text_by_page = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and text.strip():
                    text_by_page[i + 1] = text
                else:
                    text_by_page[i + 1] = ""
            logger.info(f"Extracted selectable text from {len(pdf.pages)} pages.")
    except Exception as e:
        logger.warning(f"pdfplumber failed: {e}. Falling back to OCR.")
        text_by_page = {}
    
    # If any page missing text and OCR fallback enabled, run OCR on those pages
    if use_ocr_fallback:
        pages_missing = [pg for pg, txt in text_by_page.items() if not txt.strip()]
        if pages_missing:
            logger.info(f"Pages missing text: {pages_missing}. Running OCR.")
            ocr_text = ocr_from_pdf(pdf_path, page_range=pages_missing)
            for pg, txt in ocr_text.items():
                if txt.strip():
                    text_by_page[pg] = txt
    return text_by_page

def ocr_from_pdf(pdf_path, page_range=None):
    """
    Extract text from PDF using OCR (Tesseract).
    page_range: list of page numbers (1-indexed). If None, all pages.
    Returns dict of page_number -> text.
    """
    import fitz
    import pytesseract
    from PIL import Image
    
    doc = fitz.open(pdf_path)
    if page_range is None:
        page_range = list(range(1, len(doc) + 1))
    else:
        # ensure valid page numbers
        page_range = [pg for pg in page_range if 1 <= pg <= len(doc)]
    
    text_by_page = {}
    for pg_num in page_range:
        page = doc[pg_num - 1]
        # Render page to image with zoom factor 2 for better OCR
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        img_path = tempfile.mktemp(suffix='.png')
        pix.save(img_path)
        
        try:
            image = Image.open(img_path)
            text = pytesseract.image_to_string(image)
            text_by_page[pg_num] = text
            logger.debug(f"Page {pg_num}: {len(text)} characters extracted.")
        except Exception as e:
            logger.error(f"OCR error on page {pg_num}: {e}")
            text_by_page[pg_num] = ""
        finally:
            if os.path.exists(img_path):
                os.remove(img_path)
    
    doc.close()
    return text_by_page

def ocr_from_image(image_path):
    """Extract text from a single image."""
    import pytesseract
    from PIL import Image
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        logger.error(f"OCR error on image {image_path}: {e}")
        return ""

def save_ocr_output(text_by_page, output_dir, prefix="problem"):
    """
    Save extracted text to files in output_dir.
    Naming: {prefix}-page-{pg}.txt
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    saved_files = []
    for pg, text in text_by_page.items():
        filename = output_dir / f"{prefix}-page-{pg:03d}.txt"
        with open(filename, 'w') as f:
            f.write(text)
        saved_files.append(filename)
        logger.info(f"Saved page {pg} to {filename}")
    return saved_files

def main():
    """Example usage."""
    import argparse
    parser = argparse.ArgumentParser(description="OCR Pipeline for ATOM-SG Pilot")
    parser.add_argument("input", help="Input PDF or image file")
    parser.add_argument("--output-dir", default="./ocr_output", help="Directory to save extracted text")
    parser.add_argument("--prefix", default="problem", help="Prefix for output filenames")
    parser.add_argument("--no-ocr-fallback", action="store_true", help="Disable OCR fallback for PDFs")
    args = parser.parse_args()
    
    if not check_dependencies():
        logger.error("Missing dependencies. Install pytesseract, Pillow, PyMuPDF, pdfplumber.")
        return
    
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return
    
    text_by_page = {}
    if input_path.suffix.lower() in ('.pdf', '.PDF'):
        logger.info(f"Processing PDF: {input_path}")
        text_by_page = extract_text_from_pdf(input_path, use_ocr_fallback=not args.no_ocr_fallback)
    else:
        # Assume image
        logger.info(f"Processing image: {input_path}")
        text = ocr_from_image(input_path)
        text_by_page[1] = text
    
    if not text_by_page:
        logger.warning("No text extracted.")
        return
    
    saved = save_ocr_output(text_by_page, args.output_dir, args.prefix)
    logger.info(f"Saved {len(saved)} files to {args.output_dir}")

if __name__ == "__main__":
    main()