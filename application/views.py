from application import app
from application import forms
from flask import render_template , request , redirect , url_for, flash

# Import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import classes for database tables
from database_setup import Base, Overview, System, SystemStatus, DeepSystem, SensorUnit, ControlUnit

# Create session and connect to DB
engine = create_engine('sqlite:///ahab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

### Views ###

@app.route('/')
@app.route('/overview/')
def OverviewRoute():
	messages = session.query(Overview).all()
	return render_template('overview.html', messages=messages)

@app.route('/systems/')
def SystemsRoute():
	systems = session.query(System).all()
	return render_template('systems.html', systems=systems)

@app.route('/parts/')
def partsRoute():
	sensorUnits = session.query(SensorUnit).all()
	return render_template('parts.html', sensorUnits=sensorUnits)

@app.route('/log/')
def LogRoute():
	return render_template('log.html')

@app.route('/systems/new')
def NewSystemRoute():
	return render_template('new_system.html')

@app.route('/systems/<system_id>/')
def SystemRoute(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('system.html', system=system)

@app.route('/systems/<system_id>/edit/')
def EditSystemRoute(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('edit_system.html', system=system)

@app.route('/systems/<system_id>/delete/')
def DeleteSystemRoute(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', system=system)

@app.route('/parts/new')
def NewPartRoute():
	return render_template('new_system.html')

@app.route('/parts/<system_id>/edit/')
def EditPartRoute(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('edit_system.html', system=system)

@app.route('/parts/<part_type>/<system_id>/delete/')
def DeletePartRoute(system_id):
	system = session.query(System).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', item=system)

# Sensor pages

@app.route('/parts/sensor/new/')
def newSensorRoute():
	return render_template('new_sensor.html')

@app.route('/parts/topo/<system_id>/')
def TopoRoute(system_id):
	sensor = session.query(TopoSensor).filter_by(serial_nr = system_id).one()
	return render_template('sensor.html', sensor=sensor, sensor_type='topo')

@app.route('/parts/topo/<system_id>/edit')
def EditTopoRoute(system_id):
	sensor = session.query(TopoSensor).filter_by(serial_nr = system_id).one()
	return render_template('edit_sensor.html', sensor=sensor, sensor_type='topo')

@app.route('/parts/topo/<system_id>/delete')
def DeleteTopoRoute(system_id):
	sensor = session.query(TopoSensor).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', item=sensor)

@app.route('/parts/shallow/<system_id>/')
def ShallowRoute(system_id):
	sensor = session.query(ShallowSensor).filter_by(serial_nr = system_id).one()
	return render_template('sensor.html', sensor=sensor, sensor_type='shallow')

@app.route('/parts/shallow/<system_id>/edit')
def EditShallowRoute(system_id):
	sensor = session.query(ShallowSensor).filter_by(serial_nr = system_id).one()
	return render_template('edit_sensor.html', sensor=sensor, sensor_type='shallow')

@app.route('/parts/shallow/<system_id>/delete')
def DeleteShallowRoute(system_id):
	sensor = session.query(ShallowSensor).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', item=sensor)

@app.route('/parts/deep/<system_id>/')
def DeepRoute(system_id):
	sensor = session.query(DeepSensor).filter_by(serial_nr = system_id).one()
	return render_template('sensor.html', sensor=sensor, sensor_type='deep')

@app.route('/parts/deep/<system_id>/edit')
def EditDeepRoute(system_id):
	sensor = session.query(DeepSensor).filter_by(serial_nr = system_id).one()
	return render_template('edit_sensor.html', sensor=sensor, sensor_type='deep')

@app.route('/parts/deep/<system_id>/delete')
def DeleteDeepRoute(system_id):
	sensor = session.query(DeepSensor).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', item=sensor)

# SCU pages

@app.route('/parts/scu/<system_id>/')
def SCURoute(system_id):
	scu = session.query(SCU).filter_by(serial_nr = system_id).one()
	return render_template('sensor.html', sensor=scu, sensor_type='scu')

@app.route('/parts/scu/<system_id>/edit')
def EditSCURoute(system_id):
	scu = session.query(SCU).filter_by(serial_nr = system_id).one()
	return render_template('edit_sensor.html', sensor=scu, sensor_type='scu')

@app.route('/parts/scu/<system_id>/delete')
def DeleteSCURoute(system_id):
	scu = session.query(SCU).filter_by(serial_nr = system_id).one()
	return render_template('delete.html', item=sensor)

# Units pages

@app.route('/parts/sensor_unit/new/', methods=['GET', 'POST'])
def NewSensorUnitRoute():
	form = forms.SensorUnitForm(request.form)
	if request.method == 'POST' and form.validate():
		newItem = SensorUnit(serial_nr=form.serial_nr.data, imu=form.imu.data, leica_cam=form.leica_cam.data, topo_sensor_id=form.topo_sensor_id.data, shallow_sensor_id=form.shallow_sensor_id.data)
		session.add(newItem)
		session.commit()
		flash("new SensorUnit created!")
		return redirect(url_for('partsRoute'))

	return render_template('new_sensorunit.html', form=form)