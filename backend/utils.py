from pypdf import PdfReader

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
