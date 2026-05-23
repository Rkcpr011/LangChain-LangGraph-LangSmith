from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

model=ChatGoogleGenerativeAI(
    model="gemini-1.5-pro")
# on this llm we can call invoke method to get the response
result=model.invoke("What is the capital of France?")  # Example usage
# print(result)  # Output the response from the LLM
# output of chat-based---> this does not contain only string as output like completion based models, but it has so many more information but we need to get content which is our real answer.
# To get the content from the response
print(result.content)  # Output the content of the response