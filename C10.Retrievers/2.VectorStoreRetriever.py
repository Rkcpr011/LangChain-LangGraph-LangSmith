from langchain_community.vectorstores import Chroma

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

# create croma vector store

vstore=Chroma.from_documents(
    documents=documents,
    embedding=embeddingModel,
    collection_name="myCollection"
)
retriever=vstore.as_retriever()

query="what is chroma used for?" 

result=retriever.invoke(query)

print(len(result))

for i , doc in enumerate(result):
    print(f" result ::{i+1}")
    print(f" content :: {doc.page_content}")




# why do we need vstore.asretriever???
result2=vstore.similarity_search(query,k=4)

for i , doc in enumerate(result2):
    print(f" result ::{i+1}")
    print(f" answer with similarity search :: {doc.page_content}")

