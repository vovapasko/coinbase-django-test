from typing import List

from currencyApp.services.base_api_service import BaseApiService

from currencyApp.models import Order
import requests
from django.conf import settings

from currencyApp.models import Order


# TODO: Make request calls async
# TODO: remove hardcoded urls


class CoingateApiService(BaseApiService):
    headers = {
        'Authorization': f'Token {settings.API_KEY}',
    }

    def get_currencies(self, currencies: List[Order]) -> dict:
        """currencies should be in format
        a1 = {"_from": "BTC", "_to": "EUR"}
        a2 = {"_from": "ETH", "_to": "EUR"}
        values = [a1, a2]
        get_currencies(values)
        """
        prices = {}
        for curr in currencies:
            value = self.__api_get_currency_price(curr.get('_from'), curr.get('_to'))
            prices[curr.get('_to')] = value
        return prices

    def get_all_orders(self):
        per_page = 100
        page = 1
        sort = 'created_at_desc'
        all_orders = self.__api_get_all_orders(per_page, page, sort)
        return all_orders

    def make_order(self, order: Order):
        response = self.__api_make_order(order)
        return response

    def __api_get_currency_price(self, _from, _to) -> float:
        uri = f"{settings.API_ENDPOINT}/v2/rates/merchant/{_from}/{_to}"
        res = requests.get(uri)
        try:
            value = float(res.content)
        except ValueError:
            print(f"Probably problem with the keys {_from} or {_to}")
            value = None
        return value

    def __api_get_all_orders(self, per_page: float, page: float, sort) -> str:
        """Please note that per_page is 100. If you choose more, 100 wil be selected"""
        params = (
            ('per_page', str(per_page)),
            ('page', str(page)),
            ('sort', sort),
        )
        response = requests.get(f"{settings.API_ENDPOINT}/v2/orders", headers=self.headers,
                                params=params).json()
        return response

    def __api_make_order(self, order: Order) -> requests.Response:
        params = (
            ('order_id', order.order_id),
            ('price_amount', order.price_amount),
            ('price_currency', order.price_currency),
            ('receive_currency', order.receive_currency),
            ('receive_amount', order.receive_amount)
        )
        response = requests.post(f"{settings.API_ENDPOINT}/v2/orders", headers=self.headers,
                                 params=params)
        return response
