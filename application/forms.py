from application import app
from wtforms import Form, BooleanField, TextField, StringField, PasswordField, validators

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, Required

### Forms ###

class SensorUnitForm(Form):
    serial_nr   	= StringField('Serial Number', [validators.Length(min=4, max=4)])
    imu        		= StringField('IMU', [validators.Length(min=4, max=4)])
    leica_cam 		= StringField('Leica camera', [validators.Length(min=4, max=10)])
    topo_sensor_id		= StringField('Topo Sensor', [validators.Length(min=4, max=4)])
    shallow_sensor_id	= StringField('Shallow Sensor', [validators.Length(min=4, max=4)])

