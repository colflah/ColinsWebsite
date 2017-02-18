import bottle

app = bottle.Bottle()

@app.route('/')
def home_page():
#	return "Hello"
	return bottle.static_file('index.html', root='./views')

@app.route('/static/<filepath:path>')
def static(filepath):
	return bottle.static_file(filepath, root='./static')

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
    bottle.debug(True)
    bottle.run(app=StripPathMiddleware(app),
               server='python_server',
               host='0.0.0.0',
               port=8080)

bottle.run(app, host='0.0.0.0', port=8080)
