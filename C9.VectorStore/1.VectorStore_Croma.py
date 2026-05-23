
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")  


# to make a text into a document
from langchain.schema import Document


# Create LangChain documents for IPL players

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and passion for the game.",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and explosive batting.",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"}
)

doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his deadly yorkers and calm under pressure.",
    metadata={"team": "Mumbai Indians"}
)

doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and finishing ability make him invaluable.",
    metadata={"team": "Chennai Super Kings"}
)

docs=[doc1,doc2,doc3 , doc4 , doc5]


# creating vector store of croma --need one
vector_store=Chroma(
    embedding_function=OpenAIEmbeddings(), # it will use to generate embeddings of text/docs
    persist_directory="croma_DB", # location of databse
    collection_name="Cricketers" #collection name
)

# adding documents into Croma DB
vector_store.add_documents(docs)

vector_store.get(include=["embeddings","documents","metadatas"])

vector_store.similarity_search_with_score(
   query="who among these are a bowlers",
   k=2 
)