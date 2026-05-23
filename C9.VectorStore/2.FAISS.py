from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import RetrievalQA

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# creating an instance of LLM
model=OpenAI()


# creating instance of Embedder
embedder=OpenAIEmbeddings()

# text loader
loader = TextLoader("data.txt", encoding="utf-8") 

# documemt loaded
docs=loader.load()

# print(docs)
print(type(docs[0]))

# text splitter
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)


# text splits in chunks
splitted_text=text_splitter.split_documents(docs)

# vector store creation and
"""✅ FAISS.from_documents(...) is:
A class method that:

Takes in a list of documents (splitted_text)

Converts them into vector embeddings using the given embedder (e.g., OpenAIEmbeddings)

Builds a FAISS index (a searchable vector database)

Stores the embeddings + original text in memory (inside the FAISS object)"""

# Create a FAISS vector store (database) from the embedded documents
# 'splitted_text' is a list of documents (usually text chunks), and 'embedder' turns them into numerical vectors
# FAISS.from_documents(...): Creates an in-memory searchable index from your documents
store = FAISS.from_documents(splitted_text, embedder) # this a library where all vector stored

# Define a user query to search against the vector store
query = "what is FAISS and how it works?"

# Perform similarity search: retrieves top 2 most similar documents to the query
# .similarity_search(...): Finds similar documents based on a query.
answer = store.similarity_search(query, k=2)
print(answer[0].page_content)  # Print the content of the most similar document

# Perform similarity search along with similarity score (float: lower = more similar)
answer_with_score = store.similarity_search_with_score(query)
print(answer_with_score[0])  # Prints a tuple: (Document, similarity_score)

# Convert the FAISS store into a retriever (which can be used in a QA chain)
# .as_retriever(): Converts the vector store into a retriever for use in LangChain's QA chains.
# .as_retriever(): converts your FAISS vector store into a retriever object.
retrievers = store.as_retriever()  # a librarian who know how to find relevant doc quickly.
"""💡 Real-World Analogy for what is a retriever :
Imagine this:
You have a library (FAISS store) with books split into pages (text chunks).
You hire a librarian (retriever) who:
Doesn’t know everything
But is great at quickly finding the most relevant pages based on your question"""


# Create a RetrievalQA chain
# This combines: LLM (model), Retriever, and a "stuff" chain_type (concatenates context)
# RetrievalQA: Combines a retriever + LLM to answer questions from documents.
qa_chain = RetrievalQA.from_chain_type(llm=model, retriever=retrievers, chain_type="stuff")

# Ask a question to the QA chain
retriever_query = "what are FAISS Classes?"
results = qa_chain.invoke(retriever_query)  # Calls the chain with the question
print(results)  # Prints the final generated answer from the LLM

# Save the current FAISS index (vector store) to a local folder for reuse
# save_local(...) / load_local(...): Save and load FAISS indexes to reuse later.
store.save_local("faiss_index",embedder )

# Load the saved FAISS vector store from local directory using the same embedder
Saved_embedding_local = FAISS.load_local("faiss_index", embedder,allow_dangerous_deserialization=True )

# Create a second QA chain using the loaded FAISS store
"""RetrievalQA.from_chain_type:
This is a class method in LangChain that creates a Retrieval Question-Answering chain.
📦 Breakdown of parts:
RetrievalQA  A pre-built chain that:
Takes a query
Uses a retriever to get relevant documents
Passes those documents to an LLM (like OpenAI, HuggingFace, etc.)
Returns the final answer
.from_chain_type()  A helper method to quickly build this chain using a default chain type."""
qa_chain2 = RetrievalQA.from_chain_type(llm=model, retriever=Saved_embedding_local.as_retriever(), chain_type="stuff")

# Ask a question to the second QA chain (same as earlier)
retriever_query2 = "what are FAISS Classes?"
results = qa_chain.invoke(retriever_query2)
print(results)  # Prints the answer from the second QA chain
