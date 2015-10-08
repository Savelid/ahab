from application import app
from wtforms import Form, BooleanField, TextField, StringField, PasswordField, validators

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, Required

### Forms ###

class SensorUnitForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    imu                 = StringField('IMU', [validators.Length(min=4, max=4)])
    leica_cam           = StringField('Leica camera', [validators.Length(min=4, max=10)])
    topo_sensor_id      = StringField('Topo Sensor', [validators.Length(min=4, max=4)])
    shallow_sensor_id   = StringField('Shallow Sensor', [validators.Length(min=4, max=4)])

class ControlUnitForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    battery             = StringField('Battery', [validators.Length(min=4, max=4)])
    cc32                = StringField('CC32', [validators.Length(min=4, max=4)])
    pdu                 = StringField('Power Distribution Unit', [validators.Length(min=4, max=4)])
    scu_id              = StringField('Sensor Control Unit', [validators.Length(min=4, max=4)])

class DeepSystemForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    control_system      = StringField('Control System', [validators.Length(min=4, max=4)])
    imu                 = StringField('IMU', [validators.Length(min=4, max=4)])
    pro_pack            = StringField('Pro Pack', [validators.Length(min=4, max=4)])
    deep_sensor_id      = StringField('Deep Sensor', [validators.Length(min=4, max=4)])

