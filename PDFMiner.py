#pip install pdfminer.six

from pdfminer.high_level import extract_text
 
def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text
 
if __name__ == "__main__":
 pdf_path = '/home/tippy/Downloads/WritingSample_KH.pdf'  # Replace with actual path
 extracted_text = extract_text_from_pdf(pdf_path)
 print(extracted_text)
