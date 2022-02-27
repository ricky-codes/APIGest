from src.core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract

from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel



from src.infrastructure.data.metadata import metadata_obj
from src.infrastructure.services.repository import SqlAlchemyRepository

from src.shared import parse_config

# --------------
from sqlalchemy.orm import sessionmaker


class SqlAlchemyUnitOfWork(UnitOfWorkAbstract):

    def __init__(self, logger, session_factory) -> None:
        self.session_factory = session_factory
        self.logger = logger

        self.logger.info('Unit of Work created')

    def __enter__(self):
        self.session = self.session_factory()

        self.product_periodicity_repository = SqlAlchemyRepository(logger=self.logger, session=self.session, object_type=type(ProductPeriodicityModel))
 
        self.logger.info('Session started')
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()
        self.logger.info('Session closed')

    def commit(self):
        try:
            self.session.commit()
            self.logger.info('Commit occured on the session')
        except Exception as err:
            self.rollback()
            self.logger.exception(' -> Error while commiting on the session')

    def rollback(self):
        try: 
            self.session.rollback()
            self.logger.info('Rollback occured on the session')
        except Exception as err:
            self.logger.exception(' -> Error in rollback on the session')