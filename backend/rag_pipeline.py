from backend.embedder import model
from backend.vectorstore import VectorStore

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize vector database
vector_db = VectorStore()

# Load API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)


def ingest(text_chunks):
    """
    Store embeddings into FAISS vector database
    """

    if not text_chunks:
        raise ValueError("No text chunks provided")

    embeddings = model.encode(text_chunks)

    vector_db.add(embeddings, text_chunks)


def ask_question(question):
    """
    RAG pipeline:
    1. Embed question
    2. Retrieve similar chunks
    3. Generate answer using Groq LLM
    """

    try:

        # Generate query embedding
        query_embedding = model.encode([question])[0]

        # Retrieve relevant documents
        docs = vector_db.search(query_embedding)

        if not docs:
            return "No relevant context found in uploaded documents."

        # Combine retrieved chunks
        context = "\n\n".join(docs)

        # Prompt template
        prompt = f"""
You are a senior AI, Data Science, and Analytics expert.

Answer the question ONLY using the provided context.

Context:
{context}

Question:
{question}

Instructions:
- Give a clear explanation
- Use simple language
- Add examples if useful
- Focus on insights and analytics
"""

        # Groq LLM call
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
