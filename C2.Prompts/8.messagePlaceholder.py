from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# chat template
chat_template=ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent."),
        MessagesPlaceholder(variable_name="chat_history"),  # Placeholder for chat history
        ("human", "{query}")  # Placeholder for today's user query
       ])

chat_history=[]
# load previsous chat history  ---->> this is usuallly done by loading it  from database but here we have saved it into a txt file.
with open("chathistory.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# prompt creation
prompt=chat_template.invoke({"chat_history": chat_history, "query": "where is my refund?."})

# Output the formatted prompt
print(prompt.to_messages())  # This will convert the formatted prompt to a list of 

model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
