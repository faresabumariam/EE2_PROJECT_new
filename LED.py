import RPi.GPIO as GPIO
import urllib, json
import re;


led_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)

while True:
    url = "https://studev.groept.be/api/a21ib2d04/getLightStatus"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    numberList = [int(num) for num in re.findall(r"\d+", str(data))]
    print(numberList)
    pwm.ChangeDutyCycle(numberList[0])