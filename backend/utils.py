from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_file(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        reader = PdfReader(file_path)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text


def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks
