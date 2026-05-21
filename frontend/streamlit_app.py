import streamlit as st
import requests

# ================= PAGE CONFIG (MUST BE FIRST) =================
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
st.title("📊 RAG- AI Analytics Assistant ")

# ---------------- Upload Section ----------------
file = st.file_uploader("Upload file (PDF/CSV/TXT)")

if file:
    files = {"file": (file.name, file.getvalue())}
    res = requests.post("http://127.0.0.1:8000/upload", files=files)

    if res.status_code == 200:
        st.success(res.json()["message"])
    else:
        st.error("Upload failed")

# ---------------- Query Section ----------------
query = st.text_input("Ask your analytics question")

if st.button("Get Answer"):

    if not query:
        st.warning("Please enter a question")
    else:
        res = requests.post(
            "http://127.0.0.1:8000/query",
            params={"q": query}
        )

        data = res.json()
        answer = data.get("answer", "No response received")

        st.subheader("🤖 AI Answer")
        st.markdown(answer)