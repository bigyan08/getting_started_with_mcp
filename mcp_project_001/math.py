from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Math MCP')

@mcp.tool()
def add(a:int, b:int) ->int:
    ''' Add two numbers '''
    return a+b

@mcp.tool()
def sub(a:int,b:int) ->int:
    '''Subtract two numbers'''
    return a-b

@mcp.tool()
def mul(a:int,b:int) ->int:
    '''multiply two numbers'''
    return a*b

@mcp.tool()
def div(a:int,b:int) ->int:
    '''divide two numbers'''
    return a/b


if __name__=="__main__":
    mcp.run(transport='stdio')

# There are multiple transport method like :stdio, streamable http.
# stdio is a simple standard input/output method where the console is used to run it (mainly for local use and debugging)
# streamable http is another method, that uses a web interface (dashboard for all the functionalities)