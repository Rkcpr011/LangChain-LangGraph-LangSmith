from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


# instance of DirectoryLoader
directory_loader=DirectoryLoader(path='file',glob="*.pdf" , loader_cls=PyPDFLoader)

docs=directory_loader.load()

# print(docs)

#  this will be a list of document object---- so docs will be of type list but each item will be a document object
print(type(docs))

# no fo list
print(len(docs))

# checking type of first item in list
print(type(docs[0]))


# accessing metadata and content
print(docs[0].page_content)

print(docs[0].metadata)




