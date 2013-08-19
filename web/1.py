#!/usr/bin/env python

# This is a simple web application.  It looks a lot like our
# first API server.

from bottle import route, run

@route("/")
def multiply():
	return("Hello World!")

run(port=8000, debug=True, reloader=True)

# Run with:
#
# python 1.py
#
# Test with:
#
# http://127.0.0.1:8000/ in your browser.
