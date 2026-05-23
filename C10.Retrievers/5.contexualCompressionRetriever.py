from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings ,ChatOpenAI
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")  

# Recreate the document objects from the previous data
docs = [
    Document(page_content=
    """The Grand Canyon is one of the most visited natural wonders in the world.
    Photosynthesis is the process by which green plants convert sunlight into energy.
    Millions of tourists travel to see it every year. The rocks date back millions of years.""",
    metadata={"source": "Doc1"}),

    Document(page_content=
    """In medieval Europe, castles were built primarily for defense.
    The chlorophyll in plant cells captures sunlight during photosynthesis.
    Knights wore armor made of metal. Siege weapons were often used to breach castle walls.""",
    metadata={"source": "Doc2"}),

    Document(page_content=
    """Basketball was invented by Dr. James Naismith in the late 19th century.
    It was originally played with a soccer ball and peach baskets. NBA is now a global league.""",
    metadata={"source": "Doc3"}),

    Document(page_content=
    """The history of cinema began in the late 1800s. Silent films were the earliest form.
    Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.""",
    metadata={"source": "Doc4"}),
]

embedder=OpenAIEmbeddings()
vstore=FAISS.from_documents(docs,embedder)

base_retriever=vstore.as_retriever(search_kwargs={"k":5})

# now we need compression retreiver
# a complression retreiver will need a base retriever , a complressor , which is basiccaly a llm only
model=ChatOpenAI()
compressor=LLMChainExtractor.from_llm(model)

Compression_retriever=ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
    )

query="what is photosynthesis?"

answer=Compression_retriever.invoke(query)

for i , doc in enumerate(answer):
    print(f" result ::{i+1}")
    print(f" content :: {doc.page_content}")    
