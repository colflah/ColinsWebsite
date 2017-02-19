#!/usr/bin/env python
import bottle
from bottle import route, run, default_app, static_file

@route('/')
def home_page():
#	return "Hello"
	return static_file('index.html', root='/var/www/myapp/views')

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root='/var/www/myapp/static')

class StripPathMiddleware(object):
    '''
        Get that slash out of the request
        '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(default_app()),
               host='0.0.0.0',
               port=8081)
else:
	app = application = default_app()
