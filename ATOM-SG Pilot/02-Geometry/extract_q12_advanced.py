#!/usr/bin/env python3
"""
Advanced extraction using OpenCV, PaddleOCR, and Surya
For precise measurement of Q12 diagram
"""

import cv2
import numpy as np
from PIL import Image
from pathlib import Path
import json

# Try to import OCR libraries
try:
    from paddleocr import PaddleOCR
    PADDLE_AVAILABLE = True
except ImportError:
    PADDLE_AVAILABLE = False
    print("PaddleOCR not available")

try:
    from surya.ocr import run_ocr
    from surya.model.segformer import load_model as load_surya_model
    from surya.model.processors import load_processor as load_surya_processor
    SURYA_AVAILABLE = True
except ImportError:
    SURYA_AVAILABLE = False
    print("Surya not available")


def find_squares_opencv(image_path):
    """Use OpenCV to find square shapes in the image."""
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Could not load: {image_path}")
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Threshold to find dark lines (square boundaries)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    squares = []
    for contour in contours:
        # Approximate polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Check if it's a square (4 sides, convex)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            
            # Square should have aspect ratio close to 1
            if 0.9 <= aspect_ratio <= 1.1 and w > 20:  # Min size filter
                squares.append({
                    'x': x,
                    'y': y,
                    'width': w,
                    'height': h,
                    'contour': approx.tolist()
                })
    
    return squares, img


def extract_text_paddle(image_path):
    """Use PaddleOCR to extract text with positions."""
    if not PADDLE_AVAILABLE:
        return []
    
    ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
    result = ocr.ocr(str(image_path), cls=True)
    
    text_boxes = []
    if result and result[0]:
        for line in result[0]:
            if line:
                bbox, (text, confidence) = line
                text_boxes.append({
                    'text': text,
                    'confidence': confidence,
                    'bbox': bbox
                })
    
    return text_boxes


def analyze_page(image_path):
    """Analyze a page for Q12 content."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    
    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        print("Failed to load image")
        return None
    
    print(f"Image size: {img.shape}")
    
    # Extract text with PaddleOCR
    if PADDLE_AVAILABLE:
        print("\n--- PaddleOCR Text Extraction ---")
        text_results = extract_text_paddle(image_path)
        
        q12_found = False
        for item in text_results:
            text = item['text'].lower()
            if '12' in text or 'square' in text or '4cm' in text or '4 cm' in text:
                print(f"Found: '{item['text']}' (conf: {item['confidence']:.2f})")
                print(f"  Position: {item['bbox']}")
                q12_found = True
        
        if q12_found:
            print("*** Q12 CANDIDATE ***")
    
    # Find squares with OpenCV
    print("\n--- OpenCV Square Detection ---")
    squares, _ = find_squares_opencv(image_path)
    
    if squares:
        print(f"Found {len(squares)} potential squares")
        for i, sq in enumerate(squares[:10]):  # Limit output
            print(f"  Square {i+1}: x={sq['x']}, y={sq['y']}, w={sq['width']}, h={sq['height']}")
    
    return {
        'image_path': str(image_path),
        'squares_found': len(squares) if squares else 0,
        'has_q12_content': q12_found if PADDLE_AVAILABLE else False
    }


def main():
    base_path = Path(__file__).parent
    
    # Analyze candidate pages
    candidates = [
        "acs_pdf_page010.png",
        "acs_pdf_page011.png",
        "acs_pdf_page012.png",
        "acs_pdf_page013.png",
        "acs_pdf_page014.png",
        "acs_pdf_page015.png",
    ]
    
    results = []
    for candidate in candidates:
        path = base_path / candidate
        if path.exists():
            result = analyze_page(path)
            if result:
                results.append(result)
        else:
            print(f"Not found: {candidate}")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for r in results:
        print(f"{Path(r['image_path']).name}: {r['squares_found']} squares, Q12: {r['has_q12_content']}")
    
    # Save results
    output_file = base_path / "q12_analysis_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
