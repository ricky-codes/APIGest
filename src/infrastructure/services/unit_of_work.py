from typing import List
from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel
from src.core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from src.core.interfaces.repository_abc import RepositoryAbstract
from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel

from src.infrastructure.data.metadata import metadata_obj
from src.infrastructure.services.repository import SqlAlchemyRepository

from src.shared import parse_config

from sqlalchemy.orm import sessionmaker


class SqlAlchemyUnitOfWork(UnitOfWorkAbstract):


    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.product_description_repository = SqlAlchemyRepository(object_type=ProductDescriptionModel, session=self.session)
        self.product_dimensions_repository = SqlAlchemyRepository(object_type=ProductDimensionsModel, session=self.session)
        self.product_periodicity_repository = SqlAlchemyRepository(object_type=ProductPeriodicityModel, session=self.session)
        self.product_category_repository = SqlAlchemyRepository(object_type=ProductCategoryModel, session=self.session)
        self.product_subcategory_repository = SqlAlchemyRepository(object_type=ProductSubcategoryModel, session=self.session)

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self) -> bool:
        try:
            self.session.commit()
            return True
        except Exception as err:
            self.rollback()
            return False

    def rollback(self) -> bool:
        try: 
            self.session.rollback()
            return True
        except Exception as err:
            return False