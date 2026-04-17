#!/usr/bin/env python3
"""
OCR Pipeline Testing Script
Creates synthetic handwriting samples and tests Tesseract OCR
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

def create_handwriting_text(text, style="neat", output_path=None):
    """
    Create synthetic handwriting-like image
    style: "neat", "messy", "mixed_case"
    """
    # Image dimensions
    width = 800
    height = 600

    # Create white background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Add slight noise for realism
    if style == "messy":
        for _ in range(500):
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.point((x, y), fill=(240, 240, 240))

    # Try to use system font, fall back to default
    try:
        # Common handwriting fonts on macOS
        font_paths = [
            "/System/Library/Fonts/Pencil.ttc",
            "/System/Library/Fonts/MarkerFelt.ttc",
            "/Library/Fonts/Arial.ttf",
        ]
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, 36)
                break
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    # Apply style transformations
    if style == "messy":
        # Random jitter in letter spacing
        x_positions = [random.randint(50, 150) for _ in range(len(text))]
        y_positions = [random.randint(80, 120) + i * 50 for i in range(len(text))]
        # Randomize case
        text = ''.join([c.upper() if random.random() < 0.3 else c.lower() for c in text])
    elif style == "mixed_case":
        x_positions = [50 + i * 15 for i in range(len(text))]
        y_positions = [100 + i * 50 for i in range(len(text))]
        text = ''.join([c.upper() if random.random() < 0.5 else c.lower() for c in text])
    else:  # neat
        x_positions = [50 + i * 15 for i in range(len(text))]
        y_positions = [100 + i * 50 for i in range(len(text))]
        text = text.upper()

    # Draw text
    for i, char in enumerate(text):
        try:
            draw.text((x_positions[i], y_positions[i]), char, fill='black', font=font)
        except:
            draw.text((x_positions[i], y_positions[i]), char, fill='black')

    # Apply preprocessing: grayscale, noise reduction
    img = img.convert('L')  # Grayscale

    # Enhance contrast
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)

    if output_path:
        img.save(output_path)
        return output_path
    return img

def run_ocr(image_path):
    """
    Run Tesseract OCR on an image
    Returns: (text, confidence)
    """
    # Output paths
    output_base = OCR_OUTPUT / Path(image_path).stem
    txt_path = str(output_base) + ".txt"

    # Run Tesseract with confidence output
    cmd = [
        "tesseract", str(image_path), str(output_base),
        "-l", "eng",
        "--oem", "1",
        "--psm", "6",
        "tsv"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Parse TSV for confidence
    confidence = 0
    tsv_path = str(output_base) + ".tsv"
    if os.path.exists(tsv_path):
        with open(tsv_path, 'r') as f:
            lines = f.readlines()
            if len(lines) > 1:
                confidences = []
                for line in lines[1:]:  # Skip header
                    parts = line.strip().split('\t')
                    if len(parts) > 10:
                        try:
                            confidences.append(float(parts[10]))
                        except:
                            pass
                if confidences:
                    confidence = sum(confidences) / len(confidences)

    # Read extracted text
    with open(txt_path, 'r') as f:
        text = f.read().strip()

    return text, confidence

def preprocess_image(image_path):
    """
    Apply preprocessing pipeline: grayscale, noise reduction, contrast enhancement
    """
    img = Image.open(image_path)

    # Grayscale
    img = img.convert('L')

    # Noise reduction using median filter
    from PIL import ImageFilter
    img = img.filter(ImageFilter.MedianFilter(size=3))

    # Contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)

    return img

def test_ocr_pipeline():
    """
    Main testing function
    """
    print("=" * 60)
    print("OCR PIPELINE TESTING")
    print("=" * 60)

    # Test cases
    test_cases = [
        {
            "name": "neat_handwriting",
            "text": "Math is fun",
            "style": "neat"
        },
        {
            "name": "messy_handwriting",
            "text": "Geometry",
            "style": "messy"
        },
        {
            "name": "mixed_case",
            "text": "Problem solving",
            "style": "mixed_case"
        },
        {
            "name": "numbers",
            "text": "123 456 789",
            "style": "neat"
        },
        {
            "name": "equation",
            "text": "x + y = 10",
            "style": "neat"
        }
    ]

    results = []

    for test_case in test_cases:
        print(f"\n{'-' * 60}")
        print(f"Testing: {test_case['name']}")
        print(f"Original text: {test_case['text']}")
        print(f"Style: {test_case['style']}")

        # Create test image
        image_path = TEST_IMAGES / f"{test_case['name']}.png"
        create_handwriting_text(
            test_case['text'],
            style=test_case['style'],
            output_path=str(image_path)
        )
        print(f"Created: {image_path}")

        # Test without preprocessing
        print("\n--- Without Preprocessing ---")
        text_raw, conf_raw = run_ocr(image_path)
        print(f"Extracted: {text_raw}")
        print(f"Confidence: {conf_raw:.2f}%")

        # Test with preprocessing
        print("\n--- With Preprocessing ---")
        preprocessed = preprocess_image(image_path)
        preprocessed_path = TEST_IMAGES / f"{test_case['name']}_preprocessed.png"
        preprocessed.save(preprocessed_path)
        text_pp, conf_pp = run_ocr(preprocessed_path)
        print(f"Extracted: {text_pp}")
        print(f"Confidence: {conf_pp:.2f}%")

        # Calculate accuracy
        accuracy_raw = 0
        accuracy_pp = 0

        if test_case['text']:
            accuracy_raw = len(set(text_raw.lower()) & set(test_case['text'].lower())) / len(test_case['text']) * 100
            accuracy_pp = len(set(text_pp.lower()) & set(test_case['text'].lower())) / len(test_case['text']) * 100

        result = {
            "name": test_case['name'],
            "original_text": test_case['text'],
            "style": test_case['style'],
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

        results.append(result)

    # Save results
    results_path = OCR_OUTPUT / "test_results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")

    for result in results:
        print(f"\n{result['name']}:")
        print(f"  Style: {result['style']}")
        print(f"  Without Preprocessing:")
        print(f"    Confidence: {result['raw']['confidence']:.2f}%")
        print(f"    Accuracy: {result['raw']['accuracy']:.2f}%")
        print(f"  With Preprocessing:")
        print(f"    Confidence: {result['preprocessed']['confidence']:.2f}%")
        print(f"    Accuracy: {result['preprocessed']['accuracy']:.2f}%")

    print(f"\nResults saved to: {results_path}")

    return results

if __name__ == "__main__":
    test_ocr_pipeline()
