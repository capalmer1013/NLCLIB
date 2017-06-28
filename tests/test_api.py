""" This is for testing the API that needs designed first
"""
import sys
import unittest
sys.path.append("./")
import nlclib

class TestTopLevelFunctions(unittest.TestCase):
    """ Test all of the functions available at the top level of the api
    """

    def test_launchMain(self):
        """ Basic call to the main entry point to the program
        """
        nlclib.main.main()
