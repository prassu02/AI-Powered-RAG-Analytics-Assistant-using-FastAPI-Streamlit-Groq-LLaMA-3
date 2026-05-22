from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
# Request Model
# -----------------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------------
# Home Endpoint
# -----------------------------------

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "RAG Analytics Assistant API Running Successfully"
    }

# -----------------------------------
# Health Check Endpoint
# -----------------------------------

@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }

# -----------------------------------
# Upload Endpoint
# -----------------------------------

@app.post("/upload", tags=["Document Processing"])
async def upload_file(file: UploadFile = File(...)):

    try:
        # Save uploaded file
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

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# -----------------------------------
# Query Endpoint
# -----------------------------------

@app.post("/query", tags=["RAG Q&A"])
def query(request: QueryRequest):

    try:
        answer = ask_question(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# -----------------------------------
# Run Locally
# -----------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
