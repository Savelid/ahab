import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Date, Float
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

class Overview(Base):

	__tablename__ = 'overview'

	id = Column(Integer, primary_key = True)
	datetime = Column(Date)

	message = Column(String)
	author = Column(String(40))

class System(Base):

	__tablename__ = 'system'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))
	datetime = Column(Date)

	art_nr = Column(String(20))
	client = Column(String(50))
	configuration = Column(String(50))
	comment = Column(String)
	system_status_id = Column(Integer, ForeignKey('system_status.id'))
	system_status = relationship("SystemStatus", backref="system")
	# Subunits with tables
	sensor_unit_id = Column(String(10), ForeignKey('sensor_unit.serial_nr'))
	sensor_unit = relationship("SensorUnit")
	control_unit_id = Column(String(10), ForeignKey('control_unit.serial_nr'))
	control_unit = relationship("ControlUnit")
	deep_system_id = Column(String(10), ForeignKey('deep_system.serial_nr'))
	deep_system = relationship("DeepSystem")
	# Subunit without table
	cooling_system = Column(String(10))
	
class SystemStatus(Base):

	__tablename__ = 'system_status'

	id = Column(Integer, primary_key = True)
	#system_id = Column(String(10), ForeignKey('system.serial_nr'))

	potta_heat = Column(Boolean)
	shallow_heat = Column(Boolean)
	## TODO: add rest

class SensorUnit(Base):

	__tablename__ = 'sensor_unit'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))
	#system_id = Column(String(10), ForeignKey('system.serial_nr'))

	imu = Column(String(10))
	# With tables
	leica_cam_id  = Column(String(10), ForeignKey('leica_cam.serial_nr'))
	leica_cam = relationship("LeicaCam")
	topo_sensor_id = Column(String(10), ForeignKey('sensor.serial_nr'))
	topo_sensor = relationship("Sensor", foreign_keys="SensorUnit.topo_sensor_id")
	shallow_sensor_id = Column(String(10), ForeignKey('sensor.serial_nr'))
	shallow_sensor = relationship("Sensor", foreign_keys="SensorUnit.shallow_sensor_id")

class ControlUnit(Base):

	__tablename__ = 'control_unit'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))
	#system_id = Column(String(10), ForeignKey('system.serial_nr'))

	battery = Column(String(10))
	cc32 = Column(String(10))
	pdu = Column(String(10))
	# With tables
	scu_id = Column(String(10), ForeignKey('scu.serial_nr'))
	scu = relationship("SCU")

class DeepSystem(Base):

	__tablename__ = 'deep_system'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))
	#system_id = Column(String(10), ForeignKey('system.serial_nr'))

	control_system = Column(String(10))
	imu = Column(String(10))
	pro_pack = Column(String(10))
	# With tables
	deep_sensor_id = Column(String(10), ForeignKey('sensor.serial_nr'))
	deep_sensor = relationship("Sensor", foreign_keys="DeepSystem.deep_sensor_id")

class SCU(Base):

	__tablename__ = 'scu'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))

	configuration = Column(String(20))
	digitaizer1 = Column(String(10))
	digitaizer2 = Column(String(10))
	sat = Column(String(10))
	cpu = Column(String(10))
	version = Column(String(20))
	status = Column(String(30))

# specific foreign_keys needed since there are more than one reference to this table
class Sensor(Base):

	__tablename__ = 'sensor'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))
	sensor_type = Column(String(10))

	cat = Column(String(10))
	fpga_id = Column(String(10))
	laser_id = Column(String(10), ForeignKey('laser.serial_nr'))
	laser = relationship("Laser")
	hv_card_id = Column(String(10), ForeignKey('hv_card.serial_nr'))
	hv_card = relationship("HVCard", foreign_keys="Sensor.hv_card_id")
	receiver_unit = Column(String(10))
	receiver_chip_id = Column(String(10), ForeignKey('receiver_chip.serial_nr'))
	receiver_chip = relationship("ReceiverChip", foreign_keys="Sensor.receiver_chip_id")
	hv_card_2_id = Column(String(10), ForeignKey('hv_card.serial_nr'))
	hv_card_2 = relationship("HVCard", foreign_keys="Sensor.hv_card_2_id")
	receiver_unit_2 = Column(String(10))
	receiver_chip_2_id = Column(String(10), ForeignKey('receiver_chip.serial_nr'))
	receiver_chip_2 = relationship("ReceiverChip", foreign_keys="Sensor.receiver_chip_2_id")
	dps_value_input_offset_t0 = Column(Integer)
	dps_value_input_offset_rec = Column(Integer)
	dps_value_pulse_width_t0 = Column(Integer)
	dps_value_pulse_width_rec = Column(Integer)
	status = Column(String(30))

# specific foreign_keys needed since there are more than one reference to this table
class HVCard(Base):

	__tablename__ = 'hv_card'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))

	configuration = Column(String(20))
	art_nr = Column(String(20))
	k_value = Column(Float)
	m_value = Column(Float)
	v_0 = Column(Float)
	v_500 = Column(Float)
	v_1000 = Column(Float)
	v_1500 = Column(Float)
	v_2000 = Column(Float)
	v_2500 = Column(Float)
	v_3000 = Column(Float)
	v_3250 = Column(Float)

class Laser(Base):

	__tablename__ = 'laser'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))

	v_0 = Column(Float)
	v_5 = Column(Float)
	v_10 = Column(Float)
	v_15 = Column(Float)
	v_20 = Column(Float)
	v_25 = Column(Float)
	v_30 = Column(Float)
	v_40 = Column(Float)
	v_50 = Column(Float)
	v_60 = Column(Float)
	v_70 = Column(Float)
	v_80 = Column(Float)
	v_90 = Column(Float)
	v_100 = Column(Float)

class LeicaCam(Base):

	__tablename__ = 'leica_cam'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))

	configuration = Column(String(20))
	breakdown = Column(Integer)
	operating_voltage = Column(Integer)

# specific foreign_keys needed since there are more than one reference to this table
class ReceiverChip(Base):

	__tablename__ = 'receiver_chip'

	id = Column(Integer, primary_key = True)
	serial_nr = Column(String(10))

	unit = Column(String(30))
	firmware = Column(String(10))
	art_nr = Column(String(20))



##### insert at end of file #####

engine = create_engine('sqlite:///ahab.db')
Base.metadata.create_all(engine)