from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


# Using the chat-based model gpt-3.5-turbo
chatmodel = ChatOpenAI(model="gpt-4", temperature=0.7)
# on this llm we can call invoke method to get the response
result=chatmodel.invoke("What is the capital of France?")  # Example usage
# print(result)  # Output the response from the LLM
# output of chat-based---> this doe not contain only string as output like completion based models , but it has so many more information but we need to get content which is our real answer.

# To get the content from the response
print(result.content)  # Output the content of the response

# temperature parameter:
# - 0.0: deterministic output, same input will always yield the same output.
# - 0.7: more creative and varied output, but still consistent.
# for factual answer we need 0.3-.5 temperature. 
# explanation of max-completion-tokens:
# - max_completion_tokens: This parameter controls the maximum number of tokens (words or word pieces) that the model can generate in response to a prompt.
# - It limits the length of the generated response, ensuring that it doesn't exceed a certain size.
# - For example, if set to 100, the model will generate a response that is at most 100 tokens long.