# usecase: need to give prompt to one llm , get details on a topic , then give detailes to same llm ask for summary.
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

# 2nd prompt
template2=PromptTemplate(
    template="write a 5 line Summary for the following  report {text}. please remember it should npot be more than 5 line , strongly concise." ,
    input_variables=["text"]
)

parser=StrOutputParser()

# creating a chain of the templates and model
# this will take the output of template1 as input to Model, then output of Model as
chain=template1 | Model | parser | template2 | Model| parser 

result=chain.invoke({"topic":"Black Holes"})

print(result)  # Output the summary from the LLM
