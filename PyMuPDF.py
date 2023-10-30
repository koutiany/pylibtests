import fitz  # PyMuPDF
 
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
 
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
 
    pdf_document.close()
    return text
 
if __name__ == "__main__":
    pdf_path = '/home/tippy/Downloads/WritingSample_KH.pdf'  # Replace with actual path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
