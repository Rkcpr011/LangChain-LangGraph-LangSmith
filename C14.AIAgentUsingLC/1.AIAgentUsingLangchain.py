from langchain_openai import ChatOpenAI ,OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
from openai import OpenAI
from langchain_community.tools import DuckDuckGoSearchRun


load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


# Step1. tools and LLM
search_tool=DuckDuckGoSearchRun()


result=search_tool.invoke("top 10 ews in India today?")
# print(result)
# We have an istance of LLM


@tool
def getWeatherData(city:str)->str:
    """this function fetches the current weather data for a given city"""


    url = f'https://api.weatherstack.com/current?access_key=fc5cc1f86d29ffcd8cfc7585ed59eceb&query={city}'


    response=requests.get(url)
    return response.json()
llm=ChatOpenAI()


# result=llm.invoke("hi")
# print(result.content)


# We can create an agent with tool and LLM


from langchain.agents import create_react_agent , AgentExecutor
from langchain import hub


# Step2: create a prompt: here we will pull the react prompt from langchain hub
# we will use a predefined prompt to create our reactAgent agent
prompt=hub.pull("hwchase17/react")
print(prompt)


# Step3:create the react agent Manually with pulled prompt.
# Agent need three info tool , llm , prompt


agent=create_react_agent(
    llm=llm,  #agent will use this llm for its reasoning capabilities.
    tools=[search_tool,getWeatherData], # agent will use this tool for external use
    prompt=prompt
)


# step4. wrap this agent with AgentExecutor Object
# agent: this is the main guy--break down the problem statement , make the decision when and what to do , which tool to use.
# AgentExecutor: this is the guy who will  listen to agent and execute what agent will say to execute.
agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool,getWeatherData],
    verbose=True
)








# step5:invoking the  executor --> this is a runnable
response=agent_executor({"input":"find the capital of Bihar , then find i's weather?"})
print(response)
print(response["output"])






