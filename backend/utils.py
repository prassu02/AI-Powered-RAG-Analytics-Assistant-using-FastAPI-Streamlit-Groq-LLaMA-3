from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract
import os

# -----------------------------------
# Load PDF File
# -----------------------------------

def load_file(file_path):

    text = ""

    try:

        # -----------------------------------
        # Try Normal PDF Extraction
        # -----------------------------------

        pdf = PdfReader(file_path)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        # -----------------------------------
        # If No Text -> Use OCR
        # -----------------------------------

        if not text.strip():

            images = convert_from_path(file_path)

            for image in images:

                ocr_text = pytesseract.image_to_string(image)

                if ocr_text:
                    text += ocr_text + "\n"

        return text.strip()

    except Exception as e:

        print(f"PDF Reading Error: {e}")

        return ""

# -----------------------------------
# Split Text into Chunks
# -----------------------------------

def split_text(text, chunk_size=500):

    if not text:
        return []

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks
