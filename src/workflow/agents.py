from langgraph.prebuilt import create_react_agent
from ..infrastructure.connection_ollama import OllamaConnection

llm = OllamaConnection().connect()

class Agents:
    
    def agent_dolar():
        agent_dolar = create_react_agent(
            model=llm,
            tools
        )

