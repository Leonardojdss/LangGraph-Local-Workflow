from langchain_core.tools import tool
import requests

@tool
def previous_dollar():
    """
    Busca a cotação do dólar em uma data específica através da API do Banco Central do Brasil.
    Retorna os dados da cotação do dólar para a data especificada.
    """
    response = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='09-12-2025'&$top=100&$format=json")
    data = response.json()
    return print({"Dollar_sale": f"{data['value'][0]['cotacaoVenda']} reais",
            "Dollar_buy": f"{data['value'][0]['cotacaoCompra']} reais",
            "Date": f"{data['value'][0]['dataHoraCotacao']}"})

previous_dollar.invoke({})
