# Import All the Required Libraries
import sys
import os
import torch
import textwrap

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
import nltk

# Download NLTK data
print("Downloading NLTK data (if not already present)...")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
print("NLTK data download complete.")

# Set your OpenAI API Key
os.environ['OPENAI_API_KEY'] = "xxxxxx"

# Set the URLs and extract the data from these URLs
URLs=[
    'https://blog.gopenai.com/paper-review-llama-2-open-foundation-and-fine-tuned-chat-models-23e539522acb',
    'https://www.mosaicml.com/blog/mpt-7b',
    'https://stability.ai/blog/stability-ai-launches-the-first-of-its-stablelm-suite-of-language-models',
    'https://lmsys.org/blog/2023-03-30-vicuna/'
]
print("Loading data from URLs...")

loaders = UnstructuredURLLoader(urls=URLs)
data = loaders.load()
print(f"Loaded {len(data)} documents from URLs.")

# Split the Text into Chunks
print("Splitting text into chunks...")
text_splitter=CharacterTextSplitter(separator='\n',
                                     chunk_size=1000,
                                     chunk_overlap=200)
text_chunks=text_splitter.split_documents(data)

print(f"Created {len(text_chunks)} text chunks.")

# Download the OpenAI Embeddings
print("Initializing OpenAI Embeddings...")
embeddings = OpenAIEmbeddings()
# query_result = embeddings.embed_query("Hello world")
# print(f"Embedding vector length: {len(query_result)}")

# Convert the Text Chunks into Embeddings and Create a Knowledge Base
print("Creating FAISS vector store...")
vectorstore=FAISS.from_documents(text_chunks, embeddings)
print("FAISS vector store created.")

# Create a Large Language Model (LLM) Wrapper
print("Initializing ChatOpenAI LLM...")
llm=ChatOpenAI()
# print(llm.predict("Please provide a concise summary of the Book Harry Potter"))

# Initialize the Retrieval QA with Source Chain
print("Initializing Retrieval QA with Sources Chain...")
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
print("Ready to answer questions!")

# Interactive Query Loop
print("\n--- Start interactive Q&A ---")
print("Type 'exit' to quit.")

while True:
    query = input(f"Prompt: ")
    if query.lower() == 'exit':
        print('Exiting')
        sys.exit()
    if query == '':
        continue

    try:
        result = chain({'question': query})
        print(f"\nAnswer: " + textwrap.fill(result["answer"], width=100))
        if 'sources' in result and result['sources']:
            print(f"Sources: {result['sources']}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your API key, internet connection, or try again.")