import bottle

app = bottle.Bottle()

@app.route('/')
def home_page():
#	return "Hello"
	return bottle.static_file('index.html', root='./views')

@app.route('/<filepath:path>')
def server_static(filepath):
	return bottle.static_file(filepath, root='./')

bottle.debug(True)
bottle.run(app, host='0.0.0.0', port=8080)
