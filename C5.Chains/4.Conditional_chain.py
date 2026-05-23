from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
"""RunnableBranch lets you build a conditional chain where different 
logic (chains) run based on a condition or decision at runtime"""
from langchain.schema.runnable import RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
load_dotenv()
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

parser=StrOutputParser()

class feedback(BaseModel):
    sentiment:Literal["Positive", "Negative"] = Field(description=" give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=feedback) 

template1=PromptTemplate(
    template="clasify the sentiment of following text into Positive or Negative. \n {feedback} \n format instructions --> {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)

classifier_chain=template1 | model | parser2
# create prompts for conditional branch
template2=PromptTemplate(
    template="write an appropriate reply to this Positive feedback \n {feedback}",
    input_variables=["feedback"]
)
template3=PromptTemplate(
    template="write an appropriate reply to this Negative feedback \n {feedback}",
    input_variables=["feedback"]
)
# creating branch for condtional execution
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="Positive", template2 | model| parser), # each component will have a function as condition --> which should return true and false
    (lambda x:x.sentiment=="Negative", template3 | model |parser),
     RunnableLambda(lambda x: "could not find sentiment")
)

final_chain=classifier_chain | branch_chain

result=final_chain.invoke({"feedback":"This is a terrible Phone."})
print(result)

final_chain.get_graph().print_ascii()