"""
Run from the repository root:
    uv run examples/snippets/servers/streamable_config.py
"""

import os
from mcp.server.fastmcp import FastMCP
from memory import add_note, search_memory, summarize_recent, list_notes

# Stateful server (maintains session state)
# Does not work in Blaxel's playground
# mcp = FastMCP(
#     "GreetingServer"
#     host=os.getenv('BL_SERVER_HOST', "0.0.0.0"),
#     port=os.getenv('BL_SERVER_PORT', "80")
# )

# Other configuration options:
# Stateless server (no session persistence)
mcp = FastMCP(
    "MemoryServer",
    stateless_http=True,
    host=os.getenv('BL_SERVER_HOST', "0.0.0.0"),
    port=os.getenv('BL_SERVER_PORT', "80")
)



# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


@mcp.tool()
def add_note_tool(text: str):
    return add_note(text)

@mcp.tool()
def search_tool(query: str):
    return search_memory(query)

@mcp.tool()
def summarize_tool():
    return summarize_recent()

@mcp.tool()
def list_note_tool():
    return list_notes()

# Run server with streamable_http transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")