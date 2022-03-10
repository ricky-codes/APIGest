from abc import ABC
from abc import abstractmethod
from typing import List

from src.core.interfaces.model_abc import ModelAbstract

class RepositoryAbstract(ABC):
    '''This is an abstract class to define an abstract repository. Any repository must inherit from this class

    Abstract methods:
        insert - inserting an object
        delete - delete an object
        delete_all - delete all object in a repository
        get_all - selects all object from a repository
        get_by_id - selects an object by id
        update - update an object
    '''

    @abstractmethod
    def insert(self, new) -> int:
        raise NotImplementedError

    @abstractmethod
    def delete_by_filter(self, target) -> int:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_by_filter(self) -> List[ModelAbstract]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id) -> ModelAbstract:
        raise NotImplementedError

    @abstractmethod
    def update(self, new) -> bool:
        raise NotImplementedError