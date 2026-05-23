from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel , Field

# argument schema using pydantic
class MultiplyInput(BaseModel):
     a:int=Field(required=True,description="this is first number")
     b:int=Field(required=True,description="this is second number")


class MultiplyTool(BaseTool):
     name:str="multiply",
     description="multiply two numbers",
     args_schema=Type[BaseModel] = MultiplyInput

     def _run(self,a:int , b:int)->int:
          return a*b
     
multiplytool=MultiplyTool()
result=multiplytool.invoke({"a":12,"b":12})  
print(result)   