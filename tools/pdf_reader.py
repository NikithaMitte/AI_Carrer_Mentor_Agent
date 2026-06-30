import PyPDF2
from typing import Optional

def extract_text_from_pdf(pdf_file) -> Optional[str]:
    """
    Extracts text from a given PDF file-like object.
    
    Args:
        pdf_file: A file-like object (e.g., from Streamlit file_uploader).
        
    Returns:
        The extracted text as a string, or None if extraction fails.
    """
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
