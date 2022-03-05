"""Contains functions which get data from HTTP requests"""
import requests
from django.conf import settings

headers = {
    'Authorization': f'Token {settings.API_KEY}',
}


# TODO: Make request calls async
# TODO: remove hardcoded urls

def api_get_currency_price(_from, _to) -> float:
    uri = f"{settings.API_ENDPOINT}/v2/rates/merchant/{_from}/{_to}"
    res = requests.get(uri)
    try:
        value = float(res.content)
    except ValueError:
        print(f"Probably problem with the keys {_from} or {_to}")
        value = None
    return value


def api_get_all_orders(per_page: float, page: float, sort) -> str:
    """Please note that per_page is 100. If you choose more, 100 wil be selected"""
    params = (
        ('per_page', str(per_page)),
        ('page', str(page)),
        ('sort', sort),
    )
    response = requests.get(f"{settings.API_ENDPOINT}/v2/orders", headers=headers,
                            params=params).json()
    return response


def api_make_order(order_id, price_amount, price_currency,
                   receive_currency, receive_amount=0):
    params = (
        ('order_id', order_id),
        ('price_amount', price_amount),
        ('price_currency', price_currency),
        ('receive_currency', receive_currency),
        ('receive_amount', receive_amount)
    )
    response = requests.post(f"{settings.API_ENDPOINT}/v2/orders", headers=headers,
                             params=params)
    return response
