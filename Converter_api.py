"""Module that is used to request and interact with the exchange rate api, contains a function with 4 parameters, the from code, to code, amount,
and date"""
import requests

# function to convert currency using the exchangerate api
def api_convert(from_currency, to_currency, from_amount, date):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&places=2&amount={float(from_amount)}"
    if date:
        url += f"&date={date}"
    response = requests.get(url)
    data = response.json()
    return data["result"]





