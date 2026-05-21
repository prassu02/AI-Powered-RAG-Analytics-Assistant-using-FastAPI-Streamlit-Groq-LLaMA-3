from pypdf import PdfReader
import pandas as pd

def load_file(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join([p.extract_text() for p in reader.pages])

    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        return df.to_string()

    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()


def split_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks