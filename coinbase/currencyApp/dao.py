# contains main functions for data crawling
from .request_tools import api_get_currency_price, api_get_all_orders, api_make_order
import json


# TODO: make api calls async

def get_currencies(currencies: list) -> dict:
    """currencies should be in format
    a1 = {"_from": "BTC", "_to": "EUR"}
    a2 = {"_from": "ETH", "_to": "EUR"}
    values = [a1, a2]
    get_currencies(values)
    """
    prices = {}
    for curr in currencies:
        value = api_get_currency_price(curr.get('_from'), curr.get('_to'))
        prices[curr.get('_to')] = value
    return prices


def get_all_orders():
    per_page = 100
    page = 1
    sort = 'created_at_desc'
    all_orders = api_get_all_orders(per_page, page, sort)
    return all_orders


def make_order(order_id, price_amount, price_currency, receive_currency):
    response = api_make_order(order_id, price_amount, price_currency, receive_currency)
    return response
