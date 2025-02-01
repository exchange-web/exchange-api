import requests
from exchange_django.settings import XE_ACCOUNT_ID, XE_API_KEY

def get_exchange_rate(base_currency):
    url = f"https://xecdapi.xe.com/v1/convert_from?from={base_currency}&to=USD"

    response = requests.get(url, auth=(XE_ACCOUNT_ID, XE_API_KEY))
    if response.status_code == 200:
        data = response.json()
        try:
            exchange_rate = data['to'][0]['mid']
        except IndexError:
            print("Failed to fetch exchange rate")
            return None
        return exchange_rate
    else:
        print("Failed to fetch exchange rate", response.reason)
        return None

