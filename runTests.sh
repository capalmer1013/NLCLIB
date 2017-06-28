coverage run --omit=/usr/local/lib/python2.7/* --include=./nlclib/*,./tests/* tests/main.py 
coverage html 
coverage-badge -fo coverage.svg
convert coverage.svg coverage.png
