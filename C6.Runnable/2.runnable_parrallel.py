from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# creating model
model=ChatOpenAI()
# creating prompt
template=PromptTemplate(
    template="Generate a tweet about {topic}.",
    input_variables=["topic"]

)

template2=PromptTemplate(
    template="generate a linkedin post about {topic}.",
    input_variables=["topic"]

)
# creating parser
parser=StrOutputParser()

# creating chain with a runnableSequence ---No need of pipe operator , pipe was doing same as sequencial Runnable in fact

Parallel_chain=RunnableParallel(
    {"tweet":RunnableSequence(template,model,parser),
    "LinkedIn":RunnableSequence(template2,model,parser)}
    )

# invoking the chain

result=Parallel_chain.invoke({"topic":"AI"})

print(result)

# Seq_chain.get_graph().print_ascii()
