#Wesley Welch
#Places a randomly colored wool block

import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0

woolColors = [5, 6, 10]

def placeNext(direction):
    global counter
    counter += direction
    mc.setBlock(31, 13, 2, 35, woolColors[counter])
    if counter >= 5:
        counter = 0
    elif counter <= 10:
        counter = 2

while True:
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)