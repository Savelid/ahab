from application import app

##### Server stuff #####
if __name__ == '__main__' :
	# 
	app.secret_key = 'super_secret_key'
	# Debug mode let me change code without restarting the server
	# And provides a debuger in the browser
	app.debug = True
	# Run server. if 0.0.0.0 it listens in all public IP addresses
	app.run(host = '0.0.0.0', port = 8000)