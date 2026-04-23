#!/usr/bin/env python3
"""
Extract Q12 using OpenCV only (no Paddle/Surya due to dependency issues)
"""

import cv2
import numpy as np
from pathlib import Path
import json


def find_squares_and_rectangles(image_path):
    """Use OpenCV to find squares and rectangles in the image."""
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Could not load: {image_path}")
        return None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Dilate edges to connect nearby lines
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    squares = []
    rectangles = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:  # Filter small noise
            continue
            
        # Approximate polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        if len(approx) == 4:  # Quadrilateral
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h if h > 0 else 0
            
            shape_info = {
                'x': int(x),
                'y': int(y),
                'width': int(w),
                'height': int(h),
                'aspect_ratio': float(aspect_ratio),
                'area': int(area)
            }
            
            # Classify as square or rectangle
            if 0.85 <= aspect_ratio <= 1.15:
                squares.append(shape_info)
            else:
                rectangles.append(shape_info)
    
    return squares, rectangles, img


def analyze_for_q12(image_path):
    """Analyze if this image contains Q12 (5 squares in rectangle)."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {image_path.name}")
    print(f"{'='*60}")
    
    squares, rectangles, img = find_squares_and_rectangles(image_path)
    
    if squares is None:
        return None
    
    print(f"Found {len(squares)} squares, {len(rectangles)} rectangles")
    
    # Q12 should have exactly 5 squares inside a rectangle
    is_q12_candidate = len(squares) >= 5 and len(rectangles) >= 1
    
    if squares:
        print("\nSquares detected:")
        # Sort by area
        sorted_squares = sorted(squares, key=lambda x: x['area'], reverse=True)
        for i, sq in enumerate(sorted_squares[:10]):
            print(f"  {i+1}. Size: {sq['width']}x{sq['height']} px, "
                  f"Area: {sq['area']} px², Pos: ({sq['x']}, {sq['y']})")
    
    if rectangles:
        print("\nRectangles detected:")
        sorted_rects = sorted(rectangles, key=lambda x: x['area'], reverse=True)
        for i, rect in enumerate(sorted_rects[:5]):
            print(f"  {i+1}. Size: {rect['width']}x{rect['height']} px, "
                  f"Area: {rect['area']} px²")
    
    # Create annotated image
    annotated = img.copy()
    for sq in squares:
        cv2.rectangle(annotated, (sq['x'], sq['y']), 
                     (sq['x'] + sq['width'], sq['y'] + sq['height']),
                     (0, 255, 0), 2)
    for rect in rectangles:
        cv2.rectangle(annotated, (rect['x'], rect['y']),
                     (rect['x'] + rect['width'], rect['y'] + rect['height']),
                     (255, 0, 0), 2)
    
    # Save annotated image
    output_path = image_path.parent / f"{image_path.stem}_annotated.png"
    cv2.imwrite(str(output_path), annotated)
    print(f"\nAnnotated image saved: {output_path.name}")
    
    return {
        'image': image_path.name,
        'squares': len(squares),
        'rectangles': len(rectangles),
        'square_details': squares[:10],
        'is_q12_candidate': is_q12_candidate
    }


def main():
    base_path = Path(__file__).parent
    
    # Analyze all candidate pages
    candidates = sorted(base_path.glob("acs_pdf_page*.png"))
    
    results = []
    for candidate in candidates:
        result = analyze_for_q12(candidate)
        if result:
            results.append(result)
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY - Q12 CANDIDATES")
    print(f"{'='*60}")
    
    q12_candidates = [r for r in results if r['is_q12_candidate']]
    
    if q12_candidates:
        print(f"\nFound {len(q12_candidates)} potential Q12 pages:")
        for r in q12_candidates:
            print(f"  - {r['image']}: {r['squares']} squares")
    else:
        print("\nNo clear Q12 candidates found.")
        print("Pages with most squares:")
        sorted_results = sorted(results, key=lambda x: x['squares'], reverse=True)
        for r in sorted_results[:3]:
            print(f"  - {r['image']}: {r['squares']} squares")
    
    # Save results
    output_file = base_path / "opencv_analysis_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
