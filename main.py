from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

import os
load_dotenv()

class Source (BaseModel):
    """Schema for a source used by agent"""
    url: str = Field(description = "The URL of the source")
class AgentResponse (BaseModel):
    """ Schema for agent response"""
    answer: str = Field(description= "The agents answer to the query")
    sources: list[Source]= Field(default_factory=list,description="The list of sources used to generate the answer")
    

    
    



def main():
    agent= create_agent(tools=[TavilySearch()], model=ChatOpenAI(model="gpt-4o-mini", temperature=0.7), response_format=AgentResponse)
    response = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
    print(response)


if __name__ == "__main__":
    main()
