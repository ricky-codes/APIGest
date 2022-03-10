import logging
import logging.config
import pytest
import datetime

from src.core.interfaces.model_abc import ModelAbstract
from src.core.interfaces.session_wrapper_abc import SessionWrapperAbstract

from src.infrastructure.services.session_wrapper import SessionWrapper
from src.infrastructure.services.repository import SqlAlchemyRepository

from src.shared import parse_config

class TestRepository():

    @classmethod
    def setup_class(cls):

        logging.config.dictConfig(parse_config.get_logger_config())
        cls.dev_logger = logging.getLogger('dev')
        cls.test_logger = logging.getLogger('test')

        logging.config.dictConfig(parse_config.get_logger_config())
        cls.dev_logger = logging.getLogger('dev')
        cls.test_logger = logging.getLogger('test')

        cls.session_wrapper: SessionWrapperAbstract = SessionWrapper()
        cls.session = cls.session_wrapper.get_session()

        cls.abstract_model = ModelAbstract(created_at=datetime.datetime.now())


        cls.abstract_repository = SqlAlchemyRepository(session=cls.session, object_type=ModelAbstract, logger=cls.dev_logger)

    @classmethod
    def teardown(cls):
        pass
