from abc import ABC, abstractmethod

class Operations(ABC):

    @abstractmethod
    def insert():
        raise NotImplementedError

    @abstractmethod
    def delete():
        raise NotImplementedError

    @abstractmethod
    def get():
        raise NotImplementedError

    @abstractmethod
    def update():
        raise NotImplementedError
