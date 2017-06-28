""" main test runner
"""
import glob
import subprocess

for i in glob.glob("tests/test_*.py"):
    subprocess.call(['python', i])
