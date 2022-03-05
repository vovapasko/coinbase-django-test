import abc
from abc import abstractmethod
from typing import List
from currencyApp.request_tools import api_get_currency_price, api_get_all_orders, api_make_order

from currencyApp.models import Order


class BaseApiService(abc.ABC):
    @abstractmethod
    def get_all_currencies(self):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def make_order(self, order: Order):
        pass


class CoingateApiService(BaseApiService):

    def get_currencies(self, currencies: List[Order]) -> dict:
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

    def get_all_orders(self):
        per_page = 100
        page = 1
        sort = 'created_at_desc'
        all_orders = api_get_all_orders(per_page, page, sort)
        return all_orders

    def make_order(self, order: Order):
        response = api_make_order(order)
        return response
