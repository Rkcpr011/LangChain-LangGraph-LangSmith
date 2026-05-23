from langchain.text_splitter import RecursiveCharacterTextSplitter
text="""The Deep Learning Roadmap is a comprehensive guide that outlines the essential steps, concepts, and techniques needed to master the field of deep learning. Whether you're a beginner looking to start your journey in artificial intelligence or an experienced practitioner wanting to expand your knowledge, this roadmap will help you navigate through the complex world of deep learning. From understanding neural networks to implementing advanced models, this roadmap covers everything you need to know to become proficient in deep learning"""

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10
    
)

# split text method will return a list of string , each string having chunk size character.
result=text_splitter.split_text(text)
print(type(result))
print(len(result))
print(type(result[0]))
print(result)