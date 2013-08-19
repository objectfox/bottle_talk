#!/usr/bin/env python

# This is a really simple bottle application.  In fact, it's almost
# as simple a bottle application as you can get.  Bottle is a python
# web microframework, which means it provides the minimum things you
# need to build a web application.  You can read more about bottle at:

# http://www.bottlepy.org/

# You can test this, once you run it with 'python 1.py' with this:
# 
# curl http://127.0.0.1:8080/
#

# First we need to import the route and run functions from the bottle
# package with this.  You can get bottle by running 'easy_install bottle'
# or 'pip install bottle' if you have pip.

from bottle import route, run

# Next we define a python decorator for our first HTTP Route, /.
# All you really need to know about decorators is that they apply to
# the function that immediately follows them, so in this case, requests
# for / will be sent to the next function listed, 'hello'.
@route("/")

# This is the function we're running.
def hello():

# Bottle functions return strings, which get turned into HTTP responses.
# The responses need to be strings.
	return "Hello client!\n"

# Lastly, we run our python bottle server.  In this case we're running
# it on port 8080, so we can get to our application with:
# curl http://127.0.0.1:8080/
run(port=8080)