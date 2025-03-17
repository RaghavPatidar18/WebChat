import os
# from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables
# load_dotenv()

# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Define FAISS index storage file
FAISS_INDEX_PATH = "faiss_index"

def ingest_data(urls):
    """
    Extracts text from URLs, processes it, and stores it in FAISS.
    """
    docs = []
    for url in urls:
        try:
            doc = WebBaseLoader(url).load()
            docs.extend(doc)
            print(f"Loaded content from: {url}")
        except Exception as e:
            print(f"Failed to load {url}: {e}")

    if not docs:
        return "No valid documents found."

    # Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    doc_splits = text_splitter.split_documents(docs)

    # Create FAISS vector store
    if os.path.exists(FAISS_INDEX_PATH):
        faiss_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings,allow_dangerous_deserialization=True)
        print("Loading existing FAISS index...")
    else:
        faiss_store = FAISS.from_documents(doc_splits, embeddings,allow_dangerous_deserialization=True)
        print("Creating new FAISS index...")

    # Add new documents to FAISS
    faiss_store.add_documents(doc_splits)
    faiss_store.save_local(FAISS_INDEX_PATH)

    return f"Inserted {len(doc_splits)} document chunks into FAISS."


