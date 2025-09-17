from langgraph.prebuilt import create_react_agent
from ..infrastructure.connection_ollama import OllamaConnection
from ..workflow.tools import Tools

llm = OllamaConnection().connect()
tool_dolar = Tools().previous_dollar()

class Agents:
    """
    Class of agents
    """
    def agent_dolar():
        agent_dolar = create_react_agent(
            model=llm,
            tools=[tool_dolar],
        )
