# Introduction to Bottle

This is a simple introduction to the important features of [bottle](http://www.bottlepy.org), the python web microframework.  It includes walkthroughs of:

* A Basic Bottle 'Hello World' (api/1.py)
* Ports (api/1.py)
* Routes (api/1.py)
* Debug and Reloader Features (api/2.py)
* Extracting Variables from Routes (api/3.py)
* Reading POST data (api/4.py)
* HTTP Errors (api/5.py)
* Redirects (api/6.py)
* Simple Templates (web/2.py)
* Static Files (web/3.py)
* Event Driven Services with gevent (api-gevent/8.py)
* Using Generators for Streaming Applications & Web Sockets (api-gevent/9.py)

This talk was originally given by [Jeff Kramer](http://www.jeffkramer.com/) at [PyTexas 2013](http://www.pytexas.org).

## Dependencies

All you'll need for the web and api sections are bottle, which you can install with `easy_install bottle` or `pip install bottle`.

To try the api-gevent event driven features, you'll need [gevent](http://www.gevent.org/), which has a more complicated installation.

## Best Process

Start with api/1 - api/6, then web/1 - web/5, and then if you have gevent, try api-gevent/7 - api/gevent/9.

## Questions & License

This content is licenced under an MIT license.  If you have questions, hit me up on the contact form on my blog at [Jeff Kramer](http://www.jeffkramer.com/) or on twitter [@jeffk](http://twitter.com/jeffk).

