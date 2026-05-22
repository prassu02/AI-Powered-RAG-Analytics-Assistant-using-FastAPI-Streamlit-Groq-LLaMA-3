from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os

from backend.utils import load_file, split_text
from backend.ragpipeline import ingest, ask_question

app = FastAPI()


# -------------------
# Health Check
# -------------------
@app.get("/")
def home():
    return {"message": "AI Powered RAG Analytics Assistant Running"}


# -------------------
# Upload PDF / Document
# -------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text
        text = load_file(file_path)

        if not text or not text.strip():
            return {"error": "No text extracted from document"}

        # Split into chunks
        chunks = split_text(text)

        if not chunks:
            return {"error": "No chunks created from document"}

        # Store embeddings
        ingest(chunks)

        return {
            "message": "Document uploaded successfully",
            "chunks": len(chunks)
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------
# ASK QUESTION API
# -------------------
class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(req: QuestionRequest):

    try:
        answer = ask_question(req.question)

        return {
            "question": req.question,
            "answer": answer
        }

    except Exception as e:
        return {"error": str(e)}
