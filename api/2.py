#!/usr/bin/env python

from bottle import route, run

@route("/")
def hello():

# Here's a line we know will fail.

	'foo' * 3.4

	return "Hello client!\n"

# We can add more options to the run function, in this example we're
# adding debug, which prints stack traces in the output when we have
# an error, and the reloader, which reloads the server whenever we
# change this file.

run(port=8080, debug=True, reloader=True)

# Run with:
#
# python 2.py
#
# Test with:
#
# curl http://127.0.0.1:8080/
#