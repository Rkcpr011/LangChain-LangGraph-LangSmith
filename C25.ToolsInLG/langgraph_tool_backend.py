from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import TypedDict , Literal ,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel , Field 
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage ,SystemMessage , BaseMessage
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import os
import requests
import random
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3 # to connect with checkpointer
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI()
# tools
search_tools=DuckDuckGoSearchRun() #prebuild tool

@tool
def calculator(first_nu:float,second_num:float , operation:str)->dict:
    """perfrom basic arithmetic operations like add, subtract,multiply , divide"""

    try:
        if operation=='add':
            return {"result":first_nu+second_num}
        elif operation=='subtract':
            return {"result":first_nu-second_num}   
        elif operation=='multiply':
            return {"result":first_nu*second_num}
        elif operation=='divide':
            return {"result":first_nu/second_num}
        else:
            return {'error':f'unsupported operation {operation}'}
        return {}
    except Exception as e:
        return {'error':str(e)}
    
@tool    
def get_stock_price(symbol:str)->dict:
       """get the current stock price for a given stock symbol eg AAPL , TSLA"""
       url=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=X1PHC8TFH5JGRA75'
       response=requests.get(url)
       return response.json()


tools=[search_tools,calculator,get_stock_price]

llm_with_tools=llm.bind_tools(tools)
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
def chat_node(state:ChatState):
    """This is a LLM node which can answer or request a tool call"""
    messages=state['messages']
    response=llm_with_tools.invoke(messages)
    return {"messages":[response]}
tool_node=ToolNode(tools)

# checkpointer 
connection=sqlite3.connect(database='chatbot.db',check_same_thread=False)
checkpointer=SqliteSaver(conn=connection)

graph=StateGraph(ChatState)
graph.add_node("chat_node",chat_node)
graph.add_node("tools",tool_node)
graph.add_edge(START,"chat_node")
# if a llm ask for a tool
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge('tools','chat_node')
chatbot=graph.compile(checkpointer=checkpointer)


# out=chatbot.invoke({'messages':[HumanMessage(content="hi")]})
# print(out['messages'][-1].content)
# out=chatbot.invoke({'messages':[HumanMessage(content="what is 23 multiply by 32")]})
# print(out['messages'][-1].content)
# out=chatbot.invoke({'messages':[HumanMessage(content="stock price of apple")]})
# print(out['messages'][-1].content)

def retrieve_allExistingThreads():
    all_threads=set()
# to return the total exsiting chat threads.
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads) 