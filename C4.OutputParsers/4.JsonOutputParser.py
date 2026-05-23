from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
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

parser = JsonOutputParser()

template=PromptTemplate(
    template="Give me the name , age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()})

prompt= template.format()

print(prompt)  # Output the prompt

chain=template | model | parser
result = chain.invoke({})  # by default the input is empty as we are not passing any input variables

print(result)  


