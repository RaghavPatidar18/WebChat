# AI Web Content Q&A System

This project is an AI-powered question-answering system that retrieves content from given web pages, stores it in a vector database (FAISS), and answers user queries based **only** on the retrieved data. It utilizes **LangChain**, **Hugging Face Embeddings**, **Groq API**, and **FAISS** for efficient information retrieval and response generation.

## Features
- Extracts webpage content from given URLs
- Stores and retrieves text using **FAISS**
- Uses **Hugging Face Embeddings** for vectorization
- Answers user questions based only on stored data
- Conversational memory support for contextual Q&A

## Technologies Used
- **Python**
- **LangChain**
- **FAISS (Facebook AI Similarity Search)**
- **Hugging Face Embeddings**
- **Groq API (LLM Inference)**
- **dotenv (Environment Variables Handling)**

## Project Structure
```
AISENSY/
│── templates/             # Contains HTML, CSS, and JS files for frontend
│   ├── index.html         # Main frontend page
│   ├── styles.css         # Styling for frontend
│   ├── script.js          # JavaScript functionality
│── answer_question.py     # Handles user queries using FAISS & Groq LLM
│── ingest_data.py         # Extracts and stores webpage content into FAISS
│── app.py                 # Main application script
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (GROQ API Key, etc.)
```

## Installation

### 1. Clone the Repository and go to the directory
```sh
git clone https://github.com/RaghavPatidar18/WebChat.git
```
```sh
cd WebChat
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run
```sh
python app.py
```

You can modify the script to include specific URLs for ingestion.

### 5. Start the Application
Run the Q&A system:
```sh
python app.py
```

### 6. Application live on
```sh
http://localhost:5000/
http://127.0.0.1:5000
```

## Usage
- Open the **index.html** in your browser.
- Enter a question related to the ingested content.
- The AI will respond based **only** on the retrieved webpage content.

## How It Works
1. **`ingest_data.py`**
   - Extracts text from given URLs.
   - Splits text into chunks.
   - Converts text into vector embeddings and stores them in FAISS.

2. **`answer_question.py`**
   - Loads FAISS index and retrieves relevant context.
   - Uses **Groq API (Gemma-2-9B-IT LLM)** to generate answers.
   - Stores conversation history for contextual responses.

## Future Enhancements
- Deploy as a web app using **Streamlit / FastAPI**
- Add support for multiple document formats (PDF, TXT, etc.)
- Improve response detail with a larger LLM model


