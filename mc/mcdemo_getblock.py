#Wesley Welch
#Gets Minecraft Blocks by Position

import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import time

while True:
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW:
        pos = mc.player.getTilePos()
        blockData = mc.getBlock(pos.x, pos.y - 1, pos.z)
        mc.postToChat(blockData)
        if blockData == 57:
            mc.player.setTilePos(pos.x, pos.y + 20, pos.z)
        #if the blockData is a Diamond block, change the player's position
        #to it's current position plus 20 to the y position
        