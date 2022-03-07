import abc
from abc import abstractmethod
from typing import List

from ..models import Order


class BaseApiService(abc.ABC):
    @abstractmethod
    async def get_supported_currencies(self) -> dict:
        pass

    @abstractmethod
    async def get_exchange_rate(self, _from, _to) -> float:
        pass

    @abstractmethod
    async def get_all_orders(self) -> list:
        pass

    @abstractmethod
    async def make_order(self, order: Order):
        pass
