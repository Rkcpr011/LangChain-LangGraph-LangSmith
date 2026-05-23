from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage , ToolMessage
import requests

from dotenv import load_dotenv
load_dotenv()
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# step1+++++++++++++++++++++++++++ tool creation +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# tool creation we need two tools , one for conversion factor another for multiplication
@tool
def get_conversionFactor(baseCurrency:str , targetCurrency:str)->float:
    """This function takes two string Basecurrency and targetcurrency and fetch the  currency conversion factor between them."""
    URL=f"https://v6.exchangerate-api.com/v6/c9a8c6a3938d23d4f5dec929/pair/{baseCurrency}/{targetCurrency}"


    response=requests.get(URL)
    return  response.json()

# result=get_conversionFactor.invoke({"baseCurrency":"USD","targetCurrency":"INR"})
# print(result)
# print(result["conversion_rate"])

# second tool
@tool
def convert(base_cuurency_value:int , conversion_factor:float)->float:
    """this function will be used to multiply the conversion factor to the baseCurrency to get the target currrecy"""
    targetValue=base_cuurency_value*conversion_factor
    return targetValue

# result2=multiplication.invoke({"base":2,"conversion_factor":result["conversion_rate"]})
# print(f'Total amount in from  USD into INR is : {result2}')

# step2++++++++++++++++++++++++++++++++ tool binding ++++++++++++++++++++++++++++++++++++++++++++++++++++
# tool binding
model =ChatOpenAI()
llm_with_tool=model.bind_tools([get_conversionFactor,convert])

# # Now last step5 to sent this all to LLM so that LLm can think and generate the final output.
Messages=[HumanMessage("what is the conversion factor Between USD and INR? based on that can you convert  10 USD into INR? ")]

# # tool calling
AI_Suugested_Tool_Call_result=llm_with_tool.invoke(Messages)
Messages.append(AI_Suugested_Tool_Call_result)
print(Messages)
print(AI_Suugested_Tool_Call_result.tool_calls)

# # tool execution ----> here also we will mot get LLM generated output , only output of tool function will be available. now those answer will be passed into LLM as conversation history , LLM will get the enitre context and generate a AI response.

toolresult1=get_conversionFactor.invoke({"baseCurrency":"USD","targetCurrency":"INR"})
print(toolresult1)
Messages.append(
    ToolMessage(tool_call_id="tool1", content=str(toolresult1))
)
print(toolresult1["conversion_rate"])

toolResult2=convert.invoke({"base_cuurency_value":10,"conversion_factor":toolresult1["conversion_rate"]})
Messages.append(
    ToolMessage(tool_call_id="tool2", content=str(toolResult2))
)
print(Messages)

# # till here we were maintaining the history of our chat , and it is supposed to pass to LLM so that LLM can use them and understand and generate the output
gen_AI_output=llm_with_tool.invoke(Messages)
print(gen_AI_output)