import minecraft.minecraft as minecraft
import minecraft.block as block
import RPi.GPIO as GPIO
mc = minecraft.Minecraft.create()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings (False)
GPIO.setup(11, GPIO.OUT)
while True:
Xpos = mc.player.getPos().x
zpos = mc.player.getPos().z
if -98 <= xpos <= -91 and -108 <= zpos <= 115:
GPIO.output(11, GPIO.HIGH)
		time.sleep(0.5)
GPIO.output(11, GPIO.LOW)
		time.sleep(0.5)
else:
		GPIO.output(11, GPIO.LOW)
