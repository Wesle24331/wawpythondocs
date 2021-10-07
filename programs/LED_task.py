#Wesley Welch
#Four Buttons, One LED

#Setup for buttons and LEDs

#Import Paspberry Pi GPIO library
import RPi.GPIO as GPIO
#Ignore Warning for now
GPIO.setwarnings(False)
#Use physical pin numbering
GPIO.setmode(GPIO.BCM)

#Use a module for requesting data online
import requests

#Use a module to control time
import time

#Set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Start an inifinite loop
while True:
    #Wait for one second
    time.sleep(1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        requests.get("http://192.168.10.53:5000/sfx?file=willheimscrem")
    elif GPIO.input(13) == GPIO.LOW:
        print("Button 13 was pressed")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button 19 was pressed")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button 26 was pressed")
    
        