import PyPDF2
import io
# def pdf_to_text(pdf_file: str) -> str:
#     with open(pdf_file, 'rb') as pdf:  # Use 'rb' mode (read binary) for PDFs
#         reader = PyPDF2.PdfReader(pdf)  # Use PdfReader instead of PdfFileReader
#         text = ""

#         for page in reader.pages:
#             text += page.extract_text() +"\n"


def pdf_to_text(resume_file) -> str:
    # Use PyPDF2 PdfReader directly on the file-like object
    reader = PyPDF2.PdfReader(resume_file)  # No need to wrap with io.BytesIO
    
    text = ""
    
    # Extract text from each page
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text
