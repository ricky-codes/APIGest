from core.interfaces import connector_abc
from core import parse_config

from infrastructure.data.metadata import metadata_obj

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class SqlAlchemyConnector(connector_abc.Connector):

    def start_engine(self) -> Engine:
        self.connection_config = parse_config.get_connection_config()
        self.engine = create_engine(
            f"mysql+mysqlconnector://{self.connection_config['USER']}:{self.connection_config['PASSWORD']}@{self.connection_config['HOST']}/{self.connection_config['DATABASE']}?charset=utf8mb4"
            )
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        return self.engine

    def start_session(self, engine) -> Session:
        self.Session = sessionmaker(bind=engine.connect())
        self.session: Session = self.Session()
        return self.session

    def start_connection(self):
        engine = self.start_engine()
        session = self.start_session(engine)
        metadata_obj.create_all(engine)
        return session

    def stop_connection(self, session: Session):
        session.close()

    def get_connection_status(self):
        return self.engine
