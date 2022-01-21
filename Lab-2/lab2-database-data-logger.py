import sqlite3
import datetime
import time

from sense_hat import SenseHat
sense = SenseHat()

#INIT
#connect ot the database
dbconnect = sqlite3.connect("sensorDB.db")

#create a cursor
cursor = dbconnect.cursor()

#create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS sensordata (id integer, readTime timestamp, 
		temperature float, humidity float, pressure float);''' )

dbconnect.row_factory = sqlite3.Row;
id = 0
#Data insertion loop
while True:
	id+= 1
	readTime =  datetime.datetime.now()
	temperature = round( sense.get_temperature(),2)
	humidity = round( sense.get_humidity(), 2)
	pressure = round( sense.get_pressure(), 2)
	
	cursor.execute('''INSERT INTO sensordata VALUES(?, ?, ?, ?, ?);''', (id, readTime, temperature, humidity, pressure))
	print(id)
	dbconnect.commit()
	time.sleep(1)

