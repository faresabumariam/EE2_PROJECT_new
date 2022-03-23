import RPi.GPIO as GPIO, time
import urllib, json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)

# getting data from the database
url = "https://studev.groept.be/api/a21ib2d04/getZone"
response = urllib.urlopen(url)
data = json.loads(response.read())
zone = str(data)
print(zone)

tone1 = GPIO.PWM(23, 100)

#50 seems to be the all around best value for duty cycle for buzzers
tone1.start(50)
#Note frequencies, starting with a C
#speaker works good from 32hz to about 500hz, so the first four octaves here
c = [32, 65, 131, 262, 523]
db= [34, 69, 139, 277, 554]
d = [36, 73, 147, 294, 587]
eb= [37, 78, 156, 311, 622]
e = [41, 82, 165, 330, 659]
f = [43, 87, 175, 349, 698]
gb= [46, 92, 185, 370, 740]
g = [49, 98, 196, 392, 784]
ab= [52, 104, 208, 415, 831]
a = [55, 110, 220, 440, 880]
bb= [58, 117, 223, 466, 932]
b = [61, 123, 246, 492, 984]

#notes of two scales, feel free to add more
cmajor = [c, d, e, f, g, a, b]
aminor = [a, b, c, d, e, f, g]

def playScale(scale, pause):
    for i in range(0, 5):
        for note in scale:
            tone1.ChangeFrequency(note[i])
            time.sleep(pause)
    tone1.stop()

#Star Wars Theme -- Key of C
if zone == "[{u'zone': u'1'}]" or zone == "[{u'zone': u'4'}]" or zone == "[{u'zone': u'7'}]":
    starwars_notes = [c[3], g[3], f[3], e[3], d[3], c[4], g[3], f[3], e[3], d[3], c[4], g[3],
                    f[3], e[3], f[3], d[3]]
    starwars_beats = [4,4,1,1,1,4,4,1,1,1,4,4,1,1,1,4]
elif zone == "[{u'zone': u'2'}]" or zone == "[{u'zone': u'5'}]" or zone == "[{u'zone': u'8'}]":
    starwars_notes = [c[2], g[2], f[2], e[2], d[2], c[3], g[2], f[2], e[2], d[2], c[3], g[2],
                      f[2], e[2], f[2], d[2]]
    starwars_beats = [4,4,1,1,1,4,4,1,1,1,4,4,1,1,1,4]
elif zone == "[{u'zone': u'3'}]" or zone == "[{u'zone': u'6'}]" or zone == "[{u'zone': u'9'}]":
    starwars_notes = [c[1], g[1], f[1], e[1], d[1], c[2], g[1], f[1], e[1], d[1], c[2], g[1],
                      f[1], e[1], f[1], d[1]]
    starwars_beats = [4,4,1,1,1,4,4,1,1,1,4,4,1,1,1,4]
else:
    starwars_notes = [a[0]]
    starwars_beats = [1]
    print("zone not possible")



def playSong(songnotes, songbeats, tempo):
    while True:
        tone1.ChangeDutyCycle(50)
        for i in range(0, len(songnotes)):
            tone1.ChangeFrequency(songnotes[i])
            time.sleep(songbeats[i]*tempo)
        tone1.ChangeDutyCycle(0)


playSong(starwars_notes, starwars_beats, 0.2)

