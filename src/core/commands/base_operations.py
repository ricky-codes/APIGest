from abc import ABCMeta, abstractmethod

class BaseOperations:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self): 
        raise NotImplementedError

    @abstractmethod
    def get(self): 
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError