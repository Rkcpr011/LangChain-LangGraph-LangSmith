from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")  

# Relevant health & wellness documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

embedder=OpenAIEmbeddings()

vstore=FAISS.from_documents(documents=all_docs , embedding=embedder)

similarity_retriever=vstore.as_retriever(
    search_type="similarity",search_kwargs={"k":5}
)

multiQuery_retriever=MultiQueryRetriever.from_llm(
    retriever=vstore.as_retriever(search_kwargs={"k":5}),
    llm=ChatOpenAI()
)

query="how to improve energy level and maintain balance"

similar_result=similarity_retriever.invoke(query)
multi_query_result=MultiQueryRetriever.invoke(query)

for i , doc in enumerate(similar_result):
    print(f" result ::{i+1}")
    print(f" content :: {doc.page_content}")

for i , doc in enumerate(multi_query_result):
    print(f" result ::{i+1}")
    print(f" content :: {doc.page_content}")    


