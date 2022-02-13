from abc import ABC
from abc import abstractmethod

class RepositoryAbstract(ABC):

    @abstractmethod
    @property
    def session(self):
        pass


    @abstractmethod
    def insert(self, new):
        raise NotImplementedError

    @abstractmethod
    def delete(self, target):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, new):
        raise NotImplementedError