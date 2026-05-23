from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# creating model
model=ChatOpenAI()
# creating prompt
template=PromptTemplate(
    template="Give me 2 scientific facts about {topic}.",
    input_variables=["topic"]

)

template2=PromptTemplate(
    template="explain the facts in 2 lines each {text}.",
    input_variables=["text"]

)
# creating parser
parser=StrOutputParser()

# creating chain with a runnableSequence ---No need of pipe operator , pipe was doing same as sequencial Runnable in fact

Seq_chain=RunnableSequence(template , model , parser , template2 , model , parser)

# invoking the chain

# result=Seq_chain.invoke({"topic":"thoery of relativity"})

# print(result)

Seq_chain.get_graph().print_ascii()
