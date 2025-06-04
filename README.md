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

**Usage:**

Once the installation and configuration are complete, you can run the application:
- Activate your virtual environment (if not already active).
- Run the Python script:

         python app.py

The script will first:
- Download NLTK data (if not already present).
- Load data from the predefined URLs.
- Split the text into chunks.
- Initialize OpenAI embeddings and create the FAISS vector store.
- Initialize the OpenAI Chat LLM and the Retrieval QA chain.

After these setup steps, you will see a Prompt where you can type your questions:

    Downloading NLTK data (if not already present)...
    NLTK data download complete.
    Loading data from URLs...
    Loaded X documents from URLs.
    Splitting text into chunks...
    Created Y text chunks.
    Initializing OpenAI Embeddings...
    Creating FAISS vector store...
    FAISS vector store created.
    Initializing ChatOpenAI LLM...
    Initializing Retrieval QA with Sources Chain...
    Ready to answer questions!
    
    --- Start interactive Q&A ---
    Type 'exit' to quit.
    Prompt: What is Vicuna?

Type your question and press Enter. The assistant will provide an answer and, if available, the source URLs.

- To exit the application, type exit and press Enter.

**Author:** This project is developed and maintained by Priyamvadha Pradeep.
