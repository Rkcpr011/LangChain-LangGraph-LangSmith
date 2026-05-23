from langchain_community.document_loaders import  WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# instance of DirectoryLoader
url="https://www.flipkart.com/motorola-g45-5g-brilliant-blue-128-gb/p/itmc45105311348e?pid=MOBH3YKQT2HEAPAM&lid=LSTMOBH3YKQT2HEAPAMTX4TTX&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=e6895025-774b-47cb-a373-cb1febb50a39.MOBH3YKQT2HEAPAM.SEARCH&ppt=browse&ppn=browse&ssid=3fzdnb1bbk0000001754056409510"
Web_Base_Loader=WebBaseLoader(url)
docs=Web_Base_Loader.load()
print(docs)
print(type(docs)) 
print(type(docs[0]))
print(len(docs))

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question","text"]
)

chain=prompt | model | parser

result=chain.invoke({"question":"What is the price of this phone","text":docs[0].page_content})

print(result)





