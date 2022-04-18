from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import logging.config

from src.core.interfaces.session_wrapper_abc import SessionWrapperAbstract

from src.infrastructure.orm.metadata import metadata_obj
from src.infrastructure.services.mapper import Mapper

from src.shared import parse_config

class SqlSession(SessionWrapperAbstract):

    ENGINE = None
    SESSION = None

    def __init__(self):
        logging.config.dictConfig(parse_config.get_logger_config())
        self.dev_logger = logging.getLogger('dev')
        self.ENGINE = create_engine(parse_config.get_mysql_connection_uri())

    def get_engine(self):
        return self.ENGINE

    def get_session(self):
        '''This function returns a session factory ready to be instanciated'''

        self.ENGINE = self.get_engine()
        self.SESSION = sessionmaker(bind=self.ENGINE)
        metadata_obj.create_all(self.ENGINE)
        self.mapper = Mapper()
        self.mapper.start_mappers()
        return self.SESSION