""" This is for testing the API that needs designed first
"""
import sys
import unittest
sys.path.append("./")
import nlclib

# todo, make all url calls to a local server
class TestTopLevelFunctions(unittest.TestCase):
    """ Test all of the functions available at the top level of the api
    """

    def test_launchMain(self):
        """ Basic call to the main entry point to the program
        """
        nlclib.main.main()

    def test_generalUse(self):
        """ TDD example of how to use the API
        """
        view = nlclib.View()
        model = nlclib.Model()
        controller = nlclib.Controller()

        model.setHtml(controller.getHtml("http://google.com"))
        # there should be a lighter weight way to do this
        # maybe just pass the model into the view constructor
        view.update(model)

    def test_UrlWithoutHttp(self):
        """ make call to url without http
        """
        controller = nlclib.Controller()
        controller.getHtml("google.com")
