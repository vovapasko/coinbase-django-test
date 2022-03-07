from typing import List

import aiohttp
from ..services.base_api_service import BaseApiService

import requests
from django.conf import settings

from ..models import Order, CoingateOrder


# TODO: Make request calls async
# TODO: remove hardcoded urls


class CoingateApiService(BaseApiService):
    headers = {
        'Authorization': f'Token {settings.API_KEY}',
    }

    async def get_currencies(self) -> dict:
        return await self.__fetch_currencies(settings.CURRENCIES)

    async def __fetch_currencies(self, currencies: List[CoingateOrder]):
        """currencies should be in format
               a1 = {"_from": "BTC", "_to": "EUR"}
               a2 = {"_from": "ETH", "_to": "EUR"}
               values = [a1, a2]
               get_currencies(values)
               """
        prices = {}
        for curr in currencies:
            # TODO: can be cached
            value = await self.__api_get_currency_price(curr.get('_from'), curr.get('_to'))
            prices[curr.get('_to')] = value
        return prices

    async def get_all_orders(self):
        per_page = 100
        page = 1
        sort = 'created_at_desc'
        all_orders = await self.__api_get_all_orders(per_page, page, sort)
        return all_orders

    async def make_order(self, order: CoingateOrder):
        response = await self.__api_make_order(order)
        return response

    async def __make_async_get_request(self, url: str, headers: dict = None, params: tuple = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                print("Status:", response.status)
                return await response.json()

    async def __make_async_post_request(self, url: str, headers: dict = None, params: tuple = None):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=params) as response:
                print("Status:", response.status)
                return await response.json()

    async def __api_get_currency_price(self, _from, _to) -> float:
        url = f"{settings.COINBASE_API_ENDPOINT}/v2/rates/merchant/{_from}/{_to}"
        try:
            return await self.__make_async_get_request(url)
        except ValueError as error:
            print(f"Probably problem with the keys {_from} or {_to}")
            raise error

    async def __api_get_all_orders(self, per_page: float, page: float, sort) -> str:
        """Please note that per_page is 100. If you choose more, 100 wil be selected"""
        params = (
            ('per_page', str(per_page)),
            ('page', str(page)),
            ('sort', sort),
        )
        response = await self.__make_async_get_request(f"{settings.COINBASE_SANDBOX_API_ENDPOINT}/v2/orders",
                                                       headers=self.headers,
                                                       params=params)
        return response

    async def __api_make_order(self, order: CoingateOrder) -> requests.Response:
        params = (
            ('order_id', order.order_id),
            ('price_amount', order.price_amount),
            ('price_currency', order.price_currency),
            ('receive_currency', order.receive_currency),
            ('receive_amount', order.receive_amount)
        )
        response = await self.__make_async_post_request(f"{settings.COINBASE_SANDBOX_API_ENDPOINT}/v2/orders",
                                                        headers=self.headers,
                                                        params=params)
        return response
