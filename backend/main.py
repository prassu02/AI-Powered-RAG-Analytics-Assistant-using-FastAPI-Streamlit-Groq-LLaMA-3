from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.utils import load_file, split_text
from backend.rag_pipeline import ask_question, ingest

# -----------------------------------
# FastAPI App
# -----------------------------------

app = FastAPI(
    title="RAG Analytics Assistant API",
    version="1.0",
    description="AI-powered RAG system using FastAPI + Groq + FAISS"
)

# -----------------------------------
# CORS Configuration
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Upload Directory
# -----------------------------------

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "RAG Analytics Assistant API Running"
    }

# -----------------------------------
# Upload Endpoint
# -----------------------------------

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Load document text
    text = load_file(file_path)

    # Split into chunks
    chunks = split_text(text)

    # Store embeddings
    ingest(chunks)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks": len(chunks),
        "message": "File uploaded and processed successfully"
    }

# -----------------------------------
# Query Endpoint
# -----------------------------------

@app.post("/query")
def query(q: str):

    answer = ask_question(q)

    return {
        "question": q,
        "answer": answer
    }
