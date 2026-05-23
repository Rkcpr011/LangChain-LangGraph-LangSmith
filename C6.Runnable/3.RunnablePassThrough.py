from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# creating model
model=ChatOpenAI()
# creating prompt

template=PromptTemplate(
    template="Generate a Joke {topic}.",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="generate explanation of the joke {joke}.",
    input_variables=["joke"]
)

# creating parser
parser=StrOutputParser()

# creating chain with a runnableSequence ---No need of pipe operator , pipe was doing same as sequencial Runnable in fact

Joke_generator_chain=RunnableSequence(template,model,parser)

parallel_chain=RunnableParallel({
    "explanation": RunnableSequence(template2, model , parser),
    "Joke":RunnablePassthrough()
})

final_chain=RunnableSequence(Joke_generator_chain , parallel_chain)

result=final_chain.invoke({"topic":"Democracy"})
print(result)
# Seq_chain.get_graph().print_ascii()
