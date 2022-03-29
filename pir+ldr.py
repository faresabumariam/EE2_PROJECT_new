import RPi.GPIO as GPIO
import time
from gpiozero import LED
import urllib.request
import urllib.parse
import json

PIR1, PIR2, LDR, LED1, LED2 = 26, 19, 13, 17, 12

# led = LED(26)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIR1, GPIO.IN)  # PIR1
GPIO.setup(PIR2, GPIO.IN)  # PIR2
GPIO.setup(LDR, GPIO.IN)  # LDR
GPIO.setup(LED1, GPIO.OUT)  # LED1
GPIO.setup(LED2, GPIO.OUT)  # LED2
# another led pin, connect on the board

counter1 = 0
counter2 = 0

LDRon = False
PIR1on = False
PIR2on = False

room1Full = False
room2Full = False

startTime1 = 0
stopTime1 = 0
startTime2 = 0
stopTime2 = 0

duration = 0


def read_button():
    url = 'https://studev.groept.be/api/a21ib2D04/getLightStatus'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    button = str(data)
    print(button)

    if button == "[{'lights': '1'}]":
        print(1)
        button_out = 1
    elif button == "[{'lights': '0'}]":
        print(0)
        button_out = 0
    else:
        print("default")
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

    if GPIO.input(LDR):
        print("light on")
        LDRon = True
        time.sleep(0.5)
    else:
        print("light off")
        LDRon = False
        time.sleep(0.5)

    if GPIO.input(PIR1):
        print("movement detected in room 1")
        # movementdetected =1
        counter1 += 1
        time.sleep(2)
    if GPIO.input(PIR2):
        print("movement detected in room 2")
        # movementdetected =1
        counter2 += 1
        time.sleep(2)

    if counter1 % 2 == 0:
        print("room 1 is empty")
        room1Full = False

    else:
        print("room 1 is full")
        room1Full = True

    if counter2 % 2 == 0:
        print("room 2 is empty")
        room2Full = False

    else:
        print("room 2 is full")
        room2Full = True
    print("__________________________")
    # led1

    if (PIR1on == True and LDRon == True and b_out == 1):
        GPIO.output(LED1, GPIO.HIGH)
    else:
        GPIO.output(LED2, GPIO.LOW)

    # led2, still choose a GPIO pin

    if (PIR2on == True and LDRon == True and b_out == 1):
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
    else:
        GPIO.output(LED2, GPIO.LOW)
        if (PIR1on == True and LDRon == True and b_out == 1):
            GPIO.output(LED2, GPIO.HIGH)

    # time calc
    # if(room1Full):
    #     startTime1=time.time()
    # else:
    #     stopTime1=time.time()
    #     duration += startTime1-stopTime1
    #
    # if(room2Full):
    #     startTime2=time.time()
    # else:
    #     stopTime2=time.time()
    #     duration += startTime2-stopTime2

# print('LDR: '+ str(LDRon) + 'PIR: ' + str(PIRon))
