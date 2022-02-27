import unittest
from datetime import datetime, timedelta, date
import random
import logging
import logging.config

from src.core.interfaces import repository_abc
from src.core.models.product_periodicity_model import ProductPeriodicityModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_description_model import ProductDescriptionModel

from src.infrastructure.services.repository import SqlAlchemyRepository
from src.infrastructure.services.mapper import Mapper
from src.infrastructure.data.metadata import metadata_obj

from src.shared import parse_config


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        logging.config.dictConfig(parse_config.get_logger_config())
        cls.test_logger = logging.getLogger('test')
        cls.dev_logger = logging.getLogger('dev')

        cls.ENGINE = create_engine(parse_config.get_mysql_connection_uri())
        cls.SESSION = sessionmaker(bind=cls.ENGINE)
        metadata_obj.create_all(cls.ENGINE)
        cls.mapper = Mapper(cls.dev_logger)
        cls.mapper.start_mappers()
        cls.session = cls.SESSION()

        cls.product_periodicity_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductPeriodicityModel, logger=cls.dev_logger)
        cls.product_dimensions_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductDimensionsModel, logger=cls.dev_logger)
        cls.product_description_repository = SqlAlchemyRepository(session=cls.session, object_type=ProductDescriptionModel, logger=cls.dev_logger)

        cls.randomdate_1 = date(2000,3,10) + timedelta(random.randint(1,365))
        cls.randomdate_2 = date(2010,3,1) + timedelta(random.randint(1,365))

        cls.new_product_periodicity = ProductPeriodicityModel(entry_on_warehouse=cls.randomdate_1, expire_date=cls.randomdate_2, created_at=datetime.now())

        cls.new_product_dimensions = ProductDimensionsModel(
            unity_of_measure='unidade',
            unity_per_pack=random.randint(1, 100),
            pack_per_level=random.randint(1, 50),
            level_per_pallet=random.randint(1,8),
            unity_area=random.randint(1,1000),
            created_at=datetime.now()
        )

        cls.new_product_description = ProductDescriptionModel(
            name='Compal Frutos Vermelhos',
            category='Sumos',
            subcategory='Nectares',
            internal_code= random.randint(1,10000),
            ean=random.getrandbits(32),
            created_at=datetime.now(),
            product_dimensions=cls.new_product_dimensions,
            product_periodicity=cls.new_product_periodicity
        )




    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.test_logger.debug("Session closed")


    def test_insert_product_periodicity(self):
        '''Testing function to insert product_periodicity'''

        self.__class__.product_periodicity_repository.insert(self.__class__.new_product_periodicity)
        self.__class__.session.commit()
        self.__class__.test_logger.debug("Commit occured on product_periodicity_repository")
        self.inserted_product_periodicity = self.__class__.session.query(ProductPeriodicityModel).order_by(ProductPeriodicityModel.id.desc()).first()
        self.assertEqual(self.__class__.new_product_periodicity, self.inserted_product_periodicity)

    def test_insert_product_dimensions(self):
        '''Testing function to insert product_dimensions'''

        self.__class__.product_dimensions_repository.insert(self.__class__.new_product_dimensions)
        self.__class__.session.commit()
        self.__class__.test_logger.debug("Commit occured on product_dimensions_repository")
        self.inserted_product_dimensions = self.__class__.session.query(ProductDimensionsModel).order_by(ProductDimensionsModel.id.desc()).first()
        self.assertEqual(self.__class__.new_product_dimensions, self.inserted_product_dimensions)


    def test_insert_product_description(self):
        '''Testing function to insert product_description'''

        self.__class__.product_description_repository.insert(self.__class__.new_product_description)
        self.__class__.session.commit()
        self.__class__.test_logger.debug("Commit occured on product_description_repository")
        self.inserted_new_product_description = self.__class__.session.query(ProductDescriptionModel).order_by(ProductDescriptionModel.id.desc()).first()
        self.assertEqual(self.__class__.new_product_description, self.inserted_new_product_description)

    def test_delete_product_description(self):
        '''Testing function to delete product_description'''

        object_from_database = self.__class__.product_description_repository.get_all()
        self.assertIsNotNone(object_from_database)
        self.assertIsInstance(object_from_database[0], ProductDescriptionModel)
        self.__class__.product_description_repository.delete(object_from_database[0])
        self.__class__.session.commit()

    def test_delete_product_dimensions(self):
        '''Testing function to delete product_description'''

        object_from_database = self.__class__.product_dimensions_repository.get_all()
        self.assertIsNotNone(object_from_database)
        self.assertIsInstance(object_from_database[0], ProductDimensionsModel)
        self.__class__.product_dimensions_repository.delete(object_from_database[0])
        self.__class__.session.commit()

    def test_delete_product_periodicity(self):
        '''Testing function to delete product_description'''

        object_from_database = self.__class__.product_periodicity_repository.get_all()
        self.assertIsNotNone(object_from_database)
        self.assertIsInstance(object_from_database[0], ProductPeriodicityModel)
        self.__class__.product_periodicity_repository.delete(object_from_database[0])
        self.__class__.session.commit()