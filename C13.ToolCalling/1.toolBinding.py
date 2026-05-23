from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

from dotenv import load_dotenv
load_dotenv()
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# tool creation
@tool
def multiply(a:int , b:int)->int:
    """This function takes two number a and b and return their product as output"""
    return a*b


# tool binding
model =ChatOpenAI()
llm_with_tool=model.bind_tools(multiply)

result=llm_with_tool.invoke({"a":12,"b":1})
print(result)