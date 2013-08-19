#!/usr/bin/env python

# This example adds some time delay to the echo function, simulating
# a real request.  Database requests, requests to other HTTP APIs,
# and may other things can make web apps slow.
from bottle import route, run, request, HTTPResponse, redirect

# For this example, we'll import sleep from the time module.  Sleep
# pauses our application for a certain amount of time.
from time import sleep

@route("/old/")
def new_home():
	redirect("/")

@route("/")
def hello():
	"""
	Simple welcome message.
	"""
# Now we're going to wait 5/10ths of a second, just enough time
# so you'll notice it.
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

run(port=8080, debug=True, reloader=True)

# Run with:
#
# python 7.py
#
# Test with:
#
# This one should take about a half a second:
# ab -n 1 -c 1 http://127.0.0.1:8080/
# 
# But this one, trying to run 5 requests at the same time
# takes 2.5 seconds!
# ab -n 5 -c 5 http://127.0.0.1:8080/
#
