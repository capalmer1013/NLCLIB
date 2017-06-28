""" Controller Module
"""
import requests

defaultGet = requests.get
class Controller(object):
    """ Controller
        This will handle all of the interactions
        between the view and the model
    """
    def __init__(self, httpGet=defaultGet):
        """ dependency injection for other functions
            to get from urls
        """
        self.httpGet = httpGet

    def getHtml(self, url):
        """ given a url return the html
        """
        if "://" not in url:
            url = "https://"+url

        return self.httpGet(url).text
