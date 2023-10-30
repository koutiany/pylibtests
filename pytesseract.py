#sudo apt-get install tesseract-ocr
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
 
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
 
    text = ''
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
 
        # Save the image to disk temporarily
        image_file = f"page_{page_num + 1}.png"
        image.save(image_file)
 
        # Perform OCR and append extracted text
        extracted_text = pytesseract.image_to_string(image)
        text += extracted_text
 
        # Remove the generated image file after extraction
        import os
        os.remove(image_file)
 
    pdf_document.close()
    return text
 
if __name__ == "__main__":
     pdf_path = '/home/tippy/Downloads/WritingSample_KH.pdf'  # Replace with your file path
     extracted_text = extract_text_from_pdf(pdf_path)
     print(extracted_text)
