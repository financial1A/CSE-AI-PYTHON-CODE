import fitz  # PyMuPDF
from PIL import Image
import numpy as np
import cv2
import io
import os

def save_image(image, output_path):
    image.save(output_path)
    print(f"Saved image to {output_path}")

def detect_chart_type(image):
    # Convert PIL Image to NumPy array
    image_np = np.array(image)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    
    # Apply binary thresholding to get a binary image
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Heuristics for bar charts and line charts
    num_bars = sum(cv2.contourArea(c) > 500 for c in contours)
    num_lines = sum(len(cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)) > 2 for c in contours)
    
    if num_bars > 5:
        return 'bar_chart'
    elif num_lines > 5:
        return 'line_chart'
    else:
        return 'unknown'

def crop_and_save_charts(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            
            chart_type = detect_chart_type(image)
            if chart_type in ['bar_chart', 'line_chart']:
                output_path = f"{output_folder}/page_{page_num + 1}_{chart_type}_{img_index + 1}.png"
                save_image(image, output_path)
                
    pdf_document.close()

# Example usage
pdf_path = 'prices_and_wages.pdf'
output_folder = 'extracted_images'
crop_and_save_charts(pdf_path, output_folder)
