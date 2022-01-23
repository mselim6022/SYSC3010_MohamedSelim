import sqlite3
import time

from sense_hat import SenseHat
sense = SenseHat()

#INIT
#connect ot the database
dbconnect = sqlite3.connect("sensorDB.db")

#create a cursor
cursor = dbconnect.cursor()

#clear table from any previous entries, create new table
cursor.execute('''DROP TABLE IF EXISTS sensordata''')

cursor.execute('''CREATE TABLE IF NOT EXISTS sensordata (id integer, readTime timestamp, 
		temperature float, humidity float, pressure float);''' )

dbconnect.row_factory = sqlite3.Row;
id = 0
#Data insertion loop
while True:
	id+= 1
	temperature = round( sense.get_temperature(),2)
	humidity = round( sense.get_humidity(), 2)
	pressure = round( sense.get_pressure(), 2)
	
	cursor.execute('''INSERT INTO sensordata VALUES(?, datetime('now'), ?, ?, ?);''', (id, temperature, humidity, pressure))
	print("Value with ID "+ str(id) + " has been recorded.")
	dbconnect.commit()
	time.sleep(1)
	#Determines how many values are recorded
	if id == 15:
		break
