# OpenaI Embeddings are Closed Source Embeddings.
# OpenAI provides a powerful API for generating embeddings from text.
# here we wiil embed docs ,instead of a query.
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-small" 
     )

docs=[
    "The capital of France is Paris.",
    "The capital of India is New Delhi.",
    "The capital of Japan is Tokyo.",
    "The capital of Germany is Berlin."
]


# we can use this embedding model to converr our docs into vectors.
# the more dimension you give , the more context it can captures.
# we can call embed documents method to get the embedding of a documents.
# this will return a list of floats representing the embedding vector.
result = embeddings.embed_documents(docs)  # Example usage
# this will return a list of embedding vectors for each document. basically a 2d list.
# each vector is a list of floats representing the embedding of the document.
print(str(result))  # Output the embedding vector