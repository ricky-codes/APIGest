from sqlalchemy.engine import Connection
from core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from core.interfaces.connection_abc import ConnectionAbstract

from infrastructure.data.metadata import metadata_obj

from sqlalchemy import engine
from sqlalchemy.orm import session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session



class SqlAlchemyUnitOfWork(UnitOfWorkAbstract):

    def __init__(self, connection: ConnectionAbstract) -> None:
        self.connection: ConnectionAbstract = connection

    def enter(self):
        self.connection_for_session: Connection = self.connection.start_connection()
        metadata_obj.create_all(self.connection_for_session.engine)
        self.Session = sessionmaker(bind=self.connection_for_session)
        self.session = self.Session()
        return self.session

    def exit(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()