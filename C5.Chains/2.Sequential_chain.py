from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

parser=StrOutputParser()

template1= PromptTemplate(
    template="Generate a very technical,detailed and Beginner friendly report on  {topic}.",
    input_variables=["topic"]
)

template2= PromptTemplate(
    template="Generate a brief summary of the following   {text}.",
    input_variables=["text"]
)

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic":"Machine Learning"})

print(result)  # Output the response from the LLM


chain.get_graph().print_ascii() # Visualize the chain grap