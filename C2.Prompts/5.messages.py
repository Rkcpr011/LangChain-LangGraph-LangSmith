from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
models = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# human message: which is the user input
# AI message:which is the model output
# system message:which is the system prompt set by developer , to define the behavior of the model.

messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
]
result= models.invoke(messages)  # Example usage
messages.append(AIMessage(content=result.content))  # Append the model's response to the messages list
print(messages)  # Output the messages list, which now includes the AI's response