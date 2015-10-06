import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#################################

## Examples of attributes ##
# String(250) - string of maximum 250 char
# Integer
# relationship(Class) - defines relationships between tables
# nullable = False - must have a value
# primary_key = True - identifier
# ForeignKey('some_table.id') - referense a row in different table with relation to this table

class System(Base):

	__tablename__ = 'system'

	serial_nr = Column(String(10), primary_key = True)
	datetime = Column(Date)

	art_nr = Column(String(20))
	client = Column(String(50))
	configuration = Column(String(50))
	comment = Column(String)
	system_status_id = Column(Integer, ForeignKey('system_status.id'))
	system_status = relationship("SystemStatus")  #, backref=backref("system", uselist=False))
	# Subunits with tables
	sensor_unit_id = Column(String(10), ForeignKey('sensor_unit.serial_nr'))
	sensor_unit = relationship("SensorUnit")  #, backref=backref("system", uselist=False))
	control_unit_id = Column(String(10), ForeignKey('control_unit.serial_nr'))
	control_unit = relationship("ControlUnit")  #, backref=backref("system", uselist=False))
	deep_system_id = Column(String(10), ForeignKey('deep_system.serial_nr'))
	deep_system = relationship("DeepSystem")  #, backref=backref("system", uselist=False))
	# Subunit without table
	cooling_system = Column(String(10))

class Overview(Base):

	__tablename__ = 'overview'

	id = Column(Integer, primary_key = True)
	datetime = Column(Date)

	message = Column(String)
	author = Column(String(40))
	
class SystemStatus(Base):

	__tablename__ = 'system_status'

	id = Column(Integer, primary_key = True)

	potta_heat = Column(Boolean)
	shallow_heat = Column(Boolean)
	## TODO: add rest

class SensorUnit(Base):

	__tablename__ = 'sensor_unit'

	serial_nr = Column(String(10), primary_key = True)

	imu = Column(String(10))
	# With tables
	leica_cam  = Column(String(10)) # TODO: add table and relation
	topo_sensor_id = Column(String(10), ForeignKey('topo_sensor.serial_nr'))
	topo_sensor = relationship("TopoSensor")  #, backref=backref("sensor_unit", uselist=False))
	shallow_sensor_id = Column(String(10), ForeignKey('shallow_sensor.serial_nr'))
	shallow_sensor = relationship("ShallowSensor")  #, backref=backref("sensor_unit", uselist=False))

class ControlUnit(Base):

	__tablename__ = 'control_unit'

	serial_nr = Column(String(10), primary_key = True)

	battery = Column(String(10))
	cc32 = Column(String(10))
	pdu = Column(String(10))
	# With tables
	scu_id = Column(String(10), ForeignKey('scu.serial_nr'))
	scu = relationship("SCU")  #, backref=backref("control_unit", uselist=False))

class DeepSystem(Base):

	__tablename__ = 'deep_system'

	serial_nr = Column(String(10), primary_key = True)

	control_system = Column(String(10))
	imu = Column(String(10))
	pro_pack = Column(String(10))
	# With tables
	deep_sensor_id = Column(String(10), ForeignKey('deep_sensor.serial_nr'))
	deep_sensor = relationship("DeepSensor")  #, backref=backref("deep_system", uselist=False))

class SCU(Base):

	__tablename__ = 'scu'

	serial_nr = Column(String(10), primary_key = True)

	# configuration ??
	digitaizer1 = Column(String(10))
	digitaizer2 = Column(String(10))
	sat = Column(String(10))
	cpu = Column(String(10))
	version = Column(String(20))
	status = Column(String(30))

class TopoSensor(Base):

	__tablename__ = 'topo_sensor'

	serial_nr = Column(String(10), primary_key = True)

	cat = Column(String(10))
	fpga_id = Column(String(10))
	laser = Column(String(10))
	hv_card = Column(String(10)) # TODO Add relationship??
	receiver_unit = Column(String(10))
	receiver_chip = Column(String(10))
	dps_value_input_offset_t0 = Column(Integer)
	dps_value_input_offset_rec = Column(Integer)
	dps_value_pulse_width_t0 = Column(Integer)
	dps_value_pulse_width_rec = Column(Integer)
	status = Column(String(30))

class ShallowSensor(Base):

	__tablename__ = 'shallow_sensor'

	serial_nr = Column(String(10), primary_key = True)

	cat = Column(String(10))
	fpga_id = Column(String(10))
	laser = Column(String(10))
	hv_card = Column(String(10)) # TODO Add relationship??
	receiver_unit = Column(String(10))
	receiver_chip = Column(String(10))
	dps_value_input_offset_t0 = Column(Integer)
	dps_value_input_offset_rec = Column(Integer)
	dps_value_pulse_width_t0 = Column(Integer)
	dps_value_pulse_width_rec = Column(Integer)
	status = Column(String(30))

class DeepSensor(Base):

	__tablename__ = 'deep_sensor'

	serial_nr = Column(String(10), primary_key = True)

	cat = Column(String(10))
	fpga_id = Column(String(10))
	laser = Column(String(10))
	hv_card_1 = Column(String(10)) # TODO Add relationship??
	receiver_unit_1 = Column(String(10))
	receiver_chip_1 = Column(String(10))
	hv_card_2 = Column(String(10)) # TODO Add relationship??
	receiver_unit_2 = Column(String(10))
	receiver_chip_2 = Column(String(10))
	dps_value_input_offset_t0 = Column(Integer)
	dps_value_input_offset_rec = Column(Integer)
	dps_value_pulse_width_t0 = Column(Integer)
	dps_value_pulse_width_rec = Column(Integer)
	status = Column(String(30))

# class HVCard(Base):

# 	__tablename__ = 'hv_card'

# 	serial_nr = Column(String(10), primary_key = True)

# 	art_nr = Column(String(20))
# 	k_value
# 	m_value

# 	hv_module ??

# # TODO add rest of exel sheet



##### insert at end of file #####

engine = create_engine('sqlite:///ahab.db')
Base.metadata.create_all(engine)