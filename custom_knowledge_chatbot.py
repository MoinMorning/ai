from pathlib import Path
from typing import List, Tuple

from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import TextLoader
from langchain.embeddings import LlamaCppEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from pydantic import BaseModel, Field
from langchain.chains import ConversationalRetrievalChain

# Functions
def initialize_embeddings() -> LlamaCppEmbeddings:
    return LlamaCppEmbeddings(model_path=model_path)

def load_documents() -> List:
    with open(text_path, 'r', encoding='utf-8') as f:
        return [f.read()]


def split_chunks(sources: List) -> List:
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=32)
    for chunk in splitter.split_documents(sources):
        chunks.append(chunk)
    return chunks

def generate_index(chunks: List, embeddings: LlamaCppEmbeddings) -> FAISS:
    texts = [doc.page_content for doc in chunks]
    metadatas = [doc.metadata for doc in chunks]
    return FAISS.from_texts(texts, embeddings, metadatas=metadatas)

# Constants
local_path = Path("./models/gpt4all-converted.bin")
model_path = Path("./models/ggml-model-q4_0.bin")
text_path = Path("./docs/state_of_the_union.txt")
index_path = Path("./full_sotu_index")

# Main execution
print("loading documents...")
sources = load_documents()
print("splitting chunks...")
chunks = split_chunks(sources)
print("loading embeddings...")
embeddings = initialize_embeddings()
print("generating index...")
vectorstore = generate_index(chunks, embeddings)
print("saving index...")
vectorstore.save_local(index_path)
print("index saved to", index_path)

# Chatbot loop
print("loading indexes...")
index = FAISS.load_local(index_path, embeddings)
print("index loaded")
print("loading language model...")
llm = GPT4All(model=local_path, n_ctx=2048, verbose=True)
qa = ConversationalRetrievalChain.from_llm(llm, index.as_retriever(), max_tokens_limit=400)

chat_history = []
print("Welcome to the State of the Union chatbot! Type 'exit' to stop.")
while True:
    query = input("Please enter your question: ")
    
    if query.lower() == 'exit':
        break
    result = qa({"question": query, "chat_history": chat_history})

    print("Answer:", result['answer'])
