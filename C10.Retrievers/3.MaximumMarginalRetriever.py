from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")  

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# step2 initialize the imbedding model
embeddingModel=OpenAIEmbeddings()

# create FAISS vector store

vstore=FAISS.from_documents(
    documents=documents,
    embedding=embeddingModel
)

retriever=vstore.as_retriever(
    search_type="mmr", # similarity search is default one , this will enable MMR
    search_kwargs={"k":3 , "lambda_mult":1}
)

query="what is chroma used for?" 

result=retriever.invoke(query)

print(len(result))

for i , doc in enumerate(result):
    print(f" result ::{i+1}")
    print(f" content :: {doc.page_content}")


