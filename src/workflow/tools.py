from langchain_core.tools import tool
from datetime import datetime, timedelta
from dotenv import load_dotenv
import yfinance as yf
import requests
import os

load_dotenv()

class Tools:
    """
    Class of tools.
    """
    @staticmethod
    def dollar(date):
        """
        Get previous day US dollar exchange rate using the Central Bank of Brazil API.
        
        args:
            date: Date in the format 'MM-DD-YYYY'
        """
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

        try:
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
        except Exception as error:
            return {"Error": f"Error when running tool: {error}"} 
         
    @staticmethod
    @tool("search_yahoo_finance")
    def yahoo_finance(companies: list) -> list:
        """
        Tool to fetch stock prices of companies listed on the US stock exchange.

        Args:
            companies: List of company codes (e.g., ["MSFT", "GOOG", "AAPL"]).
        """
        results = []
        try:    
            for company in companies:
                current_price = yf.Ticker(company).info
                results.append(f"{company}: {current_price['currentPrice']}")
            return results
        except Exception as error:
            return [f"Error when running tool: {error}"]
    
    @staticmethod
    @tool("search_trend_topic_previous_day")
    def trend_topic_previous_day() -> dict:
        """
        Tool for search trend topics of previous day
        """
        api_key_news_notice = os.getenv("KEY_NEWS_API")
        
        if not api_key_news_notice:
            return {"Error": "Missing KEY_NEWS_API in environment."}
        
        try:
            previous_day = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news_notice}&from={previous_day}&pageSize=5"
            response = requests.get(url).json()
            return response
        except Exception as error:
            return {"Error": f"Error when running tool: {error}"}
        
#trend_topic_previous_day = Tools.trend_topic_previous_day.invoke({})