import unittest

from tests.integration.repository_operations_test import TestRepository

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRepository('test_insert_product_periodicity'))
    suite.addTest(TestRepository('test_insert_product_dimensions'))
    suite.addTest(TestRepository('test_insert_product_description'))
    suite.addTest(TestRepository('test_delete_product_description'))
    suite.addTest(TestRepository('test_delete_product_dimensions'))
    suite.addTest(TestRepository('test_delete_product_periodicity'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())