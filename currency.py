import requests

def get_spot_rate(from_currency, to_currency):
    url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}'
    response = requests.get(url)
    data = response.json()

    print(data)
    return data['result']

def convert(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return round(converted_amount, 2)


def available_currencies():
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        currencies = data['symbols']
        return currencies
    else:
        print("Error: Unable to fetch currency data")
        return []  #fetch both currencies or crypto with a buttonn that opens up or drops down ot the list of currencies, start with typing ticker, if cant remeber click list button when you can click and have it fiill your box
        
    
def get_historical_rate(base_currency, target_currency, date):
    url = f'https://api.exchangerate.host/timeseries?start_date={date}&end_date={date}&base={base_currency}&symbols={target_currency}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        rates = data['rates']
        if date in rates:
            return rates[date][target_currency]
        else:
            print(f"Exchange rate not available for {date}")
            return None
    else:
        print("Error: Unable to fetch exchange rate data")
        return None
