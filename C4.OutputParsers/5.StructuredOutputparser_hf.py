from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
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

schema=[
    ResponseSchema(name="fact-1", description="A fact-1 about the topic"),
    ResponseSchema(name="fact-2", description="A fact-2 about the topic"),
    ResponseSchema(name="fact-3", description="A fact-3 about the topic")
        ]
parser = StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give 3 facts about the {topic} \n  {format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions':parser.get_format_instructions()}
    )

prompt= template.invoke({"topic":"Artificial Intelligence"})

print(prompt)  # Output the prompt

chain=template | model | parser
result = chain.invoke({"topic":"Artificial Intelligence"})  # by default the input is empty as we are not passing any input variables

print(result)  


