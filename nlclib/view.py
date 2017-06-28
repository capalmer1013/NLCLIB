""" View Module
"""
import copy
class View(object):
    """ View
        This will handle everything that the
        user sees and can interact with
    """
    def __init__(self):
        """ need to figure out what the view will have
        """
        self.model = None

    def update(self, inModel):
        """ given a model object, update the views model
        """
        # shallow copy, may want deep copy
        self.model = copy.copy(inModel)
