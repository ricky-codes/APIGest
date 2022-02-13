from abc import ABC
from abc import abstractmethod

class ModelAbstract():

    @property
    def id(self):
        raise NotImplementedError