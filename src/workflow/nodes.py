from typing_extensions import TypedDict
from src.workflow.agents import Agents

class State(TypedDict):
    dolar: str
    notices: str
    yahoo_finance: str
    combined_output: str

class Workflow:
    
    @staticmethod
    def dolar(state: State):
        agent_dollar = Agents.agent_dollar()
        result_dollar = agent_dollar.invoke({
            "messages": [("user", "Qual é a ultima cotação do dólar?")]
        })
        
        response_content = result_dollar["messages"][-1].content
        return {"dolar": response_content}
