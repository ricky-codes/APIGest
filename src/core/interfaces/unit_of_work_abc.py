from abc import ABC, abstractmethod

from src.core.interfaces.repository_abc import RepositoryAbstract


class UnitOfWorkAbstract(ABC):

    engine = None

    product_periodicity_repository: RepositoryAbstract
    product_dimensions_repository: RepositoryAbstract
    product_description_repository: RepositoryAbstract

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError