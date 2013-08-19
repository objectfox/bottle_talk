#!/usr/bin/env python

# For this example we'll return an error if the user gives us
# bad data, so we'll need to import HTTPResponse from the bottle
# package.
from bottle import route, run, request, HTTPResponse

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
	return "Hello client!\n"

# Let's define a function that checks to see if a variable is a valid
# integer or not.  We'll do that by running a try/except, and checking
# for ValueError.  If you don't understand this, don't worry.
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

# Now we'll alter our application to check and see if a and b are
# both valid integers.  If they aren't, we'll run some other code.
	if not is_int(a) or not is_int(b):

# If a or b aren't integers, let's raise an HTTP 400 error.  400 means
# the request was bad, and the client shouldn't try it again.  We add
# some text to output to tell the user what went wrong.
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
# python 5.py
#
# Test with:
#
# curl http://127.0.0.1:8080/multiply/foo/2
# curl -I http://127.0.0.1:8080/multiply/foo/2
#
