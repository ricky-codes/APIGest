from core.interfaces.connection_abc import ConnectionAbstract
from shared import parse_config

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

    def __init__(self, logger, configuration) -> None:
        self.connection_config = configuration
        self.logger = logger

    def start_connection(self):
        self.engine = create_engine(
            f"mysql+mysqlconnector://{self.connection_config['USER']}:{self.connection_config['PASSWORD']}@{self.connection_config['HOST']}/{self.connection_config['DATABASE']}?charset=utf8mb4"
            )
        self.logger.debug('Engine has been created')
        if not database_exists(self.engine.url):
            self.logger.warning("The database {} doesn't exists".format(self.connection_config['DATABASE']))
            create_database(self.engine.url)
            self.logger.info("The database {} has been created".format(self.connection_config['DATABASE']))
        self.connection = self.engine.connect()
        self.logger.info("Connection established")
        #metadata_obj.create_all(engine)
        return self.connection

    def stop_connection(self):
        self.connection.close()
        self.logger.warning('Connection closed')

    def get_connection(self):
        return self.connection
