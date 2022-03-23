import time
from gpiozero import Servo
from time import sleep
import spidev
import json

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
        v1=(readChannel(0)/1023.0)*3.3
        v2=(readChannel(0)/1023.0)*3.3
        v3=(readChannel(0)/1023.0)*3.3
       # dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
        dist1 = 8.53* v1**4 -54.90*v1**3 +131.26*v1**2 -144.85*v1 +72.28
        dist2 = 8.53* v2**4 -54.90*v2**3 +131.26*v2**2 -144.85*v2 +72.28
        dist3 = 8.53* v3**4 -54.90*v3**3 +131.26*v3**2 -144.85*v3 +72.28
        print ("Distanz: %.2f cm" % dist1)
        zone = ''
        servo.value = val


        if dist1<27 and dist2>27 and dist3>27:
            if dist1 < 10:
                zone = "zone 1"
                val=0.8
            else:
                if dist1 < 20:
                    zone = "zone 2"
                    val=0.5
                else:
                    zone = "zone 3"
                    val=0.2

        elif dist1>27 and dist2<27 and dist3>27:
            if dist2 < 10:
                zone = "zone 4"
                val=0.8
            else:
                if dist2 < 20:
                    zone = "zone 5"
                    val=0.5
                else:
                    zone = "zone 6"
                    val=0.2

        elif dist1>27 and dist2>27 and dist3<27:
            if dist3 < 10:
                zone = "zone 7"
                val=0.8
            else:
                if dist3 < 20:
                    zone = "zone 8"
                    val=0.5
                else:
                    zone = "zone 9"
                    val=0.2

        print(zone)
        time.sleep(0.25)

