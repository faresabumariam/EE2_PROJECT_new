from gpiozero import Servo

from time import sleep



servo = Servo(17)
val = -1
count=0
servo.value = val
try:
    while True:
        servo.value = val
        sleep(0.2)
        val = val + 0.05
        count+=1
        if val > 1:
            break
        print(count)
except KeyboardInterrupt:
    print("Program stopped")

#
# while True:
#
#     servo.value=0.1
#
#     print("mid")
#
#     sleep(1)
#
#     servo.min()
#
#     print("min")
#
#     sleep(1)
#
#     servo.mid()
#
#     print("mid")
#
#     sleep(1)
#
#     servo.max()
#
#     print("max")
#
#     sleep(1)
