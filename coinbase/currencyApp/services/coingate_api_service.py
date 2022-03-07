from typing import List, Union

import aiohttp
from ..services.base_api_service import BaseApiService
from typing import Union
import requests
from django.conf import settings

from ..models import Order, CoingateOrder


class CoingateApiService(BaseApiService):
    headers = {
        'Authorization': f'Token {settings.API_KEY}',
    }

    async def get_supported_currencies(self) -> dict:
        url = f"{settings.COINBASE_API_ENDPOINT}/{settings.COINBASE_API_VERSION}/currencies/"
        return await self.__make_async_get_request(url)

    async def get_all_orders(self):
        per_page = settings.ORDERS_PER_PAGE
        page = settings.ORDER_PAGES
        sort = settings.ORDERS_SORT
        all_orders = await self.__api_get_all_orders(per_page, page, sort)
        return all_orders

    async def make_order(self, order: CoingateOrder):
        response = await self.__api_make_order(order)
        return response

    async def get_exchange_rate(self, _from, _to) -> str:
        url = f"{settings.COINBASE_API_ENDPOINT}/{settings.COINBASE_API_VERSION}/rates/merchant/{_from}/{_to}"
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

    async def __api_make_order(self, order: CoingateOrder) -> Union[dict, str]:
        params = (
            ('order_id', order.order_id),
            ('price_amount', order.price_amount),
            ('price_currency', order.price_currency),
            ('receive_currency', order.receive_currency),
            ('receive_amount', order.receive_amount)
        )
        response = await self.__make_async_post_request(
            f"{settings.COINBASE_SANDBOX_API_ENDPOINT}/{settings.COINBASE_API_VERSION}/orders",
            headers=self.headers,
            params=params)
        return response

    async def __make_async_get_request(self, url: str, headers: dict = None, params: tuple = None) -> Union[dict, str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                return await response.json()

    async def __make_async_post_request(self, url: str, headers: dict = None, params: tuple = None) -> Union[dict, str]:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=params) as response:
                return await response.json()
