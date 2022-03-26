import RPi.GPIO as GPIO
import time
from gpiozero import LED
import urllib.request
import urllib.parse
import json

led = LED(26)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19,GPIO.IN)
counter1 = 0
counter2 = 0
GPIO.setup(13, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
#another led pin, connect on the board
GPIO.setup(,GPIO.OUT)

LDRon = False
PIR1on = False
PIR2on = False




def read_button():
    url = 'https://studev.groept.be/api/a21ib2D04/getLightStatus'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    button = str(data)
    print (button)

    if button == "[{'lights': '1'}]":
        print (1)
        button_out = 1
    elif button == "[{'lights': '0'}]":
        print (0)
        button_out = 0
    else:
        print ("default")
    return button_out




while True:

    b_out = read_button()


    if (counter1 % 2 != 0):
        PIR1on = True
    else:
        PIR1on = False
    if (counter2 % 2 != 0):
        PIR2on = True
    else:
        PIR2on = False

    if GPIO.input(13):
        print("light on")
        LDRon = True
        time.sleep(0.5)
    else:
        print("light off")
        LDRon = False
        time.sleep(0.5)

    if GPIO.input(26):
        print("movement detected in room 1")
        #movementdetected =1
        counter1 += 1
        time.sleep(2)
    if GPIO.input(19):
        print("movement detected in room 2")
        #movementdetected =1
        counter2 += 1
        time.sleep(2)

    if counter1 % 2 == 0:
        print("room 1 is empty")

    else:
        print("room 1 is full")

    if counter2 % 2 == 0:
        print("room 2 is empty")

    else:
        print("room 2 is full")

    # led1

    if (PIR1on == True and LDRon == True and b_out == 1):
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)

    #led2, still choose a GPIO pin

    if (PIR2on == True and LDRon == True and b_out == 1):
        GPIO.output(26,GPIO.LOW)
        GPIO.output(,GPIO.HIGH)
    else:
        GPIO.output(,GPIO.LOW)
        if (PIR1on == True and LDRon == True and b_out == 1):
            GPIO.output(26,GPIO.HIGH)


   # print('LDR: '+ str(LDRon) + 'PIR: ' + str(PIRon))




