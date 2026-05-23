from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model=ChatOpenAI()

while True:
    User_query= input("You: ")
    if User_query.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    response = model.invoke(User_query)  # Example usage
    print("Chatbot:", response.content) 
    
    
    
     # Output the content of the response
# This code allows you to have a chat with the OpenAI model.
# You can type your queries, and the model will respond until you type "exit" to
# this chatbot does not have the context of previous messages, so it will not remember past interactions.
# If you want to maintain context, you would need to implement a way to store and pass previous messages to the model.
# chat history we need to send every time.

