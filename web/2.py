#!/usr/bin/env python

# Now we're going to use a simple template to let us
# make our web application prettier.  To do that, we'll
# import template.
from bottle import route, run, template

@route("/")
def multiply():
# We'll put greeting into its own variable.
	greet = "Hello World!"

# Then we'll return the output of template.  Template takes
# a few options, the first is the name of the template file
# (without the .tpl extension), the rest are names of variables
# to pass into the template.  In this case, we're passing greeting
# into the greeting variable in the template.
	return template('2-multiply',greeting=greet)


run(port=8000, debug=True, reloader=True)

# Run with:
#
# python 2.py
#
# Test with:
#
# http://127.0.0.1:8000/ in your browser.
