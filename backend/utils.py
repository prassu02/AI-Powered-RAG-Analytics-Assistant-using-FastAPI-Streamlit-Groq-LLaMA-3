from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# -----------------------------------
# Load PDF File
# -----------------------------------

def load_file(file_path):

    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

    return text.strip()


# -----------------------------------
# Split Text into Chunks
# -----------------------------------

def split_text(text):

    if not text or len(text.strip()) == 0:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks
