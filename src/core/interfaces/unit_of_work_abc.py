from abc import ABC, abstractmethod

class UnitOfWorkAbstract(ABC):

    @abstractmethod
    def enter(self):
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError