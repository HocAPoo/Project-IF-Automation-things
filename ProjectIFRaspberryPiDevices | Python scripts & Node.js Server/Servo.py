from gpiozero import Servo
from gpiozero import Button
from gpiozero import LED
from time import sleep

servo = Servo(17)
red = LED(27)
button = Button(2)
bool = True

def the_servo():
    servo.min()
    red.on()
    sleep(1)
    servo.max()
    red.off()
    sleep(1)

while bool:
    sleep(.5)
    if button.is_pressed:
        print("terminated")
        red.off()
        bool = False
    else:
        print("WOW")
        the_servo()
