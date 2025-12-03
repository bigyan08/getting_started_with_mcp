#For langgraph studio we would require a dependency : langgraph-cli[inmem]

#LangGraph Studio operates as a server, not a notebook kernel.
#When you run LangGraph Studio, it doesn't just "read" your code,it actually imports it to spin up a local API server. 
#Because of how Python works, servers can import .py modules easily, but they cannot natively "import" a Jupyter Notebook (.ipynb).

from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
load_dotenv()

os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.environ['LANGSMITH_TRACING']="true"
os.environ['LANGSMITH_PROJECT']= 'first-project'

llm = init_chat_model("groq:llama-3.3-70b-versatile")

class State(TypedDict):
    messages: Annotated[list,add_messages]

def make_tool_graph():
    def add(a:int,b:int):
        '''Add two numbers'''
        return a+b
    
    search_tool = TavilySearch(max_results=2)

    tool_node = ToolNode([search_tool,add])
    llm_with_tools = llm.bind_tools([search_tool,add])

    def should_continue(state:State):
        last_message = state["messages"][-1]
        if last_message.tool_calls:
            return "tools"
        return END

    def agent_node(state:State):
        messages = state["messages"]
        response = llm_with_tools.invoke(messages)
        return {"messages":response}

    builder = StateGraph(State)
    builder.add_node("agent",agent_node)
    builder.add_node("tools",tool_node)
    builder.add_edge(START,"agent")
    builder.add_conditional_edges(
        "agent",
        should_continue,
        ["tools",END]
    )
    graph = builder.compile()

    return graph

tool_agent = make_tool_graph()