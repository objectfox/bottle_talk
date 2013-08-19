#!/usr/bin/env python

# We can also use gevent to stream content to our users, or output
# it as we generate it or recieve it from a database or other service.

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

# To do that, we're going to turn our echo function into a generator.
# Generators are a really powerful feature of python, that you should
# look up if you have time.  The unique feature about generators is
# that they don't return all at once, they yield one thing, and can
# then be run again, yielding another, until they're done.  This
# function returns one character from the text you give it, sleeps for
# 5/100ths of a second, then prints another.
	for char in request.body.read():
		sleep(0.05)
		yield char

def is_int(a=''):
	"""
	Determines if we have an integer, else false.
	"""
	try:
		int(a)
	except ValueError:
		return False
	return True

run(port=8080, debug=True, server="gevent")

# Run with:
#
# python 9.py
#
# Test with:
#
# curl -N -d "This is some text we will echo." http://127.0.0.1:8080/echo
#
# Note the -N tells curl not to buffer the output, so we see it as it
# comes in.
#
