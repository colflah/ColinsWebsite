#!/usr/bin/env python
import bottle
from bottle import route, run, default_app, static_file
import pymongo
import arrow

#open('/var/www/myapp/write.txt','a').write("app.py runs2").close()

@route('/home')
@route('/')
def home_page():
#	return "Hello"
	return static_file('index.html', root='/var/www/myapp/views')

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root='/var/www/myapp/static')

@route('/mailinglist', method='POST')
def add_email():
	email = bottle.request.forms.get("email")
	connection = pymongo.MongoClient("mongodb://colflah:9A8-EXQ-xzY-FUF@ds123331.mlab.com:23331/colinandcamilleswebsitemailinglist")
	db = connection["colinandcamilleswebsitemailinglist"]
	collection = db['emailslist']
	collection.insert_one({"email":email, "insert_date":arrow.utcnow().to('US/Pacific').format('YYYY-MM-DD HH:mm:ss ZZ')})
	# open('/var/www/myapp/write.txt','a').write("hi").close()
	# return static_file('index.html', root='/var/www/myapp/views')


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
