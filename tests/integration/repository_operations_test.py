import pytest
from datetime import datetime, timedelta, date
import random
import logging
import logging.config

from src.core.interfaces.session_wrapper_abc import SessionWrapperAbstract
from src.core.models.product_periodicity_model import ProductPeriodicityModel
from src.core.models.product_dimensions_model import ProductDimensionsModel, UnityOfMeasure
from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel

from src.infrastructure.services.session_wrapper import SqlSession
from src.infrastructure.services.repository import SqlAlchemyRepository

from src.shared import parse_config


class TestRepositoryOperations():

    @classmethod
    def setup_class(cls):
        logging.config.dictConfig(parse_config.get_logger_config())
        cls.dev_logger = logging.getLogger('dev')
        cls.test_logger = logging.getLogger('test')

        cls.session_wrapper: SessionWrapperAbstract = SqlSession()
        cls.session_factory = cls.session_wrapper.get_session()
        cls.session = cls.session_factory()


        cls.product_periodicity_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductPeriodicityModel)
        cls.product_dimensions_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductDimensionsModel)
        cls.product_description_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductDescriptionModel)
        cls.product_category_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductCategoryModel)
        cls.product_subcategory_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductSubcategoryModel)


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

    @classmethod
    def teardown_class(cls):
        cls.session.close()
        cls.test_logger.debug("Session closed")


    def test_insert_product_category(self):
        '''Testing function to insert product_category'''

        self.product_category_repository.insert(self.new_product_category)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_category_repository")
        self.inserted_product_category = self.session.query(ProductCategoryModel).order_by(ProductCategoryModel.id.desc()).first()
        assert self.new_product_category == self.inserted_product_category


    def test_insert_product_subcategory(self):
        '''Testing function to insert product_category'''

        self.product_subcategory_repository.insert(self.new_product_subcategory)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_subcategory_repository")
        self.inserted_product_subcategory = self.session.query(ProductSubcategoryModel).order_by(ProductSubcategoryModel.id.desc()).first()
        assert self.new_product_subcategory, self.inserted_product_subcategory


    def test_insert_product_periodicity(self):
        '''Testing function to insert product_periodicity'''

        self.product_periodicity_repository.insert(self.new_product_periodicity)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")
        self.inserted_product_periodicity = self.session.query(ProductPeriodicityModel).order_by(ProductPeriodicityModel.id.desc()).first()
        assert self.new_product_periodicity, self.inserted_product_periodicity

    def test_insert_product_dimensions(self):
        '''Testing function to insert product_dimensions'''

        self.product_dimensions_repository.insert(self.new_product_dimensions)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_dimensions_repository")
        self.inserted_product_dimensions = self.session.query(ProductDimensionsModel).order_by(ProductDimensionsModel.id.desc()).first()
        assert self.new_product_dimensions, self.inserted_product_dimensions


    def test_insert_product_description(self):
        '''Testing function to insert product_description'''

        self.product_description_repository.insert(self.new_product_description)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_description_repository")
        self.inserted_new_product_description = self.session.query(ProductDescriptionModel).order_by(ProductDescriptionModel.id.desc()).first()
        assert self.new_product_description, self.inserted_new_product_description





    def test_delete_product_description_by_filter(self):
        '''Testing function to delete product_description'''

        result = self.product_description_repository.delete_by_filter(ProductDescriptionModel.id > 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")

    def test_delete_product_dimensions_by_filter(self):
        '''Testing function to delete product_description'''

        result = self.product_dimensions_repository.delete_by_filter(ProductDimensionsModel.id > 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")

    def test_delete_product_periodicity_by_filter(self):
        '''Testing function to delete product_description'''

        result = self.product_periodicity_repository.delete_by_filter(ProductPeriodicityModel.id > 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")