from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(2)
yellow = LED(27)
bool = True

while bool:
    sleep(.5)
    if button.is_pressed:
        yellow.off()
        bool = False
    else:
        yellow.on()
        print("Button is not pressed")