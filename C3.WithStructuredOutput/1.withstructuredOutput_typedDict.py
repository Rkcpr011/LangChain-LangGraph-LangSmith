from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

Model= ChatOpenAI()

# providing the data fortmat and with_structured_output method calling before invoking the model.
class review(TypedDict):
    Summary: str
    sentiment: str
    

structured_model=Model.with_structured_output(review)    

# now instead of callinf model and invoking we will invoke the structured_model.
response = structured_model.invoke(""""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
""")  # Example usage

print(response)  # Output the response from the LLM

print(type(response))  # Output the type of the response

print("summary is:",response["Summary"])  # Output the summary from the response
print("sentiment is:",response["sentiment"])  # Output the sentiment from the response

# how it works:
# 1. We define a TypedDict called `review` that specifies the structure of the output we expect from the model.
# 2. We create a structured model using `with_structured_output` method, passing the `review` TypedDict.
# 3. We invoke the structured model with a text input.
# 4. The model processes the input and returns a response that matches the structure defined in the `review` TypedDict.
# 5. We can access the structured output using the keys defined in the TypedDict.
