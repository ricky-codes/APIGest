import unittest
from sqlalchemy import inspect

from infrastructure.services.mapper import start_mappers
from src.core.models import product_description_model, product_dimensions_model, product_periodicity_model

class TestCase(unittest.TestCase):

    def test_mapper(self):
        self.assertTrue(start_mappers())