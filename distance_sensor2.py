import time
import urllib.request
import urllib.parse
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
PIR1 = -1
PIR2 = -1


def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data


while True:
    if __name__ == "__main__":
        v1 = (readChannel(0) / 1023.0) * 3.3
        v2 = (readChannel(1) / 1023.0) * 3.3
        v3 = (readChannel(2) / 1023.0) * 3.3
        dist1 = 8.53 * v1 ** 4 - 54.90 * v1 ** 3 + 131.26 * v1 ** 2 - 144.85 * v1 + 72.28 - 0.3
        dist2 = 8.53 * v2 ** 4 - 54.90 * v2 ** 3 + 131.26 * v2 ** 2 - 144.85 * v2 + 72.28 - 0.3
        dist3 = 8.53 * v3 ** 4 - 54.90 * v3 ** 3 + 131.26 * v3 ** 2 - 144.85 * v3 + 72.28 - 0.3
        #print("Distance: %.2f cm" % dist1)

        if dist1 < 30 and dist2 > 30 and dist3 > 30:
            if dist1 < 10:
                print('zone 1')
                zone = str(1)
                urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
            else:
                if dist1 < 20:
                    print('zone 2')
                    zone = str(2)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
                else:
                    print("zone 3")
                    zone = str(3)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)


        elif dist1 > 30 and dist2 < 30 and dist3>30:
            if dist2 < 10:
                print('zone 4')
                zone = str(4)
                urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
            else:
                if dist2 < 20:
                    print('zone 5')
                    zone = str(5)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
                else:
                    print("zone 6")
                    zone = str(6)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)

        elif dist1 > 30 and dist2 > 30 and dist3 < 30:
            if dist3 < 10:
                print('zone 7')
                zone = str(7)
                urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
            else:
                if dist3 < 20:
                    print('zone 8')
                    zone = str(8)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)
                else:
                    print("zone 9")
                    zone = str(1)
                    urllib.request.urlopen('https://studev.groept.be/api/a21ib2D04/input/'+zone+'/'+PIR1+'/'+PIR2)

    time.sleep(1);

