
# 🧠 Smart FAQ Chatbot

A lightweight, free, and fully local chatbot for answering common questions using document embeddings — powered by FAISS, HuggingFaceEmbeddings, and a FastAPI + Streamlit stack.

---

## 📌 Use Case

This chatbot is ideal for:
- 📋 Customer support portals (answering FAQs)
- 🏢 Internal HR or IT helpdesks
- 🏫 College or course FAQs
- 🧾 Policy bots (company rules, return/shipping policy, etc.)

Unlike generative AI models (which can hallucinate), this system retrieves only verified answers from your uploaded content — making it accurate, safe, and free.

---

## 🔭 Future Scope

- ✅ Add an LLM (like GPT4All or LLaMA) for answer generation
- 🌐 Host frontend with Streamlit Cloud, backend with Render
- 🧾 Upload PDFs, TXT, DOCX files (not just CSV)
- 🔐 Add authentication
- 🧠 Summarize long documents using chunking + LLM
- 🌎 Multilingual Q&A via translation pipelines

---

## 🧱 Folder Structure

```
smart_faq_chatbot/
├── backend/                    # FastAPI backend with FAISS and LangChain
│   ├── main.py                # API routes and retrieval logic
│   ├── faq.csv                # Your FAQ data (Question, Answer)
│   ├── requirements.txt       # Backend dependencies
│   ├── utils/
│   │   └── create_index.py    # Script to build FAISS vector index
│   └── vector_store/          # Auto-created FAISS index store
│
├── frontend/                   # Streamlit frontend
│   ├── app.py                 # Streamlit UI
│   ├── requirements.txt       # Frontend dependencies
│   └── .streamlit/config.toml # (Optional) Port/CORS settings
```

---

## ⚙️ Architecture

```
User → Streamlit UI → FastAPI → FAISS (via LangChain) → Answer
                          ↓
                  HuggingFace Embeddings
```

### 📚 Data Flow:

1. User asks a question in UI
2. Frontend sends it to FastAPI via `/query`
3. FastAPI uses FAISS + Embeddings to find the most similar FAQ answer
4. The matched answer is returned

---

## 🧪 Components Explained

| Component | Technology | Purpose |
|----------|------------|---------|
| `faq.csv` | CSV | Source of truth for Q&A pairs |
| `HuggingFaceEmbeddings` | sentence-transformers | Convert answers to dense vectors |
| `FAISS` | Facebook AI Similarity Search | Store and retrieve embeddings efficiently |
| `FastAPI` | Backend API | Receives question, returns answer |
| `Streamlit` | UI | Simple web interface for interaction |

---

## 🚀 How to Run

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
python utils/create_index.py    # builds FAISS index
uvicorn main:app --port 10000
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Access frontend at:
```
http://localhost:8501
```

---

## 🧠 Example Questions

| Question | Answer |
|---------|--------|
| What is your return policy? | You can return items within 30 days. |
| How can I track my order? | Log in and check the 'My Orders' section. |

---

## 🛠️ Requirements

| Dependency | Version |
|------------|---------|
| Python | 3.9+ |
| FAISS | faiss-cpu |
| LangChain | langchain, langchain-community |
| Hugging Face | sentence-transformers |
| Streamlit | 1.20+ |
| FastAPI & Uvicorn | Latest |

---

## 🌐 Deployment

- 📦 Backend: Deploy on [Render](https://render.com)
- 🎯 Frontend: Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
- 🔐 Add secrets for keys or future LLMs via `.env` or cloud env settings

---

## 🏁 Credits

- Built using [LangChain](https://github.com/langchain-ai/langchain)
- Embeddings: `all-MiniLM-L6-v2` from `sentence-transformers`
- Inspired by RAG (Retrieval-Augmented Generation) pipelines
