from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import TypedDict , Literal ,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel , Field 
from langchain_core.messages import HumanMessage ,SystemMessage , BaseMessage
import os
from langgraph.checkpoint.memory import MemorySaver
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
checkpointer=MemorySaver()
graph=StateGraph(chatState)
graph.add_node("chat_node",chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatBot=graph.compile(checkpointer=checkpointer)

# config={'configurable':{'thread_id':"thread_1"}}
# response=chatBot.invoke({'messages':[HumanMessage(content="hi")]},config=config)
# ai_message=response['messages'][-1].content
# print(ai_message)

