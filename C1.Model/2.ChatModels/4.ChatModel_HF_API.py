# there is two way to use open source Chat models
# 1 using Hugging face inference API
# 2. dowlonad the model and use it locally.
# here we will use the first one.
from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
import os
load_dotenv()
api_key=os.getenv("HUGGINGFACE_API_KEY")    

llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
   task="text-generation",    
    temperature=0.7,
    huggingfacehub_api_token=api_key
    )
model=ChatHuggingFace(llm=llm)
# on this llm we can call invoke method to get the response
result=model.invoke("What is the capital of india?")  # Example usage

print(result)  # Output the response from the LLM
