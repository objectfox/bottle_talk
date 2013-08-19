#!/usr/bin/env python

# Unfortunately, if we multiply 'foo' by '4', we're going to get an
# error.  Let's wrap our urllib2 request in a try/except block, to
# save ourselves from bad typos.

from bottle import route, run, template, static_file, request
import urllib2

@route('/public/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./public')

@route("/")
@route("/", method="POST")
def multiply():
	a = request.forms.get('a')
	b = request.forms.get('b')
	if a and b:

# Now we're going to try the url request, but if we get something bad,
# we'll show the user the error.
		try:
			greet = urllib2.urlopen("http://127.0.0.1:8080/multiply/"
				+ a + "/" + b).read()

# Except catches the urllib2.HTTPError, which we get when our API service
# returns the 400.  e is our error, and e.read() gives us the text of the
# error message.
		except urllib2.HTTPError as e:
			greet = "Error from multiply service: " + str(e.read())
	else:
		greet = "Multiply some numbers!"
	return template('5-multiply',greeting=greet)

run(port=8000, debug=True, reloader=True)

# Run with:
#
# python 5.py
#
# Test with:
#
# http://127.0.0.1:8000/ in your browser.
#
# Now the script should handle errors better.
