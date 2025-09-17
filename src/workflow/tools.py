from langchain_core.tools import tool
from datetime import datetime, timedelta
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
    @tool
    def previous_dollar():
        """
        Busca a cotação do dólar em uma data específica através da API do Banco Central do Brasil.
        Retorna os dados da cotação do dólar para a data especificada.
        """
        day_week = datetime.now().strftime('%A')
        day_actual = datetime.now()

        if day_week == "Sunday" or day_week == "Monday":
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
            dollar_quote = Tools.dollar(day_actual)
            return dollar_quote
                
# invoke = Tools().previous_dollar.invoke({})
# print(invoke)