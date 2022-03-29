import RPi.GPIO as GPIO
import time
import urllib.request
import urllib.parse

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN)
counter = 0
zone = 0

while True:

    if GPIO.input(26):
        print("movement detected")
        counter += 1
        time.sleep(5)

    if counter % 2 == 0:
        print("room is empty")
        PIR1 = 0
        # urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
        time.sleep(2)
    else:
        print("room is full")
        PIR1 = 1
        # urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
        time.sleep(2)

    if GPIO.input(26):
        print("movement detected")
        counter += 1
        time.sleep(5)

    if counter % 2 == 0:
        print("room is empty")
        PIR2 = 0
        # urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
        time.sleep(2)
    else:
        print("room is full")
        PIR2 = 1
        # urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
        time.sleep(2)