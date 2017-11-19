import minecraft.minecraft as minecraft
import time
import RPi.GPIO as GPIO
mc = minecraft.minecraft.create()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
pulse = GPIO.PWM(11,300)

while True:
    pos = mc.player.getPos()
    if -125 <= pos.x <= -110 and 121 <= pos.z <= 124:
        print(“C”)
        Pulse = GPIO.PWM(11,262)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 117 <= pos.z <= 120:
        print(“D”)
        Pulse = GPIO.PWM(11,294)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 112 <= pos.z <= 115:
        print(“E”)
        Pulse = GPIO.PWM(11,330)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 107 <= pos.z <= 110:
        print(“F”)
        Pulse = GPIO.PWM(11,349)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 102 <= pos.z <= 105:
        print(“G”)
        Pulse = GPIO.PWM(11,393)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 97 <= pos.z <= 100:
        print(“A”)
        Pulse = GPIO.PWM(11,440)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 92 <= pos.z <= 95:
        print(“B”)
        Pulse = GPIO.PWM(11,494)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
    elif -125 <= pos.x <= -110 and 87 <= pos.z <= 90:
        print(“C”)
        Pulse = GPIO.PWM(11,523)
        pulse.start(50)
        pulse.ChangeDutyCycle(0.2)
        time.sleep(0.2)
        pulse.stop()
