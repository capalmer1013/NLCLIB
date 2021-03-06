""" Model Module
"""
from bs4 import BeautifulSoup

defaultParser = BeautifulSoup
class Model(object):
    """ model
        This will store the state of the
        web browser
    """
    def __init__(self, parser=defaultParser):
        """ need to figure out what the model will have
        """
        self.parser = parser
        self.html = ""
        self.tree = None

    def setHtml(self, inHtml):
        """ setting internal state using raw html
        """
        self.html = inHtml
        self.tree = self.parser(inHtml, "html5lib")
        # remove the script and style tags
        _ = [x.extract() for x in self.tree('style')]
        _ = [x.extract() for x in self.tree('script')]
