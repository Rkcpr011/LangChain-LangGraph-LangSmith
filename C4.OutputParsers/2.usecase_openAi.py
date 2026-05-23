# usecase: need to give prompt to one llm , get details on a topic , then give detailes to same llm ask for summary.
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")  

Model=ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,    
)

# 1st prompt
template1=PromptTemplate(
    template="write a detailed report on a {topic}.",
    input_variables=["topic"]
)

prompt1=template1.invoke({"topic":"Artificial Intelligence"})
response1=Model.invoke(prompt1)

# 2nd prompt
template2=PromptTemplate(
    template="write a5 line Summary for the following  report {text}.",
    input_variables=["text"]
)
prompt2=template2.invoke({"text":response1.content})
response2=Model.invoke(prompt2)

# printing final summary
print(response2.content)  # Output the summary from the LLM