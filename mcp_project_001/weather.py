from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import requests

load_dotenv()
mcp = FastMCP('Weather MCP')

@mcp.tool()
async def get_weather(location:str) -> str:
    '''Get the weather of the given location'''
    url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": os.environ['WEATHER_API_KEY'], "q": location}

    response = requests.get(url, params=params)
    data = response.json()

    temp=data["current"]["temp_c"]
    condition=data["current"]["condition"]["text"]
    return f"Temperature:{temp} degree Celcius, Condition:{condition}"


if __name__=='__main__':
    mcp.run(transport="streamable-http")
