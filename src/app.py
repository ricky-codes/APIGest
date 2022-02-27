from datetime import date
import logging
import logging.config
from logging import Logger
from sqlalchemy import create_engine

from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

# imports from shared
from shared import parse_config

# imports from core

from src.core.interfaces.model_abc import ModelAbstract
from src.core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract


# imports from infrastructure
from src.infrastructure.services.unit_of_work import SqlAlchemyUnitOfWork
from src.infrastructure.services.mapper import Mapper

from src.infrastructure.data.metadata import metadata_obj


def main(current_unitofwork):
    '''
        This function is responsible to initialize everything at startup that needs to be initialized

        Parameters:
            connector (Connector): Connector instance that will be used
        Returns:
            None
    '''
    unitofwork: UnitOfWorkAbstract = current_unitofwork


if __name__ == '__main__':
    logging.config.dictConfig(parse_config.get_logger_config())
    logger = logging.getLogger('dev')
    logger.info('▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁')

    ENGINE = create_engine(parse_config.get_mysql_connection_uri())
    SESSION = sessionmaker(bind= ENGINE)

    metadata_obj.create_all(ENGINE)


    # Instanciate the mappers and pass the Connector used to the main function
    mapper = Mapper(logger)
    mapper.start_mappers()

    current_unit_of_work = SqlAlchemyUnitOfWork(logger, session_factory=SESSION)
    main(current_unit_of_work)
