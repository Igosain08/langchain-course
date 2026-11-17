from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

import os
load_dotenv()



def main():
    agent= create_agent(tools=[TavilygitSearch()], model=ChatOpenAI(model="gpt-4o-mini", temperature=0.7))
    response = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
    print(response)


if __name__ == "__main__":
    main()
