from pypdf import PdfReader

# -----------------------------------
# Load PDF File
# -----------------------------------

def load_file(file_path):

    text = ""

    try:

        if file_path.endswith(".pdf"):

            pdf = PdfReader(file_path)

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        text = text.strip()

        return text

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
