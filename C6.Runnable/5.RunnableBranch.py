from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableBranch , RunnablePassthrough

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# creating model
model=ChatOpenAI()
# creating prompt
template=PromptTemplate(
    template="write a detailed report on  {topic}.",
    input_variables=["topic"]

)

template2=PromptTemplate(
    template="Summarize the following text \n {text}.",
    input_variables=["text"]

)
# creating parser
parser=StrOutputParser()

# creating chain with a runnableSequence ---No need of pipe operator , pipe was doing same as sequencial Runnable in fact

report_generator=RunnableSequence(template,model , parser)

# creating the conditional branch
Conditional_branch=RunnableBranch(
    (lambda x: len(x.split())>200), RunnableSequence(template2,model ,parser),
    RunnablePassthrough()
    
) 

# final chain
final_chain=RunnableSequence(report_generator , Conditional_branch)
# invoking the chain

result=final_chain.invoke({"topic":"AI"})

print(result)

# Seq_chain.get_graph().print_ascii()
