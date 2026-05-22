from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_file(file_path):
    """Extract text from PDF safely"""

    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text.strip()

    except Exception as e:
        print("PDF Extraction Error:", e)
        return ""


def split_text(text):
    """Split text into chunks"""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_text(text)
