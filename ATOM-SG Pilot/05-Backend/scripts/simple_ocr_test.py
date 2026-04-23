#!/usr/bin/env python3
"""
Simple OCR Test Script
Tests Tesseract with various sample inputs
"""

import os
import subprocess
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random

# Paths
BASE_DIR = Path("/Users/zcaeth/.openclaw/workspace/ATOM-SG Pilot/05-Backend")
ARTIFACTS_OCR = BASE_DIR / "artifacts/ocr"
TEST_IMAGES = ARTIFACTS_OCR / "test_images"
OCR_OUTPUT = ARTIFACTS_OCR / "test_results"

# Ensure directories exist
TEST_IMAGES.mkdir(parents=True, exist_ok=True)
OCR_OUTPUT.mkdir(parents=True, exist_ok=True)

def run_ocr(image_path, output_base):
    """
    Run Tesseract OCR on an image
    Returns: (text, confidence)
    """
    # Run Tesseract with confidence output
    cmd = [
        "tesseract", str(image_path), str(output_base),
        "-l", "eng",
        "--oem", "1",
        "--psm", "6",
        "tsv"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Tesseract error: {result.stderr}")
        return "", 0

    # Parse TSV for confidence
    confidence = 0
    tsv_path = str(output_base) + ".tsv"
    txt_path = str(output_base) + ".txt"

    if os.path.exists(tsv_path):
        with open(tsv_path, 'r') as f:
            lines = f.readlines()
            if len(lines) > 1:
                confidences = []
                for line in lines[1:]:  # Skip header
                    parts = line.strip().split('\t')
                    if len(parts) > 10:
                        try:
                            conf_val = float(parts[10])
                            if conf_val > 0:  # Filter out zero confidence
                                confidences.append(conf_val)
                        except:
                            pass
                if confidences:
                    confidence = sum(confidences) / len(confidences)

    # Read extracted text
    text = ""
    if os.path.exists(txt_path):
        with open(txt_path, 'r') as f:
            text = f.read().strip()

    return text, confidence

def test_simple_text():
    """Test with simple text rendered directly"""
    print("\n" + "=" * 60)
    print("TEST 1: Simple Text (No handwriting simulation)")
    print("=" * 60)

    # Create simple test image with clear text
    width, height = 800, 400
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Try to use system font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    test_text = "Math is fun"
    draw.text((100, 150), test_text, fill='black', font=font)

    img_path = TEST_IMAGES / "simple_text.png"
    img.save(img_path)
    print(f"Created: {img_path}")

    # Run OCR
    output_base = OCR_OUTPUT / "simple_text"
    text, confidence = run_ocr(img_path, output_base)

    print(f"Original: {test_text}")
    print(f"Extracted: {text}")
    print(f"Confidence: {confidence:.2f}%")

    # Calculate accuracy
    if test_text and text:
        accuracy = len(set(text.lower()) & set(test_text.lower())) / len(test_text) * 100
        print(f"Character accuracy: {accuracy:.2f}%")
    else:
        accuracy = 0

    return {
        "test": "simple_text",
        "original": test_text,
        "extracted": text,
        "confidence": confidence,
        "accuracy": accuracy
    }

def test_numbers():
    """Test with numbers"""
    print("\n" + "=" * 60)
    print("TEST 2: Numbers")
    print("=" * 60)

    width, height = 800, 400
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    test_text = "123 456 789"
    draw.text((100, 150), test_text, fill='black', font=font)

    img_path = TEST_IMAGES / "numbers.png"
    img.save(img_path)
    print(f"Created: {img_path}")

    output_base = OCR_OUTPUT / "numbers"
    text, confidence = run_ocr(img_path, output_base)

    print(f"Original: {test_text}")
    print(f"Extracted: {text}")
    print(f"Confidence: {confidence:.2f}%")

    accuracy = 0
    if test_text and text:
        accuracy = len(set(text) & set(test_text)) / len(test_text) * 100
        print(f"Character accuracy: {accuracy:.2f}%")

    return {
        "test": "numbers",
        "original": test_text,
        "extracted": text,
        "confidence": confidence,
        "accuracy": accuracy
    }

def test_equation():
    """Test with equation"""
    print("\n" + "=" * 60)
    print("TEST 3: Equation")
    print("=" * 60)

    width, height = 800, 400
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    test_text = "x + y = 10"
    draw.text((100, 150), test_text, fill='black', font=font)

    img_path = TEST_IMAGES / "equation.png"
    img.save(img_path)
    print(f"Created: {img_path}")

    output_base = OCR_OUTPUT / "equation"
    text, confidence = run_ocr(img_path, output_base)

    print(f"Original: {test_text}")
    print(f"Extracted: {text}")
    print(f"Confidence: {confidence:.2f}%")

    accuracy = 0
    if test_text and text:
        accuracy = len(set(text.lower()) & set(test_text.lower())) / len(test_text) * 100
        print(f"Character accuracy: {accuracy:.2f}%")

    return {
        "test": "equation",
        "original": test_text,
        "extracted": text,
        "confidence": confidence,
        "accuracy": accuracy
    }

def test_with_preprocessing():
    """Test with preprocessing pipeline"""
    print("\n" + "=" * 60)
    print("TEST 4: With Preprocessing (Grayscale + Noise Reduction + Contrast)")
    print("=" * 60)

    from PIL import ImageFilter, ImageEnhance

    width, height = 800, 400
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    test_text = "Geometry Problem"
    draw.text((100, 150), test_text, fill='black', font=font)

    # Original
    img_path = TEST_IMAGES / "geometry_original.png"
    img.save(img_path)
    print(f"Created: {img_path}")

    output_base = OCR_OUTPUT / "geometry_original"
    text_raw, conf_raw = run_ocr(img_path, output_base)
    print(f"\nWithout preprocessing:")
    print(f"Extracted: {text_raw}")
    print(f"Confidence: {conf_raw:.2f}%")

    # Preprocessing
    img_gray = img.convert('L')
    img_denoised = img_gray.filter(ImageFilter.MedianFilter(size=3))
    img_enhanced = ImageEnhance.Contrast(img_denoised).enhance(2.0)

    img_pp_path = TEST_IMAGES / "geometry_preprocessed.png"
    img_enhanced.save(img_pp_path)
    print(f"Created: {img_pp_path}")

    output_base_pp = OCR_OUTPUT / "geometry_preprocessed"
    text_pp, conf_pp = run_ocr(img_pp_path, output_base_pp)
    print(f"\nWith preprocessing:")
    print(f"Extracted: {text_pp}")
    print(f"Confidence: {conf_pp:.2f}%")

    # Calculate accuracy
    accuracy_raw = 0
    accuracy_pp = 0
    if test_text:
        if text_raw:
            accuracy_raw = len(set(text_raw.lower()) & set(test_text.lower())) / len(test_text) * 100
        if text_pp:
            accuracy_pp = len(set(text_pp.lower()) & set(test_text.lower())) / len(test_text) * 100

    print(f"\nAccuracy without preprocessing: {accuracy_raw:.2f}%")
    print(f"Accuracy with preprocessing: {accuracy_pp:.2f}%")

    return {
        "test": "geometry_preprocessing",
        "original": test_text,
        "raw": {
            "text": text_raw,
            "confidence": conf_raw,
            "accuracy": accuracy_raw
        },
        "preprocessed": {
            "text": text_pp,
            "confidence": conf_pp,
            "accuracy": accuracy_pp
        }
    }

def main():
    print("=" * 60)
    print("OCR PIPELINE READINESS TEST")
    print("=" * 60)
    print(f"Tesseract version: 5.5.2")
    print(f"Test directory: {TEST_IMAGES}")
    print(f"Output directory: {OCR_OUTPUT}")

    results = []

    # Run tests
    results.append(test_simple_text())
    results.append(test_numbers())
    results.append(test_equation())
    results.append(test_with_preprocessing())

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for result in results:
        print(f"\n{result['test'].upper()}:")
        if "raw" in result:
            print(f"  Original: {result['original']}")
            print(f"  Without preprocessing:")
            print(f"    Confidence: {result['raw']['confidence']:.2f}%")
            print(f"    Accuracy: {result['raw']['accuracy']:.2f}%")
            print(f"  With preprocessing:")
            print(f"    Confidence: {result['preprocessed']['confidence']:.2f}%")
            print(f"    Accuracy: {result['preprocessed']['accuracy']:.2f}%")
        else:
            print(f"  Original: {result['original']}")
            print(f"  Extracted: {result['extracted']}")
            print(f"  Confidence: {result['confidence']:.2f}%")
            print(f"  Accuracy: {result['accuracy']:.2f}%")

    # Save results
    results_path = OCR_OUTPUT / "test_results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {results_path}")

    # Assessment
    print("\n" + "=" * 60)
    print("OCR PIPELINE ASSESSMENT")
    print("=" * 60)

    avg_confidence = sum(r.get('confidence', r.get('raw', {}).get('confidence', 0)) for r in results[:3]) / 3
    avg_accuracy = sum(r.get('accuracy', r.get('raw', {}).get('accuracy', 0)) for r in results[:3]) / 3

    print(f"Average confidence (baseline): {avg_confidence:.2f}%")
    print(f"Average accuracy (baseline): {avg_accuracy:.2f}%")

    if avg_accuracy >= 90:
        status = "EXCELLENT"
    elif avg_accuracy >= 75:
        status = "GOOD"
    elif avg_accuracy >= 50:
        status = "ACCEPTABLE"
    else:
        status = "NEEDS IMPROVEMENT"

    print(f"\nOverall status: {status}")

    # Handwriting quality expectations
    print("\nExpected accuracy for 11-year-old handwriting:")
    print("  - Neat handwriting: 85-95%")
    print("  - Average handwriting: 75-85%")
    print("  - Messy handwriting: 60-75%")

    # Threshold configuration
    print("\nRecommended threshold configuration:")
    print("  - Confidence threshold for review: 70%")
    print("  - Accuracy threshold for review: 75%")
    print("  - Low confidence handling: Flag for manual review")

if __name__ == "__main__":
    main()
