from fastapi import FastAPI, UploadFile
import os

from backend.utils import load_file, split_text
from backend.rag_pipeline import ingest, ask_question

app = FastAPI()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = load_file(file_path)
    chunks = split_text(text)

    ingest(chunks)

    return {"message": "File uploaded and processed successfully"}

@app.post("/query")
def query(q: str):
    answer = ask_question(q)
    return {"answer": answer}
