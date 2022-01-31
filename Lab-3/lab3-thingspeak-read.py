import requests
from sense_hat import SenseHat

sense = SenseHat()
readKey = "XEVSPUEX8ALF4QM3"
channelNumber = "1642575"
url = "https://api.thingspeak.com/channels/" + channelNumber + "/feeds.json"
results = 1

def main():
    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.python-requests.org)
    payload = {'api_key': readKey, 'results': results}

    # Sends an HTTP GET request
    response = requests.get(url, params=payload)
    response = response.json()

    print("Channel Name: {}".format(response['channel']['name']))
    
    entries = response['feeds']

    # Print out the temperature at each entry's time
    for e in entries:
        sense.show_message("Entry {}: Temperature: {} Humidity: {} Pressure: {}".format(e['entry_id'], int(float(e['field1'])), int(float(e['field2'])), int(float(e['field3']))), scroll_speed= 0.05)
        

if __name__ == "__main__":
    main()
