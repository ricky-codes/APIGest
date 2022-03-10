import pytest
from datetime import datetime, timedelta, date
import random
import logging
import logging.config

from src.core.interfaces.session_wrapper_abc import SessionWrapperAbstract
from src.core.interfaces.unit_of_work_abc import UnitOfWorkAbstract
from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel
from src.core.models.product_dimensions_model import ProductDimensionsModel, UnityOfMeasure
from src.core.models.product_periodicity_model import ProductPeriodicityModel

from src.infrastructure.services.session_wrapper import SqlSession
from src.infrastructure.services.repository import SqlAlchemyRepository
from src.infrastructure.services.unit_of_work import SqlAlchemyUnitOfWork

from src.shared import parse_config


class TestUnitOfWork():

    @classmethod
    def setup_class(cls):
        logging.config.dictConfig(parse_config.get_logger_config())
        cls.dev_logger = logging.getLogger('dev')
        cls.test_logger = logging.getLogger('test')

        cls.session_wrapper: SessionWrapperAbstract = SqlSession()
        cls.session_factory = cls.session_wrapper.get_session()



        cls.randomdate_1 = date(2000,3,10) + timedelta(random.randint(1,365))
        cls.randomdate_2 = date(2010,3,1) + timedelta(random.randint(1,365))


        cls.new_product_category = ProductCategoryModel(
            description="SUMOS",
            iva=23,
            created_at=datetime.now()
        )

        cls.new_product_subcategory = ProductSubcategoryModel(
            description="NECTARES",
            product_category=cls.new_product_category,
            created_at=datetime.now()
        )


        cls.new_product_periodicity = ProductPeriodicityModel(
            entry_on_warehouse=cls.randomdate_1, 
            expire_date=cls.randomdate_2, 
            created_at=datetime.now()
        )

        cls.new_product_dimensions = ProductDimensionsModel(
            unity_of_measure=UnityOfMeasure.UNIDADE,
            unity_per_pack=random.randint(1, 100),
            pack_per_level=random.randint(1, 50),
            level_per_pallet=random.randint(1,8),
            unity_area=random.randint(1,1000),
            created_at=datetime.now()
        )

        cls.new_product_description = ProductDescriptionModel(
            name='Compal Frutos Vermelhos',
            product_category=cls.new_product_subcategory.product_category,
            product_subcategory=cls.new_product_subcategory,
            internal_code= random.randint(1,10000),
            ean=random.getrandbits(32),
            created_at=datetime.now(),
            product_dimensions=cls.new_product_dimensions,
            product_periodicity=cls.new_product_periodicity
        )

    def test_unit_of_work_has_repositories(self):
        unit_of_work = SqlAlchemyUnitOfWork(session_factory=self.session_factory)
        with unit_of_work as uow:
            assert hasattr(uow, 'product_description_repository')
            assert hasattr(uow, 'product_dimensions_repository')
            assert hasattr(uow, 'product_periodicity_repository')
            assert hasattr(uow, 'product_category_repository')
            assert hasattr(uow, 'product_subcategory_repository')


    def test_unit_of_work_creates_repositories(self):
        unit_of_work = SqlAlchemyUnitOfWork(session_factory=self.session_factory)
        with unit_of_work as uow:
            assert type(uow.product_description_repository) is SqlAlchemyRepository
            assert type(uow.product_dimensions_repository) is SqlAlchemyRepository
            assert type(uow.product_periodicity_repository) is SqlAlchemyRepository
            assert type(uow.product_category_repository) is SqlAlchemyRepository
            assert type(uow.product_subcategory_repository) is SqlAlchemyRepository


    def test_unit_of_work_can_insert(self):
        unit_of_work = SqlAlchemyUnitOfWork(session_factory=self.session_factory)
        with unit_of_work as uow:
            uow.product_description_repository.insert(self.new_product_description)
            uow.product_dimensions_repository.insert(self.new_product_dimensions)
            uow.product_periodicity_repository.insert(self.new_product_periodicity)
            uow.product_category_repository.insert(self.new_product_category)
            uow.product_subcategory_repository.insert(self.new_product_subcategory)
            assert uow.session._is_clean() == False
            assert uow.commit() == True
            assert uow.session._is_clean() == True

    def test_unit_of_work_can_rollback(self):
        unit_of_work = SqlAlchemyUnitOfWork(session_factory=self.session_factory)
        with unit_of_work as uow:
            uow.product_description_repository.insert(self.new_product_description)
            uow.product_dimensions_repository.insert(self.new_product_dimensions)
            uow.product_periodicity_repository.insert(self.new_product_periodicity)
            uow.product_category_repository.insert(self.new_product_category)
            uow.product_subcategory_repository.insert(self.new_product_subcategory)
            assert uow.session._is_clean() == False
            assert uow.commit() == True
            assert uow.rollback() == True
            assert uow.session._is_clean() == True
