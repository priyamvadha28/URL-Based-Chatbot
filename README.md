# URL-Based-Chatbot

This application is a Python-based Q&A assistant that can answer questions by retrieving information directly from specified URLs. It leverages LangChain for orchestration, OpenAI for embeddings and language models, and FAISS for efficient similarity search.


Features:

URL-Based Knowledge: Extracts content from a predefined list of URLs to build its knowledge base.

Text Chunking: Splits large documents into smaller, manageable chunks for efficient processing.

Vector Embeddings: Converts text chunks into numerical vector embeddings using OpenAI's models.

FAISS Vector Store: Utilizes FAISS for fast and efficient similarity search to find relevant information.

Retrieval-Augmented Generation (RAG): Combines information retrieval with a large language model (OpenAI's Chat model) to generate accurate and contextually relevant answers.

Source Attribution: Provides the source URL(s) from which the answer was derived.

Interactive Command-Line Interface: Allows users to ask questions directly in the terminal.