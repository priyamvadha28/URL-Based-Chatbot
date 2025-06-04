# URL-Based-Chatbot

This application is a Python-based Q&A assistant that can answer questions by retrieving information directly from specified URLs. It leverages LangChain for orchestration, OpenAI for embeddings and language models, and FAISS for efficient similarity search.

**Features:**

- **URL-Based Knowledge:** Extracts content from a predefined list of URLs to build its knowledge base.
- **Text Chunking:** Splits large documents into smaller, manageable chunks for efficient processing.
- **Vector Embeddings:** Converts text chunks into numerical vector embeddings using OpenAI's models.
- **FAISS Vector Store:** Utilizes FAISS for fast and efficient similarity search to find relevant information.
- **Retrieval-Augmented Generation (RAG):** Combines information retrieval with a large language model (OpenAI's Chat model) to generate accurate and contextually relevant answers.
- **Source Attribution:** Provides the source URL(s) from which the answer was derived.
- **Interactive Command-Line Interface:** Allows users to ask questions directly in the terminal.

**Prerequisites:**

Before you begin, ensure you have the following installed:
- **Python 3.8+:** Download from python.org.
- **OpenAI API Key:** You'll need an API key from OpenAI to use their embedding and chat models. Obtain one from the OpenAI Platform.

**Installation:**

Follow these steps to set up the application locally:

**Clone the Repository (or create the files):**
If you have this code in a Git repository, clone it. Otherwise, create a new directory (e.g., url-qa-assistant) and save the provided Python code as app.py inside it.

git clone https://github.com/priyamvadha28/URL-Based-Chatbot.git:

    cd URL-Based-Chatbot

**Create a Virtual Environment**:
Navigate to your project directory in the terminal (URL-Based-Chatbot/) and create a virtual environment:

    python -m venv venv

Activate the Virtual Environment:
    
    .\venv\Scripts\activate

Your terminal prompt should now show (venv) at the beginning, indicating the virtual environment is active.

**Install Dependencies:**
      
      pip install -r requirements.txt
