from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

parser=StrOutputParser()

template= PromptTemplate(
    template="Generate 5 interesting facts about {topic}?",
    input_variables=["topic"]
)

chain=template | model | parser

# result=chain.invoke({"topic":"Artificial Intelligence"})

# print(result)  # Output the response from the LLM


chain.get_graph().print_ascii() # Visualize the chain grap