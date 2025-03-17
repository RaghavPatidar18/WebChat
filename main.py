import streamlit as st
from ingest_data import ingest_data
from answer_question import answer_question

# Set Streamlit Page Config
st.set_page_config(page_title="AiSensy Q&A Chatbot", layout="centered")

# Custom CSS for Centered Layout
st.markdown(
    """
    <style>
    .stApp {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .main-container {
        width: 60%;
        max-width: 700px;
        padding: 2rem;
        background-color: #f9f9f9;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }
    .stTextArea, .stTextInput {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Container
with st.container():
    st.markdown("<h1 style='text-align: center;'>AiSensy Chatbot</h1>", unsafe_allow_html=True)
    st.write("A web-based chatbot to answer your queries.")

    # Section 1: URL Ingestion
    st.markdown("---")
    st.subheader(" Ingest Webpages")
    
    urls_input = st.text_area("Enter URLs (one per line):", height=120, placeholder="https://aiSensy.com")
    
    if st.button(" Ingest Data"):
        urls = [url.strip() for url in urls_input.split("\n") if url.strip()]
        if urls:
            with st.spinner("🔍 Processing URLs..."):
                result = ingest_data(urls)
                st.success(result)
        else:
            st.warning(" Please enter at least one valid URL.")

    # Section 2: Q&A System
    st.markdown("---")
    st.subheader(" Ask Questions")

    query = st.text_input("Ask a question based on the ingested content:", placeholder="e.g., What is AI?")
    
    if query:
        with st.spinner(" Fetching answer..."):
            response = answer_question(query)
            st.markdown(f"** Answer:** {response}")
