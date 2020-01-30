"""Contains functions which get data from HTTP requests"""
import requests
from .configs import request_url


def get_currency_price(_from, _to):
    uri = f"{request_url}/v2/rates/merchant/{_from}/{_to}"
    res = requests.get(uri)
    try:
        value = float(res.content)
    except ValueError:
        print(f"Probably problem with the keys {_from} or {_to}")
        value = None
    return value

