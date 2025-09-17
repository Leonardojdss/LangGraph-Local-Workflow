from langgraph.prebuilt import create_react_agent
from ..infrastructure.connection_ollama import OllamaConnection
from ..workflow.tools import Tools

llm = OllamaConnection().connect()
tool_dolar = Tools.previous_dollar

class Agents:
    """
    Class of agents
    """
    @staticmethod 
    def agent_dollar():
        agent_dollar = create_react_agent(
            model=llm,
            tools=[tool_dolar],
        )
        return agent_dollar
