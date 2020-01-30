# contains main functions for data crawling
from .request_tools import get_currency_price


def get_currencies(currencies: list) -> dict:
    """currencies should be in format
    a1 = {"_from": "BTC", "_to": "EUR"}
    a2 = {"_from": "ETH", "_to": "EUR"}
    values = [a1, a2]
    get_currencies(values)
    """
    prices = {}
    for curr in currencies:
        value = get_currency_price(curr.get('_from'), curr.get('_to'))
        prices[curr.get('_to')] = value
    return prices
