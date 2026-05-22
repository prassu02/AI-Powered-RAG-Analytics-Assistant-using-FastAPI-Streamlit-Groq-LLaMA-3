from fastapi import FastAPI, UploadFile, File
from backend.utils import load_file, split_text
from backend.ragpipeline import ingest

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Powered RAG Analytics Assistant Running"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        # Save uploaded file
        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text
        text = load_file(file_path)

        # Check empty text
        if not text.strip():
            return {"error": "No text extracted from document"}

        # Split into chunks
        chunks = split_text(text)

        # Store in vector DB
        ingest(chunks)

        return {
            "message": "Document uploaded successfully",
            "chunks": len(chunks)
        }

    except Exception as e:
        return {"error": str(e)}
