# Lab 3

This file includes brief descriptions to the files in [Lab-3](https://github.com/mselim6022/SYSC3010_MohamedSelim/tree/main/Lab-3)

## [lab3-thingspeak-read.py](https://github.com/mselim6022/SYSC3010_MohamedSelim/blob/main/Lab-3/lab3-thingspeak-read.py)
This program reads the most recent entry from a ThingSpeak channel and displays them on the Display of a connected SenseHat. The details of the channel 
(ReadApiKey, url and channel number) are specified at the beginning of the code.

## [lab3-thingspeak-write.py](https://github.com/mselim6022/SYSC3010_MohamedSelim/blob/main/Lab-3/lab3-thingspeak-write.py)
This program uses the sensors of a connected SenseHat to determine the Temperature, Humidity and Pressure around it, and proceeds to write this information to a provided
ThingSpeak channel. This process repeats once every 2 minutes for 5 times. The details of the channel (SendApiKey, url and channel number) 
are specified at the beginning of the code.

## [lab3-firebase.py](https://github.com/mselim6022/SYSC3010_MohamedSelim/blob/main/Lab-3/lab3-firebase.py)
This program uses the sensors of a connected SenseHat to determine the Temperature, Humidity and Pressure around it, and proceeds to write this information to
the provided Firebase database. The program then reads the last 3 entries of another provided Firebase database. The details for the database to send data to
are provided under config{}. The details for the database to read data from are provided under config2{}. 
