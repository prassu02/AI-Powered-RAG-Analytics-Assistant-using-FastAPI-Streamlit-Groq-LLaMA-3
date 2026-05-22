import streamlit as st
import requests

# ================= BACKEND URL =================
API_URL = "https://ai-powered-rag-analytics-assistant-04r8.onrender.com"

# ================= PAGE CONFIG =================
st.set_page_config(page_title="RAG Assistant", layout="wide")

# ================= CSS =================
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= TITLE =================
st.title("📊 RAG AI Analytics Assistant")

# ================= UPLOAD SECTION =================
st.header("📁 Upload Document")

file = st.file_uploader("Upload PDF / TXT / CSV")

if file is not None:
    if st.button("Upload to Backend"):

        with st.spinner("Uploading and processing..."):
            files = {"file": (file.name, file.getvalue())}

            try:
                res = requests.post(f"{API_URL}/upload", files=files)

                if res.status_code == 200:
                    data = res.json()

                    if "error" in data:
                        st.error(data["error"])
                    else:
                        st.success(f"Uploaded successfully! Chunks: {data.get('chunks', 0)}")

                else:
                    st.error(f"Upload failed: {res.text}")

            except Exception as e:
                st.error(f"Error: {str(e)}")

# ================= QUERY SECTION =================
st.header("💬 Ask Questions")

query = st.text_input("Enter your question about the document")

if st.button("Get Answer"):

    if not query:
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):

            try:
                res = requests.post(
                    f"{API_URL}/ask",
                    json={"question": query}
                )

                if res.status_code == 200:
                    data = res.json()
                    st.subheader("🤖 AI Answer")
                    st.write(data.get("answer", "No answer returned"))
                else:
                    st.error(f"Error: {res.text}")

            except Exception as e:
                st.error(f"Request failed: {str(e)}")
