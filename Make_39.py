import minecraft.minecraft as minecraft 
import minecraft.block as block
import RPi.GPIO as GPIO 
import time 
import random

mc = minecraft.Minecraft.create() 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings (False) 
GPIO.setup(11, GPIO.OUT) 

mc.setBlock(29, 0, 45, block.DIAMOND_BLOCK) 

mc.player.setPos (3, 1, 3) 
GPIO.output(11, GPIO.LOW) 

time.sleep(5)
mc.postToChat("Welcome to Zork.")
time.sleep(0.5)
mc.postToChat("You are in my world now!")
time.sleep(0.5)
mc.postToChat("How goes it?")
time.sleep(0.5)
mc.postToChat("Narrative blah blah blah...go here!! or Here!!")
time.sleep (5)
while True: 
    x, y, z = mc.player.getPos() 

    post = (int(x), int(y), int(z)) 
    if post == (29, 1, 45): 
        mc.postToChat("Great work")         time.sleep(3)
        mc.postToChat("You have reached position 1")
        time.sleep(3)
        mc.postToChat("Do you want a sword??")
        time.sleep(3)
        sword = raw_input ("Do you want the sword?") 
        if sword == ("Yes"):
            GPIO.output(11, GPIO.HIGH) 
    else:
        chat = ["We Hope you are well", "Are You Lost", "You're Mummy can't help you here!"]
        thing = random.randint (0,2)
        mc.postToChat (chat[thing])
        time.sleep (5)
