from langgraph.prebuilt import create_react_agent
from ..infrastructure.connection_ollama import OllamaConnection
from ..workflow.tools import Tools

llm = OllamaConnection().connect()
tools = Tools

class Agents:
    """
    Class of agents
    """
    @staticmethod 
    def agent_dollar():
        agent_dollar = create_react_agent(
            prompt="Você é um assistente que sempre responde a última cotação do dolar usando a ferramenta disponível.",
            model=llm,
            tools=[tools.previous_dollar],
        )
        return agent_dollar
    
    @staticmethod
    def agent_yahoo_finance():
        agent_yahoo_finance = create_react_agent(
            prompt="Você é um assistente que sempre responde o valor de ações das empresas enviadas pelo usuário",
            model=llm,
            tools=[tools.yahoo_finance],
        )
        return agent_yahoo_finance