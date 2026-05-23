from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# chatPromptTemplate will take list of tuples as input
chat_template=ChatPromptTemplate(
[("system", "You are a helpful {domain} expert."),
("human", "Explain in simple terms {topic}?")])

# filing the placeholders
prompts=chat_template.invoke({"domain":"AI", "topic":"ChatGPT"})

print(prompts)

# Output the formatted prompts
print(prompts.to_messages())  # This will convert the formatted prompt to a list of messages

