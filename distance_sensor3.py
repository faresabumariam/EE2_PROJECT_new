import time

import spidev

spi = spidev.SpiDev()see
spi.open(0,0)
spi.max_speed_hz=1000000


def readChannel(channel):
    val = spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data
while (True):
    if __name__ == "__main__":
        v=(readChannel(0)/1023.0)*3.3
        dist = 8.53* v**4 -54.90*v**3 +131.26*v**2 -144.85*v +72.28-0.3
        print ("Distanz: %.2f cm" % dist)

        if ( dist<10):
            print('zone 7')
        else :
            if ( dist < 20):
                print ('zone 8')
            else:
                print ( "zone 9")

        time.sleep(1 );