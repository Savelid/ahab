from flask import Flask , render_template , request , redirect , url_for, flash

# Import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import classes for database tables
from database_setup import Base, System, Overview

app = Flask(__name__)

# Create session and connect to DB
engine = create_engine('sqlite:///ahab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/overview/')
def Overview():
	messages = session.query(Overview).all()
	return render_template('overview.html', messages=messages)

@app.route('/systems/')
def Systems():
	systems = session.query(System).all()
	return render_template('systems.html', systems=systems)

@app.route('/subsystems/')
def Subsystems():
	return render_template('subsystems.html')

@app.route('/log/')
def Log():
	return render_template('log.html')

@app.route('/systems/<system_id>/')
def System(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('system.html', system=system)

@app.route('/systems/<system_id>/edit/')
def EditSystem(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('edit_system.html', system=system)

@app.route('/systems/<system_id>/delete/')
def Delete(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', system=system)

##### Server stuff #####
if __name__ == '__main__' :
	# 
	app.secret_key = 'super_secret_key'
	# Debug mode let me change code without restarting the server
	# And provides a debuger in the browser
	app.debug = True
	# Run server. if 0.0.0.0 it listens in all public IP addresses
	app.run(host = '0.0.0.0', port = 5000)
