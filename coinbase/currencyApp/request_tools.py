"""Contains functions which get data from HTTP requests"""
import requests
from .configs import request_url, API_KEY

headers = {
    'Authorization': f'Token {API_KEY}',
}


def api_get_currency_price(_from, _to) -> float:
    uri = f"{request_url}/v2/rates/merchant/{_from}/{_to}"
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
    response = requests.get(f"{request_url}/v2/orders", headers=headers,
                            params=params).json()
    return response
