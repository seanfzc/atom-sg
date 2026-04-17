#!/usr/bin/env python3
"""
Test script for Tesseract OCR pipeline readiness.
Extracts text from a sample PDF page and validates basic functionality.
"""

import tempfile
import os
import sys
from pathlib import Path

def check_dependencies():
    """Check if required Python packages are installed."""
    try:
        import pytesseract
        from PIL import Image
        import fitz  # PyMuPDF
        print("✅ All Python dependencies installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def check_tesseract_command():
    """Check if tesseract command is available."""
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract version: {version}")
        return True
    except Exception as e:
        print(f"❌ Tesseract not accessible: {e}")
        return False

def extract_page_image(pdf_path, page_num=1, zoom=2):
    """Convert a PDF page to image."""
    import fitz
    doc = fitz.open(pdf_path)
    if page_num < 1 or page_num > len(doc):
        print(f"Page number {page_num} out of range (1-{len(doc)})")
        doc.close()
        return None
    page = doc[page_num - 1]
    # Render page to image
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img_path = tempfile.mktemp(suffix='.png')
    pix.save(img_path)
    doc.close()
    print(f"Page {page_num} saved as image: {img_path}")
    return img_path

def ocr_image(img_path):
    """Perform OCR on image."""
    import pytesseract
    from PIL import Image
    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"OCR error: {e}")
        return None

def main():
    print("=" * 60)
    print("OCR Pipeline Readiness Test (Tesseract)")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    if not check_tesseract_command():
        sys.exit(1)
    
    # Use sample PDF (Rosyth P6 Maths Weighted Assessment 1)
    pdf_path = Path("/Users/zcaeth/Desktop/sg_exam_papers/Maths/P6/2025/Other/2025 P6 Maths Weighted Assessment 1 Rosyth.pdf")
    if not pdf_path.exists():
        print(f"Sample PDF not found at {pdf_path}")
        print("Using alternative test: creating a simple text image.")
        # Create a simple image with text using PIL
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (400, 200), color='white')
        d = ImageDraw.Draw(img)
        # Use default font
        try:
            font = ImageFont.truetype("Arial", 24)
        except:
            font = ImageFont.load_default()
        d.text((20, 20), "OCR Test: 2 + 3 = 5", fill='black', font=font)
        img_path = tempfile.mktemp(suffix='.png')
        img.save(img_path)
        print(f"Created test image: {img_path}")
        test_text = ocr_image(img_path)
        if test_text:
            print("\nOCR Result:")
            print(test_text)
            if "OCR Test" in test_text or "2 + 3 = 5" in test_text:
                print("✅ OCR test passed (basic text recognition).")
            else:
                print("⚠️  OCR may have low accuracy.")
            os.remove(img_path)
        else:
            print("❌ OCR failed.")
        sys.exit(0)
    
    print(f"\nUsing sample PDF: {pdf_path.name}")
    # Extract page 2 (likely contains questions)
    img_path = extract_page_image(pdf_path, page_num=2, zoom=2)
    if not img_path:
        sys.exit(1)
    
    text = ocr_image(img_path)
    os.remove(img_path)  # cleanup
    
    if text:
        print("\nOCR Result (first 500 chars):")
        print(text[:500])
        # Basic validation: check if any alphanumeric characters found
        import re
        if re.search(r'\w', text):
            print("✅ OCR extracted meaningful text.")
        else:
            print("⚠️  OCR may not have extracted text.")
        # Save sample output to OCR folder
        output_dir = Path(__file__).parent
        output_file = output_dir / "sample_ocr_output.txt"
        with open(output_file, 'w') as f:
            f.write(text)
        print(f"Sample output saved to: {output_file}")
    else:
        print("❌ OCR returned empty text.")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("OCR Pipeline Readiness Test Complete.")
    print("Next steps:")
    print("1. Coordinate with BackendBot for OCR output storage")
    print("2. Integrate OCR extraction into rendering pipeline")
    print("3. Test accuracy on geometry problem images")
    print("=" * 60)

if __name__ == "__main__":
    main()