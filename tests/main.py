import sys
import unittest
from unittest import TestLoader
from lib import CreateSingleDirNoParams, CreateNestedDirNoParams, CreateSingleDirParentsOption
from utils import ModifiedTestResult


def suite() -> None:
    """
    Create a test suite containing the test cases.

    Returns:
        unittest.TestSuite: A test suite containing the specified test cases.
    """
    loader = TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(loader.loadTestsFromTestCase(CreateSingleDirNoParams))
    suite.addTest(loader.loadTestsFromTestCase(CreateNestedDirNoParams))
    suite.addTest(loader.loadTestsFromTestCase(CreateSingleDirParentsOption))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2, descriptions=False, resultclass=ModifiedTestResult)
    runner.run(suite())
