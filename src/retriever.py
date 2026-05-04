from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings)

    return db.as_retriever(search_kwargs={"k": 3})