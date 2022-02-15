from core.interfaces.repository_abc import RepositoryAbstract
from core.interfaces.model_abc import ModelAbstract
from core.interfaces.unit_of_work_abc import UnitOfWorkAbstract

from sqlalchemy.orm import Session

class SQLAlchemyRepository(RepositoryAbstract):

    def __init__(self, logger, unit_of_work: UnitOfWorkAbstract) -> None:
        self.unitofwork = unit_of_work
        self.logger = logger
        self.session = self.unitofwork.enter()

    def insert(self, new_object: ModelAbstract):
        self.session.add(new_object)
        self.logger.info("Object {} added to Repository".format(type(new_object)))
        self.unitofwork.commit()

    def delete(self, target_object):
        self.session.delete(target_object)
        self.logger.info("Object {} deleted from Repository".format(type(target_object)))
        self.session.commit()

    def update(self):
        pass

    def get_all(self, object_type):
        return self.session.query(object_type).all()

    def get_by_id(self, object_type, id):
        return self.session.query(object_type).get(id)