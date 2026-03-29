from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()

def create_vector_store(chunks):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("faiss_index")
    return db

def load_vector_store():
    return FAISS.load_local("faiss_index", embeddings)