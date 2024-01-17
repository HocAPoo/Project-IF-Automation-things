from gpiozero import LED
from time import sleep
from gpiozero import Button

red = LED(17)
button = Button(2)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    if button.is_pressed:
        print('you pushed me :D')
        break