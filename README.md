# 📊 RAG-Based Analytics Assistant

An **End-to-End Retrieval-Augmented Generation (RAG) system** that allows users to upload documents (PDF, CSV, TXT) and ask intelligent questions using a combination of **vector search (embeddings)** and **Large Language Models (Groq LLM)**.

---

## 🚀 Live Features

* 📄 Upload documents (PDF / CSV / TXT)
* 🧠 AI-powered question answering
* 🔍 Semantic search using embeddings
* 📊 Context-aware analytics responses
* ⚡ Fast inference using Groq LLM (LLaMA 3)
* 🌐 REST API with FastAPI backend
* 🎨 Interactive Streamlit UI

---

## 🧠 System Architecture

```
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
Document Processing (PDF/CSV/TXT)
        ↓
Text Chunking
        ↓
Embedding Model (Sentence Transformers)
        ↓
Vector Database (FAISS-like store)
        ↓
Similarity Search
        ↓
Groq LLM (LLaMA 3)
        ↓
Final Answer Returned to UI
```

---

## 📁 Project Structure

```
rag-analytics-assistant/
│
├── backend/
│   ├── main.py              # FastAPI server
│   ├── rag_pipeline.py      # RAG logic (ingestion + QA)
│   ├── vectorstore.py      # Vector database (FAISS-like)
│   ├── embedder.py         # Embedding model
│   ├── utils.py            # Helper functions
│
├── frontend/
│   ├── streamlit_app.py    # Streamlit UI
│
├── data/
│   ├── uploads/            # Uploaded documents
│
├── vectorstore/
│   ├── faiss_index/        # Stored embeddings
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Tech Stack

### 🔹 Backend

* FastAPI
* Python 3.10+
* Uvicorn

### 🔹 AI / ML

* SentenceTransformers (Embeddings)
* Groq API (LLaMA 3.3 / 70B)
* RAG (Retrieval Augmented Generation)

### 🔹 Vector Database

* FAISS / Custom Vector Store

### 🔹 Frontend

* Streamlit

---

## 🔧 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-analytics-assistant.git
cd rag-analytics-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Run the Project

### ▶️ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### ▶️ Start Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 📡 API Endpoints

### 🔹 Upload File

```
POST /upload
```

**Body:** file (PDF/CSV/TXT)

---

### 🔹 Ask Question

```
POST /query?q=your_question
```

**Response:**

```json
{
  "answer": "AI-generated response based on document context"
}
```

---

## 🧪 Example Use Cases

* Explain ML concepts (Overfitting, Bias-Variance)
* Summarize uploaded PDFs
* Data analytics Q&A
* Document-based chat assistant
* Knowledge retrieval system

---

## 💡 Key Features Explained

### 🔹 RAG Pipeline

Combines:

* Document retrieval (Vector Search)
* Generative AI (Groq LLM)

### 🔹 Embedding Model

Converts text → vector representations for semantic search.

### 🔹 Vector Store

Stores embeddings for fast similarity search.

---

## 📊 Example Query

**User:**

> What is Overfitting?

**AI Response:**

* Definition
* Explanation
* Real-world analogy
* Example
* Solution (regularization, cross-validation)

---

## 🐳 Docker Support (Optional)

```bash
docker build -t rag-assistant .
docker run -p 8000:8000 rag-assistant
```

---

## 📈 Future Improvements

* 🔥 Chat memory (multi-turn conversation)
* 🔥 Streaming responses (ChatGPT-like typing)
* 🔥 Reranking (BGE / Cohere)
* 🔥 Multi-document RAG
* 🔥 AWS deployment (EC2 + S3)
* 🔥 Authentication system

---

## 👨‍💻 Author

**Prasanna Kumar**
Data Science & AI Engineer
Specialized in Machine Learning, Deep Learning, and RAG Systems

---

## ⭐ Project Highlights

✔ End-to-end RAG system
✔ Real-world AI assistant
✔ Production-style architecture
✔ Portfolio-ready ML project
