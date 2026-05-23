from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  

import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large" )

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

embeds= embeddings.embed_documents(documents)  # Embed the documents

# user query
query = "Who is known for his aggressive batting in cricket?"
query_embedding = embeddings.embed_query(query)  # Embed the query
# Calculate cosine similarity between the query embedding and document embeddings
# vector should be 2d list
similarities = cosine_similarity([query_embedding], embeds)[0] # to get the first row of a 2d array
print("Cosine Similarities:", similarities)

index,score=sorted(list(enumerate(similarities)), key=lambda x:x[1])[-1] #enumarate just to give them a index , conver them into list ,then sort it on behalf of second value get the last value
print(index,score)
print(query)
print(documents[index])
print("similarity scoere:", score)

#  here we are generating embedding every time we run the code.
# we are not saving our embedding which is not cost effective.
# we can save the embedding in a database or a file and then load it when needed.
# vector db we can use to save our vectors.