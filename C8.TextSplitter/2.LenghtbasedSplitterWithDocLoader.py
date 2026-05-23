from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(file_path="Deep_learning.pdf")

doc_obj=loader.load()  # we will get one document object corresponding to each page with pyPDF loader
print(type(doc_obj))

Doc_obj_splitter=CharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10,
    separator=""
)
# here we will not use split_text method , instead we will use split_documents
# each chunk here will be a document object
result=Doc_obj_splitter.split_documents(doc_obj)
print(type(result))
print(len(result))
print(type(result[0]))  #every chunk even is a doc obj
print((result[0].page_content))
print((result[0].metadata))


