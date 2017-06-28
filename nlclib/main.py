""" main might not be the
    appropriate name for this
"""

splash = r"""
   _  __ __   _____ __    ____ ___ 
  / |/ // /  / ___// /   /  _// _ )
 /    // /__/ /__ / /__ _/ / / _  |
/_/|_//____/\___//____//___//____/ 
"""

def writeToScreen(input):
    """ A wrapper for writing to the screen
    """
    print input

def splashScreen():
    """ display the opening splashscreen
    """
    writeToScreen(splash)


def main():
    """ entry point for the app
    """
    splashScreen()
