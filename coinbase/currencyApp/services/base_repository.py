import abc
from abc import abstractmethod


class BaseRepository(abc.ABC):

    @abstractmethod
    def get(self, reference):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass
