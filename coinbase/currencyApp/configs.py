"""This file stores important data such as API key, currencies which should be requested and so on..."""
API_KEY = "_6ZFr1vZWkuW6HHoHe-Hap6QnnKxo8-u7YV3T3J7"
request_url = "https://api.coingate.com"
# you can add extra currencies here. Be careful about codes
CURRENCIES = [
    {"_from": "BTC", "_to": "EUR"},
    {"_from": "BTC", "_to": "USD"},
    {"_from": "BTC", "_to": "GBP"},
]