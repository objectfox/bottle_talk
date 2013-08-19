#!/usr/bin/env python

# For this example we'll need to import 'request' from the bottle
# package as well.  Request holds all kinds of information about
# the HTTP request we recieved.
from bottle import route, run, request

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
	return "Hello client!\n"

@route("/multiply/:a/:b")
def multiply(a=0,b=0):
	"""
	Multiplies two variables together.
	"""
	return str(int(a)*int(b))

# Routes by default support HTTP GETs, but we can handle other
# HTTP verb types, like POST, DEL or PUT by defining the method:
@route("/echo", method='POST')
@route("/echo/", method='POST')
def echo():
	"""
	Prints out what we post to it.
	"""

# request.body.read() gives us the raw data posted to our web
# application, which in this example we just return to the user.
# You could use this feature to read in JSON or other data sent
# by the user.
	return request.body.read() + "\n"

run(port=8080, debug=True, reloader=True)

# Run with:
#
# python 4.py
#
# Test with:
#
# curl --data "Hello lovely people." http://127.0.0.1:8080/echo
#
