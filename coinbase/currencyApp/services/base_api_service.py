import abc
from abc import abstractmethod
from typing import List

from ..models import Order


class BaseApiService(abc.ABC):
    @abstractmethod
    def get_currencies(self):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def make_order(self, order: Order):
        pass
