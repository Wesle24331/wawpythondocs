#Wesley Welch


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
playerPosition = mc.player.getTilePos()

mc.postToChat(playerPosition)
#Wesley Welch
#Four Buttons, One LED

#Setup for buttons and leds

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
        mc.postToChat("Button 6 was pressed!")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        mc.postToChat("Button 13 was pressed!")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    elif GPIO.input(19) == GPIO.LOW:
        mc.postToChat("Button 19 was pressed!")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    elif GPIO.input(26) == GPIO.LOW:
        mc.postToChat("Button 26 was pressed!")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")
    
        
