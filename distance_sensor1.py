import time
from gpiozero import Servo

from time import sleep
import spidev

servo = Servo(17)
val = 0

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000


def readChannel(channel):
    value = spi.xfer2([1,(8+channel)<<4,0])
    data = ((value[1]&3) << 8) + value[2]
    return data

while (True):
    if __name__ == "__main__":
        v=(readChannel(0)/1023.0)*3.3
       # dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
        dist = 8.53* v**4 -54.90*v**3 +131.26*v**2 -144.85*v +72.28
        print ("Distanz: %.2f cm" % dist)
        zone = ''
        servo.value = val

        if dist < 10:
            zone = "zone 1"
            val=0.8
        else:
            if dist < 20:
                zone = "zone 2"
                val=0.5
            else:
                zone = "zone 3"
                val=0.2

        print(zone)
        time.sleep(0.25)

