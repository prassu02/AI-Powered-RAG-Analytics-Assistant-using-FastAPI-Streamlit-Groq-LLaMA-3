from backend.embedder import model
from backend.vectorstore import VectorStore

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Vector DB (global)
vector_db = VectorStore()

# API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Groq client
client = Groq(api_key=api_key)


def ingest(text_chunks):
    """Store embeddings into FAISS"""
    embeddings = model.encode(text_chunks)
    vector_db.add(embeddings, text_chunks)


def ask_question(question):
    """RAG pipeline: retrieve + generate"""

    try:
        # Step 1: Embed query
        query_embedding = model.encode([question])[0]

        # Step 2: Retrieve similar chunks
        docs = vector_db.search(query_embedding)

        # Safety check
        if not docs:
            return "No relevant context found in uploaded documents."

        context = "\n".join(docs)

        # Step 3: Prompt engineering (important for ML interviews)
        prompt = f"""
You are a senior data science and AI analytics expert.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

Instructions:
- Give clear explanation
- Use simple language
- Add examples if helpful
- Focus on insights, not raw text
"""

        # Step 4: Groq LLM call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI analytics assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred in RAG pipeline: {str(e)}"