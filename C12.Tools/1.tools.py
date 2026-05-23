from langchain_community.tools import DuckDuckGoSearchRun


#BUilt-In tools-- DuckDUckGO tool
SearchTools=DuckDuckGoSearchRun()
result=SearchTools.invoke("current News?")
print(result)


#BUilt-In tools-- shell tool


from langchain_community.tools import ShellTool
shell_tool=ShellTool()
shellResult=shell_tool.invoke("whoami")
print(shellResult)

# custom tool

from langchain_core.tools import tool
# three steps involved in defining a custom tool

# Step1.---> create your own function , docstring in function body will be useful for LLM
# LLM will undestand by this docstring that this tool does this operation.
def multiply(a,b):
    """ this Multiply two number"""
    return a*b

# step2 add type hinting to your function
def multiply(a:int , b:int)->int:
    """this Multiply two number"""
    return a*b

# step3. add a tool decorator
@tool # this decorator enables LLM to talk with our  normal python functions
def multiply(a:int , b:int)->int:
    """this Multiply two number"""
    return a*b

result=multiply.invoke({"a":3,"b":5})
print(result)

# features of the tools

print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema()) # this is what we sent to LLM when we connect our tool to LLM.


