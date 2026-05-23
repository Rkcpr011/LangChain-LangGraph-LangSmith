from langchain.tools import StructuredTool
from pydantic import BaseModel ,Field

class multiplyInput(BaseModel):
    a:int=Field(required=True,description="this is first number")
    b:int=Field(required=True,description="this is second number")

def MultiplyFunc(a:int , b:int)->int:
    return a*b

multiplyTool=StructuredTool.from_function(
    func=MultiplyFunc,
    name="multiply",
    description="Multiply two numbers",
    args_schema=multiplyInput
)    

# call this tool as runnable
Result=multiplyTool.invoke({"a":3,"b":12})

print(Result)