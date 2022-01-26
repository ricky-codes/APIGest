from flask import session
from core.interfaces import connector_abc
from core import parse_config

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class SqlAlchemyConnector(connector_abc.Connector):

    def start_engine(self) -> Engine:
        self.connection_config = parse_config.get_connection_config()
        self.engine = create_engine(
            f"mysql+mysqlconnector://{self.connection_config['USER']}:{self.connection_config['PASSWORD']}@{self.connection_config['HOST']}?charset=utf8mb4"
            )
        return self.engine

    def start_session(self, engine) -> Session:
        self.Session = sessionmaker(bind=engine.connect())
        self.session: Session = self.Session()
        return session

    def start_connection(self):
        engine = self.start_engine()
        session = self.start_session(engine)
        return session

    def stop_connection(self, session: Session):
        session.close()

    def get_connection_status(self):
        return self.engine
