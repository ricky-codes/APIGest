from sqlalchemy.engine import Connection
from core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from core.interfaces.connection_abc import ConnectionAbstract

from infrastructure.data.metadata import metadata_obj

from sqlalchemy import engine
from sqlalchemy.orm import session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session



class SqlAlchemyUnitOfWork(UnitOfWorkAbstract):

    def __init__(self, logger, connection: ConnectionAbstract) -> None:
        self.connection: ConnectionAbstract = connection
        self.logger = logger

    def enter(self):
        self.connection_for_session: Connection = self.connection.start_connection()
        metadata_obj.create_all(self.connection_for_session.engine)
        self.logger.debug('Created metadata objects')
        self.Session = sessionmaker(bind=self.connection_for_session)
        self.session = self.Session()
        self.logger.info('Session has been started: {}'.format(str(self.connection_for_session.engine)))
        return self.session

    def exit(self):
        self.session.close()
        self.logger.info('Session has been closed')

    def commit(self):
        self.session.commit()
        self.logger.info('Commit occured on the session: {}'.format(str(self.connection_for_session)))

    def rollback(self):
        self.session.rollback()
        self.logger.info('Rollback occured on the session: {}'.format(str(self.connection_for_session)))