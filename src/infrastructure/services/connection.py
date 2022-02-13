from core.interfaces.connection_abc import ConnectionAbstract
from core import parse_config

from infrastructure.data.metadata import metadata_obj

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine

from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import engine


class SqlAlchemyConnection(ConnectionAbstract):

    connection: engine.Connection = None

    #TODO invert dependency of parse_config()

    def start_connection(self):
        self.connection_config = parse_config.get_connection_config()
        self.engine = create_engine(
            f"mysql+mysqlconnector://{self.connection_config['USER']}:{self.connection_config['PASSWORD']}@{self.connection_config['HOST']}/{self.connection_config['DATABASE']}?charset=utf8mb4"
            )
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.connection = self.engine.connect()
        #metadata_obj.create_all(engine)
        return self.connection

    def stop_connection(self):
        self.connection.close()

    def get_connection(self):
        return self.connection
