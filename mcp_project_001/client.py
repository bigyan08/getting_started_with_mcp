from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["math.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools() # get the tools from the client : math and weather
    model = ChatGroq(model='llama-3.3-70b-versatile') 

    agent = create_agent( #creates ReAct agent using model and tools
        model,tools
    )

    # Math tool invoke
    math_response = await agent.ainvoke(
        {'messages':[{'role':'user','content':'What is 5*5?'}]}
    )
    print(f"Math response:{math_response['messages'][-1].content}")

    # Weather tool invoke
    weather_response = await agent.ainvoke(
        {'messages':[{'role':'user','content':'What is weather like in Kathmandu?'}]}
    )
    print(f"Weather response:{weather_response['messages'][-1].content}")


asyncio.run(main())


