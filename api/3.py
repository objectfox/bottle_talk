#!/usr/bin/env python

from bottle import route, run

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
	return "Hello client!\n"

# Now let's add a simple route to multiply two numbers together.
# We mark which fields we want to pull out of the path by listing
# :variable_name, like so:
@route("/multiply/:a/:b")

# Then we can define the defaults for those variables in our function,
# if the variables are optional:
def multiply(a=0,b=0):
	"""
	Multiplies two variables together.
	"""

# Since a and b will be strings when we recieve them, we need to
# turn them into integers, multiply them together, and turn the result
# into a string.

	return str(int(a)*int(b))

run(port=8080, debug=True, reloader=True)


# Run with:
#
# python 3.py
#
# Test with:
#
# curl http://127.0.0.1:8080/multiply/5/10
#

