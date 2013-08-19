#!/usr/bin/env python

# Now we're going to connect our web application to our API service.
# Make sure the API service is running on 8080, maybe in another terminal
# window, and then start this script.

# We'll need to get acces to the POST variables from our form, so
# let's import request from the bottle package here:
from bottle import route, run, template, static_file, request

# We also need to make requests to the API, so we'll import urllib2,
# a simple library for making HTTP requests.
import urllib2

@route('/public/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./public')

@route("/")

# We can handle both GET and POST requests in the same function by
# listing multiple routes.  Now / supports both POST and GET.
@route("/", method="POST")
def multiply():

# We need to get our 'a' and 'b' fields, so we'll use request.forms.get(),
# since that will work even if they don't exist.  request.forms is a dict
# that stores all the form fields we passed in.
	a = request.forms.get('a')
	b = request.forms.get('b')

# Now, if we have both a and b, let's make a request to the API service.
	if a and b:

# The urllib2.urlopen('url').read() function makes an HTTP request and
# loads the output.
		greet = urllib2.urlopen("http://127.0.0.1:8080/multiply/"
			+ a + "/" + b).read()

# If we don't have a and b, just show a greeting.
	else:
		greet = "Multiply some numbers!"
	return template('4-multiply',greeting=greet)


run(port=8000, debug=True, reloader=True)

# Run with:
#
# python 4.py
#
# Test with:
#
# http://127.0.0.1:8000/ in your browser.
#
# If you're running both servers, you should be able to multiply numbers!
