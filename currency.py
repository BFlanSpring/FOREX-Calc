import requests

def get_spot_rate(from_currency, to_currency):
    url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}'
    response = requests.get(url)
    data = response.json()

    print(data)
    return data['result']

def convert(amount, exchange_rate):
    return amount * exchange_rate

