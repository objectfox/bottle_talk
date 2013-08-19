#!/usr/bin/env python

# The gevent project has code that allows multiple 'greenlets' or
# really lightweight execution units, to run at the same time.
# For our bottle app, that lets us respond to multiple requests
# at the same time.
#
# To add support for gevent to your program, install it:
#
# http://www.gevent.org/
#
# And add this line to the top of your script:
from gevent import monkey, sleep; monkey.patch_all()

from bottle import route, run, request, HTTPResponse, redirect
from time import sleep

@route("/old/")
def new_home():
	redirect("/")

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
	sleep(0.5)
	return "Hello client!\n"

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

def is_int(a=''):
	"""
	Determines if we have an integer, else false.
	"""
	try:
		int(a)
	except ValueError:
		return False
	return True

# We also need to tell bottle we want to use 'gevent' as our server.
# Note that the reloader doesn't work with the gevent server.
run(port=8080, debug=True, server="gevent")

# Run with:
#
# python 8.py
#
# Test with:
#
# This one should take about a half a second:
# ab -n 1 -c 1 http://127.0.0.1:8080/
# 
# And this one, trying to run 5 requests at the same time
# now takes the same amount of time!
# ab -n 5 -c 5 http://127.0.0.1:8080/
#
