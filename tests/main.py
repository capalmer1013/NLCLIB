""" main test runner
    whenever new testcase files are added,
    they need to be imported here.
    Also, I can't figure out a better way to
    do this than with a wildcard import
"""
import unittest
from test_api import *

if __name__ == "__main__":
    unittest.main()
