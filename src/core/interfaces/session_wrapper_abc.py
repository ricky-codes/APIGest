from abc import ABC 
from abc import abstractmethod


class SessionWrapperAbstract(ABC):

    ENGINE = None
    SESSION = None

    @abstractmethod
    def get_session():
        raise NotImplementedError

    @abstractmethod
    def get_engine():
        raise NotImplementedError