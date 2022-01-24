from sqlalchemy.orm import Session
from src.core.connector import start_connection

import unittest

class TestCase(unittest.TestCase):

    def test_connection(self):
        self.assertIsInstance(start_connection(), Session)
