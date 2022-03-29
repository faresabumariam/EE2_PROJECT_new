import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.IN)
counter = 0

while True:
    if GPIO.input(13):
        print("light on")
        time.sleep(0.5)
    else:
        print("light off")
        time.sleep(0.5)

