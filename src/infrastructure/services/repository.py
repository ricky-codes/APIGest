from datetime import datetime
from src.core.interfaces.model_abc import ModelAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract

from sqlalchemy.orm import Session

class SqlAlchemyRepository(RepositoryAbstract):

    def __init__(self, logger, session, object_type) -> None:
        self.session: Session = session
        self.object_type = object_type
        self.logger = logger

    def get_all(self):
        self.logger.info("SELECT ALL operation request ...")
        return self.session.query(self.object_type).all()

    def get_by_id(self, id):
        self.logger.info("SELECT ALL BY ID operation request ...")
        return self.session.query(self.object_type).get(id)

    def delete(self, target):
        self.logger.info("DELETE operation request ...")
        self.session.delete(target)

    def delete_all(self, object_type):
        self.logger.info("DELETE ALL operation request ...")
        self.session.query(object_type).delete()

    def insert(self, new: ModelAbstract):
        self.logger.info("INSERT operation request ...")
        new.inserted_at=datetime.now()
        self.session.add(new)

    def update(self, new):
        self.logger.info("UPDATE operation request ...")
        return super().update(new)