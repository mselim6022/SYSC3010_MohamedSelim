from sense_hat import SenseHat
import requests
from time import sleep
sendKey = "BYLR94KJ30A5NPQS"
url = "https://api.thingspeak.com/update"

def main():
    sense = SenseHat()
    i = 5
    while i > 0:
      try:
          
          #Update Data
          temperature = sense.get_temperature()
          humidity = sense.get_humidity()
          pressure = sense.get_pressure()
          
          # payload includes the headers to be sent with the GET request
          # read the documentation for more information (https://docs.python-requests.org)
          payload = {'field1': temperature, 'field2': humidity, 'field3': pressure,'api_key': sendKey}
          # Sends an HTTP GET request
          response = requests.get(url, params=payload)
          # The library can also decode JSON responses
          response = response.json()
          
          print(response)
      except:
          print("Connection Failed")
      sleep(120)
      i -= 1
if __name__ == "__main__":
    main()
