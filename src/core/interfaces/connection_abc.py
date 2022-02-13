from abc import ABC, abstractmethod

class ConnectionAbstract(ABC): 

    @abstractmethod
    def start_connection():
        raise NotImplementedError

    @abstractmethod
    def stop_connection():
        raise NotImplementedError

    @abstractmethod
    def get_connection():
        raise NotImplementedError