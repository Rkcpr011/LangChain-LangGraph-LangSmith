# OpenaI Embeddings are Closed Source Embeddings.
# OpenAI provides a powerful API for generating embeddings from text.
# here we wiil embed only a single query which will passed in embed_query method  during the call.
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-small" 
     )


# we can use this embedding model to converr our text into vectors.
# the more dimension you give , the more context it can captures.
# we can call embed_query method to get the embedding of a query.
# this will return a list of floats representing the embedding vector.
result = embeddings.embed_query("What is the capital of France?")  # Example usage
print(str(result))  # Output the embedding vector