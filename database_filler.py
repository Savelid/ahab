from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, Overview, System, SystemStatus, SensorUnit, ControlUnit, DeepSystem, SCU, TopoSensor, ShallowSensor, DeepSensor
from random import randint
import datetime
import random

engine = create_engine('sqlite:///ahab.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

## Randomizing tools
client_names = ["AHAB", "Jilin", "SIS1", "SIS2", "Nova Scotia", "SigmaMetrix", "China demo", "Pelydryn", "HEIII (AHAB)"]
config_names = ["DualDragon", "Chiroptera", "HawkEye III"]

def CreateRandomDate():
	today = datetime.date.today()
	days_old = randint(0,540)
	editedDate = today - datetime.timedelta(days = days_old)
	return editedDate

def CreateRandomSN():
	serial_number = randint(1000,1400)
	return serial_number

##
# Add a few systems
for i in range(1200,1210):
	ranprocent = randint(0,100)
	shallowValue = True
	if ranprocent < 20:
		shallowValue = False

	system = System(serial_nr = i, datetime = CreateRandomDate(), art_nr = CreateRandomSN(), client = client_names[randint(0,7)], configuration = config_names[randint(0,2)], system_status_id = i)
	system_status = SystemStatus(id = i, potta_heat = True, shallow_heat = shallowValue)
	session.add(system)
	session.add(system_status)
	session.commit()

# Add a few comments to Overview
message1 = "Dependent sometimes additions recommend fat our. Direction has strangers now believing. Respect enjoyed gay far exposed parlors towards. Enjoyment use tolerably dependent listening men. No peculiar in handsome together unlocked do by. Article concern joy anxious did picture sir her. Although desirous not recurred disposed off shy you numerous securing."
comment1 = Overview(datetime = CreateRandomDate(), message = message1, author = "Sven")
session.add(comment1)
session.commit()
message2 = "Songs in oh other avoid it hours woman style. In myself family as if be agreed."
comment2 = Overview(datetime = CreateRandomDate(), message = message2, author = "Birger")
session.add(comment2)
session.commit()
message3 = "Now eldest new tastes plenty mother called misery get. Longer excuse for county nor except met its things. Narrow enough sex moment desire are. Hold who what come that seen read age its. Contained or estimable earnestly so perceived."
comment3 = Overview(datetime = CreateRandomDate(), message = message3, author = "Sven")
session.add(comment3)
session.commit()