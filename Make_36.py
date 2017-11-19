import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
mc = minecraft.minecraft.create()

while True:
    xPos = mc.player.getPos().x
    yPos = mc.player.getPos().y-1
    zPos = mc.player.getPos().z
    mc.postToChat(mc.getBlockWithData(xPos,yPos,zPos))
    if mc.getBlockWithData(xPos,yPos,zPos).id == 35 and mc.getBlockWithData(xPos,yPos,zPos).data == 14:
        GPIO.output(11, GPIO.HIGH)
    elif mc.getBlockWithData(xPos,yPos,zPos).id == 35 and mc.getBlockWithData(xPos,yPos,zPos).data == 1:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.2)
    elif mc.getBlockWithData(xPos,yPos,zPos).id == 35 and mc.getBlockWithData(xPos,yPos,zPos).data == 5:
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
