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

# config={'configurable':{'thread_id':"User123"}}

# response=chatBot.invoke({'messages':[HumanMessage(content="hi")]},config=config)
# # ai_message=response['messages'][-1].content
# # print(ai_message)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# instead of invoking , we will stram the response , to get the straming of output.
# below are the alone changes which we can do and see the streaming effect in backend.
# stream_generator_obj=chatBot.stream(
#     {'messages':[HumanMessage(content="how to make pasta?")]},
#     config=config,
#     stream_mode='messages'
# )
# print(type(stream_generator_obj))

# # now we need to iterate this stream obj
# # this has two major component 
# # message_chunk and metadata

# for message_chunk, metadata  in stream_generator_obj:
#     if message_chunk.content:
#         print(message_chunk.content , end=" " , flush=True)


#this is what we have to implement into frontend.
# here we have just checked and understand how this works. 


