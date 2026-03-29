from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.loader_service import load_pdf
from app.services.embedding_service import create_vector_store
from app.services.rag_service import get_qa_chain
from app.services.minio_service import upload_file

router = APIRouter()

qa_chain = None

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Upload to MinIO
    upload_file(file, file.filename)

    # Load + process
    docs = load_pdf(file_path)

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    """
    def split_my_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True # Helpful for referencing original PDF pages
    )
    return text_splitter.split_documents(docs)
    """

    chunks = splitter.split_documents(docs)

    create_vector_store(chunks)

    global qa_chain
    qa_chain = get_qa_chain()

    return {"message": "File uploaded and processed"}

@router.get("/ask")
def ask(query: str):
    global qa_chain
    if not qa_chain:
        qa_chain = get_qa_chain()

    answer = qa_chain.run(query)
    return {"answer": answer}