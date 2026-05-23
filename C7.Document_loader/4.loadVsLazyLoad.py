from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# instance of DirectoryLoader
directory_loader=DirectoryLoader(path='file',glob="*.pdf" , loader_cls=PyPDFLoader)
docs=directory_loader.lazy_load()
#  this will be a list of document object---- so docs will be of type list but each item will be a document object
print(type(docs))  #--> return a generator object  which can be iterate

# no fo list
# print(len(docs))  ---> this wil; not work
# checking type of first item in list
# print(type(docs[0]))   ---> this wil; not work
# accessing metadata and content
# print(docs[0].page_content)  ---> this wil; not work
# print(docs[0].metadata)  ---> this wil; not work
# accessing meta data for each document object--- iteration
for document in docs:
    print(document.metadata)



