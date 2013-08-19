#!/usr/bin/env python

# Let's add a style sheet to our web page, to make it a little
# prettier.  To do that, we need to serve files from the file system,
# so we'll create a 'public' directory, and create a style.css file
# in there.

# Note that the bottle reloader function doesn't check our templates
# to see if they've changed, so if we tweak something in the CSS file
# or template, we need to quit our server with Ctrl-C and restart it.

# Bottle uses the static_file function to serve files from the
# file system, so we need to import it.
from bottle import route, run, template, static_file

# <filename:path> grabs the rest of the URL after /public/ for our
# function.
@route('/public/<filename:path>')

# We pass filename into our script, so we know what to serve.
def send_static(filename):

# We use the static_file function to return the file to the user,
# passing it the filename to serve, and the root directory to look in.
# In this case that's the public directory where this script lives.
    return static_file(filename, root='./public')

@route("/")
def multiply():
	greet = "Hello World!"
	return template('3-multiply',greeting=greet)


run(port=8000, debug=True, reloader=True)

# Run with:
#
# python 3.py
#
# Test with:
#
# http://127.0.0.1:8000/ in your browser.
#
# The page should now use san-serif fonts!
