import pytest
from datetime import datetime, timedelta, date
import random
import logging
import logging.config

from sqlalchemy import inspect

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


    @classmethod
    def teardown_class(cls):
        cls.session.close()
        cls.test_logger.debug("Session closed")

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_insert_product_category(self):
        '''Testing function to insert product_category'''

        self.new_product_category = ProductCategoryModel(
            description="FRUTOS",
            iva=23,
            created_at=datetime.now()
        )

        self.product_category_repository.insert(self.new_product_category)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_category_repository")
        self.inserted_product_category = self.session.query(ProductCategoryModel).order_by(ProductCategoryModel.id.desc()).first()
        assert self.new_product_category == self.inserted_product_category

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_insert_product_subcategory(self):
        '''Testing function to insert product_category'''

        self.product_category: ProductCategoryModel = self.product_category_repository.get_by_filter(ProductCategoryModel.description == 'SUMOS')[0]

        self.child1_product_subcategory = ProductSubcategoryModel(
            description="GRANEL",
            product_category=self.product_category,
            created_at=datetime.now(),
        )
        self.child2_product_subcategory = ProductSubcategoryModel(
            description="CUVETE",
            product_category=self.product_category,
            created_at=datetime.now(),
        )

        self.parent_product_subcategory = ProductSubcategoryModel(
            description="SECOS",
            product_category=self.product_category,
            created_at=datetime.now()
        )


        self.parent_product_subcategory.product_subcategory_parent = [self.child1_product_subcategory, self.child2_product_subcategory]

        self.product_subcategory_repository.insert(self.parent_product_subcategory)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_subcategory_repository")
        self.inserted_product_subcategory = self.session.query(ProductSubcategoryModel).order_by(ProductSubcategoryModel.id.desc()).first()
        assert self.child1_product_subcategory, self.inserted_product_subcategory


    @pytest.mark.skip(reason="Not part of aggregate")
    def test_insert_product_description(self):
        '''Testing function to insert product_description'''

        self.product_subcategory = self.product_subcategory_repository.get_by_filter(ProductSubcategoryModel.description == "NECTARES")[0]

        self.new_product_description = ProductDescriptionModel(
            name='Compal Frutos Vermelhos',
            internal_code=random.randint(1,10000),
            ean=random.getrandbits(32),
            created_at=datetime.now(),
            product_dimensions=self.new_product_dimensions,
            product_periodicity=self.new_product_periodicity,
            product_subcategory=self.product_subcategory
        )

        self.product_description_repository.insert(self.new_product_description)
        self.session.commit()
        self.test_logger.debug("Commit occured on product_description_repository")
        self.inserted_new_product_description = self.session.query(ProductDescriptionModel).order_by(ProductDescriptionModel.id.desc()).first()
        assert self.new_product_description, self.inserted_new_product_description

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_delete_product_description_by_filter(self):
        '''Testing function to delete product_description'''

        result = self.product_description_repository.delete_by_filter(ProductDescriptionModel.id == 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_delete_product_dimensions_by_filter(self):
        '''Testing function to delete product_dimensions'''

        result = self.product_dimensions_repository.delete_by_filter(ProductDimensionsModel.id > 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_delete_product_periodicity_by_filter(self):
        '''Testing function to delete product_periodicity'''

        result = self.product_periodicity_repository.delete_by_filter(ProductPeriodicityModel.id > 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_periodicity_repository")

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_delete_product_category_by_filter(self):
        '''Testing function to delete product_category'''

        result = self.product_category_repository.delete_by_filter(ProductCategoryModel.id == 1)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_category_repository")

    @pytest.mark.skip(reason="Not part of aggregate")
    def test_delete_product_subcategory_by_filter(self):
        '''Testing function to delete product_category'''

        result = self.product_subcategory_repository.delete_by_filter(ProductSubcategoryModel.id == 13)
        assert type(result) is int
        self.session.commit()
        self.test_logger.debug("Commit occured on product_subcategory_repository")