from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os   
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model=ChatOpenAI()

Chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    User_query= input("You: ")
    Chat_history.append(HumanMessage(content=User_query))
    if User_query.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    response = model.invoke(User_query)  
    Chat_history.append(AIMessage(content=response.content))
    print("Chatbot:", response.content) 

print(Chat_history)    

# roles are not defined in the chat_history, this is not a good practice to maintain such chat history.
# we need to maintain dictionary with roles like this:
# Chat_history = [{"role": "user", "content": User_query}, {"role":