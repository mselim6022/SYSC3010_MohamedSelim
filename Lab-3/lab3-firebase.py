import pyrebase
import random
import time
from sense_hat import SenseHat

# Create new Firebase config and database object
config = {
  "apiKey": "AIzaSyDqevs8PW0sIpRblR_J6KgffYdBlsKcnP0",
  "authDomain": "sysc3010-lab3-87285.firebaseapp.com",
  "databaseURL": "https://sysc3010-lab3-87285-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-lab3-87285.appspot.com"
}

config2 = {
  "apiKey": "AIzaSyDqevs8PW0sIpRblR_J6KgffYdBlsKcnP0",
  "authDomain": "sysc3010-lab3-87285.firebaseapp.com",
  "databaseURL": "https://sysc3010-lab3-87285-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-lab3-87285.appspot.com"
}


sense = SenseHat()
firebase = pyrebase.initialize_app(config)
db = firebase.database()

firebase = pyrebase.initialize_app(config2)
db2 = firebase.database()

dataset = "senseHat readings"

def main():
  writeData()
  readData()
  
# Write random numbers to database
def writeData():
  
  key = 0
  
  while key < 5:
    sensorData = {
       "sensor1" : {
         "temperature" : sense.get_temperature(),
         "humidity" : sense.get_humidity(),
         "pressure" : sense.get_pressure()
       }
     }
       
      # Each 'child' is a JSON key:value pair
    db.child(dataset).child(key).set(sensorData)
  
    key = key + 1
    time.sleep(1)

def readData():
  # Returns the entry as an ordered dictionary (parsed from json)
  mySensorData = db2.child(dataset).get()

  print("Parent Key: {}".format(mySensorData.key()))
  #print("Parent Value: {}\n".format(mySensorData.val()))

  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  #splices the last 3 elements of the list
  entries = mySensorData_list[-3:]
  #Loops through the splice and prints each entry
  for i in entries:
    print("Child Key: {}".format(i.key()))
    print("Child Value: {}\n".format(i.val()))

if __name__ == "__main__":
    main()
