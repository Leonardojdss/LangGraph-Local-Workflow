from langchain_core.tools import tool
from datetime import datetime, timedelta
import yfinance as yf
import requests

class Tools:
    """
    Classe de ferramentas para consulta de dados financeiros.
    """
    @staticmethod
    def dollar(date):
        response = requests.get(f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{date}'&$top=100&$format=json")
        data = response.json()
        return {"Dollar_sale": f"{data['value'][0]['cotacaoVenda']} reais",
                "Dollar_buy": f"{data['value'][0]['cotacaoCompra']} reais",
                "Date": f"{data['value'][0]['dataHoraCotacao']}"}
            
    @staticmethod
    @tool("previous_dollar")
    def previous_dollar():
        """
        Fetches the previous day's US dollar exchange rate using the Central Bank of Brazil API.
        Returns the exchange rate data for the specified date.
        """
        day_week = datetime.now().strftime('%A')
        day_actual = datetime.now()

        if day_week == "Sunday":
            day_adjusted = day_actual - timedelta(days=2)
            day_adjusted = day_adjusted.strftime('%m-%d-%Y')
            dollar_quote = Tools.dollar(day_adjusted)
            return dollar_quote
        elif day_week == "Monday":
            day_adjusted = day_actual - timedelta(days=3)
            day_adjusted = day_adjusted.strftime('%m-%d-%Y')
            dollar_quote = Tools.dollar(day_adjusted)
            return dollar_quote
        else:
            day_adjusted = day_actual - timedelta(days=1)
            day_adjusted = day_adjusted.strftime('%m-%d-%Y')
            dollar_quote = Tools.dollar(day_adjusted)
            return dollar_quote
         
    @staticmethod
    @tool("search_yahoo_finance")
    def yahoo_finance(companies: list) -> list:
        """
        Tool to fetch stock prices of companies listed on the US stock exchange.

        Args:
            companies: List of company codes (e.g., ["MSFT", "GOOG", "AAPL"]).
        """
        results = []
        for company in companies:
            current_price = yf.Ticker(company).info
            results.append(f"{company}: {current_price['currentPrice']}")
        print(results)
        return results
    
# invoke = Tools().yahoo_finance.invoke({"companies": ["MSFT", "GOOG", "AAPL"]})