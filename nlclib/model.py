""" Model Module
"""
class Model(object):
    """ model
        This will store the state of the
        web browser
    """
    def __init__(self):
        """ need to figure out what the model will have
        """
        self.html = ""

    def setHtml(self, inHtml):
        """ setting internal state using raw html
        """
        self.html = inHtml
