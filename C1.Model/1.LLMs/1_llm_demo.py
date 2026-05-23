# completion based LLM--> general purpose ,text generation
# this has become obsolete now
# this takes string as input and returns a string as output.
from langchain_openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llms =OpenAI(model="text-davinci-003", temperature=0.7)
# on this llm we can call invoke method to get the response
response=llms.invoke("What is the capital of France?")  # Example usage
print(response)  # Output the response from the LLM
# we are not getting output because the completion based LLM model from openai all has been depricated.
# To use the latest models, you need to use the chat-based models like gpt-3.5-turbo or gpt-4.



