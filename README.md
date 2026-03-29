# 🚀 ContextifyAI – Document Q&A (RAG System)

ContextifyAI is a production-ready Retrieval-Augmented Generation (RAG) application that allows users to upload documents (PDFs) and ask context-aware questions using LLMs.

---

## 🧠 Features

* 📄 Upload PDF documents
* 🧠 Automatic text chunking & embeddings
* 🔍 Semantic search using FAISS
* 🤖 Context-aware Q&A using LLM (OpenAI GPT)
* ☁️ MinIO integration for scalable file storage
* 🐳 Fully Dockerized setup

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM:** OpenAI GPT
* **Embeddings:** OpenAI Embeddings
* **Vector DB:** FAISS
* **Storage:** MinIO
* **Containerization:** Docker

---

## ⚙️ System Architecture

1. Upload PDF → stored in MinIO
2. Extract text → split into chunks
3. Generate embeddings → store in FAISS
4. User query → retrieve relevant chunks
5. LLM generates answer using context

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/tkushal-16/contextify-ai.git
cd contextify-ai
```

### 2. Setup Environment

```bash
cp .env.example .env
```

Update `.env`:

```
OPENAI_API_KEY=your_key
```

---

### 3. Run with Docker

```bash
docker-compose up --build
```

---

## 🌐 API Endpoints

### Upload PDF

```
POST /upload
```

### Ask Question

```
GET /ask?query=your_question
```

---

## 📦 Project Structure

```
contextify-ai/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes.py
│   ├── services/
│   │   ├── rag_service.py
│   │   ├── minio_service.py
│   │   ├── embedding_service.py
│   │   ├── loader_service.py
│   ├── utils/
│
├── data/
├── faiss_index/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## 🔥 Future Enhancements

* Multi-user document isolation
* Streaming responses (WebSockets)
* Hybrid search (BM25 + Vector)
* UI (React Chat Interface)
* Role-based access control

---

## 📌 Use Cases

* Internal company knowledge base
* Resume / document analyzer
* Customer support chatbot
* Legal / medical assistant

---

## 👨‍💻 Author

**T KUSHAL** [ *Backend Developer | AI Enthusiast* ]

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

## System Design Diagram 
### High-Level flow

```
                ┌──────────────────────┐
                │      User (UI)       │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │     FastAPI App      │
                └─────────┬────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MinIO      │  │  FAISS DB    │  │   OpenAI LLM │
│ (PDF Store)  │  │ (Embeddings) │  │ (Answer Gen) │
└──────────────┘  └──────────────┘  └──────────────┘
                          ▲
                          │
                  ┌──────────────┐
                  │  Retriever   │
                  └──────────────┘
```

### Detailed Flow
```
                [UPLOAD FLOW]

                User → Upload PDF → FastAPI
                        ↓
                Store in MinIO
                        ↓
                Extract Text (PyPDF)
                        ↓
                Chunking
                        ↓
                Embeddings
                        ↓
                Store in FAISS


                [QUERY FLOW]

                User → Ask Question
                        ↓
                Retriever (FAISS similarity search)
                        ↓
                Top-K relevant chunks
                        ↓
                Send context + query → LLM
                        ↓
                Return Answer
```
