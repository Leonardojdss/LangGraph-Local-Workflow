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
        # Passar o input como um dicionário com 'messages'
        result_dollar = agent_dollar.invoke({
            "messages": [("user", "Qual é a ultima cotação do dólar?")]
        })
        
        # Extrair a resposta do agente corretamente
        response_content = result_dollar["messages"][-1].content
        return {"dolar": response_content}

print(Workflow.dolar({"dolar":"","notices":"","yahoo_finance":"","combined_output":""}))
