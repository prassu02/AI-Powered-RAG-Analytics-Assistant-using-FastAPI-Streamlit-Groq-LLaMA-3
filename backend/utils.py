from pypdf import PdfReader

# -----------------------------------
# Load File
# -----------------------------------

def load_file(file_path):

    text = ""

    # PDF Files
    if file_path.endswith(".pdf"):

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # TXT Files
    elif file_path.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    # CSV Files
    elif file_path.endswith(".csv"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    return text

# -----------------------------------
# Split Text into Chunks
# -----------------------------------

def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks
