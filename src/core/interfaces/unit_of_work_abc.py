from abc import ABC, abstractmethod
from typing import List

from src.core.interfaces.repository_abc import RepositoryAbstract


class UnitOfWorkAbstract(ABC):
    '''This abstract class is a definition for implementing the unit of work pattern. This particular definition supports context manager implementation

    ---------
    Attributes:
        engine
             the engine that will be used to connect to the database
    ---------
    Methods:
        __enter__
            important method when using the 'with' keyword (context manager)
        __exit__
            important method when using the 'with' keyword (context manager). In this case, it always performs a rollback
    ---------
    Abstract methods:
        commit
            This method is the definition for commiting work in the current repository
        rollback
            This method is the definition for rolling back work in the current repository
    '''


    engine = None

    product_description_repository: RepositoryAbstract
    product_dimensions_repository: RepositoryAbstract
    product_periodicity_repository: RepositoryAbstract
    product_category_repository: RepositoryAbstract
    product_subcategory_repository: RepositoryAbstract

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> bool:
        raise NotImplementedError