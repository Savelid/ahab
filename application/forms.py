from application import app
from wtforms import Form, BooleanField, TextField, StringField, PasswordField, SelectField, validators

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, Required

### Forms ###

class SensorUnitForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    imu                 = StringField('IMU', [validators.optional(), validators.Length(min=4, max=4)])
    leica_cam           = StringField('Leica camera', [validators.optional(), validators.Length(min=4, max=10)])
    topo_sensor_id      = StringField('Topo Sensor', [validators.optional(), validators.Length(min=4, max=4)])
    shallow_sensor_id   = StringField('Shallow Sensor', [validators.optional(), validators.Length(min=4, max=4)])

class ControlUnitForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    battery             = StringField('Battery', [validators.optional(), validators.Length(min=4, max=4)])
    cc32                = StringField('CC32', [validators.optional(), validators.Length(min=4, max=4)])
    pdu                 = StringField('Power Distribution Unit', [validators.optional(), validators.Length(min=4, max=4)])
    scu_id              = StringField('Sensor Control Unit', [validators.optional(), validators.Length(min=4, max=4)])

class DeepSystemForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    control_system      = StringField('Control System', [validators.optional(), validators.Length(min=4, max=4)])
    imu                 = StringField('IMU', [validators.optional(), validators.Length(min=4, max=4)])
    pro_pack            = StringField('Pro Pack', [validators.optional(), validators.Length(min=4, max=4)])
    deep_sensor_list    = session.query(Sensor).filter_by(sensor_type = 'deep').all()
   # deep_sensor_fake    = SelectField(u'Deep Sensor Test', choices=[(a.serial_nr, a.serial_nr) for a in deep_sensor_list])
    deep_sensor_id      = StringField('Deep Sensor', [validators.Length(min=4, max=4)])

class SensorForm(Form):
    sensor_type =         SelectField(u'Sensor Type', choices=[('topo', 'Topo Sensor'), ('shallow', 'Shallow Sensor'), ('deep', 'Deep Sensor')])
    serial_nr =                  StringField('Serial Number', [validators.Length(min=4, max=4)])
    cat =                        StringField('CAT', [validators.optional(), validators.Length(min=4, max=4)])
    fpga_id =                    StringField('FGPA', [validators.optional(), validators.Length(min=10, max=10)])
    laser =                      StringField('Laser', [validators.optional(), validators.Length(min=8, max=8)])
    hv_card =                    StringField('HV card', [validators.optional(), validators.Length(min=4, max=4)])
    receiver_unit =              StringField('Receiver Unit', [validators.optional(), validators.Length(min=4, max=4)])
    receiver_chip =              StringField('Receiver Chip', [validators.optional(), validators.Length(min=8, max=8)])
    hv_card_2 =                  StringField('HV card 2', [validators.optional(), validators.Length(min=4, max=4)])
    receiver_unit_2 =            StringField('Receiver Unit 2', [validators.optional(), validators.Length(min=4, max=4)])
    receiver_chip_2 =            StringField('Receiver Chip 2', [validators.optional(), validators.Length(min=8, max=8)])
    dps_value_input_offset_t0 =  StringField('Input offset t0', [validators.optional(), validators.NumberRange()])
    dps_value_input_offset_rec = StringField('Input offset rec', [validators.optional(), validators.optional(), validators.NumberRange()])
    dps_value_pulse_width_t0 =   StringField('Pulse width t0', [validators.optional(), validators.NumberRange()])
    dps_value_pulse_width_rec =  StringField('Pulse width rec', [validators.optional(), validators.NumberRange()])
    status =                     TextField('Status', [validators.Optional()])

class SystemForm(Form):
    serial_nr           = StringField('Serial Number', [validators.Length(min=4, max=4)])
    art_nr              = StringField('Art Nr', [validators.optional(), validators.Length(min=4, max=20)])
    client              = StringField('Client', [validators.Optional(), validators.Length(max=50)])
    configuration       = SelectField(u'Configuration', choices=[('HawkEyeIII', 'HawkEyeIII'), ('DualDragon', 'DualDragon'), ('Chiroptera', 'Chiroptera')])
    sensor_unit_id      = StringField('Sensor Unit', [validators.Length(min=4, max=4)])
    control_unit_id     = StringField('Control Unit', [validators.Length(min=4, max=4)])
    deep_system_id      = StringField('Deep System', [validators.Length(min=4, max=4)])
    cooling_system      = StringField('Cooling System', [validators.optional(), validators.Length(min=4, max=4)])
    comment             = TextField('Comment', [validators.Optional()])

    potta_heat          = BooleanField('Potta Heat')
    shallow_heat        = BooleanField('Shallow Heat')

class OverviewForm(Form):
    message             = TextField('Message', [validators.Required()])
    author              = StringField('Name', [validators.Required()])
