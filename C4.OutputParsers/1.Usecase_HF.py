# usecase: need to give prompt to one llm , get details on a topic , then give detailes to same llm ask for summary.
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
api_key=os.getenv("HUGGINGFACE_API_KEY")

llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
   task="chat-completion",
    huggingfacehub_api_token=api_key
    )

Model=ChatHuggingFace(llm=llm)

# 1st prompt
template1=PromptTemplate(
    template="write a detailed report on a {topic}.",
    input_variables=["topic"]
)
prompt1=template1.invoke({"topic":"Artificial Intelligence"})
response1=Model.invoke(prompt1)

# 2nd prompt
template2=PromptTemplate(
    template="write a5 line Summary for the report {text}.",
    input_variables=["text"]
)
prompt2=template2.format({"text":response1.content})
response2=Model.invoke(prompt2)

# printing final summary
print(response2.content)  # Output the summary from the LLM