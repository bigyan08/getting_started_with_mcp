# Debugging and Monitoring with LangSmith

## Setup
- Install the langsmith package and generate an api key from langsmith
- Set the environment variable

## Tracing
- The tracing is done in the monitoring.ipynb notebook in this directory.
- Basically, you can enable tracing by setting the `LANGCHAIN_TRACING` environment variable to `true`.
- Using that, the flow of the data is visually learnt.


## Langsmith Studio
- For this, we have to create a python script (will not work in notebooks because it needs to spin up the python file in the local api server).
- Hence, 'agent.py' is created in this directory.
- Now we have just the raw code, but for the langgraph studio
would require information about 'Exactly which variable is the compiled graph we want to run'. With langgraph.json, we provide exactly that.
- We can find 'agent.py:tool_agent' in langgraph.json, that represents the compiled graph variable tool_agent in agent.py.
- To run, we navigate to this directory and run:
```bash
langgraph dev
```
