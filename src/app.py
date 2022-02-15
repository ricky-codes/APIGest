from datetime import date
from distutils.debug import DEBUG
import logging
import logging.config
from logging import Logger

from sqlalchemy.orm import mapper
from infrastructure.repositories.repository import SQLAlchemyRepository

# imports from shared
from shared import parse_config

# imports from core
from core.models.product_dimensions_model import ProductDimensionsModel
from core.models.product_periodicity_model import ProductPeriodicityModel
from core.models.product_description_model import ProductDescriptionModel

from core.interfaces.connection_abc import ConnectionAbstract
from core.interfaces.model_abc import ModelAbstract
from core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from core.interfaces.repository_abc import RepositoryAbstract


# imports from infrastructure
from infrastructure.services.connection import SqlAlchemyConnection
from infrastructure.services.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.services.mapper import Mapper

from infrastructure.repositories.repository import SQLAlchemyRepository

from infrastructure.data.product_periodicity_entity import product_periodicity_table
from infrastructure.data.product_dimensions_entity import product_dimensions_table


def main(current_logger, connector, unitofwork, repository):
    '''
        This function is responsible to initialize everything at startup that needs to be initialized

        Parameters:
            connector (Connector): Connector instance that will be used
        Returns:
            None
    '''
    connector_base: ConnectionAbstract = connector
    unitofwork_base: UnitOfWorkAbstract = unitofwork
    repository_base: RepositoryAbstract = repository
    logger: Logger = current_logger

    new_product_periodicity = ProductPeriodicityModel(entry_on_warehouse=date(day=12,month=11,year=2022), expire_date=date(day=23,month=10,year=1999))
    new_product_dimensions = ProductDimensionsModel(
        unity_of_measure='unidade',
        unity_per_pack=12,
        pack_per_level=54,
        level_per_pallet=5,
        unity_area=76
    )

    new_product_description = ProductDescriptionModel(
        name='Compal Frutos Vermelhos',
        category='Sumos',
        subcategory='Nectares',
        internal_code='12345',
        ean='53245676543245',
        product_dimensions=new_product_dimensions,
        product_periodicity=new_product_periodicity
    )

    base_product: ModelAbstract = new_product_description


if __name__ == '__main__':
    logging.config.dictConfig(parse_config.get_logger_config())
    logger = logging.getLogger('dev')
    logger.info('▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁')
    # Instanciate the mappers and pass the Connector used to the main function
    logger.debug("Starting mappers")
    mapper = Mapper(logger)
    mapper.start_mappers()
    connection_config = parse_config.get_connection_config()
    current_connection = SqlAlchemyConnection(logger, connection_config)
    current_unit_of_work = SqlAlchemyUnitOfWork(logger, current_connection)
    current_repository = SQLAlchemyRepository(logger, current_unit_of_work)
    main(logger, current_connection, current_unit_of_work, current_repository)
