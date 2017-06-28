coverage run tests/mainTest.py
coverage html --omit=/usr/local/lib/python2.7/*
coverage-badge -fo coverage.svg
convert coverage.svg coverage.png
