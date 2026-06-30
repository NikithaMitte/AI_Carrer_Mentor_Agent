import os
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from tools.embeddings import get_embeddings
from langchain_core.documents import Document

VECTOR_STORE_DIR = "data/resources/faiss_index"

def get_vector_store():
    """
    Retrieves the FAISS vector store. Loads from disk if exists, otherwise creates a new one.
    """
    embeddings = get_embeddings()
    if os.path.exists(VECTOR_STORE_DIR) and os.path.exists(os.path.join(VECTOR_STORE_DIR, "index.faiss")):
        try:
            # allow_dangerous_deserialization is required for local loading in newer langchain versions
            return FAISS.load_local(VECTOR_STORE_DIR, embeddings, allow_dangerous_deserialization=True)
        except Exception as e:
            print(f"Error loading FAISS index, creating new one: {e}")
            
    # Initialize new FAISS store
    dim = len(embeddings.embed_query("test"))
    index = faiss.IndexFlatL2(dim)
    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )
    return vector_store

def add_to_vector_store(text: str, metadata: dict = None):
    """
    Adds a document to the vector store and saves it to disk.
    """
    vector_store = get_vector_store()
    doc = Document(page_content=text, metadata=metadata or {})
    vector_store.add_documents([doc])
    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)
    vector_store.save_local(VECTOR_STORE_DIR)
