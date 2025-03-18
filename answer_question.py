import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define FAISS index path
FAISS_INDEX_PATH = "faiss_index"

# Load the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Define a structured prompt template
prompt_template = PromptTemplate(
    template=(
        "You are an AI assistant answering questions **ONLY** based on retrieved web content.\n\n"
        "Previous Conversation:\n{chat_history}\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n\n"
        "Instructions:\n"
        "- Answer concisely and accurately using only the provided context.\n"
        "- If the answer is not in the context, say: 'I don't have enough information from the given sources.'\n"
        "- Do NOT make up any information.\n"
        "- If multiple answers exist, summarize them clearly.\n\n"
        "Answer:"
    ),
    input_variables=["chat_history", "context", "question"]
)

# Initialize memory for storing conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def answer_question(query, chat_history=None):
    # Load FAISS vector store (ensure FAISS index exists)
    if os.path.exists(FAISS_INDEX_PATH):
        faiss_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        print(" FAISS index loaded successfully.")
    else:
        raise ValueError(" FAISS index not found! Please run `ingest_data.py` first.")

    # Setup retriever & LLM
    retriever = faiss_store.as_retriever(search_kwargs={"k": 5})
    llm = ChatGroq(model="gemma2-9b-it", groq_api_key=GROQ_API_KEY)

    # Create a conversational retrieval chain (adds memory)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        output_key="answer",
        combine_docs_chain_kwargs={"prompt": prompt_template}  
    )

    # Run query with history
    result = qa_chain.invoke({"question": query})
    response = result["answer"]

    return response 
