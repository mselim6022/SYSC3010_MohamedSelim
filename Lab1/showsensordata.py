from sense_hat import SenseHat
sense = SenseHat()

temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()
i = 1
while i:
  if i == 1:
    sense.show_message(str(temperature))
    i++
  elif i == 2:
    sense.show_message(str(humidity))
    i++
  else:
    sense.show_message(str(pressure))
    i = 1
