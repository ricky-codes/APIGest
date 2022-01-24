from abc import ABC, abstractmethod

class Connector(ABC): 

    @abstractmethod
    def start_connection():
        raise NotImplementedError

    @abstractmethod
    def stop_connection():
        raise NotImplementedError

    @abstractmethod
    def get_connection_status():
        raise NotImplementedError