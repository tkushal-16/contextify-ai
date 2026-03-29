from langchain_openai import OpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.services.embedding_service import load_vector_store

def get_qa_chain():
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model="gpt-4")

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

# This is the old code using RetrievalQA.from_chain_type, which is now deprecated. The new recommended approach is to create the retrieval chain manually, as shown in the commented-out code below.
"""
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from app.services.embedding_service import load_vector_store

def get_qa_chain():
    # 1. Load your vector store and set up retriever
    db = load_vector_store()
    retriever = db.as_retriever(search_kwargs={"k": 3})

    # 2. Setup the LLM
    llm = ChatOpenAI(model="gpt-4")

    # 3. Create the "System Prompt" (Tells the AI how to behave)
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise.\n\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # 4. Create the document chain (How documents are processed)
    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    # 5. Create the final retrieval chain
    # This replaces the old RetrievalQA.from_chain_type
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain
"""