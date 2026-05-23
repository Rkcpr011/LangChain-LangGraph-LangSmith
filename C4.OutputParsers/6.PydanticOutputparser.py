from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import  PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    temperature=0.7,
    huggingfacehub_api_token=api_key
    )

model= ChatHuggingFace(llm=llm)
# pydantic object----this will act  as schema
class person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="City of the person")  

parser=PydanticOutputParser(pydantic_object=person)

template=PromptTemplate(
    template="generate name , age and city of a fictional {place} person  \n {format_instructions}",
    input_variables=["place"],
    partial_variables={'format_instructions':parser.get_format_instructions()}
    )

prompt= template.invoke({"place":"Chinise "})

print(prompt)  # Output the prompt

chain=template | model | parser
result = chain.invoke({"place":"Chinise "})  # by default the input is empty as we are not passing any input variables

print(result)  


