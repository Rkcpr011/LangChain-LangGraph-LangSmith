# here instead of Inmemory saver we will use sqlite db.

from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import TypedDict , Literal ,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel , Field 
from langchain_core.messages import HumanMessage ,SystemMessage , BaseMessage
import os
from langgraph.checkpoint.sqlite import SqliteSaver

import sqlite3 # to connect with checkpointer
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

model=ChatOpenAI(model="gpt-4o")

from langgraph.graph.message import add_messages
class chatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]
def chat_node(state:chatState):
    query=state['messages']
    response=model.invoke(query)
    return {'messages':[response]}


connection=sqlite3.connect(database='chatbot.db',check_same_thread=False)
checkpointer=SqliteSaver(conn=connection)

graph=StateGraph(chatState)
graph.add_node("chat_node",chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatBot=graph.compile(checkpointer=checkpointer)

def retrieve_allExistingThreads():
    all_threads=set()
# to return the total exsiting chat threads.
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads) 
    

