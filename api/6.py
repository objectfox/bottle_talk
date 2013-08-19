#!/usr/bin/env python


# For this example, we want to send people from one path to
# another.  We do that using redirect, so we need to import
# redirect from the bottle package.
from bottle import route, run, request, HTTPResponse, redirect

# This new route catches requests for /old/ and redirects them to /.
@route("/old/")
def new_home():
	redirect("/")

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
	return "Hello client!\n"

def is_int(a=''):
	"""
	Determines if we have an integer, else false.
	"""
	try:
		int(a)
	except ValueError:
		return False
	return True

@route("/multiply/:a/:b")
def multiply(a=0,b=0):
	"""
	Multiplies two variables together.
	"""
	if not is_int(a) or not is_int(b):
		raise HTTPResponse(output='We only support integers.',
				 status=400, header=None)
	return str(int(a)*int(b))

@route("/echo", method='POST')
@route("/echo/", method='POST')
def echo():
	"""
	Prints out what we post to it.
	"""
	return request.body.read() + "\n"

run(port=8080, debug=True, reloader=True)

# Run with:
#
# python 6.py
#
# Test with:
#
# curl -I http://127.0.0.1:8080/old/
#
