import RPi.GPIO as GPIO
import time
from gpiozero import LED

led = LED(26)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)
counter = 0
GPIO.setup(20, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

LDRon = False
PIRon = False


while True:
    if (counter % 2 != 0):
        PIRon = True
    else:
        PIRon = False

    if GPIO.input(20):
        print("light on")
        LDRon = True
        time.sleep(0.5)
    else:
        print("light off")
        LDRon = False
        time.sleep(0.5)

    if GPIO.input(21):
        print("movement detected")
        #movementdetected =1
        counter += 1
        time.sleep(2)

    if counter % 2 == 0:
        print("room is empty")

    else:
        print("room is full")

    # LDR

    if (PIRon == True and LDRon == True):
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)

   # print('LDR: '+ str(LDRon) + 'PIR: ' + str(PIRon))




