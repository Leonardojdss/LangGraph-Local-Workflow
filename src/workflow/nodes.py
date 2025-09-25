from typing_extensions import TypedDict
from src.workflow.agents import Agents

class State(TypedDict):
    dolar: str
    notices: str
    yahoo_finance: str
    combined_output: str

class Nodes:
    
    @staticmethod
    def dolar(state: State):
        agent_dollar = Agents.agent_dollar()
        result_dollar = agent_dollar.invoke({
            "messages": [("user", "Qual é a ultima cotação do dólar?")]
        })
        
        response_content = result_dollar["messages"][-1].content
        return {"dolar": response_content}
    
    @staticmethod
    def yahoo_finance(state: State):
        agent_yahoo = Agents.agent_yahoo_finance()
        result_yahoo = agent_yahoo.invoke({
            "messages": [("user", "Quais são os preços atuais das ações das empresas MSFT, GOOG e AAPL?")]
        })
        
        response_content = result_yahoo["messages"][-1].content
        return {"yahoo_finance": response_content}
    
    @staticmethod
    def notices(state: State):
        agent_notices = Agents.agent_trend_topic_previous_day()
        result_notices = agent_notices.invoke({
            "messages": [("user", "Quais são as principais notícias de hoje?")]
        })
        
        response_content = result_notices["messages"][-1].content
        return {"notices": response_content}

    @staticmethod
    def aggregator(state: State):
        """Combine the dollar, Yahoo Finance, and notices into a single output"""

        combined = f"Dólar: {state['dolar']}\
                    Ações: {state['yahoo_finance']}\
                    Notícias: {state['notices']}"
        return {"combined_output": combined}

# print(Nodes.dolar({"dolar":"","notices":"","yahoo_finance":"","combined_output":""}))
# print(Nodes.yahoo_finance({"dolar":"","notices":"","yahoo_finance":"","combined_output":""}))
# print(Nodes.notices({"dolar":"","notices":"","yahoo_finance":"","combined_output":""}))