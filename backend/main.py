from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.utils import load_file, split_text
from backend.embeddings import get_embeddings
from backend.vectorstore import VectorStore

app = FastAPI(title="AI Powered RAG Analytics Assistant")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Upload folder
UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize vector store
vectorstore = VectorStore()


@app.get("/")
def home():

    return {
        "message": "RAG Analytics Assistant Running Successfully"
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as f:

            content = await file.read()

            f.write(content)

        # Load document
        text = load_file(file_path)

        if not text.strip():

            return {
                "error": "No text extracted from document"
            }

        # Split into chunks
        chunks = split_text(text)

        # Generate embeddings
        embeddings = get_embeddings(chunks)

        # Store vectors
        vectorstore.add(embeddings, chunks)

        return {
            "message": "File uploaded successfully",
            "chunks": len(chunks)
        }

    except Exception as e:

        return {
            "detail": str(e)
        }
