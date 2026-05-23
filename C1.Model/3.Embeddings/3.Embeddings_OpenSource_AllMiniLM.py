# embedding using a open source model.
# here we will use AllMiniLM model from Hugging Face.

# This is a sentence-transformers model: It maps sentences & paragraphs 
# to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv  

import os
load_dotenv()

embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

# we can use this embedding model to convert our text into vectors.
# the more dimension you give, the more context it can capture.

text="PATNA is the capital of Bihar, India. It is located on the southern bank of the Ganges River."
result= embedding.embed_query(text)  # Example usage
# this will return a list of floats representing the embedding vector.
print(str(result))  # Output the embedding vector
# we can also embed documents using the same model.
docs=[
    "The capital of France is Paris.",
    "The capital of India is New Delhi.",
    "The capital of Japan is Tokyo.",
    "The capital of Germany is Berlin."
]
# we can call embed_documents method to get the embedding of a documents.

result_docs = embedding.embed_documents(docs)  # Example usage
# this will return a list of embedding vectors for each document. basically a 2d list.
# each vector is a list of floats representing the embedding of the document.   