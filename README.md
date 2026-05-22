 # 📊 RAG-Based Analytics Assistant

An **End-to-End Retrieval-Augmented Generation (RAG) system** that enables users to upload documents (PDF, CSV, TXT) and interact with them using **AI-powered semantic search + Groq LLM (LLaMA 3)**.

It combines **vector embeddings, similarity search, and LLM reasoning** to deliver intelligent, context-aware responses.

---

## 🚀 Live Demo

### 🔹 Backend API (Render)

👉 [https://ai-powered-rag-analytics-assistant-04r8.onrender.com](https://ai-powered-rag-analytics-assistant-04r8.onrender.com)

### 🔹 Frontend (Streamlit Cloud)

👉 [https://dwyzqnkno3wfpaptskstjg.streamlit.app/](https://dwyzqnkno3wfpaptskstjg.streamlit.app/)

---

## 🧠 System Architecture

```
User (Streamlit UI)
        ↓
FastAPI Backend (Render)
        ↓
Document Upload & Processing
        ↓
Text Chunking
        ↓
Embedding Model (Sentence Transformers)
        ↓
Vector Store (FAISS-like)
        ↓
Semantic Similarity Search
        ↓
Groq LLM (LLaMA 3)
        ↓
AI Response to UI
```

---

## 📁 Project Structure

```
rag-analytics-assistant/
│
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── embedder.py
│   ├── main.py
│   ├── ragpipeline.py
│   ├── utils.py
│   ├── vectorstore.py
│   ├── requirements.txt
│
├── frontend/
│   ├── __init__.py
│   ├── streamlit_app.py
│   ├── requirements.txt
│
├── uploads/
│
├── venv/
├── .env
├── .gitignore
├── Dockerfile
├── render.yaml
└── README.md
```

---

## ⚙️ Tech Stack

### 🔹 Backend

* FastAPI
* Uvicorn
* Python 3.10+

### 🔹 AI / ML

* SentenceTransformers (Embeddings)
* Groq API (LLaMA 3)
* Retrieval-Augmented Generation (RAG)

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
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Run Locally

### ▶️ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

---

### ▶️ Start Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```
http://localhost:8501
```

---

## 📡 API Endpoints

### 🔹 Upload Document

```
POST /upload
```

### 🔹 Query Document

```
POST /query?q=your_question
```

### 🔹 Response Format

```json
{
  "answer": "AI-generated response based on document context"
}
```

---

## 🧪 Example Use Cases

* 📄 PDF summarization
* 📊 Data analytics Q&A
* 🧠 Machine learning concept explanation
* 🔍 Semantic document search
* 💬 AI-powered knowledge assistant

---

## 💡 Key Features

### 🔹 RAG Pipeline

Combines:

* Document retrieval (Vector Search)
* Generative AI (Groq LLM)

### 🔹 Embeddings

Converts text into dense vector representations for semantic search.

### 🔹 Vector Store

Efficient similarity search over document embeddings.

### 🔹 Fast Inference

Powered by **Groq LLaMA 3 API** for ultra-fast responses.

---

## 🐳 Docker Support

```bash
docker build -t rag-assistant .
docker run -p 8000:8000 rag-assistant
```

---

## ☁️ Deployment

### 🔹 Backend (Render)

* Service: FastAPI
* Auto Deploy: GitHub Integration
* Live URL:
  👉 [https://ai-powered-rag-analytics-assistant-04r8.onrender.com](https://ai-powered-rag-analytics-assistant-04r8.onrender.com)

### 🔹 Frontend (Streamlit Cloud)

* Hosted on Streamlit Community Cloud
* Live URL:
  👉 [https://dwyzqnkno3wfpaptskstjg.streamlit.app/](https://dwyzqnkno3wfpaptskstjg.streamlit.app/)

---

## 📈 Future Improvements

* 🔥 Multi-turn conversation memory
* 🔥 Streaming responses (ChatGPT-like UI)
* 🔥 Advanced reranking (BGE / Cohere rerankers)
* 🔥 Multi-document RAG fusion
* 🔥 AWS deployment (EC2 + S3 + Lambda)
* 🔥 User authentication system
* 🔥 Chat history database (MongoDB / PostgreSQL)

---

## 👨‍💻 Author

**Prasanna Kumar**
Data Science & AI Engineer
Specialized in Machine Learning, Deep Learning, and RAG Systems

---

## ⭐ Project Highlights

✔ End-to-end RAG system
✔ Production-ready architecture
✔ Deployed backend + frontend
✔ Real-world AI assistant
✔ Portfolio-ready ML engineering project

