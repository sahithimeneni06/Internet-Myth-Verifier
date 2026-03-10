from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

load_dotenv()

def create_agent_executor():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )
    search = DuckDuckGoSearchRun()

    @tool
    def search_web(query: str):
        """Search the internet for factual information"""
        return search.run(query)

    tools = [search_web]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a fact-checking AI that verifies internet myths using web search."
    )

    return agent