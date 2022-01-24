from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

#INIT SQLITE3
dbconnect = sqlite3.connect("jsonDB.db")
cursor = dbconnect.cursor()

#Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS weatherdata (city TEXT, temp INTEGER, humidity INTEGER, pressure INTEGER, windpeed INTEGER)''')


# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)
temp = int(current["temp"])
humid = int(current["humidity"])
press = int(current["pressure"])

current = data["wind"]
wspeed = int(current["speed"])

cursor.execute('''INSERT INTO weatherdata VALUES(?, ?, ?, ?, ?)''', (city, temp, humid, press, wspeed))

dbconnect.commit()
print(wspeed)

dbconnect.close()
