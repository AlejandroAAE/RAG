from PyPDF2 import PdfReader
from io import BytesIO


def load_pdf_text(pdf_bytes):
    reader = PdfReader(BytesIO(pdf_bytes))
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text
