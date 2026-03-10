from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import Tool

def get_search_tool():
    search = DuckDuckGoSearchRun()

    search_tool = Tool(
        name = 'search_web',
        func = search.run,
        description = 'Search the internet for factual information'
    )
    return search_tool